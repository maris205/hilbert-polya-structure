#!/usr/bin/env python3
"""Freeze Round-10 Stage-2 pre-prose artifacts before canonical drafting."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "2026-09-02T13:29:43Z"
PAPERS = {
    "P29": "29-bianchi-ideal-owner-refinement",
    "P30": "30-three-disk-nonconstant-roof-determinant",
    "P31": "31-level11-conjugacy-owner-ledger",
    "P32": "32-homology-cover-renormalization-uniformity",
    "P33": "33-bolza-control-matched-census",
}
NAMES = (
    "stage2_claim_intent_manifest.json",
    "stage2_claim_lineage.json",
    "stage2_paper_configuration.md",
    "stage2_paper_outline.md",
    "stage2_argument_blueprint.md",
    "stage2_writer_precommitment.md",
    "stage2_evaluator_precommitment.md",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    input_freeze = json.loads((ROOT / "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json").read_text())
    files: list[dict[str, str]] = []
    paper_rows: list[dict[str, object]] = []
    for code, slug in PAPERS.items():
        note_dir = ROOT / "papers" / slug / "notes"
        rows = []
        for name in NAMES:
            path = note_dir / name
            relative = path.relative_to(ROOT).as_posix()
            row = {"path": relative, "sha256": sha(path)}
            files.append(row)
            rows.append(row)
        manifest = json.loads((note_dir / "stage2_claim_intent_manifest.json").read_text())
        lineage = json.loads((note_dir / "stage2_claim_lineage.json").read_text())
        paper_rows.append(
            {
                "paper": code,
                "slug": slug,
                "claim_intents": len(manifest["claims"]),
                "lineage_mappings": len(lineage["mappings"]),
                "strength_relation": "same_or_narrower",
                "artifacts": rows,
            }
        )
    digest_lines = "".join(f"{row['sha256']}  {row['path']}\n" for row in files)
    payload = {
        "schema": "round10-stage2-preprose-freeze/1.0",
        "frozen_at": STAMP,
        "pipeline_stage": "2-write-preprose-freeze",
        "authorization_sha256": sha(ROOT / "BATCH_ROUND10_STAGE2_AUTHORIZATION_20260902.txt"),
        "writing_contract_sha256": sha(ROOT / "BATCH_ROUND10_STAGE2_WRITING_CONTRACT.md"),
        "input_freeze_sha256": sha(ROOT / "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json"),
        "stage1_handoff_sha256": input_freeze["stage1_batch"]["handoff_sha256"],
        "papers": paper_rows,
        "aggregate": {
            "papers": len(paper_rows),
            "claim_intents": sum(row["claim_intents"] for row in paper_rows),
            "lineage_mappings": sum(row["lineage_mappings"] for row in paper_rows),
            "preprose_artifacts": len(files),
            "preprose_tree_sha256": hashlib.sha256(digest_lines.encode()).hexdigest(),
        },
        "mutation_policy": {
            "frozen_here": "All listed pre-prose files are immutable for this Stage-2 composition run.",
            "allowed_next": [
                "paper/manuscript.tex",
                "paper/references.bib",
                "paper/paper.pdf",
                "paper/README.md",
                "paper/stage2_manuscript_audit.md",
                "notes/stage2_* review, build, and state artifacts",
                "paper and repository README/state summaries",
                "Round-10 Stage-2 batch receipts, audits, and handoff",
                "Round-10 Stage-2 build and audit tools",
            ],
            "forbidden": [
                "new literature retrieval",
                "code, experiments, or canonical scientific results",
                "Route-A tuple assignment or Route-B invocation",
                "Stage-2.5 integrity execution",
            ],
        },
    }
    target = ROOT / "BATCH_ROUND10_STAGE2_PREPROSE_FREEZE.json"
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {target.relative_to(ROOT)}")
    print(f"papers={len(paper_rows)} claims={payload['aggregate']['claim_intents']} artifacts={len(files)}")


if __name__ == "__main__":
    main()
