#!/usr/bin/env python3
"""Produce the deterministic HCS-C226 one-phase Stefan certificate.

The receipt is source-local: it certifies the Neumann similarity profile,
the unique Stefan root, both endpoint asymptotics, flux and energy ledgers,
and explicitly labelled degenerate limits.  No arithmetic target data are
read or inferred.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "489672bd36abd3a4f6da92d1446a0af575917959"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c226_stefan_evidence.json"
WORKING_DIGITS = 100
SERIALIZED_DIGITS = 78
mp.mp.dps = WORKING_DIGITS

# Exact rational probes span the small-Stefan, crossover, and large-Stefan
# regimes.  The two labelled boundary rows are not fed to the root solver.
STE_VALUES = [F(1, 100), F(1, 10), F(1, 2), F(1), F(2), F(10), F(100), F(10000)]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def q(value: F) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def ftext(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dec(value: mp.mpf | None, digits: int = SERIALIZED_DIGITS) -> str | None:
    if value is None:
        return None
    if abs(value) < mp.mpf("1e-90"):
        return "0.0"
    return mp.nstr(value, digits, strip_zeros=False, min_fixed=-80, max_fixed=80)


def erf_root_function(lam: mp.mpf) -> mp.mpf:
    """F(lambda)=sqrt(pi)*lambda*exp(lambda^2)*erf(lambda)."""
    return mp.sqrt(mp.pi) * lam * mp.exp(lam * lam) * mp.erf(lam)


def root_lambda(ste: mp.mpf) -> mp.mpf:
    """Monotone bisection, independent of any initial Newton guess."""
    if ste <= 0:
        raise ValueError("Ste must be positive")
    lo = mp.mpf("0")
    hi = mp.mpf("1")
    while erf_root_function(hi) < ste:
        hi *= 2
    # Fixed iterations make serialization reproducible across processes.
    for _ in range(420):
        mid = (lo + hi) / 2
        if erf_root_function(mid) < ste:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def lambert_bounds(ste: mp.mpf) -> tuple[mp.mpf | None, mp.mpf | None]:
    """Bounds on lambda^2 from z < sqrt(pi*x)e^x < z+1 (z=Ste).

    The erfc inequality erfc(lambda)<exp(-lambda^2)/(sqrt(pi)*lambda)
    gives these bounds for every positive lambda; we expose them only in
    the large-Stefan rows where they are asymptotically informative.
    """
    if ste <= 1:
        return None, None
    lo = mp.mpf("0.5") * mp.lambertw(2 * ste * ste / mp.pi)
    hi = mp.mpf("0.5") * mp.lambertw(2 * (ste + 1) * (ste + 1) / mp.pi)
    return mp.re(lo), mp.re(hi)


def series_lambda2(ste: mp.mpf) -> mp.mpf:
    """Five-term inverse series for x=lambda^2."""
    return (ste / 2 - ste**2 / 6 + mp.mpf(7) * ste**3 / 90
            - mp.mpf(79) * ste**4 / 1890 + mp.mpf(689) * ste**5 / 28350)


def row(ste_q: F) -> dict:
    ste = q(ste_q)
    lam = root_lambda(ste)
    erf_l = mp.erf(lam)
    wall = 1 / (mp.sqrt(mp.pi) * erf_l)
    interface = mp.exp(-lam * lam) * wall
    beta = 1 / ste
    sensible = 2 * (1 - mp.exp(-lam * lam)) * wall
    latent = 2 * beta * lam
    input_coeff = 2 * wall
    lower, upper = lambert_bounds(ste)
    erfc_value = mp.erfc(lam)
    erfc_bound = mp.exp(-lam * lam) / (mp.sqrt(mp.pi) * lam)
    return {
        "case_id": f"ste_{ftext(ste_q).replace('/', '_')}",
        "regime": "positive",
        "ste": ftext(ste_q),
        "beta": dec(beta),
        "lambda": dec(lam),
        "F_lambda": dec(erf_root_function(lam)),
        "root_residual": dec(erf_root_function(lam) - ste),
        "wall_flux_coefficient": dec(wall),
        "interface_flux_coefficient": dec(interface),
        "interface_wall_flux_ratio": dec(interface / wall),
        "sensible_energy_coefficient": dec(sensible),
        "latent_energy_coefficient": dec(latent),
        "input_energy_coefficient": dec(input_coeff),
        "energy_residual": dec(input_coeff - sensible - latent),
        "lambda2": dec(lam * lam),
        "small_ste_lambda2_series5": dec(series_lambda2(ste)),
        "erfc_value": dec(erfc_value),
        "erfc_upper_bound": dec(erfc_bound),
        "erfc_bound_gap": dec(erfc_bound - erfc_value),
        "lambert_lambda2_lower": dec(lower),
        "lambert_lambda2_upper": dec(upper),
    }


def boundary_rows() -> list[dict]:
    return [
        {
            "case_id": "zero_superheat",
            "regime": "degenerate_boundary",
            "ste": "0",
            "beta": "infinity",
            "lambda": "0.0",
            "statement": "Ste=0 (zero superheat) leaves the normalized temperature problem singular; the unscaled interface has no positive similarity speed.",
        },
        {
            "case_id": "zero_latent_heat",
            "regime": "degenerate_boundary",
            "ste": "infinity",
            "beta": "0.0",
            "lambda": "infinity",
            "statement": "L=0 corresponds to Ste=infinity and requires a separate heat-equation rescaling; no finite-lambda Stefan interface is asserted.",
        },
        {
            "case_id": "zero_diffusivity",
            "regime": "degenerate_boundary",
            "ste": "fixed",
            "beta": "fixed",
            "lambda": "fixed",
            "statement": "the dimensional thermal diffusivity kappa=0 collapses the similarity length 2 lambda sqrt(kappa t); the parabolic Neumann construction does not extend as a finite-interface classical solution.",
        },
    ]


def build() -> dict:
    cases = [row(v) for v in STE_VALUES]
    boundaries = boundary_rows()
    data = {
        "schema": "hcs-c226-one-phase-stefan-neumann-v1",
        "candidate_id": "HCS-C226",
        "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": "The one-phase Stefan problem has a unique Neumann similarity root with certified endpoint asymptotics, flux partition, and exact sensible-plus-latent energy balance.",
        "frozen_object": {
            "pde": "u_t=u_xx on 0<x<s(t), t>0",
            "boundary_conditions": "u(0,t)=1, u(s(t),t)=0, beta*s'(t)=-u_x(s(t)^-,t)",
            "initial_geometry": "s(0)=0 with the liquid initially at the phase-change temperature",
            "parameters": "beta=Ste^{-1}>0, physical similarity clock t>0",
            "dimensional_diffusivity": "kappa>0 denotes the dimensional thermal diffusivity before scaling; the displayed PDE uses kappa=1",
            "similarity_coordinate": "eta=x/(2*sqrt(t))",
            "phase_space": "classical one-phase free-boundary profiles with s(t)>0 for t>0",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert-Polya operators, and Route-B input",
        },
        "theorem": {
            "similarity_solution": "s(t)=2*lambda*sqrt(t), u(x,t)=1-erf(x/(2*sqrt(t)))/erf(lambda), 0<=x<=s(t)",
            "stefan_root": "F(lambda)=sqrt(pi)*lambda*exp(lambda^2)*erf(lambda)=Ste=1/beta",
            "root_existence_uniqueness": "F(0)=0, F(lambda)->infinity, and F'(lambda)=sqrt(pi)*exp(lambda^2)*erf(lambda)*(1+2 lambda^2)+2 lambda>0; hence exactly one lambda>0 for every Ste>0",
            "small_ste_series": "lambda^2=Ste/2-Ste^2/6+7 Ste^3/90-79 Ste^4/1890+689 Ste^5/28350+O(Ste^6); equivalently lambda=sqrt(Ste/2)(1-Ste/6+23 Ste^2/360-157 Ste^3/5040+O(Ste^4))",
            "large_ste_lambert_bounds": "For Ste>1, x_-=W(2 Ste^2/pi)/2 < lambda^2 < x_+=W(2(Ste+1)^2/pi)/2; therefore lambda^2~W(2 Ste^2/pi)/2",
            "flux_partition": "J_wall=-u_x(0,t)=1/(sqrt(pi*t)*erf(lambda)); J_interface=-u_x(s(t)^-,t)=exp(-lambda^2)J_wall, so J_interface/J_wall=exp(-lambda^2)",
            "energy_identity": "Integral_0^t J_wall(tau)d tau = Integral_0^{s(t)}u(x,t)dx + beta*s(t)",
            "sensible_energy": "Integral_0^{s(t)}u dx = 2 sqrt(t)*(1-exp(-lambda^2))/(sqrt(pi)*erf(lambda))",
            "latent_energy": "beta*s(t)=2 beta lambda sqrt(t)=2 exp(-lambda^2)sqrt(t)/(sqrt(pi)*erf(lambda))",
            "input_energy": "Integral_0^t J_wall d tau=2 sqrt(t)/(sqrt(pi)*erf(lambda)); input=sensible+latent exactly",
            "degenerate_limits": "beta->infinity (Ste->0) gives lambda->0 and a vanishing normalized interface; beta->0+ (Ste->infinity) gives lambda->infinity with Lambert-W growth; zero superheat and dimensional thermal diffusivity kappa=0 are singular rescalings, not finite-interface extensions; L=0 requires a separate zero-latent rescaling",
            "uniqueness_scope": "Uniqueness is for the positive Neumann similarity root and its similarity profile, not a claim of global uniqueness for arbitrary free-boundary data",
            "analytic_boundary": "The erf profile and Lambert-W asymptotic are source-local explicit solvability; they are not a target continuation/divisor/counting law and do not satisfy A3",
        },
        "regression": {
            "cases": cases,
            "boundary_cases": boundaries,
            "ste_values": [ftext(v) for v in STE_VALUES],
            "case_count": len(cases),
            "boundary_count": len(boundaries),
            "working_decimal_digits": WORKING_DIGITS,
            "serialized_significant_digits": SERIALIZED_DIGITS,
        },
        "exact_identities": [
            {"name": "similarity_heat_equation", "formula": "u_t-u_xx=0 after eta=x/(2 sqrt(t))"},
            {"name": "stefan_balance", "formula": "beta lambda=exp(-lambda^2)/(sqrt(pi) erf(lambda))"},
            {"name": "root_derivative", "formula": "F'(lambda)=sqrt(pi)e^(lambda^2)erf(lambda)(1+2lambda^2)+2lambda>0"},
            {"name": "energy_integral", "formula": "Integral_0^t J_wall=Integral_0^s u dx+beta s"},
            {"name": "sensible_integral", "formula": "Integral_0^{2lambda sqrt(t)}u dx=2sqrt(t)(1-e^(-lambda^2))/(sqrt(pi)erf(lambda))"},
            {"name": "lambert_enclosure", "formula": "Ste<sqrt(pi lambda^2)e^(lambda^2)<Ste+1"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "A complete source-native free-boundary similarity theorem with an exact energy and flux ledger",
            "strongest_failure": "The Stefan similarity clock has no primitive periodic-orbit owner, arithmetic carrier, target divisor, or Hilbert-Polya operator",
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
            {"key": "AddisonHowisonKing2005", "claim": "small-latent-heat Stefan asymptotics and free-boundary formulation", "title": "Ray methods for Free Boundary Problems", "authors": "J. A. Addison, S. D. Howison, and J. R. King", "venue": "Oxford/University of Nottingham preprint", "year": 2005, "url": "https://people.maths.ox.ac.uk/howison/papers/smallstefan.pdf"},
            {"key": "Gupta2003", "claim": "classical Stefan problem, one-dimensional Neumann solution, and phase-change conventions", "title": "The Classical Stefan Problem: Basic Concepts, Modelling and Analysis", "authors": "S. C. Gupta", "venue": "Elsevier, North-Holland Series in Applied Mathematics and Mechanics, Volume 45", "year": 2003, "isbn": "978-0-444-51086-0", "url": "https://shop.elsevier.com/books/the-classical-stefan-problem/gupta/978-0-444-51086-0"},
            {"key": "Rubinstein1982", "claim": "global stability of the Neumann solution of the two-phase Stefan problem; background only, not a one-phase priority claim", "title": "Global Stability of the Neumann Solution of the Two-phase Stefan Problem", "authors": "L. I. Rubinstein", "venue": "IMA Journal of Applied Mathematics 28(3), 287--299", "year": 1982, "doi": "10.1093/imamat/28.3.287", "url": "https://academic.oup.com/imamat/article-abstract/28/3/287/660860"},
        ],
        "nonclaims": [
            "priority or novelty for the classical Neumann solution",
            "global uniqueness for arbitrary non-similar Stefan data",
            "a finite-interface solution at zero superheat, zero diffusivity, or zero latent heat without the required rescaling",
            "the Lambert-W endpoint is an exact closed form for lambda (it is an asymptotic enclosure)",
            "the source heat clock is a target continuation/divisor/counting law and it is not an A3 analytic match",
            "any target prime/zero law, Euler factor, root number, automorphy, functional equation, Hilbert-Polya operator, or Route-B authorization",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(os.environ.get("C226_OUTPUT", DEFAULT_OUTPUT)))
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    data = json.loads(args.output.read_text())
    print(json.dumps({"status": "C226_PRODUCER_PASS", "case_count": data["regression"]["case_count"], "payload_sha256": data["payload_sha256"], "output": str(args.output)}, sort_keys=True))


if __name__ == "__main__":
    main()
