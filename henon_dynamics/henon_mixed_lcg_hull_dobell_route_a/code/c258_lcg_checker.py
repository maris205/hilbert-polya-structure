#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C258."""
from __future__ import annotations

import argparse
import json
import math
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c258_lcg_evidence.json"
SOURCE = "b89544f1f7b1043f4158dfdf9db77787b332f146"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
MAX_MODULUS = 96
EXPECTED_TUPLE = [
    "A0_WEAK_ARITHMETIC_RELATION",
    "A1_WEAK",
    "A2_FAIL",
    "A3_FAIL",
    "A4_NATURAL_QUANTIZATION",
]
FLAGS = {
    "uses_target_zero_table",
    "uses_prime_table",
    "claims_arithmetic_local_data",
    "claims_euler_factors",
    "claims_root_numbers",
    "claims_automorphy",
    "claims_target_divisor_or_functional_equation",
    "claims_hilbert_polya_operator",
    "invokes_route_b",
}


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def factors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def totient(n):
    return sum(math.gcd(k, n) == 1 for k in range(n))


def local_modulus(m):
    rad = math.prod(p for p, _ in factors(m))
    return math.lcm(rad, 4 if m % 4 == 0 else 1)


def criterion(m, a, c):
    return (
        math.gcd(c, m) == 1
        and all((a - 1) % p == 0 for p, _ in factors(m))
        and (m % 4 != 0 or (a - 1) % 4 == 0)
    )


def orbit(m, a, c):
    order = []
    where = {}
    x = 0
    while x not in where:
        where[x] = len(order)
        order.append(x)
        x = (a * x + c) % m
    return x == 0 and len(order) == m, len(order)


def power(m, a, c, x, n):
    for _ in range(n):
        x = (a * x + c) % m
    return x


def vp(n, p):
    ans = 0
    while n and n % p == 0:
        ans += 1
        n //= p
    return ans


