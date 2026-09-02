#!/usr/bin/env python3
"""Compile Round-10 (P29--P33) ARS Stage-2.5 integrity reports.

This is a report compiler, not an adjudicator.  It refuses to write anything
unless all five final audit receipts already exist, the final post-repair
freeze matches the current canonical bytes, the scholar's no-experiment
declaration is valid, and every registered selected claim has a passing,
hash-bound semantic receipt.  It never edits manuscripts, bibliographies,
PDFs, results, README files, roadmaps, or pipeline state.

Required per-paper machine inputs (under ``notes/``):

* ``stage2_5_phase_ab_final.json``
* ``stage2_5_phase_c_data_trace.json`` (the legacy alias
  ``stage2_5_phase_c_trace.json`` is accepted only when the canonical name is
  absent)
* the Claim Registry, coverage, evidence-row, drift, originality, semantic,
  and seven-failure-mode carriers named below.

The final freeze and repair receipt are discovered by content, not by a fixed
canonical hash.  ``ROUND10_STAGE2_5_FREEZE`` and
``ROUND10_STAGE2_5_REPAIR_RECEIPT`` may name explicit workspace-relative
files.  Auto-discovery deliberately fails on ambiguity.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
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
DECLARATION_PATH = ROOT / "BATCH_ROUND10_STAGE2_5_EXPERIMENT_DECLARATION_RECEIPT.json"
CORRECTION_REQUEST_PATH = ROOT / "BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_REQUEST.md"
ROUTE_CROSSWALK_PATH = ROOT / "BATCH_ROUND10_STAGE2_5_ROUTE_CROSSWALK.md"
REQUIRED_REPAIR_FINDINGS = {
    "P29-AB-MEDIUM-01",
    "P31-E1-056",
    "P31-E1-078",
    "P32-AB-MINOR-01",
}


PAPERS: dict[str, dict[str, Any]] = {
    "29-bianchi-ideal-owner-refinement": {
        "paper_id": "P29",
        "number": 29,
        "title": "Literal Gaussian-prime-ideal ownership in a level-(3) Bianchi flow",
        "references": 22,
        "references_verified": 22,
        "references_plausible": 0,
        "citation_contexts": 22,
        "contexts_sampled": 7,
        "registered": 83,
        "high": 68,
        "random": 3,
        "selected": 71,
        "tuples": 71,
        "phase_c_claims": 45,
        "originality": (23, 75),
        "table_traces": 0,
        "e6_revision_evidence_available": False,
        "subtype": (
            "level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic "
            "arclength; inversion-paired primitive loxodromic owners; one literal "
            "nonzero Gaussian prime ideal"
        ),
    },
    "30-three-disk-nonconstant-roof-determinant": {
        "paper_id": "P30",
        "number": 30,
        "title": "A nonconstant-roof determinant architecture for three-disk scattering",
        "references": 26,
        "references_verified": 26,
        "references_plausible": 0,
        "citation_contexts": 26,
        "contexts_sampled": 8,
        "registered": 95,
        "high": 75,
        "random": 3,
        "selected": 78,
        "tuples": 78,
        "phase_c_claims": 53,
        "originality": (27, 87),
        "table_traces": 0,
        "e6_revision_evidence_available": False,
        "subtype": (
            "no-eclipse equilateral three-disk scattering at d=6a; Euclidean "
            "free-flight time; cyclic collision owners; physical roof kept "
            "distinct from the unit-roof symbolic control"
        ),
    },
    "31-level11-conjugacy-owner-ledger": {
        "paper_id": "P31",
        "number": 31,
        "title": "A conjugacy-owner ledger for a level-11 time-changed flow",
        "references": 22,
        "references_verified": 22,
        "references_plausible": 0,
        "citation_contexts": 22,
        "contexts_sampled": 7,
        "registered": 78,
        "high": 68,
        "random": 3,
        "selected": 71,
        "tuples": 89,
        "phase_c_claims": 45,
        "originality": (21, 67),
        "table_traces": 0,
        "e6_revision_evidence_available": False,
        "integrity_corrected_without_revision_evidence_bundle": True,
        "subtype": (
            "positive time change of the Gamma_0(11) flow; oriented primitive "
            "owners; inverse kept separate; powers are repetitions; Hecke degree "
            "is not an owner"
        ),
    },
    "32-homology-cover-renormalization-uniformity": {
        "paper_id": "P32",
        "number": 32,
        "title": "Uniform renormalization over genus-two homology covers",
        "references": 26,
        "references_verified": 26,
        "references_plausible": 0,
        "citation_contexts": 26,
        "contexts_sampled": 8,
        "registered": 98,
        "high": 85,
        "random": 3,
        "selected": 88,
        "tuples": 108,
        "phase_c_claims": 58,
        "originality": (24, 77),
        "table_traces": 0,
        "e6_revision_evidence_available": False,
        "integrity_corrected_without_revision_evidence_bundle": True,
        "subtype": (
            "pure genus-two homology covers H_N; all-content oriented primitive "
            "owners; 1/N time scaling; 1/N^3 logarithmic normalization"
        ),
    },
    "33-bolza-control-matched-census": {
        "paper_id": "P33",
        "number": 33,
        "title": "A control-matched Bolza owner-census architecture",
        "references": 20,
        "references_verified": 19,
        "references_plausible": 1,
        "citation_contexts": 48,
        "contexts_sampled": 18,
        "registered": 126,
        "high": 68,
        "random": 6,
        "selected": 74,
        "tuples": 108,
        "phase_c_claims": 43,
        "originality": (21, 68),
        "table_traces": 2,
        "e6_revision_evidence_available": False,
        "subtype": (
            "Bolza b=1/2 even signed-field target plus source-locked control; "
            "unit-speed base time; inverse-paired owners; target-blind Lambda=21/10"
        ),
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


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def require_regular(path: Path) -> Path:
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"required regular file missing or symlinked: {path}")
    return path


def load_json(path: Path) -> Any:
    require_regular(path)
    try:
        return json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise RuntimeError(f"invalid JSON input {path}: {exc}") from exc


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def json_bytes(value: Any) -> bytes:
    return json_text(value).encode("utf-8")


def canonical_sha(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def sha(path: Path) -> str:
    require_regular(path)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def utc_now() -> str:
    return (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


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


def deep_strings(value: Any) -> set[str]:
    return {item for item in deep_scalars(value) if isinstance(item, str)}


def get_any(mapping: dict[str, Any], keys: tuple[str, ...], label: str) -> Any:
    present = [key for key in keys if key in mapping]
    if not present:
        raise RuntimeError(f"missing {label}; expected one of {keys}")
    values = [mapping[key] for key in present]
    if any(value != values[0] for value in values[1:]):
        raise RuntimeError(f"conflicting aliases for {label}: {present}")
    return values[0]


def safe_workspace_path(raw: str, label: str) -> Path:
    path = Path(raw)
    path = path if path.is_absolute() else ROOT / path
    resolved = path.resolve()
    try:
        resolved.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise RuntimeError(f"{label} escapes workspace: {raw}") from exc
    return require_regular(resolved)


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


def discover_repair_receipt() -> tuple[Path, dict[str, Any]]:
    explicit = os.environ.get("ROUND10_STAGE2_5_REPAIR_RECEIPT")
    if explicit:
        candidates = [safe_workspace_path(explicit, "repair receipt")]
    else:
        candidates = sorted(
            {
                *ROOT.glob("BATCH_ROUND10_STAGE2_5*REPAIR*RECEIPT*.json"),
                *ROOT.glob("BATCH_ROUND10_STAGE2_5*CORRECTION*RECEIPT*.json"),
            }
        )
    request_sha = sha(CORRECTION_REQUEST_PATH)
    matches: list[tuple[Path, dict[str, Any]]] = []
    for path in candidates:
        value = load_json(path)
        if not isinstance(value, dict):
            continue
        strings = deep_strings(value)
        schema = str(value.get("schema", "")).lower()
        if (
            "round10" in schema
            and ("repair" in schema or "correction" in schema)
            and request_sha in strings
            and REQUIRED_REPAIR_FINDINGS <= strings
        ):
            matches.append((path, value))
    if len(matches) != 1:
        raise RuntimeError(
            "expected exactly one hash-bound Round-10 repair receipt covering "
            f"{sorted(REQUIRED_REPAIR_FINDINGS)}; found {[str(p) for p, _ in matches]}"
        )
    path, value = matches[0]
    if value.get("stage3_authorized") is not False:
        raise RuntimeError("repair receipt must state stage3_authorized=false")
    for key in (
        "scientific_execution_authorized",
        "route_a_tuple_authorized",
        "route_b_authorized",
    ):
        if key in value and value[key] is not False:
            raise RuntimeError(f"repair receipt illegally enables {key}")
    confirmation = value.get("scholar_confirmation_text")
    status = str(value.get("authorization_status", value.get("status", ""))).upper()
    if not (isinstance(confirmation, str) and confirmation.strip()):
        raise RuntimeError("repair receipt lacks the scholar confirmation text")
    if value.get("authorized") is not True and status not in {
        "AUTHORIZED",
        "APPROVED",
        "CONFIRMED",
        "COMPLETE",
    }:
        # The finding population and signed request are necessary but not a
        # substitute for an explicit authorization state.
        raise RuntimeError("repair receipt lacks an explicit authorized status")
    return path, value


def _freeze_rows(value: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rows = value.get("papers")
    if not isinstance(rows, list) or len(rows) != len(PAPERS):
        raise RuntimeError("input freeze must contain exactly five paper rows")
    result: dict[str, dict[str, Any]] = {}
    by_id = {cfg["paper_id"]: slug for slug, cfg in PAPERS.items()}
    for row in rows:
        if not isinstance(row, dict):
            raise RuntimeError("input freeze paper row must be an object")
        slug = row.get("slug")
        if slug is None:
            slug = by_id.get(row.get("paper"))
        if slug not in PAPERS or slug in result:
            raise RuntimeError(f"input freeze paper population error at {slug!r}")
        result[slug] = row
    if set(result) != set(PAPERS):
        raise RuntimeError("input freeze paper population mismatch")
    return result


def _freeze_matches_current(value: dict[str, Any]) -> bool:
    try:
        rows = _freeze_rows(value)
        for slug in PAPERS:
            base = ROOT / "papers" / slug / "paper"
            row = rows[slug]
            if row.get("manuscript_sha256") != sha(base / "manuscript.tex"):
                return False
            if row.get("bibliography_sha256") != sha(base / "references.bib"):
                return False
            if row.get("pdf_sha256") != sha(base / "paper.pdf"):
                return False
        return True
    except RuntimeError:
        return False


def discover_final_freeze(
    repair_path: Path, repair: dict[str, Any]
) -> tuple[Path, dict[str, Any], dict[str, dict[str, Any]]]:
    explicit = os.environ.get("ROUND10_STAGE2_5_FREEZE")
    candidates = (
        [safe_workspace_path(explicit, "input freeze")]
        if explicit
        else sorted(ROOT.glob("BATCH_ROUND10_STAGE2_5*INPUT_FREEZE*.json"))
    )
    repair_sha = sha(repair_path)
    declaration_sha = sha(DECLARATION_PATH)
    matches: list[tuple[Path, dict[str, Any]]] = []
    for path in candidates:
        value = load_json(path)
        if not isinstance(value, dict):
            continue
        schema = str(value.get("schema", "")).lower()
        strings = deep_strings(value)
        if (
            "round10" in schema
            and "input-freeze" in schema
            and repair_sha in strings
            and declaration_sha in strings
            and _freeze_matches_current(value)
        ):
            matches.append((path, value))
    if len(matches) != 1:
        raise RuntimeError(
            "expected exactly one current post-repair input freeze bound to the "
            f"repair and declaration receipts; found {[str(p) for p, _ in matches]}"
        )
    path, value = matches[0]
    rows = _freeze_rows(value)
    if value.get("route_a_sha256") != ROUTE_A_SHA:
        raise RuntimeError("post-repair freeze Route-A hash mismatch")
    if value.get("route_b_sha256") != ROUTE_B_SHA:
        raise RuntimeError("post-repair freeze Route-B hash mismatch")
    aggregate = value.get("aggregate", {})
    for key in (
        "scientific_executions",
        "formal_route_a_tuples",
        "positive_arithmetic_a2",
        "route_b_invocations",
    ):
        if key in aggregate and exact_int(aggregate[key], f"freeze aggregate {key}") != 0:
            raise RuntimeError(f"post-repair freeze illegally advances {key}")
    return path, value, rows


def validate_scholar_declaration() -> tuple[dict[str, Any], dict[str, str]]:
    receipt = load_json(DECLARATION_PATH)
    if not isinstance(receipt, dict):
        raise RuntimeError("experiment declaration receipt must be an object")
    declaration = receipt.get("experiment_intake_declaration")
    if not isinstance(declaration, dict) or set(declaration) != {
        "status",
        "declared_by",
        "declared_at",
    }:
        raise RuntimeError("invalid experiment intake declaration shape")
    if declaration.get("status") != "no_experiments_declared":
        raise RuntimeError("Round 10 requires status=no_experiments_declared")
    if declaration.get("declared_by") != "scholar":
        raise RuntimeError("experiment declaration must be scholar-owned")
    if not re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
        str(declaration.get("declared_at", "")),
    ):
        raise RuntimeError("invalid experiment declaration timestamp")
    if receipt.get("experiment_provenance") != []:
        raise RuntimeError("no-experiment declaration requires empty provenance")
    if receipt.get("boundary") != PROVENANCE_BOUNDARY:
        raise RuntimeError("experiment declaration loses the required C4 boundary")
    if receipt.get("stage3_authorized") is not False:
        raise RuntimeError("experiment declaration must not authorize Stage 3")
    for key in (
        "scientific_execution_authorized",
        "canonical_scientific_content_mutation_authorized",
        "route_a_tuple_authorized",
        "route_b_authorized",
    ):
        if receipt.get(key) is not False:
            raise RuntimeError(f"experiment declaration must state {key}=false")
    return declaration, {"path": DECLARATION_PATH.name, "sha256": sha(DECLARATION_PATH)}


def validate_route_inputs() -> dict[str, str]:
    route_a = ROOT / "skills/route-a-evaluator.md"
    route_b = ROOT / "skills/route-b-evaluator.md"
    if sha(route_a) != ROUTE_A_SHA or sha(route_b) != ROUTE_B_SHA:
        raise RuntimeError("roadmap evaluator changed; adjudicate it before compilation")
    text = require_regular(ROUTE_CROSSWALK_PATH).read_text(encoding="utf-8")
    required = (
        r"formal\s+Route-A\s+tuples\s+assigned:\s+\*\*0/5\*\*",
        r"candidates\s+with\s+positive\s+arithmetic\s+A2:\s+\*\*0/5\*\*",
        r"A3\s+global\s+analytic/determinant\s+closure\s+attempts:\s+\*\*0/5\*\*",
        r"A4\s+natural\s+liftability\s+evaluations:\s+\*\*0/5\*\*",
        r"Route-B\s+invocations:\s+\*\*0/5\*\*",
    )
    for pattern in required:
        if not re.search(pattern, text, flags=re.IGNORECASE):
            raise RuntimeError(f"Route crosswalk missing frozen state pattern: {pattern}")
    return {
        "route_a_sha256": ROUTE_A_SHA,
        "route_b_sha256": ROUTE_B_SHA,
        "crosswalk_path": ROUTE_CROSSWALK_PATH.name,
        "crosswalk_sha256": sha(ROUTE_CROSSWALK_PATH),
    }


def validate_bindings(
    label: str,
    bindings: dict[str, Any],
    expected: dict[str, str],
) -> None:
    if not isinstance(bindings, dict):
        raise RuntimeError(f"{label}: bindings must be an object")
    for key, value in expected.items():
        if bindings.get(key) != value:
            raise RuntimeError(f"{label}: stale or missing binding {key}")


def validate_phase_ab(
    slug: str, cfg: dict[str, Any], hashes: dict[str, str]
) -> tuple[dict[str, Any], Path]:
    notes = ROOT / "papers" / slug / "notes"
    path = notes / "stage2_5_phase_ab_final.json"
    receipt = load_json(path)
    if not isinstance(receipt, dict):
        raise RuntimeError(f"{slug}: Phase A/B receipt must be an object")
    if receipt.get("paper") not in {slug, cfg["paper_id"]}:
        raise RuntimeError(f"{slug}: Phase A/B receipt paper mismatch")
    if str(receipt.get("decision", "")).upper() != "PASS":
        raise RuntimeError(f"{slug}: Phase A/B receipt is not PASS")
    validate_bindings(f"{slug} Phase A/B", receipt.get("bindings"), hashes)
    if receipt.get("unresolved_findings") != []:
        raise RuntimeError(f"{slug}: unresolved Phase A/B finding remains")
    phase_a = receipt.get("phase_a")
    phase_b = receipt.get("phase_b")
    if not isinstance(phase_a, dict) or not isinstance(phase_b, dict):
        raise RuntimeError(f"{slug}: Phase A/B subrecords missing")
    checked = exact_int(
        get_any(phase_a, ("references_checked", "checked"), "references checked"),
        f"{slug} references checked",
    )
    verified = exact_int(
        get_any(phase_a, ("references_verified", "verified"), "references verified"),
        f"{slug} references verified",
    )
    plausible = exact_int(
        phase_a.get("references_plausible", phase_a.get("plausible", 0)),
        f"{slug} references plausible",
    )
    if (checked, verified, plausible) != (
        cfg["references"],
        cfg["references_verified"],
        cfg["references_plausible"],
    ):
        raise RuntimeError(f"{slug}: exact Phase-A denominators mismatch")
    if verified + plausible != checked:
        raise RuntimeError(f"{slug}: Phase-A reference population not closed")
    if phase_a.get("unresolved_findings", []) != []:
        raise RuntimeError(f"{slug}: Phase-A unresolved finding remains")
    total = exact_int(
        get_any(
            phase_b,
            ("citation_contexts", "contexts_total", "denominator"),
            "citation context denominator",
        ),
        f"{slug} citation contexts",
    )
    sampled = exact_int(
        get_any(phase_b, ("contexts_sampled", "sampled"), "contexts sampled"),
        f"{slug} contexts sampled",
    )
    supported = exact_int(
        get_any(
            phase_b,
            ("contexts_supported", "supported", "verified"),
            "contexts supported",
        ),
        f"{slug} contexts supported",
    )
    if (total, sampled, supported) != (
        cfg["citation_contexts"],
        cfg["contexts_sampled"],
        cfg["contexts_sampled"],
    ):
        raise RuntimeError(f"{slug}: exact Phase-B denominators mismatch")
    if phase_b.get("unresolved_findings", []) != []:
        raise RuntimeError(f"{slug}: Phase-B unresolved finding remains")
    blocking_terms = {
        str(row.get("severity", "")).upper()
        for row in receipt.get("findings", [])
        if isinstance(row, dict) and row.get("status") not in {"RESOLVED", "CLOSED"}
    }
    if blocking_terms & {"SERIOUS", "MAJOR", "MEDIUM"}:
        raise RuntimeError(f"{slug}: unresolved blocking Phase-A/B severity")
    return receipt, path


def phase_c_path(notes: Path) -> Path:
    canonical = notes / "stage2_5_phase_c_data_trace.json"
    alias = notes / "stage2_5_phase_c_trace.json"
    if canonical.is_file() and alias.is_file():
        raise RuntimeError(
            f"{notes.parent.name}: both Phase-C names exist; remove the ambiguous alias"
        )
    return canonical if canonical.is_file() else alias


def validate_phase_c(
    slug: str,
    cfg: dict[str, Any],
    hashes: dict[str, str],
    declaration: dict[str, Any],
) -> tuple[dict[str, Any], Path]:
    notes = ROOT / "papers" / slug / "notes"
    path = phase_c_path(notes)
    receipt = load_json(path)
    if not isinstance(receipt, dict):
        raise RuntimeError(f"{slug}: Phase-C trace must be an object")
    if receipt.get("paper") not in {slug, cfg["paper_id"]}:
        raise RuntimeError(f"{slug}: Phase-C paper mismatch")
    if str(receipt.get("decision", receipt.get("verdict", ""))).upper() != "PASS":
        raise RuntimeError(f"{slug}: Phase-C trace is not PASS")
    bindings = receipt.get("bindings", {})
    validate_bindings(
        f"{slug} Phase C",
        bindings,
        {
            "manuscript_sha256": hashes["manuscript_sha256"],
            "claim_registry_sha256": hashes["claim_registry_sha256"],
        },
    )
    checked = exact_int(
        get_any(
            receipt,
            (
                "claim_surfaces_checked",
                "claims_checked",
                "quantitative_data_claims_checked",
            ),
            "Phase-C claim surfaces checked",
        ),
        f"{slug} Phase-C checked",
    )
    verified = exact_int(
        get_any(
            receipt,
            ("claim_surfaces_verified", "verified", "claims_verified"),
            "Phase-C claim surfaces verified",
        ),
        f"{slug} Phase-C verified",
    )
    if (checked, verified) != (cfg["phase_c_claims"], cfg["phase_c_claims"]):
        raise RuntimeError(f"{slug}: Phase-C exact denominator mismatch")
    if receipt.get("unresolved_findings") != []:
        raise RuntimeError(f"{slug}: unresolved Phase-C finding remains")
    if receipt.get("experiment_intake_declaration") != declaration:
        raise RuntimeError(f"{slug}: Phase-C experiment declaration mismatch")
    if receipt.get("experiment_provenance") != []:
        raise RuntimeError(f"{slug}: no-experiment Phase-C trace has provenance")
    if receipt.get("boundary") != PROVENANCE_BOUNDARY:
        raise RuntimeError(f"{slug}: Phase-C trace loses the C4 boundary")
    traces = receipt.get("figure_table_trace")
    if not isinstance(traces, list) or len(traces) != cfg["table_traces"]:
        raise RuntimeError(f"{slug}: exact figure/table trace denominator mismatch")
    identifiers: set[str] = set()
    for index, row in enumerate(traces):
        if not isinstance(row, dict) or not row:
            raise RuntimeError(f"{slug}: malformed figure/table trace {index}")
        identifier = str(
            row.get(
                "artifact_id",
                row.get("trace_id", row.get("table_id", row.get("locator", ""))),
            )
        )
        if not identifier or identifier in identifiers:
            raise RuntimeError(f"{slug}: duplicate/unidentified figure-table trace")
        identifiers.add(identifier)
        for status_key in ("decision", "verdict", "status", "trace_status"):
            status = row.get(status_key)
            if isinstance(status, str) and status.upper() in {
                "FAIL",
                "FAILED",
                "UNRESOLVED",
                "UNSUPPORTED",
                "NOT_VERIFIED",
            }:
                raise RuntimeError(
                    f"{slug}: non-passing figure/table trace {identifier}"
                )
    return receipt, path


def _validate_originality(
    slug: str, cfg: dict[str, Any], manuscript_sha: str
) -> tuple[dict[str, Any], Path, Path, dict[str, int]]:
    notes = ROOT / "papers" / slug / "notes"
    sample_path = notes / "stage2_5_originality_sample.json"
    audit_path = notes / "stage2_5_originality_audit.md"
    sample = load_json(sample_path)
    if not isinstance(sample, dict) or sample.get("paper") != slug:
        raise RuntimeError(f"{slug}: originality sample paper mismatch")
    if sample.get("manuscript_sha256") != manuscript_sha:
        raise RuntimeError(f"{slug}: stale originality sample")
    selected, denominator = cfg["originality"]
    if exact_int(sample.get("body_paragraph_denominator"), f"{slug} originality denominator") != denominator:
        raise RuntimeError(f"{slug}: originality denominator mismatch")
    rows = sample.get("samples")
    if not isinstance(rows, list) or len(rows) != selected:
        raise RuntimeError(f"{slug}: originality sample count mismatch")
    ids: set[str] = set()
    verdict_counts: dict[str, int] = {}
    sections: set[str] = set()
    for row in rows:
        if not isinstance(row, dict):
            raise RuntimeError(f"{slug}: malformed originality row")
        sample_id = row.get("sample_id")
        if not isinstance(sample_id, str) or not sample_id or sample_id in ids:
            raise RuntimeError(f"{slug}: duplicate originality sample id")
        ids.add(sample_id)
        if not str(row.get("search_status", "")).startswith("COMPLETED"):
            raise RuntimeError(f"{slug}: incomplete WebSearch sample {sample_id}")
        verdict = str(row.get("verdict", ""))
        if verdict not in {"ORIGINAL", "COMMON_KNOWLEDGE", "PARAPHRASE"}:
            raise RuntimeError(f"{slug}: blocking originality verdict {verdict}")
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1
        section = row.get("major_section")
        if not isinstance(section, str) or not section.strip():
            raise RuntimeError(f"{slug}: originality sample lacks section")
        sections.add(section)
        if not re.fullmatch(r"[0-9a-f]{64}", str(row.get("paragraph_sha256", ""))):
            raise RuntimeError(f"{slug}: invalid originality paragraph hash")
    if len(sections) != 10:
        raise RuntimeError(f"{slug}: originality sample does not cover 10/10 major sections")
    audit_text = require_regular(audit_path).read_text(encoding="utf-8")
    denominator_prose = re.search(
        rf"(?is)denominator\D{{0,40}}{denominator}\b.*?sample\D{{0,40}}{selected}\s+paragraph",
        audit_text,
    )
    if manuscript_sha not in audit_text or not (
        f"{selected}/{denominator}" in audit_text or denominator_prose
    ):
        raise RuntimeError(f"{slug}: stale or denominator-free originality audit")
    return sample, sample_path, audit_path, verdict_counts


def _validate_failure_modes(slug: str, manuscript_sha: str) -> Path:
    path = ROOT / "papers" / slug / "notes/stage2_5_seven_failure_mode_final.md"
    text = require_regular(path).read_text(encoding="utf-8")
    if manuscript_sha not in text:
        raise RuntimeError(f"{slug}: stale seven-failure-mode sidecar")
    for mode in range(1, 8):
        pattern = rf"(?mi)^\|\s*{mode}(?:\.|\s*[—–-])[^|]*\|\s*(?:\*\*)?CLEAR(?:\*\*)?\s*\|"
        if not re.search(pattern, text):
            raise RuntimeError(f"{slug}: failure mode {mode} is not individually CLEAR")
    if not re.search(r"(?mi)^\|\s*CLEAR\s*\|\s*7\s*\|", text):
        raise RuntimeError(f"{slug}: seven-mode CLEAR aggregate missing")
    for label in ("SUSPECTED", "INSUFFICIENT EVIDENCE"):
        if not re.search(rf"(?mi)^\|\s*{re.escape(label)}\s*\|\s*0\s*\|", text):
            raise RuntimeError(f"{slug}: seven-mode {label}=0 aggregate missing")
    return path


def _validate_claim_artifacts(
    slug: str,
    cfg: dict[str, Any],
    manuscript: Path,
    repair_path: Path,
) -> dict[str, Any]:
    notes = ROOT / "papers" / slug / "notes"
    registry_path = notes / "stage2_5_claim_registry.json"
    coverage_path = notes / "stage2_5_claim_registry_coverage.json"
    rows_path = notes / "stage2_5_evidence_rows.json"
    drift_path = notes / "stage2_5_claim_strength_drift_findings.json"
    semantic_audit_path = notes / "stage2_5_phase_e_semantic_audit.md"
    semantic_receipt_path = notes / "stage2_5_phase_e_semantic_verdicts.json"

    registry = load_json(registry_path)
    coverage = load_json(coverage_path)
    rows = load_json(rows_path)
    drift = load_json(drift_path)
    semantic = load_json(semantic_receipt_path)
    require_regular(semantic_audit_path)

    claim_schema = load_json(ARS / "shared/contracts/evidence/claim_registry.schema.json")
    jsonschema.Draft202012Validator(claim_schema).validate(registry)
    claims = registry.get("claims")
    if not isinstance(claims, list) or len(claims) != cfg["registered"]:
        raise RuntimeError(f"{slug}: registered claim denominator mismatch")
    claim_ids = [claim.get("claim_id") for claim in claims]
    if len(set(claim_ids)) != len(claim_ids):
        raise RuntimeError(f"{slug}: duplicate registry claim id")
    selected = [claim for claim in claims if claim.get("selection_tier") != "NOT-SELECTED"]
    if len(selected) != cfg["selected"]:
        raise RuntimeError(f"{slug}: selected claim denominator mismatch")
    tiers: dict[str, int] = {}
    manuscript_bytes = manuscript.read_bytes()
    for claim in claims:
        tier = str(claim.get("selection_tier"))
        tiers[tier] = tiers.get(tier, 0) + 1
        span = claim.get("draft_span", {})
        start = exact_int(span.get("start_byte"), f"{slug} claim start")
        end = exact_int(span.get("end_byte"), f"{slug} claim end")
        if not (0 <= start < end <= len(manuscript_bytes)):
            raise RuntimeError(f"{slug}: invalid claim byte span {claim.get('claim_id')}")
        if manuscript_bytes[start:end].decode("utf-8") != claim.get("claim_text"):
            raise RuntimeError(f"{slug}: stale claim byte span {claim.get('claim_id')}")
    if tiers.get("HIGH-IMPACT", 0) != cfg["high"] or tiers.get("RANDOM", 0) != cfg["random"]:
        raise RuntimeError(f"{slug}: claim selection tier mismatch")

    if not isinstance(rows, list) or len(rows) != cfg["tuples"]:
        raise RuntimeError(f"{slug}: evidence tuple denominator mismatch")
    run_checked(
        [sys.executable, str(ARS / "scripts/evidence_rows.py"), "validate", str(rows_path)],
        f"{slug} official evidence-row validation",
    )
    selected_by_id = {claim["claim_id"]: claim for claim in selected}
    expected_projection = {
        (claim["claim_id"], ref)
        for claim in selected
        for ref in (claim.get("ref_slugs") or [None])
    }
    actual_projection: list[tuple[str, Any]] = []
    row_ids: set[str] = set()
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise RuntimeError(f"{slug}: malformed evidence row")
        row_id = row.get("row_id")
        if not isinstance(row_id, str) or row_id in row_ids:
            raise RuntimeError(f"{slug}: duplicate evidence row id")
        row_ids.add(row_id)
        if row.get("anchor") != {"kind": "none", "value_decoded": "", "value_encoded": ""}:
            raise RuntimeError(f"{slug}: non-none evidence anchor")
        if row.get("excerpt", {}).get("state") != "anchorless":
            raise RuntimeError(f"{slug}: non-anchorless evidence excerpt")
        claim_obj = row.get("claim", {})
        claim_id = claim_obj.get("claim_id")
        claim = selected_by_id.get(claim_id)
        if claim is None:
            raise RuntimeError(f"{slug}: evidence row targets unselected claim")
        expected_claim_obj = {
            "claim_id": claim_id,
            "paper_locator": claim["writer_anchors"][0],
            "selection_tier": claim["selection_tier"],
            "text": claim["claim_text"],
        }
        if claim_obj != expected_claim_obj:
            raise RuntimeError(f"{slug}: evidence claim object drift")
        projection = (claim_id, row.get("source", {}).get("ref_slug"))
        actual_projection.append(projection)
        grouped.setdefault(claim_id, []).append(row)
    if len(actual_projection) != len(set(actual_projection)) or set(actual_projection) != expected_projection:
        raise RuntimeError(f"{slug}: evidence tuple projection is not exact")

    run_checked(
        [
            sys.executable,
            str(ARS / "scripts/claim_registry_coverage.py"),
            "--draft",
            str(manuscript),
            "--registry",
            str(registry_path),
            "--validate-report",
            str(coverage_path),
        ],
        f"{slug} official coverage validation",
    )
    if (
        coverage.get("candidate_unregistered_count") != 0
        or coverage.get("semantic_extraction_coverage") != "not_machine_detectable"
        or coverage.get("draft_raw_sha256") != sha(manuscript)
        or coverage.get("registry_raw_sha256") != sha(registry_path)
    ):
        raise RuntimeError(f"{slug}: coverage report boundary mismatch")

    drift_schema = load_json(
        ARS / "shared/contracts/revision/claim_strength_drift_findings.schema.json"
    )
    jsonschema.Draft202012Validator(drift_schema).validate(drift)
    if drift.get("final_draft_sha256") != sha(manuscript) or drift.get("findings") != []:
        raise RuntimeError(f"{slug}: blocking or stale claim-strength drift")
    expected_drift_status = (
        "completed"
        if cfg["e6_revision_evidence_available"]
        else "skipped_no_revision_evidence"
    )
    if drift.get("status") != expected_drift_status:
        raise RuntimeError(f"{slug}: wrong E6 drift status after repair")
    if expected_drift_status == "completed":
        bundle_sha = drift.get("revision_evidence_bundle_sha256")
        candidate_files = [
            path
            for path in ROOT.glob("BATCH_ROUND10_STAGE2_5*.json")
            if path.is_file() and not path.is_symlink()
        ]
        if not any(sha(path) == bundle_sha for path in candidate_files):
            raise RuntimeError(f"{slug}: E6 revision bundle hash does not resolve")

    if not isinstance(semantic, dict):
        raise RuntimeError(f"{slug}: semantic receipt must be an object")
    if semantic.get("schema") != "flow-systems-stage2.5-semantic-verdict-receipt/1.0":
        raise RuntimeError(f"{slug}: semantic receipt schema mismatch")
    expected_bindings = {
        "manuscript_sha256": sha(manuscript),
        "claim_registry_sha256": sha(registry_path),
        "evidence_rows_sha256": sha(rows_path),
        "semantic_audit_sha256": sha(semantic_audit_path),
    }
    if semantic.get("bindings") != expected_bindings:
        raise RuntimeError(f"{slug}: stale semantic receipt bindings")
    if semantic.get("decision") not in {
        "PASS_SELECTED_POPULATION",
        "PASS_SELECTED_POPULATION_WITH_MINOR_DISTORTION",
        "NO_MAJOR_DISTORTION_DETECTED__PASSAGE_CLOSURE_INCOMPLETE",
    }:
        raise RuntimeError(f"{slug}: semantic receipt does not pass")
    verdicts = semantic.get("claim_verdicts")
    if not isinstance(verdicts, list) or len(verdicts) != len(selected):
        raise RuntimeError(f"{slug}: semantic verdict denominator mismatch")
    verdict_by_id = {row.get("claim_id"): row for row in verdicts if isinstance(row, dict)}
    if len(verdict_by_id) != len(verdicts) or set(verdict_by_id) != set(selected_by_id):
        raise RuntimeError(f"{slug}: semantic verdict population mismatch")
    counts = {
        "VERIFIED": 0,
        "MINOR_DISTORTION": 0,
        "MAJOR_DISTORTION": 0,
        "UNVERIFIABLE": 0,
        "UNVERIFIABLE_ACCESS": 0,
    }
    for claim_id, verdict in verdict_by_id.items():
        value = verdict.get("verdict")
        if value not in counts:
            raise RuntimeError(f"{slug}: unknown semantic verdict {value!r}")
        counts[value] += 1
        if value not in {"VERIFIED", "MINOR_DISTORTION"}:
            raise RuntimeError(f"{slug}: blocking semantic verdict for {claim_id}")
        claim_rows = grouped[claim_id]
        if verdict.get("tuple_count") != len(claim_rows):
            raise RuntimeError(f"{slug}: semantic tuple count mismatch for {claim_id}")
        if verdict.get("row_ids") != [row["row_id"] for row in claim_rows]:
            raise RuntimeError(f"{slug}: semantic row-id binding mismatch for {claim_id}")
        if verdict.get("row_sha256s") != [row["row_sha256"] for row in claim_rows]:
            raise RuntimeError(f"{slug}: semantic row-hash binding mismatch for {claim_id}")
        if verdict.get("claim_object_sha256") != canonical_sha(claim_rows[0]["claim"]):
            raise RuntimeError(f"{slug}: semantic claim-object binding mismatch")
        if any(row.get("verdict") != value for row in claim_rows):
            raise RuntimeError(f"{slug}: evidence and semantic verdict conflict")
    if semantic.get("verdict_counts") != counts:
        raise RuntimeError(f"{slug}: semantic verdict-count mismatch")

    return {
        "registry": registry,
        "registry_path": registry_path,
        "coverage": coverage,
        "coverage_path": coverage_path,
        "rows": rows,
        "rows_path": rows_path,
        "drift": drift,
        "drift_path": drift_path,
        "semantic": semantic,
        "semantic_path": semantic_receipt_path,
        "semantic_audit_path": semantic_audit_path,
        "selected": selected,
        "tiers": tiers,
        "semantic_counts": counts,
        "repair_receipt_sha256": sha(repair_path),
    }


def compliance(slug: str, cfg: dict[str, Any], timestamp: str) -> dict[str, Any]:
    return {
        "mode": "primary_research",
        "stage": "2.5",
        "generated_at": timestamp,
        "prisma_trAIce": None,
        "raise": {
            "mode": "principles_only",
            "principles": {
                "human_oversight": "fail",
                "transparency": "fail",
                "reproducibility": "fail",
                "fit_for_purpose": "fail",
            },
            "principle_evidence": {
                "human_oversight": [
                    "Liang Wang is the named scholar, but the credentials and adjudication of a qualified independent human integrity reviewer are not documented.",
                    "Agent audits do not substitute for named human oversight.",
                ],
                "transparency": [
                    "The manuscript discloses AI assistance and the Stage-2.5 artifacts bind exact bytes and denominators.",
                    "[MATERIAL GAP] Complete tool/model/version, prompt, parameter, and per-stage usage metadata are absent.",
                ],
                "reproducibility": [
                    f"Paper {cfg['number']} preserves deterministic literature, build, hash, citation, and integrity receipts.",
                    "The scholar declares no project-owned scientific experiment for this manuscript; the proposed scientific procedures remain unexecuted and experiment_provenance is empty.",
                ],
                "fit_for_purpose": [
                    "Reference, context, data/table, originality, claim, provenance, failure-mode, and route checks are kept separate.",
                    "[MATERIAL GAP] No task-specific external benchmark or per-tool selection/validation rationale establishes full fit for purpose.",
                ],
            },
            "block_decision": "warn",
        },
        "overall_decision": "warn",
        "user_action_required": True,
        "evidence": [
            "RAISE is applied in principles-only mode to primary mathematical research; this is not official RAISE compliance.",
            "RAISE is warn-only and does not supersede the independent integrity decision.",
            f"The exact audit target is papers/{slug}/paper/manuscript.tex.",
        ],
        "upstream_sync_status": "current",
    }


def preflight_one(
    slug: str,
    cfg: dict[str, Any],
    freeze_row: dict[str, Any],
    declaration: dict[str, Any],
    repair_path: Path,
) -> dict[str, Any]:
    base = ROOT / "papers" / slug
    manuscript = require_regular(base / "paper/manuscript.tex")
    bibliography = require_regular(base / "paper/references.bib")
    pdf = require_regular(base / "paper/paper.pdf")
    hashes = {
        "manuscript_sha256": sha(manuscript),
        "bibliography_sha256": sha(bibliography),
        "pdf_sha256": sha(pdf),
    }
    for key, value in hashes.items():
        if freeze_row.get(key) != value:
            raise RuntimeError(f"{slug}: post-repair freeze mismatch for {key}")
    claim = _validate_claim_artifacts(slug, cfg, manuscript, repair_path)
    hashes.update(
        {
            "claim_registry_sha256": sha(claim["registry_path"]),
            "coverage_sha256": sha(claim["coverage_path"]),
            "evidence_rows_sha256": sha(claim["rows_path"]),
            "claim_strength_drift_sha256": sha(claim["drift_path"]),
            "semantic_audit_sha256": sha(claim["semantic_audit_path"]),
            "semantic_receipt_sha256": sha(claim["semantic_path"]),
        }
    )
    phase_ab, phase_ab_path = validate_phase_ab(slug, cfg, {
        key: hashes[key]
        for key in ("manuscript_sha256", "bibliography_sha256", "pdf_sha256")
    })
    phase_c, phase_c_path_value = validate_phase_c(slug, cfg, hashes, declaration)
    originality, originality_path, originality_audit_path, originality_counts = (
        _validate_originality(slug, cfg, hashes["manuscript_sha256"])
    )
    failure_modes_path = _validate_failure_modes(slug, hashes["manuscript_sha256"])
    hashes.update(
        {
            "phase_ab_sha256": sha(phase_ab_path),
            "phase_c_sha256": sha(phase_c_path_value),
            "originality_sample_sha256": sha(originality_path),
            "originality_audit_sha256": sha(originality_audit_path),
            "failure_modes_sha256": sha(failure_modes_path),
        }
    )
    return {
        "slug": slug,
        "cfg": cfg,
        "base": base,
        "manuscript": manuscript,
        "bibliography": bibliography,
        "pdf": pdf,
        "hashes": hashes,
        "claim": claim,
        "phase_ab": phase_ab,
        "phase_ab_path": phase_ab_path,
        "phase_c": phase_c,
        "phase_c_path": phase_c_path_value,
        "originality": originality,
        "originality_path": originality_path,
        "originality_audit_path": originality_audit_path,
        "originality_counts": originality_counts,
        "failure_modes_path": failure_modes_path,
    }


def build_paper_outputs(
    state: dict[str, Any],
    timestamp: str,
    freeze_info: dict[str, str],
    repair_info: dict[str, str],
    declaration_info: dict[str, str],
    declaration: dict[str, Any],
    route: dict[str, str],
) -> tuple[dict[Path, bytes], dict[str, Any]]:
    slug = state["slug"]
    cfg = state["cfg"]
    base: Path = state["base"]
    notes = base / "notes"
    claim = state["claim"]
    hashes = state["hashes"]
    selected = claim["selected"]
    rows = claim["rows"]
    counts = claim["semantic_counts"]
    minor_count = counts["MINOR_DISTORTION"]

    adjudication_path = notes / "stage2_5_claim_registry_coverage_adjudication.md"
    adjudication = f"""# Paper {cfg['number']} Stage-2.5 Claim Registry coverage adjudication

