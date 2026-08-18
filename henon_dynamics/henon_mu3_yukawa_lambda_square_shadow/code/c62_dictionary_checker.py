#!/usr/bin/env python3
"""Checker for the C62 fixed-field type dictionary."""

from __future__ import annotations

import json
from pathlib import Path

EVIDENCE = Path(__file__).resolve().parents[1] / "results/c62_dictionary_evidence.json"


def main():
    doc = json.loads(EVIDENCE.read_text())
    assert doc["schema_id"] == "hcs-c62-fixed-field-dictionary-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G4_PASS"
    assert doc["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert doc["authority"]["ambient_order"] == 51840
    types = {item["type_id"]: item for item in doc["types"]}
    assert len(types) == doc["type_count"] == 16

    for item in types.values():
        assert item["core_order"] == 1
        assert item["field_degree"] * item["order"] == 51840
        assert item["normalizer_order"] % item["order"] == 0
        assert len(item["representative_sha256"]) == 64

    summary = {}
    for kind, sides in doc["rows"].items():
        plus_types = {row["field_type"] for row in sides["plus"]}
        minus_types = {row["field_type"] for row in sides["minus"]}
        assert plus_types != minus_types
        for side in ("plus", "minus"):
            for row in sides[side]:
                assert row["field_type"] in types
                t = types[row["field_type"]]
                assert row["core_order"] == 1
                assert row["field_degree"] == row["orbit_size"]
                assert row["field_degree"] == 51840 // row["stabilizer_order"]
                assert row["stabilizer_order"] == t["order"]
                assert row["normalizer_order"] == t["normalizer_order"]
                assert len(row["stabilizer_sha256"]) == 64
        summary[kind] = {
            "plus_type_count": len(plus_types),
            "minus_type_count": len(minus_types),
            "plus_minus_differ": True,
        }

    order_to_types = {}
    for item in types.values():
        order_to_types.setdefault(item["order"], set()).add(item["type_id"])
    assert any(len(ids) > 1 for ids in order_to_types.values())

    print(json.dumps({"status": "PASS", "type_count": len(types), "summary": summary}, sort_keys=True))


if __name__ == "__main__":
    main()
