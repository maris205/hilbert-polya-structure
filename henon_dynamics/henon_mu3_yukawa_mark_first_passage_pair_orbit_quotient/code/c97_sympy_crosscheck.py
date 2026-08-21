#!/usr/bin/env python3
"""SymPy orbit--stabilizer, Burnside, and transpose checks for C97."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]


def main() -> None:
    data = json.loads((PROJECT / "results/c97_pair_orbit_quotient_evidence.json").read_text())
    atlas = data["pair_orbit_atlas"]
    rows = atlas["rows"]
    assert len(rows) == sp.Integer(atlas["pair_orbit_count"]) == 272
    assert sum(sp.Integer(row["orbit_size"]) for row in rows) == 400
    for row in rows:
        assert sp.Integer(row["orbit_size"]) * sp.Integer(row["stabilizer_order_in_effective_label_group"]) == 1920
        transpose = rows[row["transpose_orbit_index"]]
        assert transpose["transpose_orbit_index"] == row["pair_orbit_index"]
        covariance = row["representative_covariance"]
        sp.Rational(covariance["numerator"], covariance["denominator"])
        assert len(row["joint_law_sha256"]) == 64
    burnside = sp.Rational(atlas["burnside_fixed_ordered_pair_sum"], 1920)
    assert burnside == len(rows)
    assert sum(atlas["orbit_size_spectrum"].values()) == len(rows)
    assert sum(atlas["relation_type_spectrum"].values()) == len(rows)
    print(json.dumps({"status": "C97_SYMPY_CROSSCHECK_PASS", "pair_orbit_count": len(rows), "burnside_quotient": int(burnside)}, sort_keys=True))


if __name__ == "__main__":
    main()
