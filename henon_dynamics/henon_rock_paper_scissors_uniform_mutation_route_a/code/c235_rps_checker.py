#!/usr/bin/env python3
"""Producer-independent checker for the C235 RPS certificate.

The formulas below are intentionally reimplemented rather than imported from
the producer.  This makes the evidence byte/hash and numerical rows auditable
under hostile source mutations.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c235_rps_evidence.json"
SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
SERIALIZED_DIGITS = 64
mp.mp.dps = 90

CONSERVATIVE_CASES = [("conservative_a1", F(1)), ("conservative_a2", F(2)), ("conservative_a3", F(3))]
H_VALUES = [F(1, 1000), F(1, 100), F(1, 50), F(1, 30), F(1, 28)]
MUTATION_CASES = [
    ("mu_small_interior", F(1), F(1, 10), (F(1, 2), F(1, 3), F(1, 6)), F(2)),
    ("mu_small_skew", F(2), F(1, 10), (F(3, 5), F(1, 5), F(1, 5)), F(2)),
    ("mu_large_interior", F(3), F(1, 2), (F(1, 10), F(2, 5), F(1, 2)), F(3, 2)),
    ("mu_boundary_x", F(1), F(1, 4), (F(0), F(1, 2), F(1, 2)), F(1)),
    ("mu_boundary_y", F(2), F(1, 3), (F(2, 3), F(0), F(1, 3)), F(1)),
    ("mu_boundary_z", F(3), F(1, 2), (F(1, 3), F(2, 3), F(0)), F(1)),
]
CONTRACTION_CASES = [
    ("a_zero_mu_quarter", F(1, 4), (F(4, 5), F(1, 10), F(1, 10)), F(1, 2)),
    ("a_zero_mu_two", F(2), (F(1, 6), F(1, 3), F(1, 2)), F(3, 4)),
    ("a_zero_mu_one", F(1), (F(1, 20), F(7, 20), F(3, 5)), F(1)),
]

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
NUM_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(q: F | int | str) -> mp.mpf:
    z = q if isinstance(q, F) else F(q)
    return mp.mpf(z.numerator) / z.denominator


def dec(v: mp.mpf) -> str:
    if abs(v) < mp.mpf("1e-82"):
        v = mp.mpf("0")
    return mp.nstr(v, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-70, max_fixed=70)


def field(a: mp.mpf, mu: mp.mpf, p: tuple[mp.mpf, mp.mpf, mp.mpf]) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    x, y, z = p
    return (a * x * (y - z) + mu * (mp.mpf(1) / 3 - x), a * y * (z - x) + mu * (mp.mpf(1) / 3 - y), a * z * (x - y) + mu * (mp.mpf(1) / 3 - z))


def rk4(a: mp.mpf, mu: mp.mpf, p: tuple[mp.mpf, mp.mpf, mp.mpf], t: F, steps: int) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    dt = mpq(t) / steps
    q = p
    for _ in range(steps):
        k1 = field(a, mu, q)
        k2 = field(a, mu, tuple(q[i] + dt * k1[i] / 2 for i in range(3)))
        k3 = field(a, mu, tuple(q[i] + dt * k2[i] / 2 for i in range(3)))
        k4 = field(a, mu, tuple(q[i] + dt * k3[i] for i in range(3)))
        q = tuple(q[i] + dt * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6 for i in range(3))
    return q


def cubic(x: mp.mpf, h: mp.mpf) -> mp.mpf:
    return x * (1 - x) ** 2 - 4 * h


def roots(h: F) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    hm = mpq(h)
    lo, hi = mp.mpf(0), mp.mpf(1) / 3
    for _ in range(360):
        m = (lo + hi) / 2
        if cubic(m, hm) > 0:
            hi = m
        else:
            lo = m
    xm = (lo + hi) / 2
    lo, hi = mp.mpf(1) / 3, mp.mpf(1)
    for _ in range(360):
        m = (lo + hi) / 2
        if cubic(m, hm) > 0:
            lo = m
        else:
            hi = m
    xp = (lo + hi) / 2
    return xm, xp, 2 - xm - xp


def quadrature(a: F, h: F) -> mp.mpf:
    xm, xp, x3 = roots(h)
    mid, half = (xm + xp) / 2, (xp - xm) / 2
    def fun(theta: mp.mpf) -> mp.mpf:
        x = mid + half * mp.sin(theta)
        return 1 / mp.sqrt(x * (x3 - x))
    return 2 / mpq(a) * mp.quad(fun, [-mp.pi / 2, 0, mp.pi / 2])


def close(value: str, expected: mp.mpf, label: str, check=None, tol: mp.mpf = mp.mpf("2e-42")) -> None:
    ok_syntax = isinstance(value, str) and NUM_RE.fullmatch(value) is not None
    ok_value = ok_syntax and abs(mp.mpf(value) - expected) <= tol * max(1, abs(expected))
    if check is None:
        if not ok_syntax:
            raise AssertionError(label + " syntax")
        if not ok_value:
            raise AssertionError(label + " value")
    else:
        check(ok_syntax, label + " syntax")
        check(ok_value, label + " value")


def distance(p: tuple[mp.mpf, mp.mpf, mp.mpf]) -> mp.mpf:
    return mp.sqrt(mp.fsum((q - mp.mpf(1) / 3) ** 2 for q in p))


def quick_preflight(data: dict) -> None:
    assert set(data) == TOP_KEYS
    assert data["schema"] == "hcs-c235-rps-uniform-mutation-v1" and data["candidate_id"] == "HCS-C235"
    assert data["source_commit"] == SOURCE_COMMIT and data["fixed_epoch"] == FIXED_EPOCH and data["scope_literal"] == SCOPE
    assert data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False
    assert len(data["regression"]["conservative_rows"]) == 15 and len(data["regression"]["mutation_rows"]) == 6
    print("C235 quick hostile preflight: PASS")


def validate(data: dict) -> int:
    checks = 0
    def check(ok: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            raise AssertionError(label)
    def exact(a, b, label: str) -> None:
        check(type(a) is type(b), label + " type")
        check(a == b, label)

    check(set(data) == TOP_KEYS, "top-level closure")
    exact(data["schema"], "hcs-c235-rps-uniform-mutation-v1", "schema")
    exact(data["candidate_id"], "HCS-C235", "candidate")
    exact(data["evaluation_date"], "2026-08-29", "date")
    exact(data["source_commit"], SOURCE_COMMIT, "source lock")
    exact(data["fixed_epoch"], FIXED_EPOCH, "epoch")
    exact(data["scope_literal"], SCOPE, "scope")
    exact(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route verdict")
    check(set(data["scope_flags"]) == SCOPE_KEYS and all(v is False for v in data["scope_flags"].values()), "scope firewall")
    check(data["regression"]["working_digits"] == 90 and data["regression"]["serialized_digits"] == 64, "precision lock")
    check("a>0" in data["theorem"]["conservative_integral"] and "a=0" in data["theorem"]["conservative_integral"] and data["theorem"]["center_limit"].startswith("For a>0,"), "positive-rate conservative scope")

    cr = data["regression"]["conservative_rows"]
    check(data["regression"]["conservative_row_count"] == 15 == len(cr), "conservative count")
    ckeys = {"case_id", "a", "h", "x_minus", "x_plus", "x_third", "period", "a_period", "left_residual", "right_residual", "simple_level"}
    for idx, row in enumerate(cr):
        check(set(row) == ckeys, f"conservative row {idx} keys")
        expected_case, expected_a = CONSERVATIVE_CASES[idx // 5]
        expected_h = H_VALUES[idx % 5]
        exact(row["case_id"], expected_case, f"conservative {idx} id")
        exact(row["a"], str(expected_a), f"conservative {idx} a")
        exact(row["h"], str(expected_h), f"conservative {idx} h")
        xm, xp, x3 = roots(expected_h)
        close(row["x_minus"], xm, f"conservative {idx} xminus")
        close(row["x_plus"], xp, f"conservative {idx} xplus")
        close(row["x_third"], x3, f"conservative {idx} xthird")
        T = quadrature(expected_a, expected_h)
        close(row["period"], T, f"conservative {idx} period", tol=mp.mpf("3e-38"))
        close(row["a_period"], mpq(expected_a) * T, f"conservative {idx} scaled", tol=mp.mpf("3e-38"))
        close(row["left_residual"], cubic(xm, mpq(expected_h)), f"conservative {idx} left residual", tol=mp.mpf("3e-35"))
        close(row["right_residual"], cubic(xp, mpq(expected_h)), f"conservative {idx} right residual", tol=mp.mpf("3e-35"))
        check(row["simple_level"] is True and xm > 0 and xm < xp < 1 and x3 > 1, f"conservative {idx} geometry")
        check(mp.mpf(row["period"]) > 0, f"conservative {idx} period positive")

    lr = data["regression"]["center_limit_rows"]
    check(data["regression"]["center_limit_row_count"] == 3 == len(lr), "center-limit count")
    lkeys = {"case_id", "a", "h", "period_limit", "scaled_limit", "barycenter"}
    for idx, row in enumerate(lr):
        check(set(row) == lkeys, f"limit {idx} keys")
        a = CONSERVATIVE_CASES[idx][1]
        exact(row["a"], str(a), f"limit {idx} a"); exact(row["h"], "1/27", f"limit {idx} h")
        lim = 2 * mp.pi * mp.sqrt(3) / mpq(a)
        close(row["period_limit"], lim, f"limit {idx} period")
        close(row["scaled_limit"], 2 * mp.pi * mp.sqrt(3), f"limit {idx} scaled")
        exact(row["barycenter"], ["1/3", "1/3", "1/3"], f"limit {idx} barycenter")

    mr = data["regression"]["mutation_rows"]
    check(data["regression"]["mutation_row_count"] == 6 == len(mr), "mutation count")
    mkeys = {"case_id", "a", "mu", "initial", "time", "steps", "initial_field", "field_sum", "dlog_h_exact", "initial_h", "final_state", "final_sum", "final_h", "initial_distance", "final_distance", "strictly_positive_after"}
    for idx, row in enumerate(mr):
        check(set(row) == mkeys, f"mutation {idx} keys")
        cid, a, mu, p, t = MUTATION_CASES[idx]
        exact(row["case_id"], cid, f"mutation {idx} id"); exact(row["a"], str(a), f"mutation {idx} a"); exact(row["mu"], str(mu), f"mutation {idx} mu")
        exact(row["initial"], [str(q) for q in p], f"mutation {idx} initial"); exact(row["time"], str(t), f"mutation {idx} time"); exact(row["steps"], 800, f"mutation {idx} steps")
        pm = tuple(mpq(q) for q in p); f0 = field(mpq(a), mpq(mu), pm)
        for j in range(3): close(row["initial_field"][j], f0[j], f"mutation {idx} field {j}", tol=mp.mpf("3e-40"))
        close(row["field_sum"], mp.fsum(f0), f"mutation {idx} field sum", tol=mp.mpf("3e-40"))
        if any(q == 0 for q in p): exact(row["dlog_h_exact"], None, f"mutation {idx} boundary dlog")
        else:
            d = mu * (1 / p[0] + 1 / p[1] + 1 / p[2] - 9) / 3
            exact(row["dlog_h_exact"], str(d), f"mutation {idx} dlog")
        close(row["initial_h"], pm[0] * pm[1] * pm[2], f"mutation {idx} initial h")
        end = rk4(mpq(a), mpq(mu), pm, t, 800)
        for j in range(3): close(row["final_state"][j], end[j], f"mutation {idx} final {j}", tol=mp.mpf("2e-35"))
        close(row["final_sum"], mp.fsum(end), f"mutation {idx} final sum", tol=mp.mpf("2e-35")); close(row["final_h"], end[0] * end[1] * end[2], f"mutation {idx} final h", tol=mp.mpf("2e-35"))
        close(row["initial_distance"], distance(pm), f"mutation {idx} d0"); close(row["final_distance"], distance(end), f"mutation {idx} d1", tol=mp.mpf("2e-35"))
        check(abs(mp.fsum(end) - 1) < mp.mpf("1e-35"), f"mutation {idx} mass")
        check(all(v > 0 for v in end) and row["strictly_positive_after"] is True, f"mutation {idx} positivity")
        check(end[0] * end[1] * end[2] >= pm[0] * pm[1] * pm[2] - mp.mpf("1e-25"), f"mutation {idx} Lyapunov")

    xr = data["regression"]["contraction_rows"]
    check(data["regression"]["contraction_row_count"] == 3 == len(xr), "contraction count")
    xkeys = {"case_id", "a", "mu", "initial", "time", "exact_state", "sum", "distance_factor", "positive"}
    for idx, row in enumerate(xr):
        check(set(row) == xkeys, f"contraction {idx} keys")
        cid, mu, p, t = CONTRACTION_CASES[idx]
        exact(row["case_id"], cid, f"contraction {idx} id"); exact(row["a"], "0", f"contraction {idx} a"); exact(row["mu"], str(mu), f"contraction {idx} mu"); exact(row["initial"], [str(v) for v in p], f"contraction {idx} p"); exact(row["time"], str(t), f"contraction {idx} t")
        end = tuple(mp.mpf(1) / 3 + (mpq(p[j]) - mp.mpf(1) / 3) * mp.exp(-mpq(mu) * mpq(t)) for j in range(3))
        for j in range(3): close(row["exact_state"][j], end[j], f"contraction {idx} state {j}")
        close(row["sum"], mp.fsum(end), f"contraction {idx} sum"); close(row["distance_factor"], mp.exp(-mpq(mu) * mpq(t)), f"contraction {idx} factor")
        check(row["positive"] is True and all(v > 0 for v in end), f"contraction {idx} positivity")

    lin = data["regression"]["linearization_rows"]
    check(data["regression"]["linearization_row_count"] == 4 == len(lin), "linearization count")
    lkeys2 = {"case_id", "a", "mu", "real_part", "imag_abs", "tangent_trace", "tangent_determinant"}
    for idx, row in enumerate(lin):
        check(set(row) == lkeys2, f"linearization {idx} keys")
        aa, mm = [(F(1), F(1, 10)), (F(3), F(1, 2)), (F(0), F(1, 4)), (F(0), F(0))][idx]
        exact(row["a"], str(aa), f"linearization {idx} a"); exact(row["mu"], str(mm), f"linearization {idx} mu")
        close(row["real_part"], -mpq(mm), f"linearization {idx} real"); close(row["imag_abs"], mpq(aa) / mp.sqrt(3), f"linearization {idx} imag")
        close(row["tangent_trace"], -2 * mpq(mm), f"linearization {idx} trace"); close(row["tangent_determinant"], mpq(mm) ** 2 + mpq(aa) ** 2 / 3, f"linearization {idx} det")

    check(len(data["exact_identities"]) == 9, "identity ledger")
    check(len(data["citations"]) == 3 and all(set(c) == {"key", "claim", "source"} for c in data["citations"]), "citation ledger")
    check(len(data["nonclaims"]) == 5 and all(isinstance(x, str) for x in data["nonclaims"]), "nonclaim ledger")
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    if args.quick:
        quick_preflight(data)
    else:
        n = validate(data)
        print(f"C235 independent checker: PASS ({n} assertions; conservative period, mutation Lyapunov and face atlas)")


if __name__ == "__main__":
    main()
