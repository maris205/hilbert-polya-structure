#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C257."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c257_newton_cayley_evidence.json"
SOURCE = "b89544f1f7b1043f4158dfdf9db77787b332f146"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
TOP = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "exact_receipt", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
FLAGS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}


def ph(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    primes = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            primes += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        primes += 1
    return -1 if primes % 2 else 1


def valuation_two(n: int) -> int:
    e = 0
    while n % 2 == 0:
        e += 1
        n //= 2
    return e


def order_two(q: int) -> int:
    if q == 1:
        return 1
    assert q % 2 and gcd(q, 2) == 1
    r, k = 2 % q, 1
    while r != 1:
        r = (2 * r) % q
        k += 1
    return k


def parse_q(text: str) -> F:
    return F(text)


def validate(data: dict) -> int:
    checks = 0

    def ck(ok: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            raise AssertionError(label)

    def eq(a, b, label: str) -> None:
        ck(type(a) is type(b) and a == b, label)

    eq(set(data), TOP, "top closure")
    for key, value in (("schema", "hcs-c257-quadratic-newton-cayley-global-v1"), ("candidate_id", "HCS-C257"), ("evaluation_date", "2026-08-31"), ("source_commit", SOURCE), ("fixed_epoch", EPOCH), ("scope_literal", SCOPE)):
        eq(data[key], value, key)
    eq(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    eq(data["payload_sha256"], ph(data), "payload hash")
    frozen_expected = {
        "phase_space": "Riemann sphere P^1(C)",
        "polynomial": "p_a(z)=z^2-a^2 with a in C*",
        "dynamics": "N_a(z)=z-p_a(z)/p_a'(z)=(z^2+a^2)/(2z)",
        "cayley_coordinate": "w=C_a(z)=(z-a)/(z+a)",
        "clock": "Newton iteration n in Z_{≥0}",
        "parameter": "a in C*; a=0 is a separately recorded degree-drop face",
        "arithmetic_origin": "none; deterministic complex root-finding dynamics",
    }
    for key, value in frozen_expected.items():
        eq(data["frozen_object"].get(key), value, "frozen " + key)
    route = data["route_a"]
    eq(route["tuple"], ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    eq(route["overall"], "ROUTE_A_REJECTED", "route overall")
    eq(route["route_b_invocation_allowed"], False, "route B")
    ck("universal degree-two" in route["strongest_failure"], "degree obstruction")
    eq(set(data["scope_flags"]), FLAGS, "scope key closure")
    ck(all(value is False for value in data["scope_flags"].values()), "scope false")
    theorem = data["theorem"]
    expected_theorem_keys = {"global_conjugacy", "basin_julia_atlas", "double_exponential", "periodic_preperiodic", "counts_multipliers_zeta", "boundary_measure", "parameter_boundaries", "ownership", "scope"}
    eq(set(theorem), expected_theorem_keys, "theorem closure")
    for phrase in ("Mobius conjugacy", "Re(z/a)>0", "2^n", "tail is e", "multiplier 2^n", "Cauchy", "degree-one degeneration", "C141", "C177", "source-local"):
        ck(phrase.lower() in json.dumps(theorem, ensure_ascii=False).lower(), "theorem phrase " + phrase)

    receipt = data["exact_receipt"]
    eq(set(receipt), {"period_rows", "period_row_count", "root_order_rows", "root_order_row_count", "real_sample_rows", "real_sample_row_count", "cauchy_rows", "cauchy_row_count", "receipt_status"}, "receipt closure")
    eq(receipt["period_row_count"], 16, "period row count")
    eq(len(receipt["period_rows"]), 16, "period rows length")
    pkeys = {"n", "fixed_points_on_sphere", "exact_period_points", "primitive_orbits", "julia_exact_period_points", "julia_cycle_multiplier"}
    exact_sum = 0
    for n, row in enumerate(receipt["period_rows"], 1):
        eq(set(row), pkeys, f"period {n} closure")
        eq(row["n"], n, f"period {n} n")
        fixed = 2**n + 1
        exact = sum(mu(n // d) * (2**d + 1) for d in divisors(n))
        eq(row["fixed_points_on_sphere"], fixed, f"period {n} fixed")
        eq(row["exact_period_points"], exact, f"period {n} exact")
        ck(exact % n == 0, f"period {n} divisible")
        eq(row["primitive_orbits"], exact // n, f"period {n} orbits")
        eq(row["julia_exact_period_points"], exact - (2 if n == 1 else 0), f"period {n} Julia")
        eq(row["julia_cycle_multiplier"], str(2**n), f"period {n} multiplier")
        ck(sum(receipt["period_rows"][d - 1]["exact_period_points"] for d in divisors(n)) == fixed, f"period {n} inversion")
        exact_sum += exact
    ck(exact_sum > 100000, "nontrivial period ledger")

    eq(receipt["root_order_row_count"], 128, "order count")
    eq(len(receipt["root_order_rows"]), 128, "order length")
    okeys = {"root_of_unity_order", "two_adic_tail", "odd_part", "eventual_exact_period", "landing_order", "classification", "rule"}
    for m, row in enumerate(receipt["root_order_rows"], 1):
        eq(set(row), okeys, f"order {m} closure")
        eq(row["root_of_unity_order"], m, f"order {m} m")
        e = valuation_two(m)
        q = m // (2**e)
        eq(row["two_adic_tail"], e, f"order {m} tail")
        eq(row["odd_part"], q, f"order {m} odd")
        eq(row["landing_order"], q, f"order {m} landing")
        eq(row["eventual_exact_period"], order_two(q), f"order {m} period")
        eq(row["classification"], "periodic" if e == 0 else "strictly_preperiodic", f"order {m} class")
        eq(row["rule"], "tail=v2(m); period=ord_q(2), with ord_1(2)=1", f"order {m} rule")

    eq(receipt["real_sample_row_count"], 10, "real count")
    eq(len(receipt["real_sample_rows"]), 10, "real length")
    rkeys = {"u=z/a", "w=(u-1)/(u+1)", "w_after_1", "w_after_2", "basin", "root_error_coordinate_after_n"}
    for row in receipt["real_sample_rows"]:
        eq(set(row), rkeys, "real closure")
        u = parse_q(row["u=z/a"])
        if u == -1:
            eq(row["w=(u-1)/(u+1)"], "infinity", "pole w")
            eq(row["basin"], "root -a", "pole basin")
            continue
        w = (u - 1) / (u + 1)
        eq(parse_q(row["w=(u-1)/(u+1)"]), w, "real w")
        eq(parse_q(row["w_after_1"]), w**2, "real w2")
        eq(parse_q(row["w_after_2"]), w**4, "real w4")
        expected_basin = "root +a" if abs(w) < 1 else "root -a" if abs(w) > 1 else "Julia boundary"
        eq(row["basin"], expected_basin, "real basin")

    eq(receipt["cauchy_row_count"], 8, "Cauchy count")
    eq(len(receipt["cauchy_rows"]), 8, "Cauchy length")
    ckeys = {"s", "T(s)=(s^2-1)/(2s)", "line_point", "density", "angle_owner"}
    for row in receipt["cauchy_rows"]:
        eq(set(row), ckeys, "Cauchy closure")
        s = parse_q(row["s"])
        ck(s != 0, "Cauchy no pole")
        eq(parse_q(row["T(s)=(s^2-1)/(2s)"]), (s * s - 1) / (2 * s), "Cauchy map")
        eq(row["line_point"], "z=i*a*s", "Cauchy line")
        eq(row["density"], "ds/(pi*(1+s^2))", "Cauchy density")
        ck("theta maps to 2*theta" in row["angle_owner"], "Cauchy angle")
    ck("finite exact regression" in receipt["receipt_status"], "receipt limit")

    identities = data["exact_identities"]
    ids = [row.get("identity_id") for row in identities]
    ck(len(ids) == 23 and len(set(ids)) == 23, "identity ledger")
    formulas = {row["identity_id"]: row["formula"] for row in identities}
    required = {
        "conjugacy": "C_a(N_a(z))=C_a(z)^2 on the Riemann sphere",
        "fixed_count": "#Fix(N_a^n)=2^n+1 on the Riemann sphere",
        "am_zeta": "zeta_AM(t)=exp(sum_{n>=1}(2^n+1)t^n/n)=1/((1-t)*(1-2t))",
        "degenerate_a0": "at a=0 the rational degree drops and N_0(z)=z/2 for finite z",
    }
    for key, value in required.items():
        eq(formulas.get(key), value, "formula " + key)
    eq(len(data["citations"]), 2, "citation count")
    eq(data["citations"][0]["url"], "https://doi.org/10.2307/2369201", "Cayley DOI")
    eq(data["citations"][1]["url"], "https://www.jstor.org/stable/1970384", "Artin Mazur URL")
    eq(len(data["nonclaims"]), 5, "nonclaims")
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    count = validate(data)
    label = "quick hostile preflight" if args.quick else "independent checker"
    print(f"C257 {label}: PASS ({count} assertions; conjugacy, basins, root-order tails, zeta, Cauchy law)")


if __name__ == "__main__":
    main()
