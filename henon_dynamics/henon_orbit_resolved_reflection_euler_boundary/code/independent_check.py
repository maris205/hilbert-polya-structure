#!/usr/bin/env python3
"""Independent specialization and boundary inequality audit for P70."""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
CERT = PROJECT / "results/c70_certificate.json"
OUT = PROJECT / "results/c70_independent_check.json"


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    for row in cert["boundary_samples"]:
        q = row["q"]
        expected = 1 / math.sqrt(1 + q * q)
        ratio = 1 / math.sqrt((q + 1 / q) / 2)
        if abs(row["orbit_radius"] - expected) > 1e-15:
            raise RuntimeError("radius")
        if abs(row["radius_ratio"] - ratio) > 1e-15:
            raise RuntimeError("ratio")
        if q != 1 and not row["orbit_radius"] < row["mean_field_radius"]:
            raise RuntimeError("strict shift")
    if cert["claim_status"]["arithmetic_advance"] != "NO":
        raise RuntimeError("promotion")
    payload = {
        "candidate_id": "HCS-P70",
        "five_boundary_points": "PASS",
        "unweighted_specialization": "PASS",
        "strict_radius_shift": "PASS",
        "arithmetic_firewall": "PASS",
        "certificate_sha256": hashlib.sha256(CERT.read_bytes()).hexdigest(),
        "check": True,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
