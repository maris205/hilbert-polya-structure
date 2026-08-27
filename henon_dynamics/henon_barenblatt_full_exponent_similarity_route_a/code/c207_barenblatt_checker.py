#!/usr/bin/env python3
"""Producer-independent exact/high-precision checker for HCS-C207."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c207_barenblatt_evidence.json"
SOURCE_COMMIT = "d108ef46fea7a8f62490a69071a83fcbda7c113b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
MS = [F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(1), F(3, 2), F(2), F(3), F(5)]
MASSES = [F(1), F(3, 2)]
ZS = [F(0), F(1, 2), F(1), F(3, 2), F(2)]
RS = [F(0), F(1), F(2), F(3), F(4), F(5)]
DECIMAL_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)\.[0-9]+$")

FROZEN_OBJECT = {
    "equation": "u_t=(u^m)_xx on R with m>0 and mass M>0",
    "similarity": "u(x,t)=t^(-alpha)F(x t^(-alpha)), alpha=1/(m+1)",
    "profile_class": "centered nonnegative integrable first-kind profiles of mass M with F^m locally absolutely continuous and (F^m)'+alpha*xi*F=0 almost everywhere; uniqueness is up to almost-everywhere equality",
    "clock": "physical diffusion time t>0; tau=log t only for the explicitly declared rescaled flow",
    "normalization": "mass integral equals M; translations are excluded by centered normalization",
}
THEOREM = {
    "porous": "for m>1, F=(C-k_m xi^2)_+^(1/(m-1)), k_m=(m-1)/(2m(m+1)), with compact support",
    "heat": "for m=1, F=M exp(-xi^2/4)/(2 sqrt(pi))",
    "fast": "for 0<m<1, F=(C+b_m xi^2)^(-1/(1-m)), b_m=(1-m)/(2m(m+1)), with algebraic tail",
    "mass": "C is uniquely fixed by the exact Beta integrals recorded in the theorem package",
    "moments": "all porous and Gaussian absolute moments are finite; in fast diffusion the r-th absolute moment is finite exactly when r<(1+m)/(1-m), logarithmically divergent at equality",
    "second_moment": "the fast-diffusion second moment is finite exactly for m>1/3; m=1/3 is logarithmically divergent",
    "uniqueness": "uniqueness is only among centered nonnegative integrable zero-flux first-kind similarity profiles of mass M with F^m locally absolutely continuous and the integrated profile law holding almost everywhere, up to almost-everywhere equality; it is not uniqueness among arbitrary Cauchy solutions",
    "pressure": "for m>1, P=m u^(m-1)/(m-1) is parabolic on support, X_+/-=+/-R_M t^alpha, and each one-sided interface satisfies X_+/-'=alpha X_+/-/t=-lim_inside P_x",
    "rescaled": "v_tau=(v^m)_(xi xi)+alpha(xi v)_xi and each mass-M Barenblatt profile is stationary",
    "free_energy": "F_m[v]=integral[v^m/(m-1)+alpha*xi^2*v/2] for m!=1 and F_1[v]=integral[v*log(v)-v+alpha*xi^2*v/2]",
    "dissipation": "for sufficiently regular positive rescaled solutions with finite displayed free energy (no infinity-minus-infinity) and justified boundary decay, dF_m/dtau=-integral v |partial_xi chemical_potential|^2; this is not asserted outside that class, and the unrenormalized Barenblatt free-energy/second-moment boundary is m>1/3 in fast diffusion",
}
ROUTE_A = {
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
    "overall": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "strongest_positive": "The nonlinear diffusion has a source-native mass-preserving similarity flow and exact gradient-flow dissipation in its stated finite-energy class.",
    "strongest_failure": "The flow is dissipative and supplies no rational-prime primitive owner, periodic ledger, target determinant, or same-clock unitary lift.",
}
SCOPE_FLAGS = {
    "uses_target_zero_table": False,
    "uses_prime_table": False,
    "claims_arithmetic_local_data": False,
    "claims_euler_factors": False,
    "claims_root_numbers": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_functional_equation": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
CITATIONS = [
    {"key": "Barenblatt1952", "claim": "classical source-type porous-medium solution", "reference": "G. I. Barenblatt, Prikl. Mat. Mekh. 16 (1952), 67-78"},
    {"key": "Vazquez2007", "claim": "porous-medium and fast-diffusion mathematical framework and source ownership", "doi": "10.1093/acprof:oso/9780198569039.001.0001"},
]
NONCLAIMS = [
    "priority for the porous-medium equation, Barenblatt profiles, fast diffusion, or Wasserstein gradient flow",
    "classification of arbitrary Cauchy solutions, signed profiles, non-centered profiles, or higher dimensions",
    "that finite rational-exponent regression proves the all-m theorem",
    "free-energy dissipation without regularity, integrability, and boundary-decay hypotheses",
    "a prime-orbit law, arithmetic local datum, Euler factor, root number, automorphy, target divisor, or Hilbert--Polya operator",
    "external peer review, literature exhaustiveness, novelty certification, or an acceptance score",
]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    blob = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(blob).hexdigest()


def mpq(value: F | str) -> mp.mpf:
    q = F(value)
    return mp.mpf(q.numerator) / q.denominator


def fmt82(value: mp.mpf) -> str:
    return mp.nstr(value, 82, strip_zeros=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text())
    mp.mp.dps = 140
    assertions = 0
    serialized_fields = 0
    serialized_nonzero_fields = 0

    def check(condition: bool, label: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(label)

    def keys(obj: object, expected: set[str], label: str) -> None:
        check(type(obj) is dict, label + " type")
        check(set(obj) == expected, label + " keys")

    def exact_tree(actual: object, expected: object, label: str) -> None:
        check(type(actual) is type(expected), label + " type")
        if type(expected) is dict:
            keys(actual, set(expected), label)
            for key, value in expected.items():
                exact_tree(actual[key], value, f"{label}.{key}")
        elif type(expected) is list:
            check(len(actual) == len(expected), label + " length")
            for index, value in enumerate(expected):
                exact_tree(actual[index], value, f"{label}[{index}]")
        else:
            check(actual == expected, label + " value")

    def decimal82(actual: object, expected: mp.mpf, label: str) -> None:
        nonlocal serialized_fields, serialized_nonzero_fields
        serialized_fields += 1
        check(type(actual) is str, label + " type")
        check(DECIMAL_RE.fullmatch(actual) is not None, label + " decimal syntax")
        if mp.mpf(actual) == 0:
            check(actual == "0.0", label + " canonical zero")
        else:
            serialized_nonzero_fields += 1
            digits = actual.lstrip("-").replace(".", "").lstrip("0")
            check(len(digits) == 82, label + " 82 significant digits")
        check(actual == fmt82(expected), label + " reconstructed serialization")

    top = {"schema", "candidate_id", "evaluation_date", "source_commit",
           "scope_literal", "evaluator", "headline", "frozen_object",
           "theorem", "regression", "summary", "route_a", "scope_flags",
           "citations", "nonclaims", "payload_sha256"}
    keys(data, top, "top")
    exact_tree(data["evaluator"], {
        "path": "flow_systems/skills/route-a-evaluator.md",
        "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    exact_tree(data["frozen_object"], FROZEN_OBJECT, "frozen_object")
    exact_tree(data["theorem"], THEOREM, "theorem")
    exact_tree(data["route_a"], ROUTE_A, "route_a")
    exact_tree(data["scope_flags"], SCOPE_FLAGS, "scope_flags")
    exact_tree(data["citations"], CITATIONS, "citations")
    exact_tree(data["nonclaims"], NONCLAIMS, "nonclaims")
    exact_tree(data["summary"], {
        "m_values": 9, "mass_values": 2, "profiles": 18,
        "profile_samples": 90, "moment_cells": 108,
        "working_decimal_digits": 100,
        "serialized_significant_digits": 82}, "summary")
    check(data["schema"] == "hcs-c207-barenblatt-v1", "schema")
    check(data["candidate_id"] == "HCS-C207", "candidate")
    check(data["evaluation_date"] == "2026-08-27", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["headline"] == "All one-dimensional positive exponents admit a single mass-normalized Barenblatt similarity atlas with exact compact, Gaussian, algebraic-tail, moment, pressure, and rescaled-dissipation boundaries", "headline")
    check(type(data["payload_sha256"]) is str and re.fullmatch(r"[0-9a-f]{64}", data["payload_sha256"]) is not None, "payload syntax")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    keys(data["regression"], {"profiles"}, "regression")
    profiles = data["regression"]["profiles"]
    check(type(profiles) is list and len(profiles) == 18, "profile list")

    expected_pairs = [(m_q, mass_q) for m_q in MS for mass_q in MASSES]
    seen_cases: set[str] = set()
    sample_count = moment_count = porous_count = heat_count = fast_count = 0
    for index, (row, expected_pair) in enumerate(zip(profiles, expected_pairs)):
        keys(row, {"case_id", "m", "mass", "regime", "derived", "samples", "moments"}, f"profile {index}")
        m_q, mass_q = expected_pair
        check(type(row["case_id"]) is str and row["case_id"] == f"m{m_q}_M{mass_q}", f"profile {index} case_id")
        check(row["case_id"] not in seen_cases, f"profile {index} unique case_id")
        seen_cases.add(row["case_id"])
        check(type(row["m"]) is str and row["m"] == str(m_q), f"profile {index} m grid")
        check(type(row["mass"]) is str and row["mass"] == str(mass_q), f"profile {index} mass grid")
        m, mass = mpq(m_q), mpq(mass_q)
        alpha_q = F(1) / (m_q + 1)
        alpha = mpq(alpha_q)
        keys(row["derived"], {"alpha", "shape_exponent", "quadratic_coefficient", "C", "mass_beta", "mass_reconstructed", "support_radius_at_t1", "free_boundary_speed_at_t1", "chemical_constant", "tail_power", "moment_threshold"}, f"derived {index}")
        derived = row["derived"]
        check(derived["alpha"] == str(alpha_q), f"derived {index} alpha")
        check(type(row["samples"]) is list and len(row["samples"]) == len(ZS), f"profile {index} sample length")
        check(type(row["moments"]) is list and len(row["moments"]) == len(RS), f"profile {index} moment length")

        if m_q > 1:
            porous_count += 1
            check(row["regime"] == "porous_compact", f"profile {index} porous regime")
            p_q = F(1) / (m_q - 1)
            k_q = (m_q - 1) / (2 * m_q * (m_q + 1))
            p, k = mpq(p_q), mpq(k_q)
            beta = mp.beta(mp.mpf("0.5"), p + 1)
            constant = (mass * mp.sqrt(k) / beta)**(1 / (p + mp.mpf("0.5")))
            radius = mp.sqrt(constant / k)
            chemical = m / (m - 1) * constant
            exact_tree({"shape_exponent": derived["shape_exponent"],
                        "quadratic_coefficient": derived["quadratic_coefficient"],
                        "tail_power": derived["tail_power"],
                        "moment_threshold": derived["moment_threshold"]},
                       {"shape_exponent": str(p_q),
                        "quadratic_coefficient": str(k_q),
                        "tail_power": None, "moment_threshold": None},
                       f"derived {index} porous exact/null")
            decimal82(derived["mass_beta"], beta, f"derived {index} mass_beta")
            decimal82(derived["support_radius_at_t1"], radius, f"derived {index} radius")
            decimal82(derived["free_boundary_speed_at_t1"], alpha * radius, f"derived {index} speed")
            scale = radius

            def profile_at(z: mp.mpf) -> mp.mpf:
                return constant**p * (1 - z*z)**p if z < 1 else mp.mpf("0")

            def finite_moment(r: mp.mpf) -> mp.mpf:
                return constant**(p + (r + 1) / 2) * k**(-(r + 1) / 2) * mp.beta((r + 1) / 2, p + 1)

        elif m_q < 1:
            fast_count += 1
            check(row["regime"] == "fast_algebraic", f"profile {index} fast regime")
            q_q = F(1) / (1 - m_q)
            b_q = (1 - m_q) / (2 * m_q * (m_q + 1))
            threshold_q = (1 + m_q) / (1 - m_q)
            q, b = mpq(q_q), mpq(b_q)
            beta = mp.beta(mp.mpf("0.5"), q - mp.mpf("0.5"))
            constant = (beta / (mass * mp.sqrt(b)))**(1 / (q - mp.mpf("0.5")))
            scale = mp.sqrt(constant / b)
            chemical = m / (m - 1) * constant
            exact_tree({"shape_exponent": derived["shape_exponent"],
                        "quadratic_coefficient": derived["quadratic_coefficient"],
                        "support_radius_at_t1": derived["support_radius_at_t1"],
                        "free_boundary_speed_at_t1": derived["free_boundary_speed_at_t1"],
                        "tail_power": derived["tail_power"],
                        "moment_threshold": derived["moment_threshold"]},
                       {"shape_exponent": str(q_q),
                        "quadratic_coefficient": str(b_q),
                        "support_radius_at_t1": None,
                        "free_boundary_speed_at_t1": None,
                        "tail_power": str(2*q_q),
                        "moment_threshold": str(threshold_q)},
                       f"derived {index} fast exact/null")
            decimal82(derived["mass_beta"], beta, f"derived {index} mass_beta")

            def profile_at(z: mp.mpf) -> mp.mpf:
                return constant**(-q) * (1 + z*z)**(-q)

            def finite_moment(r: mp.mpf) -> mp.mpf:
                return constant**(-q + (r + 1) / 2) * b**(-(r + 1) / 2) * mp.beta((r + 1) / 2, q - (r + 1) / 2)

        else:
            heat_count += 1
            check(row["regime"] == "heat_gaussian", f"profile {index} heat regime")
            constant = mass / (2 * mp.sqrt(mp.pi))
            chemical = mp.log(constant)
            scale = mp.mpf(1)
            exact_tree({"shape_exponent": derived["shape_exponent"],
                        "quadratic_coefficient": derived["quadratic_coefficient"],
                        "mass_beta": derived["mass_beta"],
                        "support_radius_at_t1": derived["support_radius_at_t1"],
                        "free_boundary_speed_at_t1": derived["free_boundary_speed_at_t1"],
                        "tail_power": derived["tail_power"],
                        "moment_threshold": derived["moment_threshold"]},
                       {"shape_exponent": None,
                        "quadratic_coefficient": "1/4", "mass_beta": None,
                        "support_radius_at_t1": None,
                        "free_boundary_speed_at_t1": None,
                        "tail_power": "Gaussian", "moment_threshold": "all"},
                       f"derived {index} heat exact/null")

            def profile_at(z: mp.mpf) -> mp.mpf:
                return constant * mp.e**(-z*z / 4)

            def finite_moment(r: mp.mpf) -> mp.mpf:
                return mass * 2**r * mp.gamma((r + 1) / 2) / mp.sqrt(mp.pi)

        decimal82(derived["C"], constant, f"derived {index} C")
        decimal82(derived["mass_reconstructed"], mass, f"derived {index} reconstructed mass")
        decimal82(derived["chemical_constant"], chemical, f"derived {index} chemical constant")

        seen_z: set[str] = set()
        for sample_index, (sample, z_q) in enumerate(zip(row["samples"], ZS)):
            keys(sample, {"z", "xi", "profile", "inside_support", "chemical_potential"}, f"sample {index}.{sample_index}")
            check(type(sample["z"]) is str and sample["z"] == str(z_q), f"sample {index}.{sample_index} z grid")
            check(sample["z"] not in seen_z, f"sample {index}.{sample_index} unique z")
            seen_z.add(sample["z"])
            z = mpq(z_q)
            decimal82(sample["xi"], z * scale, f"sample {index}.{sample_index} xi")
            decimal82(sample["profile"], profile_at(z), f"sample {index}.{sample_index} profile")
            inside = (z_q <= 1) if m_q > 1 else True
            check(type(sample["inside_support"]) is bool and sample["inside_support"] is inside, f"sample {index}.{sample_index} support")
            if m_q > 1 and z_q > 1:
                check(sample["chemical_potential"] is None, f"sample {index}.{sample_index} porous exterior chemical null")
            else:
                decimal82(sample["chemical_potential"], chemical, f"sample {index}.{sample_index} chemical")
            sample_count += 1

        seen_r: set[str] = set()
        threshold_q = (1 + m_q) / (1 - m_q) if m_q < 1 else None
        for moment_index, (moment, r_q) in enumerate(zip(row["moments"], RS)):
            keys(moment, {"r", "status", "coefficient"}, f"moment {index}.{moment_index}")
            check(type(moment["r"]) is str and moment["r"] == str(r_q), f"moment {index}.{moment_index} r grid")
            check(moment["r"] not in seen_r, f"moment {index}.{moment_index} unique r")
            seen_r.add(moment["r"])
            if m_q < 1 and r_q >= threshold_q:
                expected_status = "logarithmic_divergence" if r_q == threshold_q else "power_divergence"
                exact_tree({"status": moment["status"], "coefficient": moment["coefficient"]},
                           {"status": expected_status, "coefficient": None},
                           f"moment {index}.{moment_index} divergence/null")
            else:
                check(type(moment["status"]) is str and moment["status"] == "finite", f"moment {index}.{moment_index} finite status")
                decimal82(moment["coefficient"], finite_moment(mpq(r_q)), f"moment {index}.{moment_index} coefficient")
            moment_count += 1

    check(len(seen_cases) == 18, "case grid closure")
    check((porous_count, heat_count, fast_count) == (8, 2, 8), "regime populations")
    check((sample_count, moment_count) == (90, 108), "cell totals")
    print(json.dumps({"status": "C207_CHECKER_PASS", "assertions": assertions,
                      "profiles": 18, "profile_samples": sample_count,
                      "moment_cells": moment_count,
                      "working_decimal_digits": 100,
                      "serialized_significant_digits": 82,
                      "serialized_decimal_fields": serialized_fields,
                      "serialized_nonzero_decimal_fields": serialized_nonzero_fields}, sort_keys=True))


if __name__ == "__main__":
    main()
