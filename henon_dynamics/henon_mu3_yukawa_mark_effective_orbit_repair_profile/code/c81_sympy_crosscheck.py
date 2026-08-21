#!/usr/bin/env python3
"""Algebraic cross-checks for the C81 orbit quotient."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c81_effective_orbit_repair_profile_evidence.json"


def main():
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["schema_id"] == "hcs-c81-effective-1920-repair-profile-orbit-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    quotient = evidence["orbit_quotient"]
    rows = quotient["rows"]
    x = sp.symbols("x")
    weighted = sp.expand(sum(row["orbit_size"] * x ** row["support_size"] for row in rows))
    assert weighted == sp.expand((1 + x) ** 16)
    assert sum(row["orbit_size"] for row in rows) == 65536
    # Burnside's integer identity from the independently stored fixed-cycle
    # spectrum; this is an orbit count check, not a full Burnside-ring claim.
    fixed = {int(k): int(v) for k, v in quotient["fixed_support_count_spectrum"].items()}
    assert sum(k * v for k, v in fixed.items()) == 1920 * quotient["orbit_count"]
    assert quotient["orbit_count"] == 3024
    # Profile classes partition the quotient and retain the C79 joint marginal.
    classes = quotient["profile_classes"]
    assert len(classes) == quotient["profile_class_count"] == 14
    assert sum(row["orbit_count"] for row in classes) == 3024
    assert sum(row["mask_count"] for row in classes) == 65536
    class_mask_marginal = Counter()
    for row in classes:
        p = row["profile"]
        class_mask_marginal[(p["rho"], p["witness_multiplicity"])] += row["mask_count"]
    expected = {tuple(map(int, key.split(","))): value
                for key, value in evidence["repair_profile_marginals"]["mask_count_by_rho_witness"].items()}
    assert dict(class_mask_marginal) == expected
    print(json.dumps({"status": "C81_SYMPY_CROSSCHECK_PASS",
                      "weighted_polynomial": "(1+x)^16", "orbit_count": 3024,
                      "profile_classes": 14, "burnside_identity": True}, sort_keys=True))


if __name__ == "__main__":
    main()
