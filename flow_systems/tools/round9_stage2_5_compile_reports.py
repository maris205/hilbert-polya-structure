#!/usr/bin/env python3
"""Compile frozen Round-9 Stage-2.5 reports for Papers 24--28.

This compiler writes audit and handoff artifacts only.  It never mutates a
manuscript, bibliography, release PDF, source ledger, or experiment receipt.
The five passports intentionally omit ``experiment_intake_declaration``:
that scholar-owned declaration is the shared fail-closed checkpoint blocker.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import jsonschema


ROOT = Path(__file__).resolve().parent.parent
ROUTE_A_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
ROUTE_B_SHA = "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"


PAPERS: dict[str, dict[str, Any]] = {
    "24-bianchi-holonomy-flow": {
        "number": 24,
        "title": "Bianchi holonomy flow",
        "refs": 7,
        "refs_passed": 7,
        "contexts": 9,
        "data": 6,
        "originality": (21, 69),
        "tests": (71, 14),
        "shared_declaration_minor": "P24--P25 contain a 98-word exact standardized declarations block; it is administrative boilerplate, not scientific-body reuse.",
        "issues": [
            {
                "id": "P24-IL-SERIOUS-EXP-DECL-1",
                "phase": "C4/D7",
                "type": "missing_scholar_experiment_intake",
                "severity": "SERIOUS",
                "detail": "The manuscript reports project-owned computational results, but the post-#260 passport has no scholar-owned experiment_intake_declaration or experiment_provenance ledger.",
                "action": "Scholar confirms the exact batch experiment declaration; then transcribe and align the already frozen Round-2--8 provenance artifacts.",
            }
        ],
        "route": "(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL); canonical A0 controls 2/3, exploratory/negative specificity result",
    },
    "25-three-disk-scattering-flow": {
        "number": 25,
        "title": "Three-disk scattering flow",
        "refs": 8,
        "refs_passed": 7,
        "contexts": 10,
        "data": 7,
        "originality": (22, 70),
        "tests": (65, 12),
        "shared_declaration_minor": "P24--P25 contain a 98-word exact standardized declarations block; it is administrative boilerplate, not scientific-body reuse.",
        "issues": [
            {
                "id": "P25-IL-SERIOUS-REF-1",
                "phase": "A",
                "type": "reference_author_metadata_mismatch",
                "severity": "SERIOUS",
                "ref_id": "BowenLanford1970",
                "detail": "The official AMS record names O. E. Lanford III; the current author field omits the suffix III.",
                "action": "Authorize replacement of `author = {Bowen, Rufus and Lanford, Oscar E.}` with `author = {Bowen, Rufus and Lanford, III, Oscar E.}`; rebuild and re-audit Phase A/B.",
            },
            {
                "id": "P25-IL-SERIOUS-EXP-DECL-1",
                "phase": "C4/D7",
                "type": "missing_scholar_experiment_intake",
                "severity": "SERIOUS",
                "detail": "The manuscript reports project-owned computational results, but the post-#260 passport has no scholar-owned experiment_intake_declaration or experiment_provenance ledger.",
                "action": "Scholar confirms the exact batch experiment declaration; then transcribe and align the already frozen Round-2--8 provenance artifacts.",
            },
        ],
        "route": "unit-roof symbolic control (A0_FAIL, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL), rejected; no physical-flow tuple because nontransfer is proved",
    },
    "26-level11-newform-time-change": {
        "number": 26,
        "title": "Level-11 newform time change",
        "refs": 5,
        "refs_passed": 5,
        "contexts": 5,
        "data": 14,
        "originality": (21, 65),
        "tests": (74, 18),
        "shared_declaration_minor": "P26--P27 contain a 100-word exact standardized declarations block; it is administrative boilerplate, not scientific-body reuse.",
        "issues": [
            {
                "id": "P26-IL-SERIOUS-EXP-DECL-1",
                "phase": "C4/D7",
                "type": "missing_scholar_experiment_intake",
                "severity": "SERIOUS",
                "detail": "The manuscript reports project-owned computational results, but the post-#260 passport has no scholar-owned experiment_intake_declaration or experiment_provenance ledger.",
                "action": "Scholar confirms the exact batch experiment declaration; then transcribe and align the already frozen Round-2--8 provenance artifacts.",
            }
        ],
        "route": "(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL); exhaustive finite Hecke-owner obstruction",
    },
    "27-congruence-inverse-limit-no-go": {
        "number": 27,
        "title": "Congruence inverse-limit no-go",
        "refs": 5,
        "refs_passed": 5,
        "contexts": 5,
        "data": 13,
        "originality": (21, 67),
        "tests": (58, 12),
        "shared_declaration_minor": "P26--P27 contain a 100-word exact standardized declarations block; it is administrative boilerplate, not scientific-body reuse.",
        "issues": [
            {
                "id": "P27-IL-SERIOUS-EXP-DECL-1",
                "phase": "C4/D7",
                "type": "missing_scholar_experiment_intake",
                "severity": "SERIOUS",
                "detail": "The manuscript reports project-owned computational results, but the post-#260 passport has no scholar-owned experiment_intake_declaration or experiment_provenance ledger.",
                "action": "Scholar confirms the exact batch experiment declaration; then transcribe and align the already frozen Round-2--8 provenance artifacts.",
            }
        ],
        "route": "residual model (A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL), rejected; homology calibrator (A0_FAIL, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL), rejected",
    },
    "28-bolza-magnetic-flow": {
        "number": 28,
        "title": "Bolza magnetic-flow control",
        "refs": 6,
        "refs_passed": 4,
        "contexts": 9,
        "data": 10,
        "originality": (28, 72),
        "tests": (104, 24),
        "issues": [
            {
                "id": "P28-IL-SERIOUS-REF-1",
                "phase": "A",
                "type": "reference_author_and_subject_metadata_mismatch",
                "severity": "SERIOUS",
                "ref_id": "Nazarenko2013",
                "detail": "The official record gives A. V. Nazarenko (submission name Andrey Nazarenko) and primary subject math-ph; the entry expands Aleksandr V. and records hep-th.",
                "action": "Authorize `author = {Nazarenko, A. V.}` and `primaryclass = {math-ph}`; rebuild and re-audit Phase A/B.",
            },
            {
                "id": "P28-IL-SERIOUS-REF-2",
                "phase": "A",
                "type": "reference_author_metadata_mismatch",
                "severity": "SERIOUS",
                "ref_id": "AigonDupuyEtAl2005",
                "detail": "Official metadata gives Aline Aigon-Dupuy, Peter Buser, Michel Cibils, Alfred F. Künzle, and Frank Steiner; three given names in the entry are wrong.",
                "action": "Authorize `author = {Aigon-Dupuy, Aline and Buser, Peter and Cibils, Michel and K{\\\"u}nzle, Alfred F. and Steiner, Frank}`; rebuild and re-audit Phase A/B.",
            },
            {
                "id": "P28-IL-SERIOUS-EXP-DECL-1",
                "phase": "C4/D7",
                "type": "missing_scholar_experiment_intake",
                "severity": "SERIOUS",
                "detail": "The manuscript reports project-owned computational results, but the post-#260 passport has no scholar-owned experiment_intake_declaration or experiment_provenance ledger.",
                "action": "Scholar confirms the exact batch experiment declaration; then transcribe and align the already frozen Round-2--8 provenance artifacts.",
            },
        ],
        "route": "control theorem only; full Route-A tuple unassigned because the Bolza target census and magnetic comparison have not been executed",
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Any) -> None:
    write_text(
        path,
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )


def write_text(path: Path, value: str) -> None:
    """Atomically replace one generated report in its destination directory."""

    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(value, encoding="utf-8")
    tmp.replace(path)


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ars_root() -> Path:
    override = os.environ.get("ARS_CODEX_ROOT")
    if override:
        path = Path(override).expanduser().resolve()
        if (path / "scripts" / "claim_registry_coverage.py").is_file():
            return path
        raise RuntimeError(f"ARS_CODEX_ROOT is not an ARS resource root: {path}")
    search_roots = [ROOT.parent / ".codex", Path.home() / ".codex"]
    candidates = []
    for codex_root in search_roots:
        candidates.extend(
            (codex_root / "plugins" / "cache" / "ars-codex" / "ars-codex").glob(
                "*/skills/academic-research-suite/ars"
            )
        )
    candidates = sorted(set(candidates))
    if not candidates:
        raise RuntimeError("ARS-Codex academic-research-suite resources not found")
    return candidates[-1]


def compliance(paper: str, cfg: dict[str, Any], timestamp: str) -> dict[str, Any]:
    n = cfg["number"]
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
                    "Liang Wang is the named author, but qualified human-reviewer count, qualifications, and adjudication are not documented.",
                    "Independent agent audits are recorded but are not substitutes for named human oversight.",
                ],
                "transparency": [
                    "The manuscript carries an AI-assistance disclosure and the audit preserves exact artifact hashes.",
                    "[MATERIAL GAP] Complete tool/model/version, prompt, parameter, and per-stage usage metadata are absent.",
                ],
                "reproducibility": [
                    f"Paper {n} has deterministic code, tests, frozen results, and receipt hashes.",
                    "[MATERIAL GAP] The Schema-9 passport records repro_lock=null and the scholar-owned experiment intake/provenance is not yet present.",
                ],
                "fit_for_purpose": [
                    "Reference, claim, proof/artifact, originality, and route checks are separated by scope.",
                    "[MATERIAL GAP] No task-specific external benchmark or per-tool selection/validation rationale establishes full fit for purpose.",
                ],
            },
            "block_decision": "warn",
        },
        "overall_decision": "warn",
        "user_action_required": True,
        "evidence": [
            "RAISE is applied in principles-only mode to primary mathematical research; this is not official RAISE compliance.",
            "RAISE remains a warn-only compliance contribution and does not supersede the independent integrity FAIL.",
            f"The exact Stage-2.5 audit target is papers/{paper}/paper/manuscript.tex.",
        ],
        "upstream_sync_status": "current",
    }


def phase_a_issues(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for issue in cfg["issues"]:
        if issue["phase"] != "A":
            continue
        rows.append(
            {
                "ref_id": issue["ref_id"],
                "issue_type": issue["type"],
                "severity": issue["severity"],
                "detail": issue["detail"],
            }
        )
    return rows


def bib_entry(text: str, key: str) -> str:
    """Return the single-line-field BibTeX entry used by this repository."""

    marker = "{" + key + ","
    start = text.find(marker)
    if start < 0:
        return ""
    next_entry = text.find("\n@", start)
    return text[start:] if next_entry < 0 else text[start:next_entry]


def bib_field(entry: str, field: str) -> str | None:
    for line in entry.splitlines():
        if "=" not in line:
            continue
        name, value = line.split("=", 1)
        if name.strip().lower() != field.lower():
            continue
        value = value.strip().rstrip(",").strip()
        if value.startswith("{") and value.endswith("}"):
            value = value[1:-1]
        return value
    return None


def reference_issue_resolved(paper: str, issue: dict[str, Any], bib_text: str) -> bool:
    entry = bib_entry(bib_text, issue["ref_id"])
    if paper == "25-three-disk-scattering-flow":
        return bib_field(entry, "author") == "Bowen, Rufus and Lanford, III, Oscar E."
    if paper == "28-bolza-magnetic-flow" and issue["ref_id"] == "Nazarenko2013":
        return (
            bib_field(entry, "author") == "Nazarenko, A. V."
            and bib_field(entry, "primaryclass") == "math-ph"
        )
    if paper == "28-bolza-magnetic-flow" and issue["ref_id"] == "AigonDupuyEtAl2005":
        return bib_field(entry, "author") == (
            'Aigon-Dupuy, Aline and Buser, Peter and Cibils, Michel and '
            'K{\\"u}nzle, Alfred F. and Steiner, Frank'
        )
    return False


def scholar_intake_is_valid(passport: dict[str, Any]) -> bool:
    declaration = passport.get("experiment_intake_declaration")
    if not isinstance(declaration, dict):
        return False
    confirmation = (
        declaration.get("confirmation_time")
        or declaration.get("confirmed_at")
        or declaration.get("declared_at")
    )
    basic = (
        declaration.get("status") == "experiments_declared"
        and declaration.get("declared_by") == "scholar"
        and isinstance(confirmation, str)
        and bool(confirmation.strip())
        and isinstance(passport.get("experiment_provenance"), list)
        and bool(passport["experiment_provenance"])
        and isinstance(passport.get("experiment_alignment_results"), list)
        and bool(passport["experiment_alignment_results"])
        and isinstance(passport.get("claim_intent_manifests"), list)
        and bool(passport["claim_intent_manifests"])
    )
    if not basic:
        return False
    contracts = ars_root() / "shared" / "contracts" / "passport"
    provenance_schema = json.loads(
        (contracts / "experiment_provenance_entry.schema.json").read_text(
            encoding="utf-8"
        )
    )
    alignment_schema = json.loads(
        (contracts / "experiment_alignment_result.schema.json").read_text(
            encoding="utf-8"
        )
    )
    manifest_schema = json.loads(
        (contracts / "claim_intent_manifest.schema.json").read_text(encoding="utf-8")
    )
    try:
        for entry in passport["experiment_provenance"]:
            jsonschema.Draft202012Validator(provenance_schema).validate(entry)
        for entry in passport["experiment_alignment_results"]:
            jsonschema.Draft202012Validator(
                alignment_schema, format_checker=jsonschema.FormatChecker()
            ).validate(entry)
        for entry in passport["claim_intent_manifests"]:
            jsonschema.Draft202012Validator(
                manifest_schema, format_checker=jsonschema.FormatChecker()
            ).validate(entry)
    except jsonschema.ValidationError:
        return False
    experiment_ids = [entry["experiment_id"] for entry in passport["experiment_provenance"]]
    if len(experiment_ids) != len(set(experiment_ids)):
        return False
    experiment_id_set = set(experiment_ids)
    manifest_claims: dict[tuple[str, str], dict[str, Any]] = {}
    for manifest in passport["claim_intent_manifests"]:
        for claim in manifest["claims"]:
            key = (manifest["manifest_id"], claim["claim_id"])
            if key in manifest_claims:
                return False
            manifest_claims[key] = claim
            planned = claim.get("planned_experiment_ids", [])
            if any(exp_id not in experiment_id_set for exp_id in planned):
                return False
            if planned and claim["intended_evidence_kind"] != "empirical":
                return False
    alignment_pairs = []
    finding_ids = []
    for row in passport["experiment_alignment_results"]:
        key = (row["scoped_manifest_id"], row["claim_id"])
        claim = manifest_claims.get(key)
        if (
            claim is None
            or row["experiment_id"] not in claim.get("planned_experiment_ids", [])
            or row["alignment_verdict"] != "ALIGNED"
        ):
            return False
        alignment_pairs.append((key, row["experiment_id"]))
        finding_ids.append(row["finding_id"])
    expected_pairs = {
        (key, exp_id)
        for key, claim in manifest_claims.items()
        for exp_id in claim.get("planned_experiment_ids", [])
    }
    if (
        len(finding_ids) != len(set(finding_ids))
        or len(alignment_pairs) != len(set(alignment_pairs))
        or set(alignment_pairs) != expected_pairs
    ):
        return False
    if any(
        not any(unit["executed"] for unit in entry["planned_vs_executed"])
        for entry in passport["experiment_provenance"]
    ):
        return False
    return True


def runtime_config(paper: str, cfg: dict[str, Any]) -> dict[str, Any]:
    """Resolve named blockers from current authorized bytes without erasing state."""

    result = dict(cfg)
    base = ROOT / "papers" / paper
    bib_text = (base / "paper" / "references.bib").read_text(encoding="utf-8")
    passport_path = base / "notes" / "stage2_5_material_passport.json"
    passport = (
        json.loads(passport_path.read_text(encoding="utf-8"))
        if passport_path.is_file()
        else {}
    )
    has_declaration = "experiment_intake_declaration" in passport
    has_provenance = bool(passport.get("experiment_provenance"))
    has_alignment = bool(passport.get("experiment_alignment_results"))
    has_manifest = bool(passport.get("claim_intent_manifests"))
    intake_valid = scholar_intake_is_valid(passport)
    if (has_declaration or has_provenance or has_alignment or has_manifest) and not intake_valid:
        raise RuntimeError(
            f"{paper}: partial/invalid scholar experiment intake; refusing to overwrite it"
        )

    active = []
    for issue in cfg["issues"]:
        if issue["type"] == "missing_scholar_experiment_intake":
            if not intake_valid:
                active.append(issue)
        elif not reference_issue_resolved(paper, issue, bib_text):
            active.append(issue)
    result["issues"] = active
    result["refs_passed"] = result["refs"] - sum(
        1 for issue in active if issue["phase"] == "A"
    )
    result["intake_valid"] = intake_valid
    result["existing_passport"] = passport
    return result


def preflight_one(paper: str, cfg: dict[str, Any], frozen: dict[str, Any]) -> None:
    """Validate every read-only input before any generated report is replaced."""

    base = ROOT / "papers" / paper
    notes = base / "notes"
    protected = {
        "manuscript_sha256": base / "paper" / "manuscript.tex",
        "bibliography_sha256": base / "paper" / "references.bib",
        "pdf_sha256": base / "paper" / "paper.pdf",
    }
    for key, path in protected.items():
        if sha(path) != frozen[key]:
            raise RuntimeError(f"{paper}: input freeze mismatch for {key}")

    registry_path = notes / "stage2_5_claim_registry.json"
    coverage_path = notes / "stage2_5_claim_registry_coverage.json"
    rows_path = notes / "stage2_5_evidence_rows.json"
    drift_path = notes / "stage2_5_claim_strength_drift_findings.json"
    semantic_path = notes / "stage2_5_phase_e_semantic_audit.md"
    semantic_receipt_path = notes / "stage2_5_phase_e_semantic_verdicts.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    rows = json.loads(rows_path.read_text(encoding="utf-8"))
    drift = json.loads(drift_path.read_text(encoding="utf-8"))
    receipt = json.loads(semantic_receipt_path.read_text(encoding="utf-8"))
    selected = {
        claim["claim_id"]: claim
        for claim in registry["claims"]
        if claim["selection_tier"] != "NOT-SELECTED"
    }
    expected_tuples = {
        (claim_id, ref)
        for claim_id, claim in selected.items()
        for ref in (claim["ref_slugs"] or [None])
    }
    actual_tuples = [
        (row["claim"]["claim_id"], row["source"]["ref_slug"]) for row in rows
    ]
    if len(actual_tuples) != len(expected_tuples) or set(actual_tuples) != expected_tuples:
        raise RuntimeError(f"{paper}: non-exact selected evidence tuple projection")
    if any(row["excerpt"]["state"] != "anchorless" for row in rows):
        raise RuntimeError(f"{paper}: unexpected non-anchorless evidence row")
    if coverage.get("schema_version") != "claim-registry-coverage/1.0":
        raise RuntimeError(f"{paper}: coverage schema mismatch")
    if coverage.get("candidate_unregistered_count") != 0:
        raise RuntimeError(f"{paper}: unresolved coverage candidate")
    if coverage.get("draft_raw_sha256") != sha(protected["manuscript_sha256"]):
        raise RuntimeError(f"{paper}: coverage manuscript binding mismatch")
    if coverage.get("registry_raw_sha256") != sha(registry_path):
        raise RuntimeError(f"{paper}: coverage registry binding mismatch")
    if drift.get("status") != "skipped_no_revision_evidence" or drift.get("findings"):
        raise RuntimeError(f"{paper}: invalid first-pass drift state")

    bindings = receipt.get("bindings", {})
    expected_bindings = {
        "manuscript_sha256": sha(protected["manuscript_sha256"]),
        "claim_registry_sha256": sha(registry_path),
        "evidence_rows_sha256": sha(rows_path),
        "semantic_audit_sha256": sha(semantic_path),
    }
    if bindings != expected_bindings:
        raise RuntimeError(f"{paper}: stale semantic-verdict receipt bindings")
    verdicts = receipt.get("claim_verdicts", [])
    if receipt.get("decision") != "PASS_SELECTED_POPULATION":
        raise RuntimeError(f"{paper}: semantic receipt is not PASS")
    if len(verdicts) != len(selected):
        raise RuntimeError(f"{paper}: semantic distinct-claim denominator mismatch")
    verdict_by_id = {row.get("claim_id"): row for row in verdicts}
    if len(verdict_by_id) != len(verdicts) or set(verdict_by_id) != set(selected):
        raise RuntimeError(f"{paper}: semantic claim population mismatch")
    grouped_rows: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped_rows.setdefault(row["claim"]["claim_id"], []).append(row)
    for claim_id, verdict in verdict_by_id.items():
        claim_rows = grouped_rows[claim_id]
        if verdict.get("verdict") != "VERIFIED":
            raise RuntimeError(f"{paper}: non-VERIFIED semantic verdict for {claim_id}")
        if verdict.get("tuple_count") != len(claim_rows):
            raise RuntimeError(f"{paper}: semantic tuple count mismatch for {claim_id}")
        if verdict.get("row_ids") != [row["row_id"] for row in claim_rows]:
            raise RuntimeError(f"{paper}: semantic row-id binding mismatch for {claim_id}")
        if verdict.get("row_sha256s") != [row["row_sha256"] for row in claim_rows]:
            raise RuntimeError(f"{paper}: semantic row-hash binding mismatch for {claim_id}")
        if any(row["verdict"] != "VERIFIED" for row in claim_rows):
            raise RuntimeError(f"{paper}: evidence verdict conflicts with semantic audit")

    # Replay the official bounded-coverage validator before report generation.
    coverage_script = ars_root() / "scripts" / "claim_registry_coverage.py"
    subprocess.run(
        [
            sys.executable,
            str(coverage_script),
            "--draft",
            str(protected["manuscript_sha256"]),
            "--registry",
            str(registry_path),
            "--validate-report",
            str(coverage_path),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def build_one(paper: str, cfg: dict[str, Any], timestamp: str) -> dict[str, Any]:
    base = ROOT / "papers" / paper
    notes = base / "notes"
    manuscript = base / "paper" / "manuscript.tex"
    bibliography = base / "paper" / "references.bib"
    pdf = base / "paper" / "paper.pdf"
    registry_path = notes / "stage2_5_claim_registry.json"
    coverage_path = notes / "stage2_5_claim_registry_coverage.json"
    rows_path = notes / "stage2_5_evidence_rows.json"
    drift_path = notes / "stage2_5_claim_strength_drift_findings.json"
    semantic_receipt_path = notes / "stage2_5_phase_e_semantic_verdicts.json"
    adjudication_path = notes / "stage2_5_claim_registry_coverage_adjudication.md"

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    evidence_rows = json.loads(rows_path.read_text(encoding="utf-8"))
    semantic_receipt = json.loads(semantic_receipt_path.read_text(encoding="utf-8"))
    selected = [c for c in registry["claims"] if c["selection_tier"] != "NOT-SELECTED"]
    tier_counts: dict[str, int] = {}
    for claim in registry["claims"]:
        tier_counts[claim["selection_tier"]] = tier_counts.get(claim["selection_tier"], 0) + 1
    distinct_row_claims = {row["claim"]["claim_id"] for row in evidence_rows}
    expected_tuples = {
        (claim["claim_id"], ref)
        for claim in selected
        for ref in (claim["ref_slugs"] or [None])
    }
    actual_tuples = {
        (row["claim"]["claim_id"], row["source"]["ref_slug"])
        for row in evidence_rows
    }
    if expected_tuples != actual_tuples:
        raise RuntimeError(f"{paper}: selected evidence tuple mismatch")
    if distinct_row_claims != {claim["claim_id"] for claim in selected}:
        raise RuntimeError(f"{paper}: distinct evidence claim mismatch")

    adjudication = f"""# Paper {cfg['number']} Stage-2.5 Claim Registry coverage adjudication