Audit target SHA-256: `{hashes['manuscript_sha256']}`  
Registry SHA-256: `{hashes['claim_registry_sha256']}`

- Registered claims: **{cfg['registered']}**.
- Selected distinct claims: **{cfg['selected']}** = {cfg['high']} HIGH-IMPACT + {cfg['random']} RANDOM.
- Exact `(claim_id, ref_slug-or-null)` evidence tuples: **{cfg['tuples']}/{cfg['tuples']}**.
- Anchorless rows: **{cfg['tuples']}/{cfg['tuples']}**; no row is promoted to a source excerpt.
- Bounded mechanical candidate gaps: **0**.
- Semantic extraction coverage: **`not_machine_detectable`**.
- The semantic decision is supplied separately by the exact hash-bound Phase-E audit and verdict receipt.
"""
    adjudication_bytes = adjudication.encode("utf-8")

    comp = compliance(slug, cfg, timestamp)
    comp_bytes = json_bytes(comp)
    comp_path = notes / "stage2_5_compliance_report.json"

    report = {
        "verdict": "PASS",
        "mode": "pre-review",
        "phases": {
            "A_references": {
                "checked": cfg["references"],
                "verified": cfg["references_verified"],
                "plausible_bounded": cfg["references_plausible"],
                "closed": cfg["references"],
                "failed": 0,
                "unresolved_findings": [],
                "receipt_path": f"notes/{state['phase_ab_path'].name}",
                "receipt_sha256": hashes["phase_ab_sha256"],
            },
            "B_citation_context": {
                "denominator": cfg["citation_contexts"],
                "sampled": cfg["contexts_sampled"],
                "verified_with_boundaries": cfg["contexts_sampled"],
                "issues": [],
            },
            "C_data": {
                "claim_surfaces_checked": cfg["phase_c_claims"],
                "verified": cfg["phase_c_claims"],
                "figure_table_trace_count": cfg["table_traces"],
                "issues": [],
                "trace_path": f"notes/{state['phase_c_path'].name}",
                "trace_sha256": hashes["phase_c_sha256"],
            },
            "C4_experiment_intake": {
                "claims_checked": 1,
                "verified": 1,
                "declaration": declaration,
                "experiment_provenance": [],
                "boundary": PROVENANCE_BOUNDARY,
                "issues": [],
            },
            "D_originality": {
                "sampled": cfg["originality"][0],
                "denominator": cfg["originality"][1],
                "major_sections_covered": 10,
                "verdict_counts": state["originality_counts"],
                "professional_detector_used": False,
                "issues": [],
                "sample_sha256": hashes["originality_sample_sha256"],
                "audit_sha256": hashes["originality_audit_sha256"],
            },
            "E_claims": {
                "registered": cfg["registered"],
                "checked": cfg["selected"],
                "verified": counts["VERIFIED"],
                "minor_distortions": minor_count,
                "blocking_distortions": 0,
                "evidence_tuple_count": cfg["tuples"],
                "anchorless_rows": cfg["tuples"],
                "semantic_extraction_coverage": "not_machine_detectable",
                "semantic_verdict_receipt": {
                    "path": "notes/stage2_5_phase_e_semantic_verdicts.json",
                    "sha256": hashes["semantic_receipt_sha256"],
                    "semantic_audit_sha256": hashes["semantic_audit_sha256"],
                },
                "claim_registry_coverage": {
                    "path": "notes/stage2_5_claim_registry_coverage.json",
                    "sha256": hashes["coverage_sha256"],
                    "registry_sha256": hashes["claim_registry_sha256"],
                    "candidate_unregistered_count": 0,
                    "adjudication_path": "notes/stage2_5_claim_registry_coverage_adjudication.md",
                    "adjudication_sha256": sha_bytes(adjudication_bytes),
                },
                "evidence_rows": rows,
                "claim_strength_drift_findings": {
                    "path": "notes/stage2_5_claim_strength_drift_findings.json",
                    "sha256": hashes["claim_strength_drift_sha256"],
                    "status": claim["drift"]["status"],
                },
            },
        },
        "overall_issues": {
            "SERIOUS": 0,
            "MAJOR": 0,
            "MEDIUM": 0,
            "MINOR": minor_count,
        },
        "citation_integrity_score": 1.0,
        "fabrication_risk_score": 0.0,
        "timestamp": timestamp,
        "extensions": {
            "display_verdict": "PASS_AT_STAGE_2.5_CHECKPOINT",
            "input_freeze": {
                **freeze_info,
                "canonical": {
                    key: hashes[key]
                    for key in (
                        "manuscript_sha256",
                        "bibliography_sha256",
                        "pdf_sha256",
                    )
                },
            },
            "repair_receipt": repair_info,
            "experiment_declaration_receipt": declaration_info,
            "claim_selection": {
                "registered": cfg["registered"],
                "high_impact": cfg["high"],
                "random": cfg["random"],
                "selected": cfg["selected"],
                "evidence_tuples": cfg["tuples"],
                "anchorless_rows": cfg["tuples"],
            },
            "failure_modes": {f"mode_{index}": "CLEAR" for index in range(1, 8)},
            "failure_modes_sha256": hashes["failure_modes_sha256"],
            "route_crosswalk": {
                "position": "Route A A0/A1 foundation/interface",
                "dynamical_subtype": cfg["subtype"],
                "formal_route_a_tuple_assigned": False,
                "positive_arithmetic_A2": False,
                "A3": False,
                "A4": False,
                "route_b": "NOT_INVOKED",
                "gate_credit": "NONE",
                **route,
            },
            "active_issue_ids": [],
            "stage3_authorized": False,
            "score_boundary": (
                "Scores summarize registered checked surfaces; they are not "
                "probabilities or guarantees of mathematical truth, semantic "
                "completeness, corpus completeness, or global originality."
            ),
        },
    }
    report_path = notes / "stage2_5_integrity_report.json"
    report_bytes = json_bytes(report)

    passport = {
        "origin_skill": "ars-codex:academic-research-suite",
        "origin_mode": "full",
        "origin_date": timestamp,
        "verification_status": "VERIFIED",
        "version_label": f"p{cfg['number']}-round10-stage2.5-pass-v1",
        "integrity_pass_date": timestamp,
        "content_hash": hashes["manuscript_sha256"],
        "upstream_dependencies": [
            "round10-stage2-final",
            f"sha256:{freeze_info['sha256']}",
            f"sha256:{repair_info['sha256']}",
            "claim-registry/1.0",
            "claim-registry-coverage/1.0",
            "evidence-row/1.0",
            "flow-systems-stage2.5-semantic-verdict-receipt/1.0",
        ],
        "repro_lock": None,
        "slr_lineage": False,
        "experiment_intake_declaration": declaration,
        "experiment_provenance": [],
        "experiment_alignment_results": [],
        "claim_intent_manifests": [],
        "compliance_history": [comp],
        "round10_stage2_5": {
            "input_freeze": freeze_info,
            "repair_receipt": repair_info,
            "experiment_declaration_receipt": declaration_info,
            "artifact_bindings": {
                **hashes,
                "coverage_adjudication_sha256": sha_bytes(adjudication_bytes),
                "integrity_report_sha256": sha_bytes(report_bytes),
                "compliance_report_sha256": sha_bytes(comp_bytes),
            },
            "registered_claims": cfg["registered"],
            "selected_claims": cfg["selected"],
            "evidence_tuples": cfg["tuples"],
            "anchorless_rows": cfg["tuples"],
            "phase_c_claim_surfaces": cfg["phase_c_claims"],
            "formal_route_a_tuple_assigned": False,
            "positive_arithmetic_A2": False,
            "route_b_invoked": False,
            "stage3_authorized": False,
            "semantic_extraction_coverage": "not_machine_detectable",
        },
    }
    passport_path = notes / "stage2_5_material_passport.json"
    passport_bytes = json_bytes(passport)

    rows_percent = 100.0 * cfg["originality"][0] / cfg["originality"][1]
    report_md = f"""# Paper {cfg['number']} Stage-2.5 Integrity Report

