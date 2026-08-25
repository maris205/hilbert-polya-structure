#!/usr/bin/env python3
"""SymPy reconstruction of C160 polynomial fixed dimensions and sieve."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c160_rule90_sieve_evidence.json"


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    x = sp.symbols("x")
    checks = 0
    for family in data["finite_replay"]["family_rows"]:
        if family["exponent_r"] > 8:
            continue
        length = family["ring_length_L"]
        spatial = sp.Poly(x**length + 1, x, modulus=2)
        fixed_by_time = {}
        for row in family["divisor_rows"]:
            time = row["divisor"]
            temporal = sp.Poly((x**2 + 1)**time + x**time, x, modulus=2)
            dimension = sp.degree(sp.gcd(spatial, temporal))
            assert int(dimension) == row["fixed_dimension"]
            assert 2**int(dimension) == row["fixed_points"]
            fixed_by_time[time] = 2**int(dimension)
            checks += 2
        signed = 0
        for row in family["maximal_subgroup_rows"]:
            time = row["intersection_time"]
            if time not in fixed_by_time:
                temporal = sp.Poly((x**2 + 1)**time + x**time, x, modulus=2)
                fixed_by_time[time] = 2**int(sp.degree(sp.gcd(spatial, temporal)))
            assert fixed_by_time[time] == row["fixed_points"]
            assert row["signed_term"] == row["inclusion_exclusion_sign"] * fixed_by_time[time]
            signed += row["signed_term"]
            checks += 2
        assert signed == family["nonfull_periodic_points"]
        checks += 1
    cyclotomic = sp.Poly(x**2 + x + 1, x, modulus=2)
    for row in data["finite_replay"]["mersenne_prime_rows"]:
        length = row["mersenne_prime_L"]
        assert sp.degree(sp.gcd(sp.Poly(x**length + 1, x, modulus=2), cyclotomic)) == 0
        assert row["exact_period_L_points"] == row["primitive_L_cycles"] * length
        checks += 2
    assert sp.degree(sp.gcd(sp.Poly(x**3 + 1, x, modulus=2), cyclotomic)) == 2
    checks += 1
    print(json.dumps({"status": "C160_SYMPY_PASS", "checks": checks, "max_r": 8}, sort_keys=True))


if __name__ == "__main__":
    main()
