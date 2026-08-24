#!/usr/bin/env python3
"""Independent exact checker for C127 evidence."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results" / "c127_uniform_horseshoe_evidence.json"


def q(text: str) -> Fraction:
    return Fraction(text)


def mu_value(n: int) -> int:
    factors = 0
    d = 2
    x = n
    while d * d <= x:
        if x % d == 0:
            x //= d
            factors += 1
            if x % d == 0:
                return 0
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        factors += 1
    return -1 if factors % 2 else 1


def expected_primitive(n: int) -> int:
    return sum(mu_value(d) * 2 ** (n // d) for d in range(1, n + 1) if n % d == 0) // n


def validate(data: dict) -> None:
    assert data["schema"] == "HCS-C127-v1"
    payload_hash = data.pop("payload_sha256")
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(canonical).hexdigest() == payload_hash
    data["payload_sha256"] = payload_hash

    cert = data["uniform_certificates"]
    assert q(cert["minimum_domain_gap"]) == Fraction(1, 3)
    assert q(cert["minimum_image_gap"]) == Fraction(1, 3)
    assert q(cert["minimum_unstable_expansion"]) == 3
    assert q(cert["maximum_stable_contraction"]) == Fraction(1, 3)
    assert q(cert["maximum_trace_norm"]) == Fraction(3, 2)
    assert q(cert["lambda_lipschitz_constant"]) == Fraction(3, 4)
    assert q(cert["mu_lipschitz_constant"]) == Fraction(9, 4)
    assert q(cert["uniform_zero_free_radius_open"]) == Fraction(3, 2)

    assert len(data["audit_grid"]) == 9
    for item in data["audit_grid"]:
        lam, mu = q(item["lambda"]), q(item["mu"])
        assert 3 <= lam <= 4 and Fraction(1, 5) <= mu <= Fraction(1, 3)
        assert q(item["domain_gap"]) == 1 - 2 / lam
        assert q(item["image_gap"]) == 1 - 2 * mu
        assert q(item["trace_norm"]) == 2 / ((lam - 1) * (1 - mu))
        assert q(item["first_determinant_zero"]) == lam / 2
        for row in item["periods"]:
            n = row["n"]
            denominator = (lam**n - 1) * (1 - mu**n)
            assert row["fixed_points"] == 2**n
            assert row["primitive_cycles"] == expected_primitive(n)
            assert q(row["stability_denominator"]) == denominator
            assert q(row["trace"]) == Fraction(2**n, 1) / denominator

    for row in data["counts_through_12"]:
        assert row == {
            "n": row["n"],
            "fixed_points": 2 ** row["n"],
            "primitive_cycles": expected_primitive(row["n"]),
        }
    sample_lam = q(data["sample_parameter"]["lambda"])
    sample_mu = q(data["sample_parameter"]["mu"])
    assert sample_lam == Fraction(7, 2) and sample_mu == Fraction(4, 15)
    for sample in data["sample_periodic_points"]:
        word = sample["word"]
        assert word and set(word) <= {"0", "1"}
        n = len(word)
        sx = sum(sample_lam ** (n - 1 - j) * int(bit) for j, bit in enumerate(word))
        sy = sum(sample_mu ** (n - 1 - j) * int(bit) for j, bit in enumerate(word))
        x0 = (sample_lam - 1) * sx / (sample_lam**n - 1)
        y0 = (1 - sample_mu) * sy / (1 - sample_mu**n)
        assert q(sample["x0"]) == x0 and q(sample["y0"]) == y0
        x, y = x0, y0
        itinerary_ok = True
        for bit_text in word:
            bit = int(bit_text)
            if bit == 0:
                itinerary_ok &= 0 <= x <= 1 / sample_lam
            else:
                itinerary_ok &= 1 - 1 / sample_lam <= x <= 1
            x, y = (
                sample_lam * x - (sample_lam - 1) * bit,
                sample_mu * y + (1 - sample_mu) * bit,
            )
        closes = x == x0 and y == y0
        assert sample["closes"] is closes and closes
        assert sample["itinerary_ok"] is itinerary_ok and itinerary_ok
    assert all(data["checks"].values())
    assert data["route_a"]["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
    assert data["route_a"]["structural_gate"] == "UNIFORM_PARAMETER_THEOREM_PASS"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    flags = data["scope_flags"]
    assert flags["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert not any(v for k, v in flags.items() if k != "scope")


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    validate(data)
    print("C127 independent checker: PASS")


if __name__ == "__main__":
    main()
