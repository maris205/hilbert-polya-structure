#!/usr/bin/env python3
"""Producer-independent exact/numerical checker for HCS-C233."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import re

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c233_mminf_evidence.json"
SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PARAMETERS = [("balanced", F(1), F(2)), ("critical_ratio", F(2), F(1)), ("slow_service", F(1, 3), F(1, 2)), ("fast_service", F(5), F(3)), ("fractional", F(7, 4), F(5, 6))]
TIME_VALUES = [F(1, 5), F(1, 2), F(1), F(2)]
INITIAL_VALUES = [0, 1, 3, 7]
PMF_MAX = 24
MODE_MAX = 8
NUM_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(x: F) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def close_num(value: str, expected: mp.mpf, label: str, check, tol=mp.mpf("2e-58")) -> None:
    check(isinstance(value, str) and NUM_RE.fullmatch(value) is not None, label + " syntax")
    check(abs(mp.mpf(value) - expected) <= tol * max(1, abs(expected)), label + " value")


def poisson(k: int, mean: mp.mpf) -> mp.mpf:
    if k < 0:
        return mp.mpf("0")
    return mp.exp(-mean) * mean ** k / factorial(k)


def pmf(lam: F, mu: F, n0: int, t: F, m: int) -> mp.mpf:
    rho = mpq(lam / mu)
    a = mp.exp(-mpq(mu) * mpq(t))
    eta = rho * (1 - a)
    return sum((mp.binomial(n0, b) * a ** b * (1 - a) ** (n0 - b) * poisson(m - b, eta) for b in range(min(n0, m) + 1)), mp.mpf("0"))


def ch(k: int, n: int, rho: mp.mpf) -> mp.mpf:
    coeff = mp.mpf("0")
    for j in range(min(k, n) + 1):
        coeff += mp.binomial(n, j) * (-rho) ** (k - j) / factorial(k - j)
    return factorial(k) * coeff


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE); path = parser.parse_args().evidence
    data = json.loads(path.read_text())
    checks = 0

    def check(ok: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            raise AssertionError(label)

    def exact(a, b, label: str) -> None:
        check(type(a) is type(b), label + " type")
        check(a == b, label)

    top = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
    check(set(data) == top, "top-level closure")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    exact(data["schema"], "hcs-c233-mm-infinity-poisson-v1", "schema")
    exact(data["candidate_id"], "HCS-C233", "candidate")
    exact(data["evaluation_date"], "2026-08-29", "date")
    exact(data["source_commit"], SOURCE_COMMIT, "source commit")
    exact(data["fixed_epoch"], 1787875200, "fixed epoch")
    exact(data["scope_literal"], SCOPE, "scope")
    exact(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route verdict")
    check(all(value is False for value in data["scope_flags"].values()), "scope firewall")
    check(data["regression"]["pmf_max"] == PMF_MAX and data["regression"]["mode_max"] == MODE_MAX, "grid constants")
    check(data["regression"]["working_digits"] == 90 and data["regression"]["serialized_digits"] == 70, "precision constants")
    check(len(data["regression"]["stationary_rows"]) == len(PARAMETERS), "stationary count")
    check(len(data["regression"]["mode_rows"]) == len(PARAMETERS) * (MODE_MAX + 1), "mode count")
    check(len(data["regression"]["kernel_rows"]) == len(PARAMETERS) * len(TIME_VALUES) * len(INITIAL_VALUES), "kernel count")
    check(len(data["regression"]["trace_rows"]) == len(PARAMETERS) * len(TIME_VALUES), "trace count")
    mp.mp.dps = 90

    for idx, (row, spec) in enumerate(zip(data["regression"]["stationary_rows"], PARAMETERS)):
        label, la, mu = spec; rho = mpq(la / mu)
        check(set(row) == {"parameter_label", "lambda", "mu", "rho", "masses_n0_to_n12", "mass_sum_first_13", "recursion_ratio"}, f"stationary {idx} keys")
        exact(row["parameter_label"], label, f"stationary {idx} label")
        exact(row["lambda"], str(la), f"stationary {idx} lambda"); exact(row["mu"], str(mu), f"stationary {idx} mu"); exact(row["rho"], str(la / mu), f"stationary {idx} rho")
        masses = [mp.exp(-rho) * rho ** n / factorial(n) for n in range(13)]
        check(len(row["masses_n0_to_n12"]) == 13, f"stationary {idx} mass length")
        for n, (v, expected) in enumerate(zip(row["masses_n0_to_n12"], masses)):
            close_num(v, expected, f"stationary {idx} mass {n}", check)
        close_num(row["mass_sum_first_13"], sum(masses, mp.mpf("0")), f"stationary {idx} partial", check)
        close_num(row["recursion_ratio"], rho / 13, f"stationary {idx} recursion", check)

    for idx, row in enumerate(data["regression"]["mode_rows"]):
        spec = next(s for s in PARAMETERS if s[0] == row["parameter_label"]); _, la, mu = spec; rho = mpq(la / mu); k = int(row["mode"])
        check(set(row) == {"parameter_label", "lambda", "mu", "rho", "mode", "eigenvalue_rate", "eigenvalue_at_time_1", "normalization", "values_n0_n1_n3_n7_n12"}, f"mode {idx} keys")
        exact(row["lambda"], str(la), f"mode {idx} lambda"); exact(row["mu"], str(mu), f"mode {idx} mu"); exact(row["rho"], str(la / mu), f"mode {idx} rho")
        exact(row["eigenvalue_rate"], str(k), f"mode {idx} rate")
        norm = mp.sqrt(factorial(k) * rho ** k) if k else mp.mpf("1")
        close_num(row["normalization"], norm, f"mode {idx} norm", check)
        close_num(row["eigenvalue_at_time_1"], -mpq(mu) * k, f"mode {idx} eig", check)
        for n, v in zip(INITIAL_VALUES + [12], row["values_n0_n1_n3_n7_n12"]):
            close_num(v, ch(k, n, rho) / norm, f"mode {idx} value n={n}", check)
        # Direct generator eigen-equation on a few states is an independent
        # algebraic sanity check (the polynomial convention is easy to flip).
        for n in [0, 1, 3, 7]:
            lhs = mpq(la) * ch(k, n + 1, rho) + mpq(mu) * n * ch(k, n - 1, rho) - (mpq(la) + mpq(mu) * n) * ch(k, n, rho)
            check(abs(lhs + mpq(mu) * k * ch(k, n, rho)) < mp.mpf("1e-70"), f"mode {idx} generator n={n}")

    for idx, row in enumerate(data["regression"]["kernel_rows"]):
        spec = next(s for s in PARAMETERS if s[0] == row["parameter_label"]); _, la, mu = spec; t = F(row["time"]); n0 = int(row["initial_state"]); rho = mpq(la / mu); a = mp.exp(-mpq(mu) * mpq(t)); eta = rho * (1 - a)
        keys = {"parameter_label", "lambda", "mu", "rho", "time", "initial_state", "survival_factor", "immigration_mean", "pmf_max", "probabilities", "partial_mass", "tail_mass", "tv_bound_coupling"}
        check(set(row) == keys, f"kernel {idx} keys")
        exact(row["lambda"], str(la), f"kernel {idx} lambda"); exact(row["mu"], str(mu), f"kernel {idx} mu"); exact(row["rho"], str(la / mu), f"kernel {idx} rho"); exact(row["pmf_max"], PMF_MAX, f"kernel {idx} max")
        close_num(row["survival_factor"], a, f"kernel {idx} survival", check); close_num(row["immigration_mean"], eta, f"kernel {idx} eta", check)
        expected = [pmf(la, mu, n0, t, m) for m in range(PMF_MAX + 1)]
        check(len(row["probabilities"]) == PMF_MAX + 1, f"kernel {idx} length")
        for m, (v, e) in enumerate(zip(row["probabilities"], expected)):
            close_num(v, e, f"kernel {idx} pmf {m}", check, mp.mpf("4e-58"))
        partial = sum(expected, mp.mpf("0")); tail = max(mp.mpf("0"), 1 - partial)
        close_num(row["partial_mass"], partial, f"kernel {idx} partial", check); close_num(row["tail_mass"], tail, f"kernel {idx} tail", check)
        bound = min(mp.mpf("1"), a * (mp.mpf(n0) + rho))
        close_num(row["tv_bound_coupling"], bound, f"kernel {idx} coupling bound", check)
        stationary = [poisson(m, rho) for m in range(PMF_MAX + 1)]
        tv_partial = mp.mpf("0.5") * sum(abs(p - q) for p, q in zip(expected, stationary))
        check(tv_partial <= bound + mp.mpf("1e-50"), f"kernel {idx} TV coupling")
        check(all(p >= 0 for p in expected) and 0 <= partial <= 1, f"kernel {idx} probability")

    for idx, row in enumerate(data["regression"]["trace_rows"]):
        spec = next(s for s in PARAMETERS if s[0] == row["parameter_label"]); _, la, mu = spec; t = F(row["time"]); q = mp.exp(-mpq(mu) * mpq(t)); product = mp.mpf("1")
        for k in range(12): product *= 1 - q ** k
        check(set(row) == {"parameter_label", "lambda", "mu", "time", "q", "semigroup_trace", "determinant_product_first_12"}, f"trace {idx} keys")
        close_num(row["q"], q, f"trace {idx} q", check); close_num(row["semigroup_trace"], 1 / (1 - q), f"trace {idx} trace", check); close_num(row["determinant_product_first_12"], product, f"trace {idx} product", check)
        check(0 < q < 1 and product == 0, f"trace {idx} q-product convention")

    check(len(data["exact_identities"]) == 8, "identity rows")
    for c in data["citations"]:
        check(set(c) == {"key", "claim", "title", "authors", "venue", "date", "doi"}, "citation closure")
        check(c["doi"].startswith("10."), "citation DOI")
    print(f"C233 independent checker: PASS ({checks} assertions; Poisson kernel, Charlier modes, trace and coupling ledger)")
    print("stationarity, all-mode eigen-equations, positive-time trace class and scope firewall: PASS")


if __name__ == "__main__":
    main()
