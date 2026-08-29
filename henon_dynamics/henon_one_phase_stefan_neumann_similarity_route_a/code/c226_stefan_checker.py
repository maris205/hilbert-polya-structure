#!/usr/bin/env python3
"""Independent checker for the C226 Stefan receipt.

The checker does not import the producer.  Roots are recomputed with an
independent bracketed solver and all nested objects have exact-key closure.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

import mpmath as mp

SOURCE_COMMIT = "489672bd36abd3a4f6da92d1446a0af575917959"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c226_stefan_evidence.json"
mp.mp.dps = 90
NUMBER_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")
STE_VALUES = [F(1, 100), F(1, 10), F(1, 2), F(1), F(2), F(10), F(100), F(10000)]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def ftext(q: F) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def mfrac(q: F) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def Froot(x: mp.mpf) -> mp.mpf:
    return mp.sqrt(mp.pi) * x * mp.exp(x * x) * mp.erf(x)


def root_independent(ste: mp.mpf) -> mp.mpf:
    # Bracket by powers of two and use 500 fixed bisection steps.
    lo, hi = mp.mpf("0"), mp.mpf("1")
    while Froot(hi) <= ste:
        hi *= 2
    for _ in range(500):
        mid = (lo + hi) / 2
        if Froot(mid) < ste:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def close(actual: object, expected: mp.mpf, tol: mp.mpf = mp.mpf("2e-60")) -> bool:
    if not isinstance(actual, str) or NUMBER_RE.fullmatch(actual) is None:
        return False
    return abs(mp.mpf(actual) - expected) <= tol * max(mp.mpf(1), abs(expected))


def exact_keys(obj: object, expected: set[str], label: str, check) -> None:
    check(isinstance(obj, dict), label + " object")
    if isinstance(obj, dict):
        check(set(obj) == expected, label + " keys")


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

    top = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator",
           "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a",
           "scope_flags", "citations", "nonclaims", "payload_sha256"}
    check(set(data) == top, "top-level key closure")
    check(data.get("payload_sha256") == payload_hash(data), "payload hash")
    check(data.get("schema") == "hcs-c226-one-phase-stefan-neumann-v1", "schema")
    check(data.get("candidate_id") == "HCS-C226", "candidate")
    check(data.get("evaluation_date") == "2026-08-29", "date")
    check(data.get("source_commit") == SOURCE_COMMIT, "source commit")
    check(data.get("scope_literal") == SCOPE, "scope")
    exact_keys(data.get("evaluator"), {"path", "version", "sha256"}, "evaluator", check)
    check(data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator lock")
    exact_keys(data.get("frozen_object"), {"pde", "boundary_conditions", "initial_geometry", "parameters", "dimensional_diffusivity", "similarity_coordinate", "phase_space", "forbidden_data"}, "frozen", check)
    exact_keys(data.get("theorem"), {"similarity_solution", "stefan_root", "root_existence_uniqueness", "small_ste_series", "large_ste_lambert_bounds", "flux_partition", "energy_identity", "sensible_energy", "latent_energy", "input_energy", "degenerate_limits", "uniqueness_scope", "analytic_boundary"}, "theorem", check)
    exact_keys(data.get("regression"), {"cases", "boundary_cases", "ste_values", "case_count", "boundary_count", "working_decimal_digits", "serialized_significant_digits"}, "regression", check)
    exact_keys(data.get("route_a"), {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}, "route", check)
    exact_keys(data.get("scope_flags"), {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}, "scope", check)
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route verdict")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B lock")
    check(all(value is False for value in data["scope_flags"].values()), "scope firewall")
    frozen = data["frozen_object"]
    for phrase in ("u_t=u_xx", "0<x<s(t)", "u(0,t)=1", "u(s(t),t)=0", "beta*s'(t)", "Ste^{-1}", "s(0)=0", "kappa>0"):
        check(phrase in " ".join(str(v) for v in frozen.values()), "frozen " + phrase)
    theorem = data["theorem"]
    for key in theorem:
        check(isinstance(theorem[key], str) and theorem[key], "theorem text " + key)
    for phrase in ("F'(lambda)", "exactly one", "lambda^2=Ste/2", "689 Ste^5/28350", "W(2 Ste^2/pi)", "J_interface/J_wall", "input=sensible+latent", "zero-latent rescaling", "do not satisfy A3"):
        check(any(phrase in value for value in theorem.values()), "theorem lock " + phrase)

    regression = data["regression"]
    check(regression["ste_values"] == [ftext(v) for v in STE_VALUES], "Ste probes")
    check(regression["case_count"] == len(STE_VALUES), "case count")
    check(regression["boundary_count"] == 3, "boundary count")
    case_keys = {"case_id", "regime", "ste", "beta", "lambda", "F_lambda", "root_residual", "wall_flux_coefficient", "interface_flux_coefficient", "interface_wall_flux_ratio", "sensible_energy_coefficient", "latent_energy_coefficient", "input_energy_coefficient", "energy_residual", "lambda2", "small_ste_lambda2_series5", "erfc_value", "erfc_upper_bound", "erfc_bound_gap", "lambert_lambda2_lower", "lambert_lambda2_upper"}
    rows = regression["cases"]
    check(isinstance(rows, list) and len(rows) == len(STE_VALUES), "rows")
    previous = mp.mpf("0")
    for idx, (entry, ste_q) in enumerate(zip(rows, STE_VALUES)):
        exact_keys(entry, case_keys, f"case {idx}", check)
        ste = mfrac(ste_q)
        check(entry["case_id"] == "ste_" + ftext(ste_q).replace("/", "_"), f"case {idx} id")
        check(entry["regime"] == "positive", f"case {idx} regime")
        check(entry["ste"] == ftext(ste_q), f"case {idx} Ste")
        beta = 1 / ste
        lam = root_independent(ste)
        erf_l = mp.erf(lam)
        wall = 1 / (mp.sqrt(mp.pi) * erf_l)
        interface = mp.exp(-lam * lam) * wall
        sensible = 2 * (1 - mp.exp(-lam * lam)) * wall
        latent = 2 * beta * lam
        inp = 2 * wall
        series = ste / 2 - ste**2 / 6 + mp.mpf(7) * ste**3 / 90 - mp.mpf(79) * ste**4 / 1890 + mp.mpf(689) * ste**5 / 28350
        erfc_value = mp.erfc(lam)
        erfc_bound = mp.exp(-lam * lam) / (mp.sqrt(mp.pi) * lam)
        for key, expected in (("beta", beta), ("lambda", lam), ("F_lambda", ste), ("root_residual", mp.mpf(0)), ("wall_flux_coefficient", wall), ("interface_flux_coefficient", interface), ("interface_wall_flux_ratio", mp.exp(-lam*lam)), ("sensible_energy_coefficient", sensible), ("latent_energy_coefficient", latent), ("input_energy_coefficient", inp), ("energy_residual", mp.mpf(0)), ("lambda2", lam*lam), ("small_ste_lambda2_series5", series), ("erfc_value", erfc_value), ("erfc_upper_bound", erfc_bound), ("erfc_bound_gap", erfc_bound-erfc_value)):
            check(close(entry[key], expected), f"case {idx} {key}")
        check(erfc_value > 0 and erfc_value < erfc_bound, f"case {idx} erfc strict bound")
        check(mp.mpf(entry["erfc_bound_gap"]) > 0, f"case {idx} erfc gap")
        check(mp.mpf(entry["lambda"]) > previous, f"case {idx} monotone lambda")
        previous = mp.mpf(entry["lambda"])
        if ste > 1:
            lo = mp.mpf("0.5") * mp.lambertw(2 * ste**2 / mp.pi)
            hi = mp.mpf("0.5") * mp.lambertw(2 * (ste + 1)**2 / mp.pi)
            check(close(entry["lambert_lambda2_lower"], mp.re(lo)), f"case {idx} lower bound")
            check(close(entry["lambert_lambda2_upper"], mp.re(hi)), f"case {idx} upper bound")
            check(lo < lam*lam < hi, f"case {idx} Lambert enclosure")
        else:
            check(entry["lambert_lambda2_lower"] is None and entry["lambert_lambda2_upper"] is None, f"case {idx} null Lambert")

    boundary_keys = {"case_id", "regime", "ste", "beta", "lambda", "statement"}
    b_rows = regression["boundary_cases"]
    check(isinstance(b_rows, list) and len(b_rows) == 3, "boundary rows")
    expected_boundaries = [("zero_superheat", "0", "infinity", "0.0"), ("zero_latent_heat", "infinity", "0.0", "infinity"), ("zero_diffusivity", "fixed", "fixed", "fixed")]
    for i, (entry, expected) in enumerate(zip(b_rows, expected_boundaries)):
        exact_keys(entry, boundary_keys, f"boundary {i}", check)
        check((entry["case_id"], entry["ste"], entry["beta"], entry["lambda"]) == expected, f"boundary {i} labels")
        check(entry["regime"] == "degenerate_boundary" and isinstance(entry["statement"], str) and entry["statement"], f"boundary {i} statement")
    check("dimensional thermal diffusivity kappa=0" in b_rows[2]["statement"], "zero diffusivity definition")
    exact_keys(data["exact_identities"][0], {"name", "formula"}, "identity0", check)
    check(isinstance(data["exact_identities"], list) and len(data["exact_identities"]) == 6, "identity count")
    for i, item in enumerate(data["exact_identities"]):
        exact_keys(item, {"name", "formula"}, f"identity {i}", check)
        check(item["name"] and item["formula"], f"identity {i} text")
    citation_locks = [
        {"key": "AddisonHowisonKing2005", "claim": "small-latent-heat Stefan asymptotics and free-boundary formulation", "title": "Ray methods for Free Boundary Problems", "authors": "J. A. Addison, S. D. Howison, and J. R. King", "venue": "Oxford/University of Nottingham preprint", "year": 2005, "url": "https://people.maths.ox.ac.uk/howison/papers/smallstefan.pdf"},
        {"key": "Gupta2003", "claim": "classical Stefan problem, one-dimensional Neumann solution, and phase-change conventions", "title": "The Classical Stefan Problem: Basic Concepts, Modelling and Analysis", "authors": "S. C. Gupta", "venue": "Elsevier, North-Holland Series in Applied Mathematics and Mechanics, Volume 45", "year": 2003, "isbn": "978-0-444-51086-0", "url": "https://shop.elsevier.com/books/the-classical-stefan-problem/gupta/978-0-444-51086-0"},
        {"key": "Rubinstein1982", "claim": "global stability of the Neumann solution of the two-phase Stefan problem; background only, not a one-phase priority claim", "title": "Global Stability of the Neumann Solution of the Two-phase Stefan Problem", "authors": "L. I. Rubinstein", "venue": "IMA Journal of Applied Mathematics 28(3), 287--299", "year": 1982, "doi": "10.1093/imamat/28.3.287", "url": "https://academic.oup.com/imamat/article-abstract/28/3/287/660860"},
    ]
    check(data["citations"] == citation_locks, "citation metadata lock")
    for i, item in enumerate(data["citations"]):
        check(isinstance(item, dict) and item["claim"], f"citation {i} claim")
    check(isinstance(data["nonclaims"], list) and len(data["nonclaims"]) >= 5, "nonclaims")
    check(any("zero latent" in x for x in data["nonclaims"]), "zero latent nonclaim")
    check(any("target continuation/divisor/counting law" in x for x in data["nonclaims"]), "A3 nonclaim")
    print(f"C226 independent checker: PASS ({checks} assertions)")


if __name__ == "__main__":
    main()
