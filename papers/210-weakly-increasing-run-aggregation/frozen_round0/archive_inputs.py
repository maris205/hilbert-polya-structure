#!/usr/bin/env python3
"""Physically copy the explicitly used small source/proof contexts, preserving exact bytes."""
import hashlib
import json
from pathlib import Path

PAPER = Path(__file__).resolve().parent
ROOT = PAPER.parent.parent
GATE = ROOT / "docs/papers204_208_sequence/scouting/MNA_GATE"
READS = ROOT / "docs/papers204_208_sequence/qa/mna_root_source_read"
TARGET = PAPER / "sources/archive"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    TARGET.mkdir(exist_ok=False)
    selected = {
        "MNA_PROOF.md": GATE / "inputs/author_lane40/MNA_PROOF.md",
        "MNA_IMAGE_ENUMERATION_ADDENDUM.md": GATE / "inputs/author_lane40/MNA_IMAGE_ENUMERATION_ADDENDUM.md",
        "CANDIDATE_GATE.md": GATE / "CANDIDATE_GATE.md",
        "CANDIDATE_SOURCE_AND_PROOF.md": GATE / "SOURCE_AND_PROOF.md",
        "CANDIDATE_FINDINGS.json": GATE / "FINDINGS.json",
        "ROOT_SOURCE_INSPECTION.md": READS / "SOURCE_INSPECTION.md",
        "P210_ROOT_ADMISSION.md": ROOT / "docs/papers204_208_sequence/P210_ROOT_ADMISSION.md",
        "robbins_archived_primary.json": GATE / "inputs/author_lane40/sources/09_robbins_polygonal_primary.json",
        "P147_main.tex": GATE / "inputs/originals/papers/147-adjacent-run-consolidation/main.tex",
        "P121_main.tex": GATE / "inputs/originals/papers/121-random-product-plus-one-coalescence/main.tex",
        "CRG_SCOUT.md": GATE / "inputs/originals/docs/papers162_166_sequence/scouting/replacement_crossclass/SCOUT.md",
        "FPT_LEDGER.md": GATE / "inputs/originals/docs/papers182_186_sequence/scouting/combinatorial_lane/SCOUT_AND_KILL_LEDGER.md",
        "PDCF_CANDIDATES.md": GATE / "inputs/originals/docs/papers187_191_sequence/scouting/combinatorial_lane/CANDIDATES.md",
    }
    for i in range(1, 7):
        selected[f"root_web{i:02}.actual.json"] = READS / f"web{i:02}.actual.json"
    before = {name: {"original": str(path), "sha256": digest(path), "bytes": path.stat().st_size}
              for name, path in selected.items()}
    for name, source in selected.items():
        (TARGET / name).write_bytes(source.read_bytes())
    for name, source in selected.items():
        assert digest(source) == before[name]["sha256"] == digest(TARGET / name)
    result = {"status": "PASS_EXACT_ARCHIVAL_COPIES", "count": len(selected),
              "source_script_sha256": digest(Path(__file__)),
              "records": [{**before[name], "copy": str((TARGET / name).relative_to(PAPER))}
                          for name in sorted(selected)],
              "limit": "Only contexts stated in SOURCE_AUDIT were actually read; copying complete containers does not imply complete body reading."}
    (PAPER / "sources/ARCHIVE_INPUTS.actual.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "count": len(selected),
                      "receipt_sha256": digest(PAPER / "sources/ARCHIVE_INPUTS.actual.json")}, sort_keys=True))


if __name__ == "__main__":
    main()
