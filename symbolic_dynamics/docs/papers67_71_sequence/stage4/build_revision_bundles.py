#!/usr/bin/env python3
"""Build continuous Stage-4 revision-evidence bundles for P67--P71."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PAPERS = (
    "67-multiplicative-plaquette-matroid-complexity",
    "68-complete-bipartite-homshift-conjugacies",
    "69-orientation-sensitive-surface-flat-sft",
    "70-weighted-heisenberg-congruence-nullities",
    "71-zip-shift-degree-pressure",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact(paper: Path, path: Path) -> dict[str, str]:
    return {
        "path": path.relative_to(paper).as_posix(),
        "sha256": sha256(path),
    }


def main() -> None:
    for slug in PAPERS:
        paper = ROOT / "papers" / slug
        stage3 = paper / "stage3"
        stage4 = paper / "stage4"
        base = stage3 / "ANCHORED_REVIEW_DRAFT.md"
        manifest = stage3 / "BLOCK_MANIFEST.json"
        revised = stage4 / "REVISED_DRAFT.md"
        paths = {
            "receipt": stage4 / "INTEGRITY_PASS_RECEIPT.json",
            "roadmap": stage3 / "REVISION_ROADMAP.json",
            "claims": stage4 / "CLAIM_SURFACE_MANIFEST.json",
            "author": stage4 / "AUTHOR_ADJUDICATION.json",
            "patch": stage4 / "REVISION_PATCH.json",
            "report": stage4 / "REVISED_DRAFT.md.apply-report.json",
        }
        missing = [str(path) for path in (base, manifest, revised, *paths.values()) if not path.is_file()]
        if missing:
            raise SystemExit(f"{slug}: missing required artifact(s): {missing}")

        bundle = {
            "schema_version": "revision-evidence-bundle/1.0",
            "chain_start": {
                "first_revision_round": 1,
                "draft": artifact(paper, base),
                "block_manifest": artifact(paper, manifest),
                "integrity_pass_receipt": artifact(paper, paths["receipt"]),
            },
            "rounds": [
                {
                    "kind": "review_roadmap",
                    "revision_round": 1,
                    "pre_round_draft": artifact(paper, base),
                    "pre_round_block_manifest": artifact(paper, manifest),
                    "revision_roadmap": artifact(paper, paths["roadmap"]),
                    "claim_surface_manifest": artifact(paper, paths["claims"]),
                    "author_adjudication": artifact(paper, paths["author"]),
                    "revision_patch": artifact(paper, paths["patch"]),
                    "apply_report": artifact(paper, paths["report"]),
                    "post_round_draft": artifact(paper, revised),
                }
            ],
            "final_draft": artifact(paper, revised),
        }
        out = stage4 / "REVISION_EVIDENCE_BUNDLE.json"
        out.write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
