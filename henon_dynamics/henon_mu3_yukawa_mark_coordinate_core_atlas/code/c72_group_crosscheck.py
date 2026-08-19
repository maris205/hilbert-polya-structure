#!/usr/bin/env python3
"""GAP cross-check for the abstract core lattice and named-support atlas."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import subprocess

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c72_coordinate_core_atlas_evidence.json"


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    rows = evidence["subgroup_lattice_atlas"]["type_rows"]
    # GAP's structure descriptions are normalized below to the evidence labels.
    script = r'''
G:=AbelianGroup([9,3,2]);;
Print(Size(G),"\n");
for H in AllSubgroups(G) do Print(Size(H),":",StructureDescription(H),"\n"); od;
QUIT;
'''
    run = subprocess.run(["gap", "-q"], input=script, capture_output=True,
                         text=True, check=True)
    lines = [line.strip() for line in run.stdout.splitlines() if line.strip()]
    assert int(lines[0]) == 54
    normalized = {
        "1": "1",
        "C2": "Z/2",
        "C3": "Z/3",
        "C6": "Z/6",
        "C3 x C3": "(Z/3)^2",
        "C9": "Z/9",
        "C18": "Z/18",
        "C3 x C6": "Z/3 + Z/6",
        "C6 x C3": "Z/3 + Z/6",
        "C3 x C9": "Z/3 + Z/9",
        "C9 x C3": "Z/3 + Z/9",
        "C3 x C18": "Z/3 + Z/18",
        "C18 x C3": "Z/3 + Z/18",
    }
    counts = Counter()
    for line in lines[1:]:
        size, description = line.split(":", 1)
        assert description in normalized, description
        counts[normalized[description]] += 1
    expected = {row["type"]: row["subgroup_count_in_core"] for row in rows}
    assert counts == expected
    assert sum(counts.values()) == 20
    assert evidence["coordinate_realization"]["coordinates"] == [
        [1, 0, 0], [6, 0, 0], [0, 1, 0], [3, 1, 0],
        [0, 0, 0], [0, 0, 0], [4, 2, 0], [3, 2, 0],
        [0, 0, 1], [0, 0, 0], [0, 1, 0], [3, 1, 0],
        [0, 0, 0], [0, 0, 0], [2, 1, 0], [8, 2, 0],
    ]
    assert evidence["generation_complex"]["minimal_generating_support_count"] == 25
    print(json.dumps({
        "status": "GROUP_CROSSCHECK_PASS",
        "gap_core_order": 54,
        "gap_subgroup_count": sum(counts.values()),
        "gap_type_counts": dict(sorted(counts.items())),
        "named_coordinate_count": 16,
        "minimal_generating_support_count": 25,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
