#!/usr/bin/env python3
"""Independent transfer recurrence and finite enumeration for HCS-P69."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
CERT = PROJECT / "results/c69_certificate.json"
OUT = PROJECT / "results/c69_independent_check.json"


def energy(word: tuple[int, ...]) -> int:
    n = len(word)
    return sum(word[(j - 1) % n] == word[(j + 1) % n] for j in range(n))


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    for n in range(1, 18, 2):
        counts = [0] * (n + 1)
        for half in itertools.product((0, 1), repeat=(n + 1) // 2):
            word = half + half[:0:-1]
            counts[energy(word)] += 1
        expected = [0] * (n + 1)
        m = (n - 1) // 2
        row = [1]
        for _ in range(m):
            row = [1] + [row[i - 1] + row[i] for i in range(1, len(row))] + [1]
        for k, value in enumerate(row):
            expected[1 + 2 * k] = 2 * value
        if counts != expected:
            raise RuntimeError(f"transfer recurrence n={n}")
    if cert["exact_pressure_gap"] != "P_orb(s)-P_mf(s)=(1/2)log(cosh(s))":
        raise RuntimeError("pressure gap")
    if cert["claim_status"]["arithmetic_advance"] != "NO":
        raise RuntimeError("promotion")
    payload = {
        "candidate_id": "HCS-P69",
        "transfer_recurrence": "PASS",
        "enumerated_periods": list(range(1, 18, 2)),
        "pressure_identity": "PASS",
        "arithmetic_firewall": "PASS",
        "certificate_sha256": hashlib.sha256(CERT.read_bytes()).hexdigest(),
        "check": True,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