Audit target: `paper/manuscript.tex` SHA-256 `{sha(manuscript)}`  
Registry: `claim-registry/1.0` SHA-256 `{sha(registry_path)}`

## Result

- Registered population: **{len(registry['claims'])}** exact UTF-8-bound rows.
- Risk-stratified selection: **{len(selected)}** distinct claims: `{tier_counts.get('HIGH-IMPACT', 0)}` HIGH-IMPACT, `{tier_counts.get('RANDOM', 0)}` RANDOM, `{tier_counts.get('TOP-UP', 0)}` TOP-UP.
- Persisted evidence tuples: **{len(evidence_rows)}/{len(expected_tuples)}**; exact `(claim_id, ref_slug-or-null)` set equality PASS.
- Mechanically detectable candidates: **{len(coverage.get('candidates', []))}**; unresolved candidates: **{coverage.get('candidate_unregistered_count', 0)}**.
- Coverage replay state: **COMPLETED / zero bounded gaps**.
- Semantic extraction coverage remains exactly **`not_machine_detectable`**; this report never upgrades bounded lexical coverage into a completeness guarantee.
- All evidence carriers are explicitly `anchorless`; they prove registry/tuple conformance but do not independently prove a source excerpt or a semantic verdict. Semantic adjudication lives in `stage2_5_phase_e_semantic_audit.md` and the Phase A--C proof/source audits.

