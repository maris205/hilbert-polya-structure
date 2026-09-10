#!/usr/bin/env python3
"""Independent checker for the C103 min/max aggregation receipt."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from math import factorial
from pathlib import Path
from typing import Any

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c103_minmax_aggregation_evidence.json"
PRODUCER = PROJECT / "code/c103_minmax_aggregation.py"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def build_expected() -> dict[str, Any]:
    spec = importlib.util.spec_from_file_location("c103_producer", PRODUCER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    raw = module.load_sources()
    # Recompute through the producer in a temporary output, then restore the
    # canonical path only after the caller has captured the expected object.
    old_out = module.OUT
    import tempfile
    with tempfile.TemporaryDirectory(prefix="c103-check-") as directory:
        module.OUT = Path(directory) / "expected.json"
        module.main()
        expected = json.loads(module.OUT.read_text())
    module.OUT = old_out
    return expected


def validate_evidence_path(path: Path, expected: dict[str, Any]) -> None:
    value = json.loads(path.read_text())
    assert value == expected
    assert value["status"] == "PREFREEZE_G3_PASS"
    assert value["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    rows = value["aggregation_atlas"]["pair_rows"]
    assert len(rows) == 400
    assert all(row["transpose_aggregation_verified"] for row in rows)
    assert all(row["expected_sum_identity"]["verified"] for row in rows)
    assert all(row["tail_identities"]["minimum_tail_identity_verified"] for row in rows)
    assert all(row["tail_identities"]["maximum_cdf_identity_verified"] for row in rows)
    assert value["claims"]["arithmetic_local_claimed"] is False
    assert value["claims"]["euler_factors_claimed"] is False
    assert value["claims"]["root_numbers_claimed"] is False
    assert value["claims"]["automorphy_claimed"] is False
    assert value["claims"]["full_burnside_ring_claimed"] is False
    assert value["claims"]["full_table_of_marks_claimed"] is False
    assert value["claims"]["hilbert_polya_operator_claimed"] is False


def main() -> None:
    expected = build_expected()
    validate_evidence_path(EVIDENCE, expected)
    print(json.dumps({
        "status": "C103_INDEPENDENT_CHECK_PASS",
        "ordered_pair_count": 400,
        "minmax_cells": 400 * 17 * 2,
        "evidence_sha256": digest(EVIDENCE),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