Audit timestamp: **{timestamp}**  
Decision: **PASS AT THE MANDATORY STAGE-2.5 CHECKPOINT**  
Stage 3 authorized: **no**

The final post-repair manuscript, bibliography, and PDF match the hash-bound
input freeze. No unresolved SERIOUS/MAJOR/MEDIUM finding remains in the
registered audit population.

| Surface | Result |
|---|---:|
| References | {cfg['references']}/{cfg['references']} closed ({cfg['references_verified']} VERIFIED, {cfg['references_plausible']} bounded PLAUSIBLE) |
| Citation-context sample | {cfg['contexts_sampled']}/{cfg['citation_contexts']} supported within stated boundaries |
| Phase-C quantitative/data surfaces | {cfg['phase_c_claims']}/{cfg['phase_c_claims']} traced |
| Figure/table traces | {cfg['table_traces']}/{cfg['table_traces']} |
| Originality sample | {cfg['originality'][0]}/{cfg['originality'][1]} ({rows_percent:.2f}%), 10/10 major sections |
| Claim Registry | {cfg['registered']} registered; {cfg['selected']} selected |
| Evidence rows | {cfg['tuples']}/{cfg['tuples']} exact tuples; all anchorless |
| Official E6 claim-strength drift | `skipped_no_revision_evidence`; no schema-compatible official Revision-Evidence Bundle supplied |
| Experiment intake | `no_experiments_declared`; provenance 0 |
| Seven failure modes | 7 CLEAR; 0 SUSPECTED; 0 INSUFFICIENT EVIDENCE |