## Supersession record

The first Round-9 sidecar build underclassified numerical, causal, and methods-critical claims and excluded mechanical-origin rows from the RANDOM denominator. It is superseded. The stable build applies ARS #549 to every registry row, checks 100% of HIGH-IMPACT claims, applies the rounded-up 10% sentinel to the complete non-high-impact remainder, and persists one row per selected source tuple.
"""
    write_text(adjudication_path, adjudication)

    comp = compliance(paper, cfg, timestamp)
    comp_path = notes / "stage2_5_compliance_report.json"
    write_json(comp_path, comp)

    exp_issue = next(
        (i for i in cfg["issues"] if i["type"] == "missing_scholar_experiment_intake"),
        None,
    )
    c_issues = (
        [
            {
                "claim": "passport-level D7 experiment intake declaration",
                "expected": "scholar-owned status=experiments_declared plus non-empty experiment_provenance and claim alignment",
                "actual": "experiment_intake_declaration absent; provenance/alignment not inferable by an agent",
                "severity": exp_issue["severity"],
            }
        ]
        if exp_issue
        else []
    )
    severity_counts = {
        severity: sum(1 for issue in cfg["issues"] if issue["severity"] == severity)
        for severity in ("SERIOUS", "MEDIUM")
    }
    blocking_issues = severity_counts["SERIOUS"] + severity_counts["MEDIUM"]
    passed = blocking_issues == 0
    semantic_verified = semantic_receipt["verdict_counts"]["VERIFIED"]
    citation_score = cfg["refs_passed"] / cfg["refs"]
    report = {
        "verdict": "PASS" if passed else "FAIL",
        "mode": "pre-review",
        "phases": {
            "A_references": {
                "checked": cfg["refs"],
                "passed": cfg["refs_passed"],
                "failed": cfg["refs"] - cfg["refs_passed"],
                "issues": phase_a_issues(cfg),
            },
            "B_citation_context": {
                "sampled": cfg["contexts"],
                "verified": cfg["contexts"],
                "issues": [],
            },
            "C_data": {
                "claims_checked": cfg["data"],
                "verified": cfg["data"],
                "issues": [],
            },
            "C4_experiment_intake": {
                "claims_checked": 1,
                "verified": 1 if cfg["intake_valid"] else 0,
                "issues": c_issues,
            },
            "D_originality": {
                "checked": True,
                "issues": (
                    [
                        {
                            "type": "standardized_declaration_boilerplate_overlap",
                            "severity": "MINOR",
                            "detail": cfg["shared_declaration_minor"],
                        }
                    ]
                    if cfg.get("shared_declaration_minor")
                    else []
                ),
            },
            "E_claims": {
                "checked": len(selected),
                "verified": semantic_verified,
                "distortions": [],
                "semantic_verdict_receipt": {
                    "schema_version": semantic_receipt["schema"],
                    "artifact_path": "notes/stage2_5_phase_e_semantic_verdicts.json",
                    "artifact_sha256": sha(semantic_receipt_path),
                    "semantic_audit_sha256": semantic_receipt["bindings"]["semantic_audit_sha256"],
                },
                "claim_registry_coverage": {
                    "status": "completed",
                    "registry_schema_version": "claim-registry/1.0",
                    "report_path": "notes/stage2_5_claim_registry_coverage.json",
                    "report_sha256": sha(coverage_path),
                    "draft_raw_sha256": sha(manuscript),
                    "registry_raw_sha256": sha(registry_path),
                    "candidate_unregistered_count": coverage.get("candidate_unregistered_count", 0),
                    "semantic_extraction_coverage": "not_machine_detectable",
                    "adjudication_path": "notes/stage2_5_claim_registry_coverage_adjudication.md",
                    "adjudication_sha256": sha(adjudication_path),
                },
                "evidence_rows": evidence_rows,
                "claim_strength_drift_findings": {
                    "schema_version": "claim-strength-drift-findings/1.0",
                    "artifact_path": "notes/stage2_5_claim_strength_drift_findings.json",
                    "artifact_sha256": sha(drift_path),
                },
            },
        },
        "overall_issues": {
            "SERIOUS": severity_counts["SERIOUS"],
            "MEDIUM": severity_counts["MEDIUM"],
            "MINOR": 1 if cfg.get("shared_declaration_minor") else 0,
        },
        "citation_integrity_score": round(citation_score, 6),
        "fabrication_risk_score": round(1.0 - citation_score, 6),
        "timestamp": timestamp,
        "extensions": {
            "display_verdict": "PASS_AT_STAGE_2.5_CHECKPOINT" if passed else "FAIL-CLOSED",
            "content_integrity": "CLEAN_WITHIN_AUDITED_SCIENTIFIC_SURFACES" if cfg["refs"] == cfg["refs_passed"] else "CLEAN_EXCEPT_NAMED_REFERENCE_METADATA_MISMATCHES",
            "input_freeze": {
                "manuscript_sha256": sha(manuscript),
                "bibliography_sha256": sha(bibliography),
                "pdf_sha256": sha(pdf),
            },
            "claim_selection": {
                "registered": len(registry["claims"]),
                "tiers": tier_counts,
                "selected_distinct_claims": len(selected),
                "evidence_tuples": len(evidence_rows),
                "anchorless_rows": len(evidence_rows),
            },
            "originality": {
                "sampled": cfg["originality"][0],
                "denominator": cfg["originality"][1],
                "sampling_rate": round(cfg["originality"][0] / cfg["originality"][1], 6),
                "professional_detector": False,
            },
            "failure_modes": {
                "mode_1": "CLEAR_WITHIN_REPLAYED_TEST_AND_ARTIFACT_SCOPE",
                "mode_2": "SUSPECTED_BLOCKING" if cfg["refs"] != cfg["refs_passed"] else "CLEAR",
                "mode_3": "CLEAR_WITHIN_FROZEN_ARTIFACT_SCOPE",
                "mode_4": "CLEAR",
                "mode_5": "CLEAR",
                "mode_6": (
                    "CLEAR_WITHIN_DISCLOSURE_AND_PROVENANCE_FIDELITY_SCOPE"
                    if cfg["intake_valid"]
                    else "INSUFFICIENT_EVIDENCE_BLOCKING_MISSING_SCHOLAR_INTAKE"
                ),
                "mode_7": "CLEAR",
            },
            "route_crosswalk": {
                "route_a": cfg["route"],
                "route_a_sha256": ROUTE_A_SHA,
                "route_b": "NOT_INVOKED",
                "route_b_sha256": ROUTE_B_SHA,
                "positive_arithmetic_A2": False,
                "gate_credit": "NONE",
            },
            "active_issue_ids": [issue["id"] for issue in cfg["issues"]],
            "score_boundary": "Scores summarize registered checked surfaces; they are not probabilities or guarantees of mathematical truth, semantic completeness, corpus completeness, or global originality.",
        },
    }
    report_path = notes / "stage2_5_integrity_report.json"
    write_json(report_path, report)

    existing_passport = cfg["existing_passport"]
    passport = {
        "origin_skill": "ars-codex:academic-research-suite",
        "origin_mode": "full",
        "origin_date": timestamp,
        "verification_status": "VERIFIED" if passed else "UNVERIFIED",
        "version_label": (
            f"p{cfg['number']}-round9-stage2.5-pass-v2"
            if passed
            else f"p{cfg['number']}-round9-stage2.5-fail-closed-v2"
        ),
        "content_hash": sha(manuscript),
        "upstream_dependencies": [
            "round9-stage2-manuscript",
            "round9-stage2.5-input-freeze",
            "claim-registry/1.0",
            "claim-registry-coverage/1.0",
            "evidence-row/1.0",
            "flow-systems-stage2.5-semantic-verdict-receipt/1.0",
            *[issue["id"] for issue in cfg["issues"]],
        ],
        "repro_lock": existing_passport.get("repro_lock"),
        "slr_lineage": False,
        "experiment_provenance": existing_passport.get("experiment_provenance", []),
        "experiment_alignment_results": existing_passport.get(
            "experiment_alignment_results", []
        ),
        "compliance_history": [comp],
    }
    if cfg["intake_valid"]:
        passport["experiment_intake_declaration"] = existing_passport[
            "experiment_intake_declaration"
        ]
        passport["claim_intent_manifests"] = existing_passport[
            "claim_intent_manifests"
        ]
    passport_path = notes / "stage2_5_material_passport.json"
    write_json(passport_path, passport)

    if exp_issue:
        gap_md = f"""# Paper {cfg['number']} Stage-2.5 experiment-provenance gap

