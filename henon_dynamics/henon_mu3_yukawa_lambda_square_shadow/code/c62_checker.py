#!/usr/bin/env python3
"""Independent structural checker for the prefreeze C62 lambda evidence."""

from __future__ import annotations

import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c62_lambda_evidence.json"


def check() -> dict[str, object]:
    doc = json.loads(EVIDENCE.read_text())
    assert doc["schema_id"] == "hcs-c62-lambda-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_CODE_RESULTS_PASS"
    assert doc["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert doc["authority"] == {
        "ambient_order": 51840,
        "c61_group_evidence_sha256": doc["authority"]["c61_group_evidence_sha256"],
        "coset_degree": 320,
        "hminus_order": 162,
        "hplus_order": 162,
    }
    assert doc["sizes"] == {"exterior_square": 51040, "symmetric_square": 51360}
    assert doc["character_identities"] ["exterior_square_equal"] is True
    assert doc["character_identities"] ["symmetric_square_equal"] is True
    for key, expected, lower in (("exterior_square", 51040, 1), ("symmetric_square", 51360, 1)):
        plus = doc[key]["plus"]
        minus = doc[key]["minus"]
        assert len(plus) == len(minus)
        assert sum(row["orbit_size"] for row in plus) == expected
        assert sum(row["orbit_size"] for row in minus) == expected
        assert all(row["stabilizer_order"] > 0 for row in plus + minus)
    matches = doc["exterior_square"]["stabilizer_matches"]
    assert len(matches) == 10
    assert sum(not row["conjugate"] for row in matches) >= 1
    return {
        "status": "PASS",
        "exterior_orbits": len(doc["exterior_square"]["plus"]),
        "symmetric_orbits": len(doc["symmetric_square"]["plus"]),
        "exterior_nonconjugate_matches": sum(not row["conjugate"] for row in matches),
    }


if __name__ == "__main__":
    print(json.dumps(check(), sort_keys=True))

