#!/usr/bin/env python3
"""Build the Round-9 Stage-4-prime residual authority preview.

This producer is intentionally pre-authority.  It rebinds the residual
Stage-3-prime findings to the current Stage-4 working drafts, emits immutable
non-ranking roadmaps and claim-surface manifests, and renders the exact scope
that still needs an author decision.  It never creates an author-adjudication
sidecar, a revision patch, or a manuscript/result mutation.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DATE = "2026-08-30"


CONFIG: dict[str, dict[str, Any]] = {
    "24-bianchi-holonomy-flow": {
        "prefix": "P24",
        "residuals": {
            "REV-001": {
                "description": (
                    "The current draft now bounds its novelty, but the exact nearest-work "
                    "locators remain outside the hash-bound re-review input, so the "
                    "source-verified comparison is still only partially established."
                ),
                "targets": ["B0015", "B0032", "B0034", "B0104"],
                "action": (
                    "Freshly verify and bind the existing REV-001 provenance note, then "
                    "make only the minimum source-local wording changes needed to expose "
                    "the verified comparison and bounded novelty allocation."
                ),
                "criteria": (
                    "The Stage-4-prime bundle contains a hash-bound primary-source audit "
                    "for every nearest-work locator, and B0015/B0032/B0034/B0104 make no "
                    "broader novelty or full-flow claim."
                ),
                "support": [
                    "notes/stage4_rev001_008_support_provenance.md",
                    "new notes/stage4_prime_rev001_source_evidence.json",
                ],
            },
            "REV-003": {
                "description": (
                    "The loxodromic-only table and matrix-level scope are present, but the "
                    "derivative ledger, manifest, reproducer, tests, and receipt were not "
                    "bound into the re-review input, so the exact counts remain only "
                    "partially verified."
                ),
                "targets": ["B0056", "B0065", "B0067", "B0068", "B0075", "B0084"],
                "action": (
                    "Replay the existing loxodromic-profile support without refreshing "
                    "canonical results, bind every support artifact into the Round-2 "
                    "bundle, and add only exact provenance pointers or scope guards."
                ),
                "criteria": (
                    "The bound manifest, ledger, code, tests, replay command, and receipt "
                    "reproduce the displayed loxodromic counts; all six blocks retain the "
                    "matrix-compression boundary and assert no primitive-owner collision."
                ),
                "support": [
                    "experiments/stage4_loxodromic_profile_manifest.json",
                    "experiments/stage4_loxodromic_profile_receipt.json",
                    "experiments/reproduce_stage4_loxodromic_profile.sh",
                    "code/stage4_loxodromic_profile.py",
                    "code/test_stage4_loxodromic_profile.py",
                    "results/stage4_loxodromic_d9_jet_collision_profile.csv",
                    "results/stage4_loxodromic_d9_jet_metrics.json",
                ],
            },
        },
    },
    "26-level11-newform-time-change": {
        "prefix": "P26",
        "residuals": {
            "REV-02": {
                "description": (
                    "The current related-work frame still lacks a source-verified modern "
                    "nearest-neighbor comparison for primitive closed-geodesic periods and "
                    "the paper's finite Hecke-owner moment obstruction."
                ),
                "targets": ["B0029", "B0030", "B0031", "B0092"],
                "action": (
                    "Add a bounded comparison to the verified Katok antecedent and the "
                    "2025 Constantinescu--Nordentoft geodesic-period result, while stating "
                    "that neither supplies the paper's finite cycle-pushforward taxonomy."
                ),
                "criteria": (
                    "The two exact bibliography entries and primary-source audit are "
                    "hash-bound; B0029/B0030/B0031/B0092 distinguish geodesic-period "
                    "nonvanishing from this finite owner/moment obstruction without a "
                    "global priority or primitive-census claim."
                ),
                "support": [
                    "new notes/stage4_prime_rev02_nearest_work_audit.md",
                    "paper/references.bib: append only Katok1985 and ConstantinescuNordentoft2025 entries",
                ],
            },
            "REV-04": {
                "description": (
                    "The supplemental dependency manifest and receipt exist, but the "
                    "transitive source graph, replay command, tests, and outputs were not "
                    "hash-bound to the re-review input and therefore remain unverifiable "
                    "inside that review package."
                ),
                "targets": ["B0080", "B0081", "B0082", "B0083", "B0093"],
                "action": (
                    "Replay and bind the existing Round-8 support graph and receipt without "
                    "refreshing canonical results, then add only exact provenance pointers "
                    "or bounded dependency-language corrections."
                ),
                "criteria": (
                    "The Stage-4-prime bundle binds the dependency manifest, transitive "
                    "source graph, source, test, replay command, outputs, and receipt; the "
                    "five blocks claim no support beyond that closed graph."
                ),
                "support": [
                    "notes/stage4_round8_dependency_manifest.json",
                    "experiments/stage4_round8_support_receipt.json",
                    "experiments/reproduce_stage4_round8_support.sh",
                    "code/stage4_round8_support.py",
                    "code/test_stage4_round8_support.py",
                    "results/stage4_matched_exact_control_decomposition.csv",
                    "results/stage4_matched_exact_control_summary.json",
                ],
            },
        },
    },
    "27-congruence-inverse-limit-no-go": {
        "prefix": "P27",
        "residuals": {
            "REV-03": {
                "description": (
                    "The current draft adds a -I fixture, but the fixture, test output, and "
                    "receipt were not bound into re-review, and B0040 still calls the two "
                    "strategies independent without qualifying their shared scalar-sign and "
                    "matrix-multiplication kernel."
                ),
                "targets": ["B0040", "B0041", "B0042"],
                "action": (
                    "Bind and replay the existing -I fixture and test receipt, and replace "
                    "the three blocks only to state implementation independence relative "
                    "to the explicitly shared low-level kernel."
                ),
                "criteria": (
                    "The bound fixture reaches first projective scalar return -I, its test "
                    "passes, and B0040/B0041/B0042 consistently disclose the shared kernel "
                    "without weakening the separate high-level order strategies."
                ),
                "support": [
                    "notes/stage4_scalar_sign_fixture.md",
                    "experiments/stage4_scalar_sign_fixture_receipt.json",
                    "code/test_stage4_scalar_sign_fixture.py",
                ],
            }
        },
    },
    "28-bolza-magnetic-flow": {
        "prefix": "P28",
        "residuals": {
            "REV-02": {
                "description": (
                    "B0048 describes direct canonicalization and closure tests, but the "
                    "actual localized test record and replay artifact were not bound into "
                    "re-review, so the must-fix item remains unverifiable there."
                ),
                "targets": ["B0048"],
                "action": (
                    "Replay and bind the existing direct-invariant test, localization note, "
                    "and receipt without refreshing canonical results; replace B0048 only "
                    "if an exact pointer or scope correction is needed."
                ),
                "criteria": (
                    "The Stage-4-prime bundle binds the direct same-builder test, replay "
                    "record, localization note, and receipt; B0048 matches the tested "
                    "invariants exactly and claims no unexecuted magnetic-flow result."
                ),
                "support": [
                    "notes/stage4_round8_invariant_localization.md",
                    "experiments/stage4_round8_invariant_receipt.json",
                    "code/test_stage4_round8_invariants.py",
                ],
            }
        },
    },
}


P26_BIB_ENTRIES = {
    "Katok1985": {
        "author": "Katok, Svetlana",
        "title": "Closed Geodesics, Periods and Arithmetic of Modular Forms",
        "journal": "Inventiones Mathematicae",
        "year": "1985",
        "volume": "80",
        "number": "3",
        "pages": "469--480",
        "doi": "10.1007/BF01388727",
    },
    "ConstantinescuNordentoft2025": {
        "author": "Constantinescu, Petru and Nordentoft, Asbjorn Christian",
        "title": "Non-vanishing of Geodesic Periods of Automorphic Forms",
        "journal": "Geometric and Functional Analysis",
        "year": "2025",
        "volume": "35",
        "pages": "1108--1146",
        "doi": "10.1007/s00039-025-00715-z",
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def target_rows(block_ids: list[str]) -> list[dict[str, Any]]:
    return [
        {"block_id": block_id, "allowed_operations": ["replace_block"]}
        for block_id in block_ids
    ]


def rebase_claim_surfaces(
    paper_root: Path, roadmap_path: Path, draft: Path
) -> tuple[Path, int]:
    old_path = paper_root / "notes/stage4_claim_surface_manifest.json"
    old = load(old_path)
    raw = draft.read_bytes()
    surfaces = copy.deepcopy(old["surfaces"])
    for surface in surfaces:
        needle = surface["original_text"].encode("utf-8")
        count = raw.count(needle)
        if count != 1:
            raise RuntimeError(
                f"{paper_root.name}:{surface['surface_id']} expected exact-once, got {count}"
            )
        start = raw.index(needle)
        surface["utf8_start"] = start
        surface["utf8_end"] = start + len(needle)
    current = {
        "schema_version": "claim-surface-manifest/1.0",
        "revision_round": 2,
        "roadmap_sha256": sha(roadmap_path),
        "base_draft_sha256": sha(draft),
        "claim_intent_sources": copy.deepcopy(old.get("claim_intent_sources", [])),
        "surfaces": surfaces,
    }
    output = paper_root / "notes/stage4_prime_claim_surface_manifest.json"
    dump(output, current)
    return output, len(surfaces)


def build_paper(paper: str, config: dict[str, Any]) -> dict[str, Any]:
    paper_root = ROOT / "papers" / paper
    notes = paper_root / "notes"
    draft = notes / "stage4_revision_round1.tex"
    block_manifest = notes / "stage4_revision_round1.tex.block-manifest.json"
    source_roadmap = load(notes / "stage3_revision_roadmap.json")
    trace = load(notes / "stage3_prime_round2_traceability.json")
    trace_rows = {row["item_id"]: row for row in trace["rows"]}
    source_items = {item["id"]: item for item in source_roadmap["items"]}

    items: list[dict[str, Any]] = []
    for item_id, residual in config["residuals"].items():
        trace_row = trace_rows[item_id]
        if trace_row["final_verdict"] not in {"PARTIALLY_ADDRESSED", "CANNOT_VERIFY"}:
            raise RuntimeError(f"{paper}:{item_id} is not an open residual")
        item = copy.deepcopy(source_items[item_id])
        item["description"] = residual["description"]
        item["suggested_action"] = residual["action"]
        item["verification_criteria"] = residual["criteria"]
        item["proposed_targets"] = target_rows(residual["targets"])
        item["evidence_anchor"] = {
            "anchor_type": "absence",
            "locator": f"notes/stage3_prime_round2_verification_report.md, {item_id}",
            "absence_scope": trace_row.get("quality_assessment", residual["description"]),
            "check_performed": (
                "Checked the hash-bound Stage-3-prime Round-2 input manifest, verdict, "
                "traceability row, current revised draft, and the listed existing support artifacts."
            ),
        }
        item["confidence"] = 5
        item["competence_basis"] = (
            "Stage-3-prime residual verification rebound to the exact current working draft "
            "and its content-neutral block manifest"
        )
        items.append(item)

    counts = {"must_fix": 0, "should_fix": 0, "consider": 0}
    for item in items:
        counts[item["obligation_class"]] += 1
    roadmap = {
        "schema_version": "revision-roadmap/1.0",
        "revision_round": 2,
        "base_draft_sha256": sha(draft),
        "block_manifest_sha256": sha(block_manifest),
        "items": items,
        "total_items": len(items),
        "obligation_counts": counts,
        "editorial_decision": "Major Revision",
        "consensus_summary": (
            "This final revision roadmap contains only the unresolved Stage-3-prime "
            "Round-2 residuals. It is non-ranking, creates no write authority, and "
            "preserves every registered claim and Route boundary pending a new author sidecar."
        ),
        "dissenting_opinions": [],
    }
    roadmap_path = notes / "stage4_prime_revision_roadmap.json"
    dump(roadmap_path, roadmap)
    claim_path, surface_count = rebase_claim_surfaces(paper_root, roadmap_path, draft)

    return {
        "paper": config["prefix"],
        "paper_dir": f"papers/{paper}",
        "base_draft": "notes/stage4_revision_round1.tex",
        "base_draft_sha256": sha(draft),
        "block_manifest": "notes/stage4_revision_round1.tex.block-manifest.json",
        "block_manifest_sha256": sha(block_manifest),
        "roadmap": "notes/stage4_prime_revision_roadmap.json",
        "roadmap_sha256": sha(roadmap_path),
        "claim_surface_manifest": "notes/stage4_prime_claim_surface_manifest.json",
        "claim_surface_manifest_sha256": sha(claim_path),
        "registered_surfaces_rebound": surface_count,
        "residuals": [
            {
                "item_id": item_id,
                "obligation_class": source_items[item_id]["obligation_class"],
                "round2_verdict": trace_rows[item_id]["final_verdict"],
                "proposed_targets": target_rows(residual["targets"]),
                "support_scope": residual["support"],
                "claim_strength_replacement": None,
            }
            for item_id, residual in config["residuals"].items()
        ],
    }


def render_request(summary: dict[str, Any]) -> str:
    lines = [
        "# Round 9 Stage 4-prime exact authorization request",
        "",
        f"Prepared: **{DATE} UTC**  ",
        "Status: **AUTHOR DECISION REQUIRED — NO PATCH AUTHORIZED**",
        "",
        "The generic instruction `确认，继续下一轮` authorized preparation of the next legal stage, but it does not supply per-item author triage or exact write scope. This request freezes the six remaining residual items against the four current working drafts. Prior-round choices are not carried forward.",
        "",
        "## Frozen batch boundary",
        "",
        "- Stage 4-prime is the final revision opportunity for these four Major-Revision papers.",
        "- The request contains **6 residual items**: 5 `must_fix` and 1 `should_fix`.",
        "- All **51 registered ClaimIntent surfaces** in these four papers are rebound byte-exactly to the current drafts; no claim-strength replacement is proposed. (P25's separate six surfaces remain unchanged on its Stage-4.5 branch.)",
        "- Canonical manuscripts, PDFs, and scientific results remain frozen.",
        "- Route-A tuples and initial dynamical-system restrictions remain unchanged; Route B remains uninvoked.",
        "- Support replay may read existing artifacts and create manifests/receipts, but may not refresh canonical results or alter a scientific value.",
        "",
    ]
    for paper in summary["papers"]:
        lines.extend(
            [
                f"## {paper['paper']}",
                "",
                f"- base draft: `{paper['paper_dir']}/{paper['base_draft']}` — `{paper['base_draft_sha256']}`",
                f"- block manifest: `{paper['block_manifest_sha256']}`",
                f"- residual roadmap: `{paper['roadmap_sha256']}`",
                f"- Round-2 claim-surface manifest: `{paper['claim_surface_manifest_sha256']}` ({paper['registered_surfaces_rebound']} surfaces)",
                "",
            ]
        )
        for residual in paper["residuals"]:
            targets = ", ".join(
                f"{target['block_id']}/replace_block"
                for target in residual["proposed_targets"]
            )
            lines.extend(
                [
                    f"### {residual['item_id']} — {residual['round2_verdict']} / {residual['obligation_class']}",
                    "",
                    f"- proposed manuscript scope: `{targets}`",
                    "- support scope:",
                ]
            )
            lines.extend(f"  - `{entry}`" for entry in residual["support_scope"])
            lines.extend(
                [
                    "- claim-strength replacement: **none**",
                    "",
                ]
            )

    lines.extend(
        [
            "## Exact P26 bibliography additions within REV-02",
            "",
            "If P26 `REV-02` is `will_address`, authorize append-only addition of exactly these verified entries to `paper/references.bib`; no other bibliography edit is included:",
            "",
            "```json",
            json.dumps(P26_BIB_ENTRIES, ensure_ascii=False, indent=2),
            "```",
            "",
            "## Required author response",
            "",
            "For every one of the six items, choose `will_address`, `wont_address`, or `not_on_point`. For each `will_address` item, explicitly authorize a subset of the listed block/operation pairs and its listed support scope. A blanket confirmation does not create write authority.",
            "",
            "A compact all-approved response may identify this request by SHA-256 and state that all six items are `will_address`, all listed block/operation pairs and support scopes are authorized, P26's two exact append-only bibliography entries are authorized, no claim-strength replacement is authorized, and all freeze/Route boundaries remain in force.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    papers = [build_paper(paper, config) for paper, config in CONFIG.items()]
    summary = {
        "schema_version": "round9-stage4-prime-scope-manifest/1.0",
        "prepared_at": f"{DATE}T00:00:00Z",
        "status": "author_decision_required_no_patch_authorized",
        "residual_item_count": sum(len(paper["residuals"]) for paper in papers),
        "registered_surface_count": sum(
            paper["registered_surfaces_rebound"] for paper in papers
        ),
        "p26_exact_bibliography_additions": P26_BIB_ENTRIES,
        "papers": papers,
        "global_boundaries": {
            "canonical_manuscript_pdf_results_frozen": True,
            "claim_strength_replacements": [],
            "route_a_tuple_change_authorized": False,
            "route_b_invocation_authorized": False,
            "canonical_results_refresh_authorized": False,
            "author_adjudication_created": False,
            "revision_patch_created": False,
        },
    }
    manifest_path = ROOT / "BATCH_ROUND9_STAGE4_PRIME_SCOPE_MANIFEST.json"
    dump(manifest_path, summary)
    request_path = ROOT / "BATCH_ROUND9_STAGE4_PRIME_AUTHORIZATION_REQUEST.md"
    request_path.write_text(render_request(summary), encoding="utf-8")
    print(
        json.dumps(
            {
                "manifest": str(manifest_path.relative_to(ROOT)),
                "manifest_sha256": sha(manifest_path),
                "request": str(request_path.relative_to(ROOT)),
                "request_sha256": sha(request_path),
                "papers": len(papers),
                "residual_items": summary["residual_item_count"],
                "registered_surfaces": summary["registered_surface_count"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