Stable issue: **`{exp_issue['id']}` — SERIOUS / BLOCKING**.

The manuscript reports project-owned computational executions, tests, finite classifications, or certificates. The repository contains substantial source, result, freeze, test, validation, and receipt artifacts, but ARS does not permit an agent to infer or sign the scholar-owned intake decision from those files.

Required closure sequence:

1. The scholar explicitly confirms `status=experiments_declared`, `declared_by=scholar`, and the confirmation time for Paper {cfg['number']}.
2. Transcribe the already frozen Round-2--8 experiment packages into schema-valid `experiment_provenance[]`; do not invent omitted runs or results.
3. Bind experiment-backed registered claims through `planned_experiment_ids[]` and generate `experiment_alignment_results[]`.
4. Re-run C4/D7 and the seven failure modes on the exact resulting passport.

Required boundary: **This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.**
"""
    else:
        gap_md = f"""# Paper {cfg['number']} Stage-2.5 experiment-provenance closure

The scholar-owned `experiment_intake_declaration` is present with
`status=experiments_declared`, `declared_by=scholar`, and a confirmation time.
The passport also contains non-empty experiment provenance and claim-alignment
results. C4/D7 therefore closes within its disclosure/provenance-fidelity
scope.

Required boundary: **This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.**
"""
    write_text(notes / "stage2_5_experiment_provenance_gap.md", gap_md)

    rows_percent = 100.0 * cfg["originality"][0] / cfg["originality"][1]
    issue_lines = "\n".join(
        f"| `{i['id']}` | {i['phase']} | {i['detail']} | {i['action']} |" for i in cfg["issues"]
    ) or "| — | — | No active blocking integrity issue. | — |"
    decision_text = (
        "PASS AT STAGE 2.5 CHECKPOINT — AWAIT EXPLICIT STAGE 3 AUTHORIZATION"
        if passed
        else "FAIL-CLOSED — DO NOT ENTER STAGE 3"
    )
    outcome_text = (
        "The complete registered integrity surfaces pass their stated denominators. "
        "The workflow nevertheless stops at the mandatory checkpoint; Stage 3 is not "
        "authorized automatically."
        if passed
        else (
            "The complete registered integrity surfaces were audited against the frozen "
            "manuscript, bibliography, PDF, sources, proof chain, and local result "
            f"artifacts. Scientific/data surfaces are clean within the stated denominators; "
            f"the checkpoint nevertheless fails because {blocking_issues} named blocking "
            "issue(s) remain open. A FAIL is not a rejection of the paper's mathematics: "
            "it is the mandatory correction/intake boundary."
        )
    )
    intake_result = (
        "1/1 declaration | scholar-owned intake plus non-empty provenance/alignment VERIFIED"
        if cfg["intake_valid"]
        else "0/1 declaration | **FAIL-CLOSED**; scholar declaration absent"
    )
    mode6_result = (
        "CLEAR within disclosure and claim-to-provenance fidelity scope; design/run adequacy remains outside this check."
        if cfg["intake_valid"]
        else "**INSUFFICIENT EVIDENCE / BLOCKING** until the scholar-owned intake/provenance ledger exists."
    )
    checkpoint_text = (
        "Stage 2.5 passes and stops at its mandatory checkpoint with `verification_status=VERIFIED`. Manuscript, bibliography, and PDF remain frozen. Stage 3 still requires an explicit authorization and must not start automatically."
        if passed
        else "Stage 2.5 stops here with `verification_status=UNVERIFIED`. Manuscript, bibliography, and PDF remain frozen. The named bibliographic corrections require exact user authorization, and experiment intake requires the scholar's explicit declaration. Stage 3 must not start automatically."
    )
    report_md = f"""# Paper {cfg['number']} Stage-2.5 Integrity Report