All evidence rows retain `anchor.kind=none` and `excerpt.state=anchorless`.
This preserves the distinction between structural/hash/selection conformance
and exact source-passage attestation. Semantic extraction completeness remains
`not_machine_detectable`.

Official E6 claim-strength-drift detection is recorded as
`skipped_no_revision_evidence` because no schema-compatible official ARS
Revision-Evidence Bundle was supplied. Any project-local repair lineage or
manual comparison remains supplementary evidence and is not represented as
official E6 completion.

Required provenance boundary: **{PROVENANCE_BOUNDARY}**

Roadmap position: **Route A A0/A1 foundation/interface**. The frozen subtype is
{cfg['subtype']}. No formal Route-A tuple is assigned, positive arithmetic A2
is absent, A3/A4 are absent, Route B is not invoked, and this integrity audit
earns no scientific gate credit.

RAISE is recorded in principles-only, warn-only mode. Its material gaps do not
replace or reverse the independent integrity PASS.
"""
    report_md_path = notes / "stage2_5_integrity_report.md"

    experiment_md = f"""# Paper {cfg['number']} Stage-2.5 experiment-intake closure

The scholar-owned declaration is present with
`status=no_experiments_declared`, `declared_by=scholar`, and
`declared_at={declaration['declared_at']}`. The passport's
`experiment_provenance` and `experiment_alignment_results` arrays are empty,
as required by declaration/provenance symmetry. The manuscript's scientific
procedures remain prospective.

