#!/usr/bin/env python3
"""Read-only, fail-closed validation of Round-10 Stage-2.5 reports.

The validator recomputes denominators and bindings from canonical inputs.  It
does not trust the compiler's batch aggregate, embedded evidence rows, or
passport extension as an authority.  Duplicate JSON keys, duplicate IDs,
symlinked carriers, stale hashes, projection collisions, anchor upgrades,
partial scholar intake, route advancement, and output cross-link drift are
hard failures.  Official ARS evidence-row, bounded-coverage, passport
consistency, experiment-provenance, Claim Registry, drift, and compliance
validators are replayed where their contracts apply.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

import jsonschema


ROOT = Path(__file__).resolve().parent.parent
ROUTE_A_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
ROUTE_B_SHA = "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"
PROVENANCE_BOUNDARY = (
    "This check verifies disclosure and claim-to-provenance fidelity. It does "
    "not judge whether the experiment was correctly designed, run, statistically "
    "adequate, or reproducible by ARS."
)
REPAIR_FINDINGS = {
    "P29-AB-MEDIUM-01",
    "P31-E1-056",
    "P31-E1-078",
    "P32-AB-MINOR-01",
}


PAPERS: dict[str, dict[str, Any]] = {
    "29-bianchi-ideal-owner-refinement": {
        "paper_id": "P29", "number": 29, "refs": 22, "verified_refs": 22,
        "plausible_refs": 0, "contexts": 22, "sampled_contexts": 7,
        "registered": 83, "high": 68, "random": 3, "selected": 71,
        "tuples": 71, "phase_c": 45, "originality": (23, 75),
        "table_traces": 0, "e6_revision_evidence_available": False,
    },
    "30-three-disk-nonconstant-roof-determinant": {
        "paper_id": "P30", "number": 30, "refs": 26, "verified_refs": 26,
        "plausible_refs": 0, "contexts": 26, "sampled_contexts": 8,
        "registered": 95, "high": 75, "random": 3, "selected": 78,
        "tuples": 78, "phase_c": 53, "originality": (27, 87),
        "table_traces": 0, "e6_revision_evidence_available": False,
    },
    "31-level11-conjugacy-owner-ledger": {
        "paper_id": "P31", "number": 31, "refs": 22, "verified_refs": 22,
        "plausible_refs": 0, "contexts": 22, "sampled_contexts": 7,
        "registered": 78, "high": 68, "random": 3, "selected": 71,
        "tuples": 89, "phase_c": 45, "originality": (21, 67),
        "table_traces": 0, "e6_revision_evidence_available": False,
        "integrity_corrected_without_revision_evidence_bundle": True,
    },
    "32-homology-cover-renormalization-uniformity": {
        "paper_id": "P32", "number": 32, "refs": 26, "verified_refs": 26,
        "plausible_refs": 0, "contexts": 26, "sampled_contexts": 8,
        "registered": 98, "high": 85, "random": 3, "selected": 88,
        "tuples": 108, "phase_c": 58, "originality": (24, 77),
        "table_traces": 0, "e6_revision_evidence_available": False,
        "integrity_corrected_without_revision_evidence_bundle": True,
    },
    "33-bolza-control-matched-census": {
        "paper_id": "P33", "number": 33, "refs": 20, "verified_refs": 19,
        "plausible_refs": 1, "contexts": 48, "sampled_contexts": 18,
        "registered": 126, "high": 68, "random": 6, "selected": 74,
        "tuples": 108, "phase_c": 43, "originality": (21, 68),
        "table_traces": 2, "e6_revision_evidence_available": False,
    },
}


EXPECTED_AGGREGATE = {
    "papers": 5,
    "references_checked": 116,
    "references_verified": 115,
    "references_plausible": 1,
    "citation_contexts": 144,
    "contexts_sampled": 48,
    "registered_claims": 480,
    "selected_claims": 382,
    "evidence_tuples": 454,
    "anchorless_rows": 454,
    "phase_c_claim_surfaces": 244,
    "originality_sampled": 116,
    "originality_denominator": 374,
    "figure_table_traces": 2,
    "scientific_executions": 0,
    "formal_route_a_tuples": 0,
    "positive_arithmetic_a2": 0,
    "route_b_invocations": 0,
}


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def require_regular(path: Path) -> Path:
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"required regular file missing or symlinked: {path}")
    return path


def confined_path(raw: str, label: str) -> Path:
    if not isinstance(raw, str) or not raw:
        raise RuntimeError(f"{label} path is missing")
    path = (ROOT / raw).resolve() if not Path(raw).is_absolute() else Path(raw).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise RuntimeError(f"{label} path escapes workspace: {raw}") from exc
    return require_regular(path)


def load(path: Path) -> Any:
    require_regular(path)
    try:
        return json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise RuntimeError(f"invalid JSON {path}: {exc}") from exc


def sha(path: Path) -> str:
    return hashlib.sha256(require_regular(path).read_bytes()).hexdigest()


def canonical_sha(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def exact_int(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise RuntimeError(f"{label} must be an integer, got {value!r}")
    return value


def deep_scalars(value: Any) -> Iterable[Any]:
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from deep_scalars(item)
    elif isinstance(value, list):
        for item in value:
            yield from deep_scalars(item)
    else:
        yield value


def assert_no_true_key(value: Any, key: str, label: str) -> None:
    if isinstance(value, dict):
        for current, item in value.items():
            if current == key and item is not False:
                raise RuntimeError(f"{label}: {key} must be exactly false")
            assert_no_true_key(item, key, label)
    elif isinstance(value, list):
        for item in value:
            assert_no_true_key(item, key, label)


def ars_root() -> Path:
    override = os.environ.get("ARS_CODEX_ROOT")
    if override:
        path = Path(override).expanduser().resolve()
        if (path / "scripts/evidence_rows.py").is_file():
            return path
        raise RuntimeError(f"ARS_CODEX_ROOT is not an ARS resource root: {path}")
    candidates: list[Path] = []
    for codex_root in (ROOT.parent / ".codex", Path.home() / ".codex"):
        candidates.extend(
            (codex_root / "plugins/cache/ars-codex/ars-codex").glob(
                "*/skills/academic-research-suite/ars"
            )
        )
    candidates = sorted({path.resolve() for path in candidates if path.is_dir()})
    if not candidates:
        raise RuntimeError("ARS-Codex academic-research-suite resources not found")
    return candidates[-1]


ARS = ars_root()


def run_checked(argv: list[str], label: str) -> None:
    result = subprocess.run(
        argv,
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if result.returncode:
        detail = (result.stdout + "\n" + result.stderr).strip()
        raise RuntimeError(f"{label} failed (exit {result.returncode}): {detail}")


def pointer_from_record(record: Any, label: str) -> Path:
    if not isinstance(record, dict) or set(record) != {"path", "sha256"}:
        raise RuntimeError(f"{label} must be an exact path/hash pointer")
    path = confined_path(record["path"], label)
    if sha(path) != record["sha256"]:
        raise RuntimeError(f"{label} hash mismatch")
    return path


def freeze_rows(freeze: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rows = freeze.get("papers")
    if not isinstance(rows, list) or len(rows) != 5:
        raise RuntimeError("final freeze paper population malformed")
    by_id = {cfg["paper_id"]: slug for slug, cfg in PAPERS.items()}
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise RuntimeError("final freeze paper row is not an object")
        slug = row.get("slug", by_id.get(row.get("paper")))
        if slug not in PAPERS or slug in result:
            raise RuntimeError(f"final freeze duplicate/unknown paper {slug!r}")
        result[slug] = row
    if set(result) != set(PAPERS):
        raise RuntimeError("final freeze exact paper set mismatch")
    return result


def validate_authorities(summary: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    freeze_path = pointer_from_record(summary.get("input_freeze"), "input freeze")
    repair_path = pointer_from_record(summary.get("repair_receipt"), "repair receipt")
    declaration_path = pointer_from_record(
        summary.get("experiment_declaration_receipt"), "experiment declaration receipt"
    )
    freeze = load(freeze_path)
    repair = load(repair_path)
    declaration_receipt = load(declaration_path)
    if not all(isinstance(item, dict) for item in (freeze, repair, declaration_receipt)):
        raise RuntimeError("authority receipt must be a JSON object")
    request_path = ROOT / "BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_REQUEST.md"
    strings = {item for item in deep_scalars(repair) if isinstance(item, str)}
    if sha(request_path) not in strings or not REPAIR_FINDINGS <= strings:
        raise RuntimeError("repair receipt is not bound to request/all findings")
    status = str(repair.get("authorization_status", repair.get("status", ""))).upper()
    if repair.get("authorized") is not True and status not in {
        "AUTHORIZED", "APPROVED", "CONFIRMED", "COMPLETE"
    }:
        raise RuntimeError("repair receipt is not explicitly authorized")
    assert_no_true_key(repair, "stage3_authorized", "repair receipt")
    declaration = declaration_receipt.get("experiment_intake_declaration")
    expected_keys = {"status", "declared_by", "declared_at"}
    if not isinstance(declaration, dict) or set(declaration) != expected_keys:
        raise RuntimeError("scholar experiment declaration malformed")
    if declaration.get("status") != "no_experiments_declared" or declaration.get("declared_by") != "scholar":
        raise RuntimeError("scholar no-experiment declaration invalid")
    if not re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
        str(declaration.get("declared_at", "")),
    ):
        raise RuntimeError("scholar declaration timestamp malformed")
    if declaration_receipt.get("experiment_provenance") != []:
        raise RuntimeError("scholar no-experiment receipt has provenance")
    if declaration_receipt.get("boundary") != PROVENANCE_BOUNDARY:
        raise RuntimeError("scholar declaration loses provenance boundary")
    assert_no_true_key(declaration_receipt, "stage3_authorized", "declaration receipt")

    freeze_strings = {item for item in deep_scalars(freeze) if isinstance(item, str)}
    if sha(repair_path) not in freeze_strings or sha(declaration_path) not in freeze_strings:
        raise RuntimeError("final freeze is not bound to repair/declaration receipts")
    if freeze.get("route_a_sha256") != ROUTE_A_SHA or freeze.get("route_b_sha256") != ROUTE_B_SHA:
        raise RuntimeError("final freeze roadmap hash mismatch")
    aggregate = freeze.get("aggregate", {})
    for key in (
        "scientific_executions",
        "formal_route_a_tuples",
        "positive_arithmetic_a2",
        "route_b_invocations",
    ):
        if key in aggregate and exact_int(aggregate[key], f"freeze {key}") != 0:
            raise RuntimeError(f"final freeze advances {key}")
    return freeze_rows(freeze), declaration


def validate_phase_ab(notes: Path, slug: str, cfg: dict[str, Any], hashes: dict[str, str]) -> str:
    path = require_regular(notes / "stage2_5_phase_ab_final.json")
    value = load(path)
    if not isinstance(value, dict) or value.get("paper") not in {slug, cfg["paper_id"]}:
        raise RuntimeError(f"{slug}: Phase-A/B receipt paper mismatch")
    if str(value.get("decision", "")).upper() != "PASS" or value.get("unresolved_findings") != []:
        raise RuntimeError(f"{slug}: Phase-A/B not clean PASS")
    bindings = value.get("bindings")
    if not isinstance(bindings, dict) or any(bindings.get(k) != hashes[k] for k in hashes):
        raise RuntimeError(f"{slug}: stale Phase-A/B binding")
    a = value.get("phase_a", {})
    b = value.get("phase_b", {})
    checked = a.get("references_checked", a.get("checked"))
    verified = a.get("references_verified", a.get("verified"))
    plausible = a.get("references_plausible", a.get("plausible", 0))
    if tuple(exact_int(x, f"{slug} Phase A") for x in (checked, verified, plausible)) != (
        cfg["refs"], cfg["verified_refs"], cfg["plausible_refs"]
    ):
        raise RuntimeError(f"{slug}: Phase-A exact counts mismatch")
    total = b.get("citation_contexts", b.get("contexts_total", b.get("denominator")))
    sampled = b.get("contexts_sampled", b.get("sampled"))
    supported = b.get("contexts_supported", b.get("supported", b.get("verified")))
    if tuple(exact_int(x, f"{slug} Phase B") for x in (total, sampled, supported)) != (
        cfg["contexts"], cfg["sampled_contexts"], cfg["sampled_contexts"]
    ):
        raise RuntimeError(f"{slug}: Phase-B exact counts mismatch")
    if a.get("unresolved_findings", []) != [] or b.get("unresolved_findings", []) != []:
        raise RuntimeError(f"{slug}: nested Phase-A/B unresolved finding")
    return sha(path)


def phase_c_file(notes: Path) -> Path:
    canonical = notes / "stage2_5_phase_c_data_trace.json"
    alias = notes / "stage2_5_phase_c_trace.json"
    if canonical.is_file() and alias.is_file():
        raise RuntimeError(f"{notes.parent.name}: ambiguous Phase-C sidecar names")
    return require_regular(canonical if canonical.is_file() else alias)


def validate_phase_c(
    notes: Path,
    slug: str,
    cfg: dict[str, Any],
    hashes: dict[str, str],
    declaration: dict[str, Any],
) -> str:
    path = phase_c_file(notes)
    value = load(path)
    if not isinstance(value, dict) or value.get("paper") not in {slug, cfg["paper_id"]}:
        raise RuntimeError(f"{slug}: Phase-C paper mismatch")
    if str(value.get("decision", value.get("verdict", ""))).upper() != "PASS":
        raise RuntimeError(f"{slug}: Phase-C is not PASS")
    bindings = value.get("bindings", {})
    expected = {
        "manuscript_sha256": hashes["manuscript_sha256"],
        "claim_registry_sha256": hashes["claim_registry_sha256"],
    }
    if not isinstance(bindings, dict) or any(bindings.get(k) != v for k, v in expected.items()):
        raise RuntimeError(f"{slug}: stale Phase-C bindings")
    checked = value.get(
        "claim_surfaces_checked",
        value.get("claims_checked", value.get("quantitative_data_claims_checked")),
    )
    verified = value.get(
        "claim_surfaces_verified", value.get("verified", value.get("claims_verified"))
    )
    if (exact_int(checked, f"{slug} Phase-C checked"), exact_int(verified, f"{slug} Phase-C verified")) != (
        cfg["phase_c"], cfg["phase_c"]
    ):
        raise RuntimeError(f"{slug}: Phase-C exact count mismatch")
    if value.get("unresolved_findings") != []:
        raise RuntimeError(f"{slug}: unresolved Phase-C finding")
    if value.get("experiment_intake_declaration") != declaration or value.get("experiment_provenance") != []:
        raise RuntimeError(f"{slug}: Phase-C declaration/provenance mismatch")
    if value.get("boundary") != PROVENANCE_BOUNDARY:
        raise RuntimeError(f"{slug}: Phase-C provenance boundary mismatch")
    traces = value.get("figure_table_trace")
    if not isinstance(traces, list) or len(traces) != cfg["table_traces"]:
        raise RuntimeError(f"{slug}: figure/table trace count mismatch")
    seen: set[str] = set()
    for row in traces:
        if not isinstance(row, dict) or not row:
            raise RuntimeError(f"{slug}: malformed figure/table trace")
        ident = str(
            row.get(
                "artifact_id",
                row.get("trace_id", row.get("table_id", row.get("locator", ""))),
            )
        )
        if not ident or ident in seen:
            raise RuntimeError(f"{slug}: duplicate figure/table trace")
        seen.add(ident)
        for status_key in ("decision", "verdict", "status", "trace_status"):
            status = row.get(status_key)
            if isinstance(status, str) and status.upper() in {
                "FAIL", "FAILED", "UNRESOLVED", "UNSUPPORTED", "NOT_VERIFIED"
            }:
                raise RuntimeError(f"{slug}: non-passing figure/table trace")
    return sha(path)


def validate_originality(notes: Path, slug: str, cfg: dict[str, Any], manuscript_sha: str) -> tuple[str, str]:
    sample_path = notes / "stage2_5_originality_sample.json"
    audit_path = require_regular(notes / "stage2_5_originality_audit.md")
    sample = load(sample_path)
    sampled, denominator = cfg["originality"]
    if (
        not isinstance(sample, dict)
        or sample.get("paper") != slug
        or sample.get("manuscript_sha256") != manuscript_sha
        or exact_int(sample.get("body_paragraph_denominator"), f"{slug} originality denominator") != denominator
    ):
        raise RuntimeError(f"{slug}: stale originality sample")
    rows = sample.get("samples")
    if not isinstance(rows, list) or len(rows) != sampled:
        raise RuntimeError(f"{slug}: originality count mismatch")
    ids: set[str] = set()
    sections: set[str] = set()
    for row in rows:
        if not isinstance(row, dict):
            raise RuntimeError(f"{slug}: malformed originality row")
        ident = row.get("sample_id")
        if not isinstance(ident, str) or ident in ids:
            raise RuntimeError(f"{slug}: duplicate originality id")
        ids.add(ident)
        if not str(row.get("search_status", "")).startswith("COMPLETED"):
            raise RuntimeError(f"{slug}: incomplete originality WebSearch")
        if row.get("verdict") not in {"ORIGINAL", "COMMON_KNOWLEDGE", "PARAPHRASE"}:
            raise RuntimeError(f"{slug}: blocking originality verdict")
        section = row.get("major_section")
        if not isinstance(section, str) or not section:
            raise RuntimeError(f"{slug}: originality row lacks section")
        sections.add(section)
        if not re.fullmatch(r"[0-9a-f]{64}", str(row.get("paragraph_sha256", ""))):
            raise RuntimeError(f"{slug}: malformed originality paragraph hash")
    if len(sections) != 10:
        raise RuntimeError(f"{slug}: originality does not cover 10/10 sections")
    audit = audit_path.read_text(encoding="utf-8")
    denominator_prose = re.search(
        rf"(?is)denominator\D{{0,40}}{denominator}\b.*?sample\D{{0,40}}{sampled}\s+paragraph",
        audit,
    )
    if manuscript_sha not in audit or not (
        f"{sampled}/{denominator}" in audit or denominator_prose
    ):
        raise RuntimeError(f"{slug}: stale originality audit")
    return sha(sample_path), sha(audit_path)


def validate_failure_modes(notes: Path, slug: str, manuscript_sha: str) -> str:
    path = require_regular(notes / "stage2_5_seven_failure_mode_final.md")
    text = path.read_text(encoding="utf-8")
    if manuscript_sha not in text:
        raise RuntimeError(f"{slug}: stale failure-mode sidecar")
    for mode in range(1, 8):
        if not re.search(
            rf"(?mi)^\|\s*{mode}(?:\.|\s*[—–-])[^|]*\|\s*(?:\*\*)?CLEAR(?:\*\*)?\s*\|",
            text,
        ):
            raise RuntimeError(f"{slug}: failure mode {mode} is not CLEAR")
    if not re.search(r"(?mi)^\|\s*CLEAR\s*\|\s*7\s*\|", text):
        raise RuntimeError(f"{slug}: seven-mode aggregate missing")
    for label in ("SUSPECTED", "INSUFFICIENT EVIDENCE"):
        if not re.search(rf"(?mi)^\|\s*{re.escape(label)}\s*\|\s*0\s*\|", text):
            raise RuntimeError(f"{slug}: {label}=0 aggregate missing")
    return sha(path)


def validate_claim_core(
    base: Path, slug: str, cfg: dict[str, Any], manuscript: Path
) -> dict[str, Any]:
    notes = base / "notes"
    registry_path = notes / "stage2_5_claim_registry.json"
    coverage_path = notes / "stage2_5_claim_registry_coverage.json"
    rows_path = notes / "stage2_5_evidence_rows.json"
    drift_path = notes / "stage2_5_claim_strength_drift_findings.json"
    semantic_audit_path = require_regular(notes / "stage2_5_phase_e_semantic_audit.md")
    semantic_path = notes / "stage2_5_phase_e_semantic_verdicts.json"
    registry = load(registry_path)
    coverage = load(coverage_path)
    rows = load(rows_path)
    drift = load(drift_path)
    semantic = load(semantic_path)

    claim_schema = load(ARS / "shared/contracts/evidence/claim_registry.schema.json")
    jsonschema.Draft202012Validator(claim_schema).validate(registry)
    claims = registry.get("claims", [])
    if not isinstance(claims, list) or len(claims) != cfg["registered"]:
        raise RuntimeError(f"{slug}: registry denominator mismatch")
    ids = [row.get("claim_id") for row in claims if isinstance(row, dict)]
    if len(ids) != len(claims) or len(set(ids)) != len(ids):
        raise RuntimeError(f"{slug}: duplicate/malformed registry IDs")
    selected = [row for row in claims if row.get("selection_tier") != "NOT-SELECTED"]
    tiers: dict[str, int] = {}
    manuscript_bytes = manuscript.read_bytes()
    for claim in claims:
        tier = claim.get("selection_tier")
        tiers[tier] = tiers.get(tier, 0) + 1
        span = claim.get("draft_span", {})
        start = exact_int(span.get("start_byte"), f"{slug} span start")
        end = exact_int(span.get("end_byte"), f"{slug} span end")
        if not (0 <= start < end <= len(manuscript_bytes)):
            raise RuntimeError(f"{slug}: invalid claim span")
        if manuscript_bytes[start:end].decode("utf-8") != claim.get("claim_text"):
            raise RuntimeError(f"{slug}: claim span bytes drift")
    if (
        len(selected) != cfg["selected"]
        or tiers.get("HIGH-IMPACT", 0) != cfg["high"]
        or tiers.get("RANDOM", 0) != cfg["random"]
    ):
        raise RuntimeError(f"{slug}: claim selection mismatch")

    if not isinstance(rows, list) or len(rows) != cfg["tuples"]:
        raise RuntimeError(f"{slug}: evidence tuple count mismatch")
    run_checked(
        [sys.executable, str(ARS / "scripts/evidence_rows.py"), "validate", str(rows_path)],
        f"{slug} official evidence-row validation",
    )
    selected_by_id = {row["claim_id"]: row for row in selected}
    expected = {
        (row["claim_id"], ref)
        for row in selected
        for ref in (row.get("ref_slugs") or [None])
    }
    actual: list[tuple[str, Any]] = []
    row_ids: set[str] = set()
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise RuntimeError(f"{slug}: malformed evidence row")
        ident = row.get("row_id")
        if not isinstance(ident, str) or ident in row_ids:
            raise RuntimeError(f"{slug}: duplicate evidence row id")
        row_ids.add(ident)
        if row.get("anchor") != {"kind": "none", "value_decoded": "", "value_encoded": ""}:
            raise RuntimeError(f"{slug}: evidence anchor was upgraded")
        if row.get("excerpt", {}).get("state") != "anchorless":
            raise RuntimeError(f"{slug}: evidence excerpt is not anchorless")
        claim_obj = row.get("claim", {})
        claim_id = claim_obj.get("claim_id")
        claim = selected_by_id.get(claim_id)
        if claim is None:
            raise RuntimeError(f"{slug}: evidence targets unselected claim")
        expected_claim = {
            "claim_id": claim_id,
            "paper_locator": claim["writer_anchors"][0],
            "selection_tier": claim["selection_tier"],
            "text": claim["claim_text"],
        }
        if claim_obj != expected_claim:
            raise RuntimeError(f"{slug}: embedded evidence claim object mismatch")
        actual.append((claim_id, row.get("source", {}).get("ref_slug")))
        grouped.setdefault(claim_id, []).append(row)
    if len(actual) != len(set(actual)) or set(actual) != expected:
        raise RuntimeError(f"{slug}: evidence projection is not exact")

    run_checked(
        [
            sys.executable,
            str(ARS / "scripts/claim_registry_coverage.py"),
            "--draft", str(manuscript),
            "--registry", str(registry_path),
            "--validate-report", str(coverage_path),
        ],
        f"{slug} official coverage validation",
    )
    if (
        coverage.get("candidate_unregistered_count") != 0
        or coverage.get("semantic_extraction_coverage") != "not_machine_detectable"
        or coverage.get("draft_raw_sha256") != sha(manuscript)
        or coverage.get("registry_raw_sha256") != sha(registry_path)
    ):
        raise RuntimeError(f"{slug}: coverage boundary mismatch")

    drift_schema = load(
        ARS / "shared/contracts/revision/claim_strength_drift_findings.schema.json"
    )
    jsonschema.Draft202012Validator(drift_schema).validate(drift)
    expected_status = (
        "completed"
        if cfg["e6_revision_evidence_available"]
        else "skipped_no_revision_evidence"
    )
    if (
        drift.get("status") != expected_status
        or drift.get("final_draft_sha256") != sha(manuscript)
        or drift.get("findings") != []
    ):
        raise RuntimeError(f"{slug}: drift receipt is stale/blocking")
    if expected_status == "completed":
        digest = drift.get("revision_evidence_bundle_sha256")
        candidates = [
            path for path in ROOT.glob("BATCH_ROUND10_STAGE2_5*.json")
            if path.is_file() and not path.is_symlink()
        ]
        if not any(sha(path) == digest for path in candidates):
            raise RuntimeError(f"{slug}: drift bundle hash does not resolve")

    if not isinstance(semantic, dict) or semantic.get("schema") != "flow-systems-stage2.5-semantic-verdict-receipt/1.0":
        raise RuntimeError(f"{slug}: semantic receipt schema mismatch")
    bindings = {
        "manuscript_sha256": sha(manuscript),
        "claim_registry_sha256": sha(registry_path),
        "evidence_rows_sha256": sha(rows_path),
        "semantic_audit_sha256": sha(semantic_audit_path),
    }
    if semantic.get("bindings") != bindings:
        raise RuntimeError(f"{slug}: stale semantic bindings")
    if semantic.get("decision") not in {
        "PASS_SELECTED_POPULATION",
        "PASS_SELECTED_POPULATION_WITH_MINOR_DISTORTION",
        "NO_MAJOR_DISTORTION_DETECTED__PASSAGE_CLOSURE_INCOMPLETE",
    }:
        raise RuntimeError(f"{slug}: semantic decision is not PASS")
    verdicts = semantic.get("claim_verdicts")
    if not isinstance(verdicts, list) or len(verdicts) != cfg["selected"]:
        raise RuntimeError(f"{slug}: semantic verdict denominator mismatch")
    by_id = {row.get("claim_id"): row for row in verdicts if isinstance(row, dict)}
    if len(by_id) != len(verdicts) or set(by_id) != set(selected_by_id):
        raise RuntimeError(f"{slug}: semantic verdict population mismatch")
    verdict_counts = {
        "VERIFIED": 0, "MINOR_DISTORTION": 0, "MAJOR_DISTORTION": 0,
        "UNVERIFIABLE": 0, "UNVERIFIABLE_ACCESS": 0,
    }
    for claim_id, verdict in by_id.items():
        result = verdict.get("verdict")
        if result not in verdict_counts:
            raise RuntimeError(f"{slug}: unknown semantic verdict")
        verdict_counts[result] += 1
        if result not in {"VERIFIED", "MINOR_DISTORTION"}:
            raise RuntimeError(f"{slug}: blocking semantic verdict")
        claim_rows = grouped[claim_id]
        if verdict.get("tuple_count") != len(claim_rows):
            raise RuntimeError(f"{slug}: semantic tuple count drift")
        if verdict.get("row_ids") != [row["row_id"] for row in claim_rows]:
            raise RuntimeError(f"{slug}: semantic row id drift")
        if verdict.get("row_sha256s") != [row["row_sha256"] for row in claim_rows]:
            raise RuntimeError(f"{slug}: semantic row hash drift")
        if verdict.get("claim_object_sha256") != canonical_sha(claim_rows[0]["claim"]):
            raise RuntimeError(f"{slug}: semantic claim object drift")
        if any(row.get("verdict") != result for row in claim_rows):
            raise RuntimeError(f"{slug}: semantic/evidence verdict conflict")
    if semantic.get("verdict_counts") != verdict_counts:
        raise RuntimeError(f"{slug}: semantic verdict counts mismatch")

    return {
        "registry": registry,
        "coverage": coverage,
        "rows": rows,
        "drift": drift,
        "semantic": semantic,
        "verdict_counts": verdict_counts,
        "paths": {
            "registry": registry_path,
            "coverage": coverage_path,
            "rows": rows_path,
            "drift": drift_path,
            "semantic_audit": semantic_audit_path,
            "semantic": semantic_path,
        },
    }


def validate_report_and_passport(
    base: Path,
    slug: str,
    cfg: dict[str, Any],
    canonical: dict[str, str],
    core: dict[str, Any],
    declaration: dict[str, Any],
    summary_row: dict[str, Any],
    freeze_pointer: dict[str, str],
    repair_pointer: dict[str, str],
    declaration_pointer: dict[str, str],
    phase_ab_sha: str,
    phase_c_sha: str,
    originality_hashes: tuple[str, str],
    failure_sha: str,
) -> None:
    notes = base / "notes"
    report_path = require_regular(notes / "stage2_5_integrity_report.json")
    passport_path = require_regular(notes / "stage2_5_material_passport.json")
    compliance_path = require_regular(notes / "stage2_5_compliance_report.json")
    report_md_path = require_regular(notes / "stage2_5_integrity_report.md")
    closure_path = require_regular(notes / "stage2_5_experiment_provenance_closure.md")
    adjudication_path = require_regular(notes / "stage2_5_claim_registry_coverage_adjudication.md")
    report = load(report_path)
    passport = load(passport_path)
    compliance = load(compliance_path)
    if not all(isinstance(item, dict) for item in (report, passport, compliance)):
        raise RuntimeError(f"{slug}: generated JSON must be objects")

    if report.get("verdict") != "PASS" or report.get("mode") != "pre-review":
        raise RuntimeError(f"{slug}: wrong integrity report decision")
    if report.get("overall_issues") != {"SERIOUS": 0, "MAJOR": 0, "MEDIUM": 0, "MINOR": core["verdict_counts"]["MINOR_DISTORTION"]}:
        raise RuntimeError(f"{slug}: integrity severity totals mismatch")
    phases = report.get("phases", {})
    a = phases.get("A_references", {})
    if (
        a.get("checked"), a.get("verified"), a.get("plausible_bounded"),
        a.get("closed"), a.get("failed"), a.get("receipt_sha256")
    ) != (
        cfg["refs"], cfg["verified_refs"], cfg["plausible_refs"], cfg["refs"], 0,
        phase_ab_sha,
    ):
        raise RuntimeError(f"{slug}: report Phase-A mismatch")
    b = phases.get("B_citation_context", {})
    if (b.get("denominator"), b.get("sampled"), b.get("verified_with_boundaries")) != (
        cfg["contexts"], cfg["sampled_contexts"], cfg["sampled_contexts"]
    ):
        raise RuntimeError(f"{slug}: report Phase-B mismatch")
    c = phases.get("C_data", {})
    if (c.get("claim_surfaces_checked"), c.get("verified"), c.get("figure_table_trace_count"), c.get("trace_sha256")) != (
        cfg["phase_c"], cfg["phase_c"], cfg["table_traces"], phase_c_sha
    ):
        raise RuntimeError(f"{slug}: report Phase-C mismatch")
    c4 = phases.get("C4_experiment_intake", {})
    if (
        c4.get("claims_checked") != 1
        or c4.get("verified") != 1
        or c4.get("declaration") != declaration
        or c4.get("experiment_provenance") != []
        or c4.get("boundary") != PROVENANCE_BOUNDARY
    ):
        raise RuntimeError(f"{slug}: report C4 mismatch")
    d = phases.get("D_originality", {})
    if (
        d.get("sampled"), d.get("denominator"), d.get("major_sections_covered"),
        d.get("sample_sha256"), d.get("audit_sha256")
    ) != (
        cfg["originality"][0], cfg["originality"][1], 10,
        originality_hashes[0], originality_hashes[1]
    ):
        raise RuntimeError(f"{slug}: report originality mismatch")
    e = phases.get("E_claims", {})
    if (
        e.get("registered"), e.get("checked"), e.get("evidence_tuple_count"),
        e.get("anchorless_rows"), e.get("semantic_extraction_coverage")
    ) != (
        cfg["registered"], cfg["selected"], cfg["tuples"], cfg["tuples"],
        "not_machine_detectable"
    ):
        raise RuntimeError(f"{slug}: report Phase-E denominator mismatch")
    if e.get("evidence_rows") != core["rows"]:
        raise RuntimeError(f"{slug}: embedded evidence rows differ")
    semantic_pointer = e.get("semantic_verdict_receipt", {})
    if (
        semantic_pointer.get("sha256") != sha(core["paths"]["semantic"])
        or semantic_pointer.get("semantic_audit_sha256") != sha(core["paths"]["semantic_audit"])
    ):
        raise RuntimeError(f"{slug}: report semantic pointer drift")
    coverage_pointer = e.get("claim_registry_coverage", {})
    if (
        coverage_pointer.get("sha256") != sha(core["paths"]["coverage"])
        or coverage_pointer.get("registry_sha256") != sha(core["paths"]["registry"])
        or coverage_pointer.get("candidate_unregistered_count") != 0
        or coverage_pointer.get("adjudication_sha256") != sha(adjudication_path)
    ):
        raise RuntimeError(f"{slug}: report coverage pointer drift")
    if e.get("claim_strength_drift_findings", {}).get("sha256") != sha(core["paths"]["drift"]):
        raise RuntimeError(f"{slug}: report drift pointer mismatch")
    ext = report.get("extensions", {})
    if ext.get("input_freeze", {}).get("path") != freeze_pointer["path"] or ext.get("input_freeze", {}).get("sha256") != freeze_pointer["sha256"]:
        raise RuntimeError(f"{slug}: report freeze pointer mismatch")
    if ext.get("input_freeze", {}).get("canonical") != canonical:
        raise RuntimeError(f"{slug}: report canonical freeze mismatch")
    if ext.get("repair_receipt") != repair_pointer or ext.get("experiment_declaration_receipt") != declaration_pointer:
        raise RuntimeError(f"{slug}: report authority pointer mismatch")
    route = ext.get("route_crosswalk", {})
    if (
        route.get("formal_route_a_tuple_assigned") is not False
        or route.get("positive_arithmetic_A2") is not False
        or route.get("A3") is not False
        or route.get("A4") is not False
        or route.get("route_b") != "NOT_INVOKED"
        or route.get("route_a_sha256") != ROUTE_A_SHA
        or route.get("route_b_sha256") != ROUTE_B_SHA
    ):
        raise RuntimeError(f"{slug}: report route state mismatch")
    if ext.get("failure_modes") != {f"mode_{i}": "CLEAR" for i in range(1, 8)} or ext.get("failure_modes_sha256") != failure_sha:
        raise RuntimeError(f"{slug}: report failure-mode projection mismatch")
    assert_no_true_key(report, "stage3_authorized", f"{slug} report")

    compliance_schema = load(ARS / "shared/compliance_report.schema.json")
    jsonschema.Draft202012Validator(
        compliance_schema, format_checker=jsonschema.FormatChecker()
    ).validate(compliance)
    if compliance.get("overall_decision") != "warn" or compliance.get("raise", {}).get("mode") != "principles_only":
        raise RuntimeError(f"{slug}: compliance must remain warn-only principles-only")
    if passport.get("origin_skill") != "ars-codex:academic-research-suite" or passport.get("verification_status") != "VERIFIED":
        raise RuntimeError(f"{slug}: passport origin/status mismatch")
    if passport.get("content_hash") != canonical["manuscript_sha256"] or passport.get("repro_lock", "MISSING") is not None:
        raise RuntimeError(f"{slug}: passport content/repro-lock mismatch")
    if passport.get("experiment_intake_declaration") != declaration:
        raise RuntimeError(f"{slug}: passport experiment declaration mismatch")
    if passport.get("experiment_provenance") != [] or passport.get("experiment_alignment_results") != []:
        raise RuntimeError(f"{slug}: passport contains no-experiment provenance/alignment")
    if passport.get("claim_intent_manifests") != []:
        raise RuntimeError(f"{slug}: passport invents a gate-time manifest")
    if passport.get("compliance_history") != [compliance]:
        raise RuntimeError(f"{slug}: passport compliance history mismatch")
    extension = passport.get("round10_stage2_5", {})
    expected_artifacts = {
        "manuscript_sha256": canonical["manuscript_sha256"],
        "bibliography_sha256": canonical["bibliography_sha256"],
        "pdf_sha256": canonical["pdf_sha256"],
        "claim_registry_sha256": sha(core["paths"]["registry"]),
        "coverage_sha256": sha(core["paths"]["coverage"]),
        "evidence_rows_sha256": sha(core["paths"]["rows"]),
        "claim_strength_drift_sha256": sha(core["paths"]["drift"]),
        "semantic_audit_sha256": sha(core["paths"]["semantic_audit"]),
        "semantic_receipt_sha256": sha(core["paths"]["semantic"]),
        "phase_ab_sha256": phase_ab_sha,
        "phase_c_sha256": phase_c_sha,
        "originality_sample_sha256": originality_hashes[0],
        "originality_audit_sha256": originality_hashes[1],
        "failure_modes_sha256": failure_sha,
        "coverage_adjudication_sha256": sha(adjudication_path),
        "integrity_report_sha256": sha(report_path),
        "compliance_report_sha256": sha(compliance_path),
    }
    if extension.get("artifact_bindings") != expected_artifacts:
        raise RuntimeError(f"{slug}: passport artifact binding mismatch")
    if (
        extension.get("registered_claims"), extension.get("selected_claims"),
        extension.get("evidence_tuples"), extension.get("anchorless_rows"),
        extension.get("phase_c_claim_surfaces")
    ) != (cfg["registered"], cfg["selected"], cfg["tuples"], cfg["tuples"], cfg["phase_c"]):
        raise RuntimeError(f"{slug}: passport denominator mismatch")
    for key in ("formal_route_a_tuple_assigned", "positive_arithmetic_A2", "route_b_invoked", "stage3_authorized"):
        if extension.get(key) is not False:
            raise RuntimeError(f"{slug}: passport illegally sets {key}")
    run_checked(
        [sys.executable, str(ARS / "scripts/check_claim_audit_consistency.py"), "--passport", str(passport_path)],
        f"{slug} official passport consistency validation",
    )
    run_checked(
        [sys.executable, str(ARS / "scripts/check_experiment_provenance.py"), str(passport_path)],
        f"{slug} official experiment-provenance validation",
    )

    if (
        summary_row.get("integrity_report_sha256") != sha(report_path)
        or summary_row.get("material_passport_sha256") != sha(passport_path)
        or summary_row.get("compliance_report_sha256") != sha(compliance_path)
        or summary_row.get("semantic_receipt_sha256") != sha(core["paths"]["semantic"])
    ):
        raise RuntimeError(f"{slug}: batch paper hash pointer mismatch")
    report_md = report_md_path.read_text(encoding="utf-8")
    closure_md = closure_path.read_text(encoding="utf-8")
    for phrase in (
        "PASS AT THE MANDATORY STAGE-2.5 CHECKPOINT",
        "Stage 3 authorized: **no**",
        f"{cfg['tuples']}/{cfg['tuples']}",
        "anchorless",
        "Route A A0/A1",
    ):
        if phrase not in report_md:
            raise RuntimeError(f"{slug}: report Markdown missing {phrase!r}")
    if PROVENANCE_BOUNDARY not in closure_md or "no_experiments_declared" not in closure_md:
        raise RuntimeError(f"{slug}: experiment closure Markdown incomplete")


def main() -> int:
    batch_path = require_regular(ROOT / "BATCH_ROUND10_STAGE2_5_INTEGRITY_SUMMARY.json")
    batch_md_path = require_regular(ROOT / "BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md")
    checkpoint_path = require_regular(ROOT / "BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json")
    checkpoint_md_path = require_regular(ROOT / "BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.md")
    batch = load(batch_path)
    checkpoint = load(checkpoint_path)
    if not isinstance(batch, dict) or batch.get("schema") != "flow-systems-round10-stage2.5-integrity-summary/1.0":
        raise RuntimeError("batch summary schema mismatch")
    if batch.get("batch_verdict") != "PASS" or batch.get("checkpoint") != "MANDATORY_STAGE_2.5_COMPLETE":
        raise RuntimeError("batch integrity decision mismatch")
    assert_no_true_key(batch, "stage3_authorized", "batch summary")
    if batch.get("unresolved_findings") != {"SERIOUS": 0, "MAJOR": 0, "MEDIUM": 0}:
        raise RuntimeError("batch unresolved severity population mismatch")
    if batch.get("provenance_boundary") != PROVENANCE_BOUNDARY:
        raise RuntimeError("batch provenance boundary mismatch")
    compiler_path = ROOT / "tools/round10_stage2_5_compile_reports.py"
    if batch.get("compiler_sha256") != sha(compiler_path):
        raise RuntimeError("batch compiler hash is stale")

    freeze, declaration = validate_authorities(batch)
    route_a = ROOT / "skills/route-a-evaluator.md"
    route_b = ROOT / "skills/route-b-evaluator.md"
    crosswalk = ROOT / "BATCH_ROUND10_STAGE2_5_ROUTE_CROSSWALK.md"
    if sha(route_a) != ROUTE_A_SHA or sha(route_b) != ROUTE_B_SHA:
        raise RuntimeError("roadmap evaluator bytes changed")
    route = batch.get("route", {})
    if (
        route.get("route_a_sha256") != ROUTE_A_SHA
        or route.get("route_b_sha256") != ROUTE_B_SHA
        or route.get("crosswalk_sha256") != sha(crosswalk)
        or route.get("formal_tuple_assigned") is not False
        or route.get("positive_arithmetic_A2") is not False
        or route.get("A3") is not False
        or route.get("A4") is not False
        or route.get("route_b_invoked") is not False
    ):
        raise RuntimeError("batch Route-A/Route-B crosswalk mismatch")

    rows = batch.get("papers")
    if not isinstance(rows, list) or len(rows) != 5:
        raise RuntimeError("batch paper population malformed")
    by_slug = {row.get("paper"): row for row in rows if isinstance(row, dict)}
    if len(by_slug) != len(rows) or set(by_slug) != set(PAPERS):
        raise RuntimeError("batch paper population duplicate/mismatch")

    aggregate = {
        "papers": 0, "references_checked": 0, "references_verified": 0,
        "references_plausible": 0, "citation_contexts": 0,
        "contexts_sampled": 0, "registered_claims": 0, "selected_claims": 0,
        "evidence_tuples": 0, "anchorless_rows": 0,
        "phase_c_claim_surfaces": 0, "originality_sampled": 0,
        "originality_denominator": 0, "figure_table_traces": 0,
        "scientific_executions": 0, "formal_route_a_tuples": 0,
        "positive_arithmetic_a2": 0, "route_b_invocations": 0,
    }
    results: list[dict[str, Any]] = []
    for slug, cfg in PAPERS.items():
        row = by_slug[slug]
        base = ROOT / "papers" / slug
        manuscript = require_regular(base / "paper/manuscript.tex")
        bibliography = require_regular(base / "paper/references.bib")
        pdf = require_regular(base / "paper/paper.pdf")
        canonical = {
            "manuscript_sha256": sha(manuscript),
            "bibliography_sha256": sha(bibliography),
            "pdf_sha256": sha(pdf),
        }
        for key, value in canonical.items():
            if freeze[slug].get(key) != value:
                raise RuntimeError(f"{slug}: final freeze mismatch for {key}")
        core = validate_claim_core(base, slug, cfg, manuscript)
        notes = base / "notes"
        phase_ab_sha = validate_phase_ab(notes, slug, cfg, canonical)
        phase_c_sha = validate_phase_c(
            notes,
            slug,
            cfg,
            {**canonical, "claim_registry_sha256": sha(core["paths"]["registry"])},
            declaration,
        )
        originality_hashes = validate_originality(
            notes, slug, cfg, canonical["manuscript_sha256"]
        )
        failure_sha = validate_failure_modes(notes, slug, canonical["manuscript_sha256"])
        validate_report_and_passport(
            base,
            slug,
            cfg,
            canonical,
            core,
            declaration,
            row,
            batch["input_freeze"],
            batch["repair_receipt"],
            batch["experiment_declaration_receipt"],
            phase_ab_sha,
            phase_c_sha,
            originality_hashes,
            failure_sha,
        )

        expected_row = {
            "paper": slug,
            "paper_id": cfg["paper_id"],
            "number": cfg["number"],
            "verdict": "PASS",
            "registered_claims": cfg["registered"],
            "selected_claims": cfg["selected"],
            "evidence_tuples": cfg["tuples"],
            "anchorless_rows": cfg["tuples"],
            "references_checked": cfg["refs"],
            "references_verified": cfg["verified_refs"],
            "references_plausible": cfg["plausible_refs"],
            "contexts_sampled": cfg["sampled_contexts"],
            "phase_c_claim_surfaces": cfg["phase_c"],
            "originality_sampled": cfg["originality"][0],
            "originality_denominator": cfg["originality"][1],
            "figure_table_traces": cfg["table_traces"],
            "active_issue_ids": [],
            "integrity_report_sha256": row.get("integrity_report_sha256"),
            "material_passport_sha256": row.get("material_passport_sha256"),
            "compliance_report_sha256": row.get("compliance_report_sha256"),
            "semantic_receipt_sha256": row.get("semantic_receipt_sha256"),
        }
        if row != expected_row:
            raise RuntimeError(f"{slug}: batch paper row has injected/incorrect fields")

        aggregate["papers"] += 1
        aggregate["references_checked"] += cfg["refs"]
        aggregate["references_verified"] += cfg["verified_refs"]
        aggregate["references_plausible"] += cfg["plausible_refs"]
        aggregate["citation_contexts"] += cfg["contexts"]
        aggregate["contexts_sampled"] += cfg["sampled_contexts"]
        aggregate["registered_claims"] += cfg["registered"]
        aggregate["selected_claims"] += cfg["selected"]
        aggregate["evidence_tuples"] += cfg["tuples"]
        aggregate["anchorless_rows"] += cfg["tuples"]
        aggregate["phase_c_claim_surfaces"] += cfg["phase_c"]
        aggregate["originality_sampled"] += cfg["originality"][0]
        aggregate["originality_denominator"] += cfg["originality"][1]
        aggregate["figure_table_traces"] += cfg["table_traces"]
        results.append(
            {
                "paper": cfg["paper_id"],
                "registered": cfg["registered"],
                "selected": cfg["selected"],
                "tuples": cfg["tuples"],
                "status": "PASS",
            }
        )

    if aggregate != EXPECTED_AGGREGATE or batch.get("aggregate") != aggregate:
        raise RuntimeError(f"batch aggregate mismatch: {aggregate}")
    nonblocking = batch.get("nonblocking_findings")
    if (
        not isinstance(nonblocking, list)
        or len(nonblocking) != 1
        or nonblocking[0].get("finding_id") != "ROUND10-D-STANDARDIZED-DECLARATION-BOILERPLATE"
        or nonblocking[0].get("severity") != "MINOR"
    ):
        raise RuntimeError("batch nonblocking originality finding mismatch")

    if not isinstance(checkpoint, dict) or checkpoint.get("schema") != "flow-systems-round10-stage2.5-mandatory-checkpoint/1.0":
        raise RuntimeError("mandatory checkpoint schema mismatch")
    if (
        checkpoint.get("decision") != "PASS_AT_STAGE_2.5_CHECKPOINT"
        or checkpoint.get("mandatory_stop") is not True
        or checkpoint.get("stage3_authorized") is not False
        or checkpoint.get("scholar_confirmation_required") is not True
    ):
        raise RuntimeError("mandatory checkpoint decision mismatch")
    if checkpoint.get("integrity_summary") != {"path": batch_path.name, "sha256": sha(batch_path)}:
        raise RuntimeError("checkpoint summary pointer mismatch")
    if checkpoint.get("integrity_report") != {"path": batch_md_path.name, "sha256": sha(batch_md_path)}:
        raise RuntimeError("checkpoint report pointer mismatch")
    if (
        checkpoint.get("input_freeze") != batch.get("input_freeze")
        or checkpoint.get("repair_receipt") != batch.get("repair_receipt")
        or checkpoint.get("experiment_declaration_receipt") != batch.get("experiment_declaration_receipt")
    ):
        raise RuntimeError("checkpoint authority pointer mismatch")
    expected_checkpoint_papers = [
        {
            "paper": slug,
            "passport_sha256": by_slug[slug]["material_passport_sha256"],
            "integrity_report_sha256": by_slug[slug]["integrity_report_sha256"],
        }
        for slug in PAPERS
    ]
    if checkpoint.get("papers") != expected_checkpoint_papers:
        raise RuntimeError("checkpoint paper pointer population mismatch")
    if checkpoint.get("route_state") != {
        "formal_route_a_tuples": 0,
        "positive_arithmetic_a2": 0,
        "route_b_invocations": 0,
    }:
        raise RuntimeError("checkpoint route state mismatch")
    assert_no_true_key(checkpoint, "stage3_authorized", "checkpoint")

    batch_md = batch_md_path.read_text(encoding="utf-8")
    checkpoint_md = checkpoint_md_path.read_text(encoding="utf-8")
    for phrase in (
        "PASS AT THE MANDATORY STAGE-2.5 CHECKPOINT",
        "116/116 references closed",
        "480 claims registered",
        "382 distinct",
        "454/454 evidence tuples",
        "Formal\nRoute-A tuples: **0/5**",
        ROUTE_A_SHA,
        ROUTE_B_SHA,
    ):
        if phrase not in batch_md:
            raise RuntimeError(f"batch Markdown missing {phrase!r}")
    for phrase in (
        "Decision: **PASS**",
        f"Summary SHA-256: `{sha(batch_path)}`",
        f"Report SHA-256: `{sha(batch_md_path)}`",
        "stage3_authorized=false",
    ):
        if phrase not in checkpoint_md:
            raise RuntimeError(f"checkpoint Markdown missing {phrase!r}")

    print(
        json.dumps(
            {"status": "PASS", "aggregate": aggregate, "papers": results},
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