Audit timestamp: **{timestamp}**  
Mode: **pre-review / ARS Stage 2.5 Mode 1**  
Decision: **{decision_text}**

## Outcome

{outcome_text}

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `{sha(manuscript)}` |
| `paper/references.bib` | `{sha(bibliography)}` |
| `paper/paper.pdf` | `{sha(pdf)}` |
| claim registry | `{sha(registry_path)}` |
| coverage report | `{sha(coverage_path)}` |
| evidence rows | `{sha(rows_path)}` |
| semantic verdict receipt | `{sha(semantic_receipt_path)}` |

## Phase results

| Phase | Coverage | Result |
|---|---:|---|
| A — reference identity/metadata | {cfg['refs']}/{cfg['refs']} | {cfg['refs_passed']} VERIFIED; {cfg['refs'] - cfg['refs_passed']} MISMATCH |
| B — citation contexts | {cfg['contexts']}/{cfg['contexts']} | all content contexts supported |
| C — registered numerical/data families | {cfg['data']}/{cfg['data']} | all internally consistent and replayed |
| C4/D7 — experiment intake | {intake_result} |
| D — originality heuristic | {cfg['originality'][0]}/{cfg['originality'][1]} ({rows_percent:.1f}%) | no actionable body overlap; {"one shared standardized-declaration MINOR recorded" if cfg.get('shared_declaration_minor') else "no paper-specific overlap issue"} |
| E — registered claim verification | {len(selected)}/{len(registry['claims'])} selected | {semantic_verified} semantically VERIFIED in the hash-bound receipt; {len(evidence_rows)}/{len(expected_tuples)} tuple carriers valid |
| E6 — claim-strength drift | first pass | correctly skipped: no revision evidence |