**{PROVENANCE_BOUNDARY}**
"""
    experiment_md_path = notes / "stage2_5_experiment_provenance_closure.md"

    outputs = {
        adjudication_path: adjudication_bytes,
        comp_path: comp_bytes,
        report_path: report_bytes,
        report_md_path: report_md.encode("utf-8"),
        passport_path: passport_bytes,
        experiment_md_path: experiment_md.encode("utf-8"),
    }
    summary = {
        "paper": slug,
        "paper_id": cfg["paper_id"],
        "number": cfg["number"],
        "verdict": "PASS",
        "registered_claims": cfg["registered"],
        "selected_claims": cfg["selected"],
        "evidence_tuples": cfg["tuples"],
        "anchorless_rows": cfg["tuples"],
        "references_checked": cfg["references"],
        "references_verified": cfg["references_verified"],
        "references_plausible": cfg["references_plausible"],
        "contexts_sampled": cfg["contexts_sampled"],
        "phase_c_claim_surfaces": cfg["phase_c_claims"],
        "originality_sampled": cfg["originality"][0],
        "originality_denominator": cfg["originality"][1],
        "figure_table_traces": cfg["table_traces"],
        "active_issue_ids": [],
        "integrity_report_sha256": sha_bytes(report_bytes),
        "material_passport_sha256": sha_bytes(passport_bytes),
        "compliance_report_sha256": sha_bytes(comp_bytes),
        "semantic_receipt_sha256": hashes["semantic_receipt_sha256"],
    }
    return outputs, summary


def validate_generated_passports(outputs: dict[Path, bytes]) -> None:
    compliance_schema = load_json(ARS / "shared/compliance_report.schema.json")
    validator = jsonschema.Draft202012Validator(
        compliance_schema, format_checker=jsonschema.FormatChecker()
    )
    with tempfile.TemporaryDirectory(prefix="round10-stage2.5-passport-") as raw:
        tmp = Path(raw)
        for slug in PAPERS:
            notes = ROOT / "papers" / slug / "notes"
            comp_path = notes / "stage2_5_compliance_report.json"
            passport_path = notes / "stage2_5_material_passport.json"
            comp = json.loads(outputs[comp_path].decode("utf-8"))
            validator.validate(comp)
            temp_passport = tmp / f"{slug}.json"
            temp_passport.write_bytes(outputs[passport_path])
            run_checked(
                [
                    sys.executable,
                    str(ARS / "scripts/check_claim_audit_consistency.py"),
                    "--passport",
                    str(temp_passport),
                ],
                f"{slug} official passport consistency validation",
            )
            run_checked(
                [
                    sys.executable,
                    str(ARS / "scripts/check_experiment_provenance.py"),
                    str(temp_passport),
                ],
                f"{slug} official experiment-provenance validation",
            )


def atomic_write_all(outputs: dict[Path, bytes]) -> None:
    staged: list[tuple[Path, Path]] = []
    try:
        for path, payload in outputs.items():
            path.parent.mkdir(parents=False, exist_ok=True)
            if path.is_symlink():
                raise RuntimeError(f"refusing to replace symlink output: {path}")
            tmp = path.with_name(f".{path.name}.round10-stage2.5.tmp")
            if tmp.exists() or tmp.is_symlink():
                raise RuntimeError(f"staging path already exists: {tmp}")
            tmp.write_bytes(payload)
            staged.append((tmp, path))
        for tmp, path in staged:
            tmp.replace(path)
    except Exception:
        for tmp, _ in staged:
            try:
                tmp.unlink(missing_ok=True)
            except OSError:
                pass
        raise


def main() -> int:
    timestamp = utc_now()
    declaration, declaration_info = validate_scholar_declaration()
    route = validate_route_inputs()
    repair_path, repair = discover_repair_receipt()
    freeze_path, freeze, freeze_rows = discover_final_freeze(repair_path, repair)
    freeze_info = {"path": freeze_path.name, "sha256": sha(freeze_path)}
    repair_info = {"path": repair_path.name, "sha256": sha(repair_path)}

    states = [
        preflight_one(slug, cfg, freeze_rows[slug], declaration, repair_path)
        for slug, cfg in PAPERS.items()
    ]

    outputs: dict[Path, bytes] = {}
    paper_summaries: list[dict[str, Any]] = []
    for state in states:
        paper_outputs, summary = build_paper_outputs(
            state,
            timestamp,
            freeze_info,
            repair_info,
            declaration_info,
            declaration,
            route,
        )
        overlap = set(outputs) & set(paper_outputs)
        if overlap:
            raise RuntimeError(f"duplicate generated output path(s): {sorted(overlap)}")
        outputs.update(paper_outputs)
        paper_summaries.append(summary)

    aggregate = {
        "papers": len(paper_summaries),
        "references_checked": sum(row["references_checked"] for row in paper_summaries),
        "references_verified": sum(row["references_verified"] for row in paper_summaries),
        "references_plausible": sum(row["references_plausible"] for row in paper_summaries),
        "citation_contexts": sum(cfg["citation_contexts"] for cfg in PAPERS.values()),
        "contexts_sampled": sum(row["contexts_sampled"] for row in paper_summaries),
        "registered_claims": sum(row["registered_claims"] for row in paper_summaries),
        "selected_claims": sum(row["selected_claims"] for row in paper_summaries),
        "evidence_tuples": sum(row["evidence_tuples"] for row in paper_summaries),
        "anchorless_rows": sum(row["anchorless_rows"] for row in paper_summaries),
        "phase_c_claim_surfaces": sum(row["phase_c_claim_surfaces"] for row in paper_summaries),
        "originality_sampled": sum(row["originality_sampled"] for row in paper_summaries),
        "originality_denominator": sum(row["originality_denominator"] for row in paper_summaries),
        "figure_table_traces": sum(row["figure_table_traces"] for row in paper_summaries),
        "scientific_executions": 0,
        "formal_route_a_tuples": 0,
        "positive_arithmetic_a2": 0,
        "route_b_invocations": 0,
    }
    if aggregate != EXPECTED_AGGREGATE:
        raise RuntimeError(f"batch aggregate mismatch: {aggregate} != {EXPECTED_AGGREGATE}")

    batch = {
        "schema": "flow-systems-round10-stage2.5-integrity-summary/1.0",
        "generated_at": timestamp,
        "batch_verdict": "PASS",
        "checkpoint": "MANDATORY_STAGE_2.5_COMPLETE",
        "stage3_authorized": False,
        "input_freeze": freeze_info,
        "repair_receipt": repair_info,
        "experiment_declaration_receipt": declaration_info,
        "route": {
            "position": "Route A A0/A1 foundation/interface",
            "formal_tuple_assigned": False,
            "positive_arithmetic_A2": False,
            "A3": False,
            "A4": False,
            "route_b_invoked": False,
            **route,
        },
        "papers": paper_summaries,
        "aggregate": aggregate,
        "unresolved_findings": {"SERIOUS": 0, "MAJOR": 0, "MEDIUM": 0},
        "nonblocking_findings": [
            {
                "finding_id": "ROUND10-D-STANDARDIZED-DECLARATION-BOILERPLATE",
                "severity": "MINOR",
                "scope": "Administrative declarations only; excluded from scientific-body originality denominators.",
            }
        ],
        "provenance_boundary": PROVENANCE_BOUNDARY,
        "compiler_sha256": sha(Path(__file__).resolve()),
    }
    batch_path = ROOT / "BATCH_ROUND10_STAGE2_5_INTEGRITY_SUMMARY.json"
    batch_bytes = json_bytes(batch)
    outputs[batch_path] = batch_bytes

    paper_rows = "\n".join(
        f"| {row['paper_id']} | {row['references_checked']}/{row['references_checked']} | "
        f"{row['selected_claims']}/{row['registered_claims']} | "
        f"{row['evidence_tuples']} anchorless tuples | PASS |"
        for row in paper_summaries
    )
    batch_md = f"""# Round 10 Papers 29--33 — ARS Stage 2.5 Integrity Report

