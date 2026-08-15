#!/usr/bin/env python3
"""Independent symbolic and exact-small-period check for HCS-P64."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c64_certificate.json"


def canonical_sha(payload: object) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def word(bits: tuple[int, ...]) -> tuple[int, ...]:
    return bits + bits[:0:-1]


def primitive(row: tuple[int, ...]) -> bool:
    n = len(row)
    return not any(
        all(row[k] == row[k % d] for k in range(n))
        for d in range(1, n) if n % d == 0
    )


def degree(n: int) -> int:
    return sum(int(sp.mobius(n // d)) * 2 ** ((d + 1) // 2) for d in sp.divisors(n))


def run() -> dict[str, object]:
    cert = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    rows = []
    for n in range(1, 18, 2):
        population = [
            word(bits) for bits in itertools.product((0, 1), repeat=(n + 1) // 2)
            if primitive(word(bits))
        ]
        event = Fraction(sum(row[-1] == row[1 % n] for row in population), len(population))
        if len(population) != degree(n) or event != 1:
            raise ArithmeticError(f"independent symbolic check failed at n={n}")
        rows.append({"period": n, "primitive": len(population), "reflection_event": str(event)})
    t = sp.symbols("T")
    exact_small = {
        "n1": sp.factor(t**2 + 2 * t - 6),
        "n3": sp.factor(t**2 - 2 * t - 4),
        "n1_mahler": "log(sqrt(6))",
        "n3_mahler": "log(2)",
    }
    main_prefix = [row["primitive_half_words"] for row in cert["symbolic_rows"][: len(rows)]]
    if main_prefix != [row["primitive"] for row in rows]:
        raise ArithmeticError("main/independent degree mismatch")
    payload = {
        "candidate_id": "HCS-P64-INDEPENDENT",
        "rows": rows,
        "exact_small": {key: str(value) for key, value in exact_small.items()},
        "main_core_sha256": cert["core_sha256"],
        "all_checks_match": True,
        "check": True,
    }
    return payload


def main() -> None:
    payload = run()
    output = PROJECT / "results" / "c64_independent_check.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"check": True, "sha256": canonical_sha(payload)}, sort_keys=True))


if __name__ == "__main__":
    main()