Phase D is heuristic public-Web screening, not Turnitin or iThenticate. It can miss paywalled, cross-language, or unindexed overlap. Professional screening remains recommended before submission.

The batch self-overlap audit checked all 10/10 local paper pairs, 22/22 ORCID-bound Zenodo PDFs, and two older official arXiv PDFs. It found zero substantive exact eight-word body reuse. {cfg.get('shared_declaration_minor', 'No paper-specific declaration-template overlap was assigned to this manuscript.')} This note is non-blocking and does not change the scientific originality result.

## Phase E receipt and limitation

The stable risk selection contains `{tier_counts.get('HIGH-IMPACT', 0)}` HIGH-IMPACT claims checked at 100% and `{tier_counts.get('RANDOM', 0)}` RANDOM sentinels, for `{len(selected)}` distinct claims and `{len(evidence_rows)}` source tuples. Coverage replay reports zero bounded lexical gaps, while semantic extraction coverage remains `not_machine_detectable`.

All `{len(evidence_rows)}` evidence rows are explicitly `anchorless`. Their schema and tuple coverage are valid, but those rows alone do not prove semantic correctness or reproduce an external excerpt. The substantive verdict rests on the independent Phase A--C audit plus `notes/stage2_5_phase_e_semantic_audit.md`, now bound claim-by-claim by `notes/stage2_5_phase_e_semantic_verdicts.json`; this limitation is preserved rather than hidden.

## Active issues

| ID | Phase | Finding | Exact closure route |
|---|---|---|---|
{issue_lines}

