#!/usr/bin/env python3
"""Structural checker for the C62 complete-atlas prefreeze evidence."""

from __future__ import annotations

import json
from pathlib import Path

EVIDENCE = Path(__file__).resolve().parents[1] / "results/c62_atlas_evidence.json"


def main():
    doc = json.loads(EVIDENCE.read_text())
    assert doc["schema_id"] == "hcs-c62-complete-atlas-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G2_PASS"
    assert doc["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert doc["authority"]["ambient_order"] == 51840
    assert doc["authority"]["hplus_order"] == doc["authority"]["hminus_order"] == 162
    expected = {"exterior_square": (10, 51040), "symmetric_square": (11, 51360)}
    summary = {}
    for kind, (count, total) in expected.items():
        table = doc["atlases"][kind]
        assert (table["orbit_count"], table["total_size"]) == (count, total)
        assert len(table["rows"]) == count
        for row in table["rows"]:
            assert row["plus"]["orbit_size"] == row["minus"]["orbit_size"] == row["orbit_size"]
            for side in ("plus", "minus"):
                item = row[side]
                assert item["field_degree"] == item["orbit_size"]
                assert item["stabilizer_order"] * item["field_degree"] == 51840
                assert item["core_order"] > 0 and item["core_order"] <= item["stabilizer_order"]
                assert item["normalizer_order"] % item["stabilizer_order"] == 0
                assert item["automorphism_order"] == item["normalizer_order"] // item["stabilizer_order"]
        summary[kind] = {
            "orbit_count": count,
            "total_size": total,
            "nonconjugate_rows": sum(not row["stabilizers_conjugate"] for row in table["rows"]),
        }
    print(json.dumps({"status": "PASS", "summary": summary}, sort_keys=True))


if __name__ == "__main__":
    main()

