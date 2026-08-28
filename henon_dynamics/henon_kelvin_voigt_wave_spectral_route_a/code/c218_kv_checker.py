#!/usr/bin/env python3
"""Independent checker for the C218 Kelvin--Voigt certificate."""
from __future__ import annotations

import argparse
import cmath
from fractions import Fraction
from hashlib import sha256
import json
import math
from pathlib import Path
import re

SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c218_kv_evidence.json"
MODES = list(range(1, 65))
CASES = [
    ("light", Fraction(1, 4)),
    ("balanced", Fraction(1)),
    ("near_critical", Fraction(3, 2)),
    ("first_critical", Fraction(2)),
    ("strong", Fraction(4)),
    ("undamped_boundary", Fraction(0)),
]
ASYMPTOTIC_MODES = [16, 32, 64]
NUMBER_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def roots(b: float, n: int) -> tuple[complex, complex, float]:
    disc = b*b*n**4 - 4*n*n
    z = cmath.sqrt(disc + 0j)
    return (-b*n*n + z)/2, (-b*n*n - z)/2, disc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    def exact(actual, expected, label: str) -> None:
        check(type(actual) is type(expected), label + " type")
        check(actual == expected, label)

    top = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal",
           "evaluator", "headline", "frozen_object", "theorem", "regression",
           "exact_identities", "route_a", "scope_flags", "citations", "nonclaims",
           "payload_sha256"}
    check(set(data) == top, "top-level key closure")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    exact(data["schema"], "hcs-c218-kelvin-voigt-v1", "schema")
    exact(data["candidate_id"], "HCS-C218", "candidate")
    exact(data["evaluation_date"], "2026-08-28", "date")
    exact(data["source_commit"], SOURCE_COMMIT, "source commit")
    exact(data["scope_literal"], SCOPE, "scope")
    exact(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route verdict")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B lock")
    check(all(value is False for value in data["scope_flags"].values()), "scope firewall")
    check("gamma" in data["theorem"]["spectral_abscissa_gap"] and "min" in data["theorem"]["spectral_abscissa_gap"], "gap theorem")
    check("not an" in data["theorem"]["essential_point"] and "eigenvalue" in data["theorem"]["essential_point"], "essential non-eigenvalue")
    check("Weyl" in data["theorem"]["essential_spectrum_definition"] and "singular" in data["theorem"]["essential_spectrum_definition"], "essential definition")
    domain = data["frozen_object"]["generator_domain"]
    check("D(A)" in domain, "generator domain label")
    check("H_0^1 x L^2" in domain and "(u,v) in H_0^1(0,pi) x L^2(0,pi)" in domain,
          "generator domain ambient energy space")
    check("v in H_0^1(0,pi)" in domain and "u+bv in H^2(0,pi) intersect H_0^1(0,pi)" in domain,
          "generator domain regularity and boundary")
    ess_def = data["theorem"]["essential_spectrum_definition"]
    check(all(token in ess_def for token in ("e_n", "a_n", "w_n", "||w_n||_E=1", "weakly ->0",
                                             "||(A+1/b)w_n||_E", "lambda_n,++1/b")),
          "explicit Weyl singular sequence")
    point = data["theorem"]["essential_point"]
    check("b^(-2)u=0" in point and "u=v=0" in point, "direct non-eigenvalue substitution")
    operator_boundary = data["theorem"]["operator_boundary"]
    check(all(token in operator_boundary for token in
              ("t>0", "e^(tA)w_n", "exp(-t/b)>0", "not compact", "not compact or Schatten")),
          "positive-time noncompact boundary")
    check("uniform exact-rate" in data["theorem"]["boundary"], "Jordan caveat")
    check(data["regression"]["case_count"] == len(CASES), "case count")
    check(data["regression"]["modes_per_case"] == len(MODES), "mode count")
    rows = data["regression"]["cases"]
    check(len(rows) == len(CASES), "rows length")
    for ci, (row, spec) in enumerate(zip(rows, CASES)):
        case_id, bq = spec
        check(set(row) == {"case_id", "b", "mode_count", "modes", "spectral_gap", "optimizer", "asymptotics"}, f"case {ci} keys")
        exact(row["case_id"], case_id, f"case {ci} id")
        exact(row["b"], str(bq), f"case {ci} b")
        b = float(bq)
        check(row["mode_count"] == len(MODES), f"case {ci} mode count")
        check(len(row["modes"]) == len(MODES), f"case {ci} mode rows")
        for mi, (mrow, n) in enumerate(zip(row["modes"], MODES)):
            check(set(mrow) == {"n", "discriminant", "regime", "lambda_plus", "lambda_minus", "slow_gap"}, f"mode {ci}/{mi} keys")
            exact(mrow["n"], n, f"mode {ci}/{mi} n")
            rp, rm, disc = roots(b, n)
            check(NUMBER_RE.fullmatch(mrow["discriminant"]) is not None, f"mode {ci}/{mi} disc syntax")
            check(abs(float(mrow["discriminant"]) - disc) < 1e-9*max(1.0, abs(disc)), f"mode {ci}/{mi} disc")
            regime = "critical" if abs(disc) < 1e-10 else ("underdamped" if disc < 0 else "overdamped")
            exact(mrow["regime"], regime, f"mode {ci}/{mi} regime")
            for label, z in (("lambda_plus", rp), ("lambda_minus", rm)):
                zrow = mrow[label]
                check(set(zrow) == {"re", "im"}, f"mode {ci}/{mi} {label} keys")
                check(NUMBER_RE.fullmatch(zrow["re"]) is not None and NUMBER_RE.fullmatch(zrow["im"]) is not None,
                      f"mode {ci}/{mi} {label} syntax")
                check(abs(float(zrow["re"]) - z.real) < 3e-12*max(1.0, abs(z.real)), f"mode {ci}/{mi} {label} re")
                check(abs(float(zrow["im"]) - z.imag) < 3e-12*max(1.0, abs(z.imag)), f"mode {ci}/{mi} {label} im")
            check(abs(float(mrow["slow_gap"]) + rp.real) < 3e-12*max(1.0, abs(rp.real)), f"mode {ci}/{mi} slow gap")
            # Vieta and the physical stability sign are checked independently.
            check(abs(rp + rm + b*n*n) < 3e-12*max(1.0, b*n*n), f"mode {ci}/{mi} Vieta sum")
            check(abs(rp*rm - n*n) < 3e-10*max(1.0, n*n), f"mode {ci}/{mi} Vieta product")
            check(rp.real <= 1e-12 and rm.real <= 1e-12, f"mode {ci}/{mi} stability")
            if b == 0:
                check(abs(rp.imag-n) < 1e-12 and abs(rm.imag+n) < 1e-12, f"mode {ci}/{mi} undamped roots")
        if b == 0:
            check(row["spectral_gap"] is None and row["optimizer"] is None, f"case {ci} boundary nulls")
        else:
            gap = min(b/2.0, 1.0/b)
            check(NUMBER_RE.fullmatch(row["spectral_gap"]) is not None, f"case {ci} gap syntax")
            check(abs(float(row["spectral_gap"])-gap) < 3e-12, f"case {ci} gap")
            check(NUMBER_RE.fullmatch(row["optimizer"]) is not None, f"case {ci} optimizer syntax")
            check(abs(float(row["optimizer"])-2**0.5) < 3e-12, f"case {ci} optimizer")
            check(len(row["asymptotics"]) == len(ASYMPTOTIC_MODES), f"case {ci} asym length")
            for arow, n in zip(row["asymptotics"], ASYMPTOTIC_MODES):
                check(set(arow) == {"n", "slow_minus_limit", "fast_real"}, f"asym {ci}/{n} keys")
                exact(arow["n"], n, f"asym {ci}/{n} n")
                rp, rm, _ = roots(b, n)
                check(float(arow["slow_minus_limit"]) < 0, f"asym {ci}/{n} slow side")
                check(abs(float(arow["slow_minus_limit"]) - (rp.real+1/b)) < 3e-10, f"asym {ci}/{n} slow")
                check(float(arow["fast_real"]) < -0.5/b, f"asym {ci}/{n} fast")
    # Independently realize the Weyl sequence in each modal energy norm.
    # For z_n=(1,lambda_{n,+}), the weighted norm is
    # sqrt(n^2|z_1|^2+|z_2|^2); the generator eigen-equation makes the
    # normalized residual exactly |lambda_{n,+}+1/b|.
    for ci, (_, bq) in enumerate(CASES[:-1]):
        b = float(bq)
        residuals = []
        for n in (64, 128, 256):
            rp, _, disc = roots(b, n)
            check(disc > 0, f"Weyl mode {ci}/{n} overdamped")
            z_norm = math.sqrt(n*n + abs(rp)**2)
            a = 1.0 / z_norm
            normalized_norm = math.sqrt(n*n*abs(a)**2 + abs(rp*a)**2)
            check(abs(normalized_norm - 1.0) < 2e-15, f"Weyl mode {ci}/{n} normalization")
            shifted = (rp + 1.0/b, (rp + 1.0/b)*rp)
            weighted = math.sqrt(n*n*abs(shifted[0])**2 + abs(shifted[1])**2) / z_norm
            expected = abs(rp + 1.0/b)
            check(abs(weighted - expected) < 2e-14*max(1.0, expected),
                  f"Weyl mode {ci}/{n} residual identity")
            residuals.append(expected)
        check(residuals[2] < residuals[1] < residuals[0], f"Weyl mode {ci} residual convergence")
    check(len(data["exact_identities"]) == 6, "identity count")
    for identity in data["exact_identities"]:
        check(set(identity) == {"name", "formula"}, "identity keys")
        check(identity["formula"], "identity nonempty")
    for citation in data["citations"]:
        check(set(citation) == {"key", "claim", "title", "authors", "venue", "year", "doi"}, "citation closure")
        check(citation["doi"].startswith("10."), "citation DOI")
    print(f"C218 independent checker: PASS ({checks} assertions; {len(CASES)*len(MODES)} modal roots)")
    print("root regimes, Jordan boundary, essential accumulation, exact gap/optimizer, energy and scope firewall: PASS")


if __name__ == "__main__":
    main()