## Seven failure modes

- Mode 1 implementation bugs: CLEAR within the `{cfg['tests'][0]}` historical-test + `{cfg['tests'][1]}` Round-8 replay scope.
- Mode 2 hallucinated citation: {"SUSPECTED / BLOCKING because named author metadata mismatches remain" if cfg['refs'] != cfg['refs_passed'] else "CLEAR"}.
- Mode 3 hallucinated result: CLEAR within the frozen source/result/hash and replay scope.
- Mode 4 shortcut reliance: CLEAR; frozen populations and negative controls are retained.
- Mode 5 bug reframed as insight: CLEAR; the manuscript preserves negative and bounded conclusions.
- Mode 6 methodology fabrication: {mode6_result}
- Mode 7 early frame-lock: CLEAR; limitations and the next falsifiable Route-A obligation remain explicit.

## Roadmap crosswalk

- Route A: {cfg['route']}.
- Route A file SHA-256: `{ROUTE_A_SHA}`.
- Route B: **NOT INVOKED**; file SHA-256 `{ROUTE_B_SHA}`.
- Positive arithmetic candidate reaching A2: **no**.
- Gate credit from this integrity audit: **none**.

## Mandatory checkpoint

{checkpoint_text}
"""
    write_text(notes / "stage2_5_integrity_report.md", report_md)

    return {
        "paper": paper,
        "number": cfg["number"],
        "verdict": "PASS" if passed else "FAIL",
        "registered_claims": len(registry["claims"]),
        "selected_claims": len(selected),
        "evidence_tuples": len(evidence_rows),
        "references_verified": cfg["refs_passed"],
        "references_total": cfg["refs"],
        "active_issues": [issue["id"] for issue in cfg["issues"]],
        "active_issue_severities": [issue["severity"] for issue in cfg["issues"]],
        "integrity_report_sha256": sha(report_path),
        "material_passport_sha256": sha(passport_path),
        "compliance_report_sha256": sha(comp_path),
    }


def main() -> int:
    timestamp = utc_now()
    if sha(ROOT / "skills" / "route-a-evaluator.md") != ROUTE_A_SHA:
        raise RuntimeError("Route-A evaluator hash changed; adjudicate the roadmap before compiling")
    if sha(ROOT / "skills" / "route-b-evaluator.md") != ROUTE_B_SHA:
        raise RuntimeError("Route-B evaluator hash changed; adjudicate the roadmap before compiling")
    freeze = json.loads(
        (ROOT / "BATCH_ROUND9_STAGE2_5_INPUT_FREEZE.json").read_text(encoding="utf-8")
    )
    frozen = {row["paper"]: row for row in freeze["papers"]}
    if set(frozen) != set(PAPERS):
        raise RuntimeError("input freeze paper population mismatch")
    runtime_papers = {
        paper: runtime_config(paper, cfg) for paper, cfg in PAPERS.items()
    }
    # Complete read-only preflight: no report is replaced until all five
    # frozen inputs, tuple sets, semantic receipts, routes, and coverage
    # replays validate.
    for paper, cfg in runtime_papers.items():
        preflight_one(paper, cfg, frozen[paper])
    summary = [
        build_one(paper, cfg, timestamp) for paper, cfg in runtime_papers.items()
    ]
    papers_passed = sum(row["verdict"] == "PASS" for row in summary)
    batch_passed = papers_passed == len(summary)
    serious_issues = sum(
        severity == "SERIOUS"
        for row in summary
        for severity in row["active_issue_severities"]
    )
    batch = {
        "schema": "flow-systems-round9-stage2.5-integrity-summary/1.0",
        "generated_at": timestamp,
        "batch_verdict": "PASS" if batch_passed else "FAIL-CLOSED",
        "stage3_authorized": False,
        "papers": summary,
        "aggregate": {
            "papers": len(summary),
            "papers_passed": papers_passed,
            "registered_claims": sum(row["registered_claims"] for row in summary),
            "selected_claims": sum(row["selected_claims"] for row in summary),
            "evidence_tuples": sum(row["evidence_tuples"] for row in summary),
            "references_verified": sum(row["references_verified"] for row in summary),
            "references_total": sum(row["references_total"] for row in summary),
            "serious_issues": serious_issues,
            "batch_nonblocking_minor_finding_ids": [
                "ROUND9-D-DECLARATION-BOILERPLATE-OVERLAP-1"
            ],
            "batch_nonblocking_minor_findings": 1,
            "positive_arithmetic_A2": 0,
            "route_b_invocations": 0,
        },
        "route_a_sha256": ROUTE_A_SHA,
        "route_b_sha256": ROUTE_B_SHA,
    }
    write_json(ROOT / "BATCH_ROUND9_STAGE2_5_INTEGRITY_SUMMARY.json", batch)
    progress = {
        24: "universal congruence + first-jet theorem; A0 controls 2/3",
        25: "physical-roof nontransfer; symbolic control remains rejected",
        26: "exhaustive 138-instance owner taxonomy and A2 obstruction",
        27: "residual/homology four-quadrant obstruction and calibration",
        28: "exact nonarithmetic-control systole/completeness theorem",
    }
    short_issue = {
        "missing_scholar_experiment_intake": "experiment intake",
        "reference_author_metadata_mismatch": "reference metadata",
        "reference_author_and_subject_metadata_mismatch": "reference metadata",
    }
    paper_rows = []
    for row in summary:
        cfg = runtime_papers[row["paper"]]
        blockers = "; ".join(short_issue[i["type"]] for i in cfg["issues"]) or "none"
        paper_rows.append(
            f"| P{row['number']} | {row['references_verified']}/{row['references_total']} | "
            f"{row['selected_claims']} claims / {row['evidence_tuples']} tuples | "
            f"{row['verdict']} | {blockers} | {progress[row['number']]} |"
        )
    paper_table = "\n".join(paper_rows)
    intake_open = sum(
        issue["type"] == "missing_scholar_experiment_intake"
        for cfg in runtime_papers.values()
        for issue in cfg["issues"]
    )
    reference_open = sum(
        issue["phase"] == "A"
        for cfg in runtime_papers.values()
        for issue in cfg["issues"]
    )
    references_verified = sum(row["references_verified"] for row in summary)
    batch_decision_text = (
        "PASS AT STAGE 2.5 CHECKPOINT — Stage 3 still requires explicit authorization"
        if batch_passed
        else f"FAIL-CLOSED — {papers_passed}/5 papers pass; Stage 3 remains closed"
    )
    outcome_text = (
        "All five papers pass the registered Stage-2.5 denominators. The mandatory "
        "checkpoint is reached, but `stage3_authorized=false`; no review stage starts "
        "without a separate explicit authorization."
        if batch_passed
        else (
            "The scientific manuscripts are substantially intact within the audited "
            "surfaces, but the mandatory integrity checkpoint is not passed. The complete "
            f"audit found **{serious_issues} SERIOUS blockers**: {intake_open} missing "
            f"scholar-owned experiment intake declaration(s) and {reference_open} named "
            "reference-metadata mismatch(es). No manuscript, bibliography, or release PDF "
            "was changed during this report compilation."
        )
    )
    active_ids = {
        issue["id"]
        for cfg in runtime_papers.values()
        for issue in cfg["issues"]
    }
    correction_blocks = []
    if "P25-IL-SERIOUS-REF-1" in active_ids:
        correction_blocks.append(
            """Paper 25, `BowenLanford1970`:

