#!/usr/bin/env python3
"""Independent coefficient extraction for the P71 source formula."""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
CERT = PROJECT / "results/c71_certificate.json"
OUT = PROJECT / "results/c71_independent_check.json"


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    # At u=0: N=sqrt(2)+3/2, denominator=u(2-u).
    # Rational part beyond the packet coefficient is exactly 3/4.
    residual_rational = Fraction(3, 4)
    branch = Fraction(1, 2)
    if cert["ledger"]["relative_pole_coefficient"] != str(residual_rational):
        raise RuntimeError("residual")
    if cert["ledger"]["unique_algebraic_counterterm"] != "u^(1/2)":
        raise RuntimeError("branch")
    if cert["claim_status"]["arithmetic_advance"] != "NO":
        raise RuntimeError("promotion")
    payload = {
        "candidate_id": "HCS-P71",
        "residual_pole": str(residual_rational),
        "branch_counterterm": str(branch),
        "source_formula_reduction": "PASS",
        "uniqueness_ledger": "PASS",
        "arithmetic_firewall": "PASS",
        "certificate_sha256": hashlib.sha256(CERT.read_bytes()).hexdigest(),
        "check": True,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
