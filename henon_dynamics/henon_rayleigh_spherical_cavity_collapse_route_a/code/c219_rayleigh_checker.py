#!/usr/bin/env python3
"""Independent checker for the HCS-C219 Rayleigh certificate.

This file intentionally does not import the producer.  Its clock evaluations
use hypergeometric/incomplete-Beta identities, while the producer uses stable
quadratures, so a stale or semantically altered receipt is detected.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import re

import mpmath as mp

SOURCE_COMMIT = "86c7bb8a39cdd1b8e941e45833b068170ca06287"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c219_rayleigh_evidence.json"
mp.mp.dps = 80
NUMBER_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")

CASES = [
    ("collapse_unit", Fraction(1), Fraction(1), Fraction(1), "collapse"),
    ("collapse_scaled", Fraction(3, 2), Fraction(5, 4), Fraction(7, 3), "collapse"),
    ("collapse_small_pressure", Fraction(1, 7), Fraction(9, 5), Fraction(4, 3), "collapse"),
    ("collapse_large_pressure", Fraction(11, 3), Fraction(2, 3), Fraction(5, 2), "collapse"),
    ("collapse_small_radius", Fraction(2), Fraction(7, 3), Fraction(1, 5), "collapse"),
    ("equilibrium_zero_pressure", Fraction(0), Fraction(4, 3), Fraction(9, 5), "equilibrium"),
    ("equilibrium_zero_pressure_unit", Fraction(0), Fraction(1), Fraction(1), "equilibrium"),
    ("expansion_unit", Fraction(-1), Fraction(1), Fraction(1), "expansion"),
    ("expansion_scaled", Fraction(-5, 2), Fraction(7, 4), Fraction(3, 2), "expansion"),
    ("expansion_weak", Fraction(-1, 6), Fraction(5, 2), Fraction(11, 6), "expansion"),
    ("zero_radius_collapse", Fraction(2), Fraction(1), Fraction(0), "boundary"),
    ("zero_radius_equilibrium", Fraction(0), Fraction(1), Fraction(0), "boundary"),
    ("zero_radius_expansion", Fraction(-2), Fraction(1), Fraction(0), "boundary"),
]
COLLAPSE_X = [Fraction(3, 4), Fraction(1, 2), Fraction(1, 4), Fraction(1, 16)]
EXPANSION_X = [Fraction(5, 4), Fraction(3, 2), Fraction(2), Fraction(4)]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def ftext(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def mfrac(q: Fraction) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def close(actual: str, expected: mp.mpf, tol: mp.mpf = mp.mpf("2e-43")) -> bool:
    if not isinstance(actual, str) or NUMBER_RE.fullmatch(actual) is None:
        return False
    return abs(mp.mpf(actual) - expected) <= tol * max(mp.mpf(1), abs(expected))


def beta_clock() -> mp.mpf:
    return mp.beta(mp.mpf(5) / 6, mp.mpf(1) / 2) / 3


def jplus(x: mp.mpf) -> mp.mpf:
    # u=(1-s^2)^(1/3), followed by a Gauss hypergeometric primitive.
    s = mp.sqrt(1 - x**3)
    return mp.mpf(2) / 3 * s * mp.hyp2f1(mp.mpf(1) / 2, mp.mpf(1) / 6, mp.mpf(3) / 2, s**2)


def jminus(x: mp.mpf) -> mp.mpf:
    s = mp.sqrt(x**3 - 1)
    return mp.mpf(2) / 3 * s * mp.hyp2f1(mp.mpf(1) / 2, mp.mpf(1) / 6, mp.mpf(3) / 2, -s**2)


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

    def equal(actual, expected, label: str) -> None:
        check(type(actual) is type(expected), label + " type")
        check(actual == expected, label)

    def exact_keys(obj, expected: set[str], label: str) -> None:
        """Require an object and reject both missing and unknown nested keys."""
        check(isinstance(obj, dict), label + " object")
        if isinstance(obj, dict):
            check(set(obj) == expected, label + " keys")

    top = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal",
           "evaluator", "headline", "frozen_object", "theorem", "regression",
           "exact_identities", "route_a", "scope_flags", "citations", "nonclaims",
           "payload_sha256"}
    check(set(data) == top, "top-level key closure")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    equal(data["schema"], "hcs-c219-rayleigh-spherical-cavity-v1", "schema")
    equal(data["candidate_id"], "HCS-C219", "candidate")
    equal(data["evaluation_date"], "2026-08-28", "date")
    equal(data["source_commit"], SOURCE_COMMIT, "source commit")
    equal(data["scope_literal"], SCOPE, "scope")
    exact_keys(data["evaluator"], {"path", "version", "sha256"}, "evaluator closure")
    equal(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    exact_keys(data["frozen_object"], {"system", "initial_data", "parameters", "pressure_definition",
                                       "clock", "phase_space", "energy_lagrangian", "forbidden_data"},
               "frozen object closure")
    exact_keys(data["theorem"], {"first_integral", "collapse_branch", "collapse_clock",
                                  "collapse_constant", "collapse_decimal", "terminal_puiseux",
                                  "velocity_singularity", "acceleration_singularity", "sign_atlas",
                                  "energy_ledger", "volume_law", "lp_thresholds", "lagrangian",
                                  "boundary", "analytic_boundary"}, "theorem closure")
    exact_keys(data["regression"], {"cases", "case_count", "collapse_x", "expansion_x",
                                    "working_decimal_digits", "serialized_significant_digits"},
               "regression closure")
    exact_keys(data["route_a"], {"tuple", "overall", "route_b_invocation_allowed",
                                  "strongest_positive", "strongest_failure"}, "route closure")
    exact_keys(data["scope_flags"], {"uses_target_zero_table", "uses_prime_table",
                                      "claims_arithmetic_local_data", "claims_euler_factors",
                                      "claims_root_numbers", "claims_automorphy",
                                      "claims_target_divisor_or_functional_equation",
                                      "claims_hilbert_polya_operator", "invokes_route_b"},
               "scope closure")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route verdict")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B lock")
    check(all(value is False for value in data["scope_flags"].values()), "scope firewall")
    frozen = data["frozen_object"]
    check("R R_ddot" in frozen["system"] and "Pi/rho" in frozen["system"], "frozen equation")
    check("R0>0" in frozen["initial_data"] and "R_dot(0)=0" in frozen["initial_data"], "initial data")
    check("Pi in R" in frozen["parameters"] and "rho>0" in frozen["parameters"], "all parameter sign")
    check("L_phys" in frozen["energy_lagrangian"], "lagrangian frozen")
    theorem = data["theorem"]
    for key in ("first_integral", "collapse_branch", "collapse_clock", "terminal_puiseux",
                "velocity_singularity", "acceleration_singularity", "sign_atlas",
                "energy_ledger", "volume_law", "lp_thresholds", "lagrangian", "boundary"):
        check(isinstance(theorem.get(key), str) and theorem[key], f"theorem {key}")
    check("2/5" in theorem["terminal_puiseux"], "two-fifths exponent")
    check("5/3" in theorem["lp_thresholds"] and "5/8" in theorem["lp_thresholds"], "Lp thresholds")
    check(close(theorem["collapse_constant"], beta_clock()), "theorem beta constant")
    check("0.914681356501962" in theorem["collapse_decimal"], "theorem decimal constant")
    check("source Beta clock is not target continuation/divisor/counting law" in theorem["analytic_boundary"], "A3 boundary honesty")
    check("not an A3 analytic-structure match" in theorem["analytic_boundary"], "A3 failure lock")
    check(any("the source Beta clock is not target continuation/divisor/counting law and does not satisfy A3" == item
              for item in data["nonclaims"]), "A3 nonclaim")
    check(isinstance(data["regression"]["cases"], list), "cases list")
    check(isinstance(data["regression"]["collapse_x"], list), "collapse probe list")
    check(isinstance(data["regression"]["expansion_x"], list), "expansion probe list")
    rows = data["regression"]["cases"]
    check(data["regression"]["case_count"] == len(CASES), "case count")
    check(data["regression"]["collapse_x"] == [ftext(x) for x in COLLAPSE_X], "collapse probes")
    check(data["regression"]["expansion_x"] == [ftext(x) for x in EXPANSION_X], "expansion probes")
    check(len(rows) == len(CASES), "rows length")
    bclock = beta_clock()
    for ci, (entry, spec) in enumerate(zip(rows, CASES)):
        case_id, pq, rq, r0q, regime = spec
        expected_keys = {"case_id", "pressure", "density", "initial_radius", "regime", "a",
                         "beta_clock", "collapse_time", "terminal_coefficient", "initial_acceleration",
                         "energy_constant", "volume_terminal_coefficient", "dimensionless_samples",
                         "asymptotic_speed", "maximal_interval"}
        check(isinstance(entry, dict), f"case {ci} object")
        check(set(entry) == expected_keys, f"case {ci} keys")
        equal(entry["case_id"], case_id, f"case {ci} id")
        equal(entry["pressure"], ftext(pq), f"case {ci} pressure")
        equal(entry["density"], ftext(rq), f"case {ci} density")
        equal(entry["initial_radius"], ftext(r0q), f"case {ci} radius")
        equal(entry["regime"], regime, f"case {ci} regime")
        p, rho, r0 = mfrac(pq), mfrac(rq), mfrac(r0q)
        if regime == "boundary":
            for key in ("a", "collapse_time", "terminal_coefficient", "initial_acceleration",
                        "energy_constant", "volume_terminal_coefficient", "asymptotic_speed"):
                check(entry[key] is None, f"case {ci} boundary {key}")
            check(entry["beta_clock"] is None, f"case {ci} boundary beta")
            check(entry["dimensionless_samples"] == [], f"case {ci} boundary samples")
            check("no positive-radius" in entry["maximal_interval"], f"case {ci} boundary interval")
            continue
        check(close(entry["beta_clock"], bclock), f"case {ci} beta")
        if p == 0:
            equal(entry["a"], "0.0", f"case {ci} zero speed")
            check(entry["collapse_time"] is None and entry["terminal_coefficient"] is None, f"case {ci} zero nulls")
            check(close(entry["initial_acceleration"], mp.mpf(0)), f"case {ci} zero acceleration")
            check(close(entry["energy_constant"], mp.mpf(0)), f"case {ci} zero energy")
            check(entry["dimensionless_samples"] == [], f"case {ci} zero samples")
            check(entry["maximal_interval"].startswith("[0,infinity)"), f"case {ci} zero interval")
            continue
        a = mp.sqrt(2 * abs(p) / (3 * rho))
        C = r0 ** (mp.mpf(3) / 5) * (5 * a / 2) ** (mp.mpf(2) / 5)
        energy = 4 * mp.pi * p * r0**3 / 3
        check(close(entry["a"], a), f"case {ci} a")
        check(close(entry["initial_acceleration"], -p / (rho * r0)), f"case {ci} acceleration")
        check(close(entry["energy_constant"], energy), f"case {ci} energy")
        check(len(entry["dimensionless_samples"]) == 4, f"case {ci} sample count")
        if p > 0:
            check(close(entry["collapse_time"], r0 * bclock / a), f"case {ci} collapse time")
            check(close(entry["terminal_coefficient"], C), f"case {ci} terminal coefficient")
            check(close(entry["volume_terminal_coefficient"], 4 * mp.pi * C**3 / 3), f"case {ci} volume coefficient")
            check(entry["asymptotic_speed"] is None, f"case {ci} expansion speed null")
            check(entry["maximal_interval"].startswith("[0,Tc)"), f"case {ci} collapse interval")
            for sample, xq in zip(entry["dimensionless_samples"], COLLAPSE_X):
                check(set(sample) == {"x", "clock"}, f"case {ci} collapse sample keys")
                equal(sample["x"], ftext(xq), f"case {ci} sample x")
                check(close(sample["clock"], jplus(mfrac(xq))), f"case {ci} collapse clock")
            check(all(mp.mpf(entry["dimensionless_samples"][i]["clock"]) < mp.mpf(entry["dimensionless_samples"][i+1]["clock"]) for i in range(3)), f"case {ci} clock ordering")
        else:
            for key in ("collapse_time", "terminal_coefficient", "volume_terminal_coefficient"):
                check(entry[key] is None, f"case {ci} expansion {key} null")
            check(close(entry["asymptotic_speed"], a), f"case {ci} expansion speed")
            check(entry["maximal_interval"].startswith("[0,infinity)"), f"case {ci} expansion interval")
            for sample, xq in zip(entry["dimensionless_samples"], EXPANSION_X):
                check(set(sample) == {"x", "clock"}, f"case {ci} expansion sample keys")
                equal(sample["x"], ftext(xq), f"case {ci} sample x")
                check(close(sample["clock"], jminus(mfrac(xq))), f"case {ci} expansion clock")
            check(all(mp.mpf(entry["dimensionless_samples"][i]["clock"]) < mp.mpf(entry["dimensionless_samples"][i+1]["clock"]) for i in range(3)), f"case {ci} expansion ordering")
    check(isinstance(data["exact_identities"], list), "identity list")
    check(len(data["exact_identities"]) == 6, "identity count")
    for identity in data["exact_identities"]:
        check(set(identity) == {"name", "formula"}, "identity keys")
        check(isinstance(identity["formula"], str) and identity["formula"], "identity formula")
    check(isinstance(data["citations"], list), "citation list")
    check(len(data["citations"]) == 4, "citation count")
    for citation in data["citations"]:
        check(isinstance(citation, dict), "citation object")
        check(set(citation) == {"key", "claim", "title", "authors", "venue", "year", "doi"}, "citation closure")
        check(citation["doi"].startswith("10."), "citation DOI")
    check(isinstance(data["nonclaims"], list), "nonclaims list")
    check(all(isinstance(item, str) and item for item in data["nonclaims"]), "nonclaims strings")
    check(len(data["nonclaims"]) >= 4, "nonclaims")
    print(f"C219 independent checker: PASS ({checks} assertions; {len(rows)} parameter rows)")
    print("pressure-sign atlas, Beta clock, terminal 2/5 law, energy/volume/Lp ledger, boundaries and scope firewall: PASS")


if __name__ == "__main__":
    main()
