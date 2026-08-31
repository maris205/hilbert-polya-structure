#!/usr/bin/env python3
"""Deterministic certificate for the mixed linear congruential map."""
from __future__ import annotations

import argparse
import json
import math
from hashlib import sha256
from pathlib import Path

SOURCE = "b89544f1f7b1043f4158dfdf9db77787b332f146"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c258_lcg_evidence.json"
MAX_MODULUS = 96


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def factorization(n):
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


def phi(n):
    ans = n
    for p, _ in factorization(n):
        ans -= ans // p
    return ans


def condition_modulus(m):
    rad = math.prod(p for p, _ in factorization(m))
    return math.lcm(rad, 4 if m % 4 == 0 else 1)


def hull_dobell(m, a, c):
    fs = factorization(m)
    return (
        math.gcd(c, m) == 1
        and all((a - 1) % p == 0 for p, _ in fs)
        and (m % 4 != 0 or (a - 1) % 4 == 0)
    )


def single_cycle(m, a, c):
    seen = set()
    x = 0
    while x not in seen:
        seen.add(x)
        x = (a * x + c) % m
    return x == 0 and len(seen) == m, len(seen)


def iterate(m, a, c, x, n):
    for _ in range(n):
        x = (a * x + c) % m
    return x


def valuation(n, p):
    e = 0
    while n and n % p == 0:
        n //= p
        e += 1
    return e


