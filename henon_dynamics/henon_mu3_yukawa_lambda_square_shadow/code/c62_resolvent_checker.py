#!/usr/bin/env python3
"""Structural checker for C62 G3 product-form marker evidence."""

from __future__ import annotations

import json
from pathlib import Path

EVIDENCE = Path(__file__).resolve().parents[1] / "results/c62_resolvent_evidence.json"


def main():
    doc = json.loads(EVIDENCE.read_text())
    assert doc["schema_id"] == "hcs-c62-product-form-resolvent-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G3_PASS"
    assert doc["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert doc["authority"]["ambient_order"] == 51840
    assert doc["marker_contract"] == {
        "base": 512,
        "encoding": "512*(zero_based_pair_first+1)+(zero_based_pair_second+1)",
        "expanded_characteristic_zero_coefficients_claimed": False,
        "prime": 692717,
    }
    expected = {"exterior_square": (10, 51040), "symmetric_square": (11, 51360)}
    summary = {}
    for kind, (count, total) in expected.items():
        for side in ("plus", "minus"):
            rows = doc["tables"][kind][side]
            assert len(rows) == count
            assert sum(row["orbit_size"] for row in rows) == total
            for row in rows:
                assert row["carrier"]["monic"] is True
                assert row["carrier"]["terms"] == row["orbit_size"]
                assert row["carrier"]["expanded_characteristic_zero_coefficients_claimed"] is False
                assert len(row["orbit_pairs"]) == row["orbit_size"]
                assert row["noncollision_count"] == row["orbit_size"]
                assert len(set(row["marker_values_mod_prime"])) == row["orbit_size"]
                assert max(row["marker_values_mod_prime"]) < 692717
        summary[kind] = {"rows": count, "total_size": total}
    print(json.dumps({"status": "PASS", "summary": summary}, sort_keys=True))


if __name__ == "__main__":
    main()