Audit timestamp: **{timestamp}**  
Batch decision: **PASS AT THE MANDATORY STAGE-2.5 CHECKPOINT**  
Stage 3 authorized: **no**

The hash-bound post-repair corpus passes the registered audit denominators:
**116/116 references closed**, **48/144 citation contexts sampled and
supported within their declared boundaries**, **244/244 Phase-C quantitative
or data surfaces traced**, **116/374 originality paragraphs checked across
10/10 major sections per paper**, **480 claims registered**, **382 distinct
claims semantically checked**, and **454/454 evidence tuples retained as
anchorless**. P33's two prospective longtables have two explicit traces.

| Paper | References | Phase E | Evidence | Decision |
|---|---:|---:|---:|---|
{paper_rows}

The scholar declared `no_experiments_declared` for all five manuscripts;
`experiment_provenance=[]`, scientific executions are 0, and the proposed
scientific methods remain prospective. **{PROVENANCE_BOUNDARY}**

The originality screen is a bounded public-Web/local-corpus heuristic, not
Turnitin or iThenticate. Repeated funding, conflict, ethics, contribution, and
AI-assistance declarations are recorded as nonblocking standardized
administrative boilerplate, not scientific prose.

Official E6 claim-strength-drift detection is
`skipped_no_revision_evidence` for all five papers because no schema-compatible
official ARS Revision-Evidence Bundle was supplied. Project-local repair
lineage and manual comparisons for the authorized P31/P32 changes are
supplementary only and are not reported as official E6 completion.