def modulus_row(m):
    fac = factorization(m)
    L = condition_modulus(m)
    observed = 0
    mismatches = 0
    orbit_steps = 0
    first = None
    first_nontranslation = None
    for a in range(m):
        for c in range(m):
            actual, steps = single_cycle(m, a, c)
            predicted = hull_dobell(m, a, c)
            orbit_steps += steps
            observed += int(actual)
            mismatches += int(actual != predicted)
            if actual and first is None:
                first = [a, c]
            if actual and a != 1 and first_nontranslation is None:
                first_nontranslation = [a, c]
    return {
        "m": m,
        "factorization": [[p, e] for p, e in fac],
        "condition_modulus": L,
        "unit_increment_count": phi(m),
        "admissible_multiplier_count": m // L,
        "predicted_full_parameter_pairs": phi(m) * (m // L),
        "observed_full_parameter_pairs": observed,
        "criterion_mismatch_count": mismatches,
        "enumerated_parameter_pairs": m * m,
        "orbit_steps": orbit_steps,
        "first_admissible_pair": first,
        "first_nontranslation_pair": first_nontranslation,
    }


def cycle_case(m):
    L = condition_modulus(m)
    a = 1 + L if 1 + L < m else 1
    c = 1
    ok, length = single_cycle(m, a, c)
    assert ok
    fixed = []
    for n in range(1, 2 * m + 1):
        count = sum(iterate(m, a, c, x, n) == x for x in range(m))
        fixed.append(count)
    return {
        "m": m,
        "a": a,
        "c": c,
        "orbit_length": length,
        "primitive_orbits": [{"length": m, "multiplicity": 1}],
        "fixed_counts_n1_to_2m": fixed,
        "zeta": f"1/(1-t^{m})",
        "koopman_characteristic": f"u^{m}-1",
        "koopman_phase_indices": list(range(m)),
    }


def valuation_rows():
    rows = []
    for p in (2, 3, 5, 7):
        a = 5 if p == 2 else 1 + p
        for exponent in range(1, 5):
            modulus = p**exponent
            for n in sorted({1, p, p**2, p**3}):
                series = sum(a**j for j in range(n))
                gap = series * ((a - 1) * 2 + 1)
                rows.append(
                    {
                        "p": p,
                        "exponent": exponent,
                        "modulus": modulus,
                        "a": a,
                        "c": 1,
                        "x": 2,
                        "n": n,
                        "valuation_of_return_gap": valuation(gap, p),
                        "valuation_of_n": valuation(n, p),
                    }
                )
    return rows


def build():
    rows = [modulus_row(m) for m in range(2, MAX_MODULUS + 1)]
    data = {
        "schema": "hcs-c258-mixed-lcg-hull-dobell-v1",
        "candidate_id": "HCS-C258",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVAL,
        },
        "headline": (
            "Every mixed congruential map on Z/mZ has one cycle through all m "
            "states exactly under the Hull--Dobell prime-power conditions; "
            "the CRT proof, primitive ledger, zeta, and Koopman spectrum are exact."
        ),
        "frozen_object": {
            "state": "x in Z/mZ with integer m>=2",
            "map": "F(x)=a*x+c mod m",
            "parameters": "residue classes a,c modulo m",
            "clock": "one affine congruential update",
            "normalization": "least nonnegative residues; one full orbit means one m-cycle",
            "determinant_convention": "source Artin--Mazur zeta only; no target determinant",
            "arithmetic_origin": "intrinsic finite ring, its prime-power quotients, and CRT",
            "forbidden_data": (
                "target primes or zeros, arithmetic local factors, Euler factors, root "
                "numbers, automorphy, target divisor or functional equation, Hilbert--Polya operators"
            ),
        },
        "theorem": {
            "criterion": (
                "F is one m-cycle iff gcd(c,m)=1, every prime p|m divides a-1, "
                "and 4|a-1 whenever 4|m."
            ),
            "iterate": "F^n(x)=a^n*x+c*(1+a+...+a^(n-1)) mod m.",
            "local_return": (
                "On every p^e factor satisfying the criterion, the return-gap "
                "p-adic valuation equals v_p(n), so every state has exact period p^e."
            ),
            "crt": "The coprime local periods p^e have lcm m, hence every seed lies on the same m-cycle.",
            "primitive": "The admissible map has one primitive orbit of length m and no other orbit.",
            "fixed_counts": "#Fix(F^n)=m when m divides n and 0 otherwise.",
            "zeta": "The source Artin--Mazur zeta is 1/(1-t^m).",
            "koopman": "The counting-measure Koopman permutation is unitary with all m-th roots of unity once each.",
            "boundaries": (
                "Failure of the unit increment, a prime congruence, or the mod-4 "
                "condition obstructs a full cycle; m=1 is excluded as the trivial one-state face."
            ),
            "route_boundary": (
                "Prime-power CRT structure is intrinsic but supplies no rational-prime "
                "orbit dictionary, logarithmic clock, target divisor, or Hilbert--Polya spectrum."
            ),
        },
        "regression": {
            "max_modulus": MAX_MODULUS,
            "modulus_rows": rows,
            "modulus_row_count": len(rows),
            "enumerated_parameter_pairs": sum(row["enumerated_parameter_pairs"] for row in rows),
            "enumerated_orbit_steps": sum(row["orbit_steps"] for row in rows),
            "observed_full_parameter_pairs": sum(row["observed_full_parameter_pairs"] for row in rows),
            "criterion_mismatch_count": sum(row["criterion_mismatch_count"] for row in rows),
            "cycle_cases": [cycle_case(m) for m in (8, 9, 12, 25, 32, 45)],
            "valuation_rows": valuation_rows(),
        },
        "exact_identities": [
            {"identity_id": "iterate", "formula": "F^n(x)=a^n*x+c*S_n"},
            {"identity_id": "geometric_sum", "formula": "(a-1)S_n=a^n-1"},
            {"identity_id": "odd_lte", "formula": "v_p(S_n)=v_p(n) for odd p and p|(a-1)"},
            {"identity_id": "two_lte", "formula": "v_2(S_n)=v_2(n) when a=1 mod 4"},
            {"identity_id": "crt_period", "formula": "lcm_{p^e||m}(p^e)=m"},
            {"identity_id": "fixed_count", "formula": "#Fix(F^n)=m*1_{m|n}"},
            {"identity_id": "zeta", "formula": "exp(sum_n #Fix(F^n)t^n/n)=1/(1-t^m)"},
            {"identity_id": "koopman", "formula": "det(uI-U)=u^m-1"},
        ],
        "route_a": {
            "tuple": [
                "A0_WEAK_ARITHMETIC_RELATION",
                "A1_WEAK",
                "A2_FAIL",
                "A3_FAIL",
                "A4_NATURAL_QUANTIZATION",
            ],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
            "strongest_positive": (
                "Prime-power quotient dynamics, CRT assembly, the complete primitive "
                "cycle, source zeta, and same-clock unitary Koopman lift are analytic."
            ),
            "strongest_failure": (
                "No rational-prime orbit dictionary, log-prime clock, target divisor, "
                "global target analytic structure, or Hilbert--Polya identification exists."
            ),
        },
        "scope_flags": {
            "uses_target_zero_table": False,
            "uses_prime_table": False,
            "claims_arithmetic_local_data": False,
            "claims_euler_factors": False,
            "claims_root_numbers": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {
                "key": "HullDobell1962",
                "claim": "classical ownership of the full-period criterion for mixed congruential generators",
                "source": "T. E. Hull and A. R. Dobell, Random Number Generators, SIAM Review 4 (1962), 230--254",
                "doi": "10.1137/1004061",
            }
        ],
        "nonclaims": [
            "literature priority beyond the cited classical criterion",
            "that every nonadmissible affine map has a classified cycle decomposition",
            "a rational-prime primitive-orbit dictionary or logarithmic prime clock",
            "target arithmetic local data, Euler factors, root numbers, automorphy, divisor, or functional equation",
            "a target Fredholm determinant, Hilbert--Polya operator, or Route-B authorization",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "status": "C258_PRODUCER_PASS",
                "moduli": data["regression"]["modulus_row_count"],
                "parameter_pairs": data["regression"]["enumerated_parameter_pairs"],
                "payload_sha256": data["payload_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