def preflight(data):
    assert data["schema"] == "hcs-c258-mixed-lcg-hull-dobell-v1"
    assert data["candidate_id"] == "HCS-C258"
    assert data["evaluation_date"] == "2026-08-31"
    assert data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"] == {
        "path": "flow_systems/skills/route-a-evaluator.md",
        "version": "0.2.0",
        "sha256": EVAL,
    }
    assert data["payload_sha256"] == payload_hash(data)
    assert "Hull--Dobell" in data["headline"] and "CRT" in data["headline"]
    frozen = data["frozen_object"]
    assert frozen["map"] == "F(x)=a*x+c mod m"
    assert frozen["clock"] == "one affine congruential update"
    assert frozen["normalization"].startswith("least nonnegative residues")
    assert frozen["determinant_convention"].startswith("source Artin--Mazur zeta only")
    assert frozen["arithmetic_origin"].startswith("intrinsic finite ring")
    assert "Euler factors" in frozen["forbidden_data"]
    theorem = data["theorem"]
    assert "gcd(c,m)=1" in theorem["criterion"] and "4|a-1" in theorem["criterion"]
    assert "a^n*x" in theorem["iterate"]
    assert "valuation equals v_p(n)" in theorem["local_return"]
    assert "lcm m" in theorem["crt"]
    assert "one primitive orbit" in theorem["primitive"]
    assert "#Fix(F^n)=m" in theorem["fixed_counts"]
    assert theorem["zeta"] == "The source Artin--Mazur zeta is 1/(1-t^m)."
    assert "unitary" in theorem["koopman"]
    assert "mod-4" in theorem["boundaries"]
    assert "no rational-prime" in theorem["route_boundary"]
    route = data["route_a"]
    assert route["tuple"] == EXPECTED_TUPLE
    assert route["overall"] == "ROUTE_A_EXPLORATORY"
    assert route["route_b_invocation_allowed"] is False
    assert "analytic" in route["strongest_positive"]
    assert "No rational-prime" in route["strongest_failure"]
    assert set(data["scope_flags"]) == FLAGS
    assert all(value is False for value in data["scope_flags"].values())
    assert len(data["citations"]) == 1
    assert data["citations"][0]["doi"] == "10.1137/1004061"
    assert len(data["nonclaims"]) == 5
    reg = data["regression"]
    assert reg["max_modulus"] == MAX_MODULUS
    assert reg["modulus_row_count"] == MAX_MODULUS - 1
    assert len(reg["modulus_rows"]) == MAX_MODULUS - 1
    assert reg["criterion_mismatch_count"] == 0
    total_pairs = total_steps = total_full = 0
    for expected_m, row in enumerate(reg["modulus_rows"], 2):
        assert row["m"] == expected_m
        assert row["factorization"] == [[p, e] for p, e in factors(expected_m)]
        L = local_modulus(expected_m)
        predicted = totient(expected_m) * (expected_m // L)
        assert row["condition_modulus"] == L
        assert row["unit_increment_count"] == totient(expected_m)
        assert row["admissible_multiplier_count"] == expected_m // L
        assert row["predicted_full_parameter_pairs"] == predicted
        assert row["observed_full_parameter_pairs"] == predicted
        assert row["criterion_mismatch_count"] == 0
        assert row["enumerated_parameter_pairs"] == expected_m * expected_m
        assert row["first_admissible_pair"] is not None
        a, c = row["first_admissible_pair"]
        assert criterion(expected_m, a, c)
        if row["first_nontranslation_pair"] is not None:
            a, c = row["first_nontranslation_pair"]
            assert a != 1 and criterion(expected_m, a, c)
        total_pairs += row["enumerated_parameter_pairs"]
        total_steps += row["orbit_steps"]
        total_full += predicted
    assert reg["enumerated_parameter_pairs"] == total_pairs
    assert reg["enumerated_orbit_steps"] == total_steps
    assert reg["observed_full_parameter_pairs"] == total_full
    assert [row["m"] for row in reg["cycle_cases"]] == [8, 9, 12, 25, 32, 45]
    for row in reg["cycle_cases"]:
        m = row["m"]
        assert criterion(m, row["a"], row["c"])
        assert row["orbit_length"] == m
        assert row["primitive_orbits"] == [{"length": m, "multiplicity": 1}]
        assert row["fixed_counts_n1_to_2m"] == [m if n % m == 0 else 0 for n in range(1, 2 * m + 1)]
        assert row["zeta"] == f"1/(1-t^{m})"
        assert row["koopman_characteristic"] == f"u^{m}-1"
        assert row["koopman_phase_indices"] == list(range(m))
    assert len(reg["valuation_rows"]) == 64
    for row in reg["valuation_rows"]:
        assert row["valuation_of_return_gap"] == row["valuation_of_n"]
    assert len(data["exact_identities"]) == 8


def validate(data):
    preflight(data)
    assertions = 0
    reg_rows = {row["m"]: row for row in data["regression"]["modulus_rows"]}
    for m in range(2, MAX_MODULUS + 1):
        observed = 0
        steps = 0
        for a in range(m):
            for c in range(m):
                actual, length = orbit(m, a, c)
                predicted = criterion(m, a, c)
                assertions += 1
                if actual != predicted:
                    raise AssertionError(f"criterion mismatch m={m} a={a} c={c}")
                observed += int(actual)
                steps += length
        row = reg_rows[m]
        assertions += 3
        assert observed == row["observed_full_parameter_pairs"]
        assert steps == row["orbit_steps"]
        assert observed == totient(m) * (m // local_modulus(m))
    for row in data["regression"]["cycle_cases"]:
        m, a, c = row["m"], row["a"], row["c"]
        for n, expected in enumerate(row["fixed_counts_n1_to_2m"], 1):
            actual = sum(power(m, a, c, x, n) == x for x in range(m))
            assertions += 1
            assert actual == expected
    for row in data["regression"]["valuation_rows"]:
        a, p, n, x = row["a"], row["p"], row["n"], row["x"]
        series = sum(a**j for j in range(n))
        gap = series * ((a - 1) * x + row["c"])
        assertions += 2
        assert vp(gap, p) == row["valuation_of_return_gap"]
        assert vp(n, p) == row["valuation_of_n"]
    return assertions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    if args.quick:
        preflight(data)
        print("C258 quick hostile preflight: PASS")
    else:
        count = validate(data)
        print(
            f"C258 independent checker: PASS ({count} assertions; "
            "all affine pairs through modulus 96, CRT counts, fixed ledgers, and valuations)"
        )


if __name__ == "__main__":
    main()