Roadmap position remains **Route A A0/A1 foundation/interface**. Formal
Route-A tuples: **0/5**; positive arithmetic A2: **0/5**; A3: **0/5**; A4:
**0/5**; Route B: **0/5**. This integrity pass creates no scientific gate
credit. Route-A SHA-256 `{ROUTE_A_SHA}`; Route-B SHA-256 `{ROUTE_B_SHA}`.

The workflow stops here. A separate explicit scholar confirmation is required
before Stage 3; this compiler never sets `stage3_authorized=true`.
"""
    batch_md_path = ROOT / "BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md"
    batch_md_bytes = batch_md.encode("utf-8")
    outputs[batch_md_path] = batch_md_bytes

    checkpoint = {
        "schema": "flow-systems-round10-stage2.5-mandatory-checkpoint/1.0",
        "generated_at": timestamp,
        "decision": "PASS_AT_STAGE_2.5_CHECKPOINT",
        "mandatory_stop": True,
        "stage3_authorized": False,
        "scholar_confirmation_required": True,
        "next_stage_if_confirmed": "Stage 3 independent review",
        "integrity_summary": {"path": batch_path.name, "sha256": sha_bytes(batch_bytes)},
        "integrity_report": {"path": batch_md_path.name, "sha256": sha_bytes(batch_md_bytes)},
        "input_freeze": freeze_info,
        "repair_receipt": repair_info,
        "experiment_declaration_receipt": declaration_info,
        "papers": [
            {
                "paper": row["paper"],
                "passport_sha256": row["material_passport_sha256"],
                "integrity_report_sha256": row["integrity_report_sha256"],
            }
            for row in paper_summaries
        ],
        "route_state": {
            "formal_route_a_tuples": 0,
            "positive_arithmetic_a2": 0,
            "route_b_invocations": 0,
        },
    }
    checkpoint_path = ROOT / "BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json"
    checkpoint_bytes = json_bytes(checkpoint)
    outputs[checkpoint_path] = checkpoint_bytes
    checkpoint_md = f"""# Round 10 Stage 2.5 mandatory checkpoint

Decision: **PASS**  
Generated: **{timestamp}**  
Summary SHA-256: `{sha_bytes(batch_bytes)}`  
Report SHA-256: `{sha_bytes(batch_md_bytes)}`

Papers 29--33 pass the complete registered Stage-2.5 audit population. The
workflow is stopped at the mandatory boundary with `stage3_authorized=false`.
A separate scholar confirmation is required to enter Stage 3.
"""
    outputs[ROOT / "BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.md"] = checkpoint_md.encode("utf-8")

    # Validate generated Schema-12 and Schema-9-compatible content in a
    # temporary directory before any destination is replaced.
    validate_generated_passports(outputs)
    atomic_write_all(outputs)
    print(json_text(batch), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
