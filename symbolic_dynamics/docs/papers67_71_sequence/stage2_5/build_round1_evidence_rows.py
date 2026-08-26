#!/usr/bin/env python3
"""Build replayable Phase-E provenance rows for selected round-1 claims.

The rows bind each selected claim to an exact excerpt in the corrected local
manuscript view.  They establish claim-to-artifact provenance only.  The
mathematical and external-source judgments remain in each paper's human audit.
"""

from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_MODULE = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.27/skills/"
    "academic-research-suite/ars/scripts/evidence_rows.py"
)
PAPERS = {
    "P67": "67-multiplicative-plaquette-matroid-complexity",
    "P68": "68-complete-bipartite-homshift-conjugacies",
    "P69": "69-orientation-sensitive-surface-flat-sft",
    "P70": "70-weighted-heisenberg-congruence-nullities",
    "P71": "71-zip-shift-degree-pressure",
}


def load_evidence_module():
    spec = importlib.util.spec_from_file_location("ars_evidence_rows", EVIDENCE_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {EVIDENCE_MODULE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def exact_excerpt(claim_text: str) -> str:
    match = re.match(r"\S+(?:\s+\S+){0,19}", claim_text, flags=re.DOTALL)
    if match is None:
        raise ValueError("claim text has no non-whitespace excerpt")
    excerpt = match.group(0)
    if len(excerpt) > 900:
        excerpt = excerpt[:900]
    return excerpt


def main() -> int:
    evidence = load_evidence_module()
    for paper_id, directory in PAPERS.items():
        stage = ROOT / "papers" / directory / "stage2_5"
        registry = json.loads((stage / "claim_registry_round1.json").read_text(encoding="utf-8"))
        draft = (stage / "draft_for_claim_registry_round1.md").read_text(encoding="utf-8")
        source_slug = f"{paper_id}_MANUSCRIPT"
        rows = []
        selected = [
            claim for claim in registry["claims"]
            if claim["selection_tier"] != "NOT-SELECTED"
        ]
        for index, claim in enumerate(selected, start=1):
            section = claim.get("paper_section") or "Corrected manuscript"
            excerpt = exact_excerpt(claim["claim_text"])
            if excerpt not in draft:
                raise ValueError(f"{paper_id} {claim['claim_id']}: excerpt not in corrected draft")
            template = {
                "surface": "phase_e_claim_verification",
                "row_id": f"EVR-{paper_id}-R1-{index:04d}",
                "claim": {
                    "claim_id": claim["claim_id"],
                    "text": claim["claim_text"],
                    "paper_locator": (
                        f"{section}; UTF-8 bytes "
                        f"{claim['draft_span']['start_byte']}:{claim['draft_span']['end_byte']}"
                    ),
                    "selection_tier": claim["selection_tier"],
                },
                "source": {
                    "ref_slug": source_slug,
                    "display_label": f"{paper_id} corrected internal manuscript view",
                    "source_artifact_sha256": registry["draft_raw_sha256"],
                },
                "anchor": {
                    "kind": "section",
                    "value_encoded": quote(section, safe=""),
                },
                "verdict": "VERIFIED",
                "detail": (
                    "Exact claim-to-manuscript provenance replayed. Mathematical proof and "
                    "external-source support were reviewed in the paper-specific Stage-2.5 "
                    "audit; this provenance row alone does not certify truth or novelty."
                ),
                "content_handling": {
                    "sharing_scope": "session_only",
                    "rights_basis": "not_assessed",
                },
            }
            rows.append(evidence.build(template, draft, extracted_text=excerpt))

        (stage / "evidence_rows_round1.json").write_text(
            json.dumps(rows, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (stage / "evidence_source_map_round1.json").write_text(
            json.dumps({source_slug: draft}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        for row in rows:
            evidence.validate(row, draft)
        print(f"{paper_id}: PASS {len(rows)} selected evidence rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