```bibtex
  author    = {Bowen, Rufus and Lanford, III, Oscar E.},
```"""
        )
    if "P28-IL-SERIOUS-REF-1" in active_ids:
        correction_blocks.append(
            """Paper 28, `Nazarenko2013`:

```bibtex
  author        = {Nazarenko, A. V.},
  primaryclass  = {math-ph},
```"""
        )
    if "P28-IL-SERIOUS-REF-2" in active_ids:
        correction_blocks.append(
            """Paper 28, `AigonDupuyEtAl2005`:

```bibtex
  author  = {Aigon-Dupuy, Aline and Buser, Peter and Cibils, Michel and K{\\\"u}nzle, Alfred F. and Steiner, Frank},
```"""
        )
    corrections_text = (
        "\n\n".join(correction_blocks)
        + "\n\nThese are correction proposals, not write authority. After exact authorization they require bibliography mutation, PDF rebuild, freeze refresh, and fresh Phase A/B plus manuscript-structure validation."
        if correction_blocks
        else "All named reference-metadata corrections are closed in the current frozen bibliography and re-audited PDF."
    )
    intake_text = (
        """An agent cannot infer or sign the following from tests or receipts. To close
the shared D7 gate, the scholar must explicitly confirm the complete statement:

> Papers 24--28 each report computational experiments or certificates actually
> executed for this project. I authorize each passport to record
> `status=experiments_declared`, `declared_by=scholar`, and the confirmation
> time. I authorize the existing Round-2--8 source, freeze, result, test,
> validation, and receipt artifacts to be transcribed into schema-valid
> experiment provenance and aligned to the registered experiment-backed
> claims. To my knowledge, there are no additional omitted own-experiment
> results relied on by these five manuscripts."""
        if intake_open
        else "All five scholar-owned intake declarations and their non-empty provenance/alignment ledgers are present and validated."
    )
    next_action = (
        "Stage 2.5 has passed and stopped. The next legal action is a separate, explicit Stage-3 authorization; this compiler never sets `stage3_authorized=true`."
        if batch_passed
        else "Stage 3 has not started. The next legal action is an explicitly authorized integrity-correction round covering only the still-listed reference patches and/or the complete scholar declaration. After those changes, refresh the freeze, re-run Stage 2.5, and stop again at this checkpoint. A generic ‘continue’ does not authorize manuscript or bibliography mutation."
    )
    batch_md = f"""# Round 9 Papers 24--28 — ARS Stage 2.5 Integrity Report

Audit timestamp: **{timestamp}**  
Governing stage: **Stage 2.5 / pre-review integrity**  
Batch decision: **{batch_decision_text}**

## Outcome first

{outcome_text}

The earlier 58-claim Phase-E sample was invalid and has been superseded. The
stable audit registers **382 claims**, checks **316 HIGH-IMPACT + 15 RANDOM =
331 distinct claims**, and persists **340/340 exact evidence tuples**. All five
coverage reports replay with zero bounded gaps. All 340 tuple carriers are
explicitly `anchorless`: structural/hash/selection conformance passes, while
semantic support is supplied separately by the proof/artifact/source audits
and bound claim-by-claim in five semantic-verdict receipts.

## Batch denominators

| Surface | Result |
|---|---:|
| Frozen manuscripts / bibliographies / PDFs | 15/15 hashes unchanged |
| References | 31/31 checked; {references_verified} VERIFIED, {31 - references_verified} MISMATCH |
| Citation contexts | 38/38 content-supported |
| Numerical/data surface families | 50/50 traced and replayed |
| Historical tests | 372/372 PASS |
| Round-8 replay tests | 80/80 PASS |
| Originality paragraphs | 113/343 (32.9%), every major section represented |
| Local cross-paper body pairs | 10/10 exhaustive exact-eight-word screen; 0 substantive reuse |
| Author-corpus public PDFs | 22/22 ORCID-bound Zenodo + 2 arXiv; 0 substantive prose reuse |
| Claim Registry | 382 registered; semantic completeness remains `not_machine_detectable` |
| Phase-E selection | 331 distinct claims; 340/340 tuples |

The declarations contain one non-blocking shared `MINOR`: P24--P25 and
P26--P27 reuse long standardized funding/conflict/ethics/CRediT/AI-assistance
blocks. They are visibly administrative boilerplate, not scientific text.
Professional similarity screening remains recommended before submission.

## Paper-level result

| Paper | Phase A | Phase E | Stage 2.5 | Open blockers | Scientific progress preserved |
|---|---:|---:|---|---|---|
{paper_table}

## Exact named correction proposals — not yet authorized

{corrections_text}

## Scholar-owned experiment declaration required

{intake_text}

Required boundary: **This check verifies disclosure and claim-to-provenance
fidelity. It does not judge whether the experiment was correctly designed,
run, statistically adequate, or reproducible by ARS.**

## Route-A / Route-B crosswalk

- Route A remains the governing scientific roadmap; SHA-256 `{ROUTE_A_SHA}`.
- P24 and P26 remain A0--A1 exploratory/negative candidates with A2 failure.
- P25's symbolic unit-roof determinant is a rejected control and provably does
  not transfer to the physical flow.
- P27's residual owner is rejected and its homology owner is a calibrator, not
  a positive arithmetic candidate.
- P28 is a control-side completeness theorem; the target Bolza/magnetic census
  has not been run, so its full tuple remains unassigned.
- Positive arithmetic candidates reaching A2: **0/5**.
- Route B invocations: **0/5**; Route B SHA-256 `{ROUTE_B_SHA}`.

## Mandatory checkpoint and next legal action

{next_action}

Supporting batch carriers:

- `BATCH_ROUND9_STAGE2_5_INPUT_FREEZE.json`
- `BATCH_ROUND9_STAGE2_5_SIDECAR_VALIDATION.md`
- `BATCH_ROUND9_STAGE2_5_SELF_OVERLAP_AUDIT.md`
- `BATCH_ROUND9_STAGE2_5_EXPERIMENT_INTAKE_REQUEST.md`
- `BATCH_ROUND9_STAGE2_5_INTEGRITY_SUMMARY.json`
"""
    write_text(ROOT / "BATCH_ROUND9_STAGE2_5_INTEGRITY_REPORT.md", batch_md)
    print(json.dumps(batch, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
