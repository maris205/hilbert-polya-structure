#!/usr/bin/env python3
"""Deterministic exact and high-precision receipts for HCS-C335."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c335_shot_noise_ou_evidence.json"
SOURCE = "db2c816b7b6bd450f51f79b91842cb882b0bd773"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "7fbc0434474de616b456ac56c3ac69ed858982b10deee22f53e08cb787fb2a42"
EVAL_SEMANTIC = "f635ccc64622b3592891c6e900d48817bb87b17e531f067d3ce07a7b05272bf1"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
PARAMETERS = (
    (Fraction(1), Fraction(1, 2), Fraction(2)),
    (Fraction(1), Fraction(1), Fraction(1)),
    (Fraction(2), Fraction(3), Fraction(3, 2)),
    (Fraction(3, 2), Fraction(1), Fraction(4)),
    (Fraction(2, 3), Fraction(5, 3), Fraction(5, 2)),
)
DECAYS = (Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(3, 4))
LAPLACE_POINTS = (Fraction(1, 4), Fraction(1), Fraction(3))
MAX_DEGREE = 12
mp.mp.dps = 110
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}


def rat(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator)/value.denominator


def dec(value: mp.mpf) -> str:
    return mp.nstr(value, 80, strip_zeros=False, min_fixed=-120, max_fixed=120)


def rising(a: Fraction, n: int) -> Fraction:
    out = Fraction(1)
    for j in range(n):
        out *= a+j
    return out


def generator_row(gamma: Fraction, kappa: Fraction, beta: Fraction, degree: int) -> dict:
    coeffs = [Fraction(0) for _ in range(degree+1)]
    coeffs[degree] = -degree*gamma
    for j in range(degree):
        coeffs[j] = kappa*Fraction(math.factorial(degree), math.factorial(j))*beta**(-(degree-j))
    return {"degree": degree, "coefficients_low_to_high": [rat(v) for v in coeffs], "diagonal": rat(-degree*gamma)}


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C335 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    parameter_rows = []
    transform_rows = []
    semigroup_rows = []
    polynomial_rows = []
    for pid, (gamma, kappa, beta) in enumerate(PARAMETERS, 1):
        alpha = kappa/gamma
        moments = [rising(alpha, n)/beta**n for n in range(MAX_DEGREE+1)]
        cumulants = [alpha*math.factorial(n-1)/beta**n for n in range(1, MAX_DEGREE+1)]
        parameter_rows.append({
            "parameter_id": f"p{pid}", "gamma": rat(gamma), "kappa": rat(kappa),
            "beta": rat(beta), "alpha": rat(alpha),
            "stationary_moments_0_to_12": [rat(v) for v in moments],
            "stationary_cumulants_1_to_12": [rat(v) for v in cumulants],
            "stationary_variance": rat(alpha/beta**2),
        })
        for degree in range(MAX_DEGREE+1):
            row = generator_row(gamma, kappa, beta, degree)
            row["parameter_id"] = f"p{pid}"
            polynomial_rows.append(row)
        for r in DECAYS:
            time = -mp.log(mpq(r))/mpq(gamma)
            for s in LAPLACE_POINTS:
                ss, rr, bb, aa = mpq(s), mpq(r), mpq(beta), mpq(alpha)
                initial = Fraction(pid, 3)
                value = mp.exp(-ss*rr*mpq(initial))*((bb+ss*rr)/(bb+ss))**aa
                transform_rows.append({
                    "parameter_id": f"p{pid}", "decay_factor": rat(r), "laplace_s": rat(s),
                    "initial_x": rat(initial), "time": dec(time), "transition_laplace": dec(value),
                })
        for r1, r2 in ((Fraction(1, 2), Fraction(1, 3)), (Fraction(3, 4), Fraction(1, 5))):
            s = Fraction(pid+1, 3)
            bb, aa, ss = mpq(beta), mpq(alpha), mpq(s)
            one = ((bb+ss*mpq(r1))/(bb+ss))**aa
            two = ((bb+ss*mpq(r1*r2))/(bb+ss*mpq(r1)))**aa
            direct = ((bb+ss*mpq(r1*r2))/(bb+ss))**aa
            semigroup_rows.append({
                "parameter_id": f"p{pid}", "r1": rat(r1), "r2": rat(r2), "laplace_s": rat(s),
                "factor_first": dec(one), "factor_second": dec(two), "factor_direct": dec(direct),
            })

    model = {
        "sde": "dX_t=-gamma X_t dt+dJ_t on [0,infinity)",
        "driver": "J is compound Poisson of rate kappa with independent Exp(beta) marks",
        "positive_parameters": "gamma,kappa,beta>0",
        "generator": "Lf=-gamma x f'(x)+kappa integral beta exp(-beta y)(f(x+y)-f(x))dy",
    }
    theorem = {
        "pathwise_semigroup": "X_t=exp(-gamma t)x+sum_{T_j<=t}exp(-gamma(t-T_j))Y_j",
        "transition_transform": "E_x exp(-sX_t)=exp(-s exp(-gamma t)x)((beta+s exp(-gamma t))/(beta+s))^(kappa/gamma)",
        "stationarity": "the unique invariant probability is Gamma(shape kappa/gamma, rate beta)",
        "coupling": "for every p>=1, W_p(P_t(x,.),P_t(y,.))=exp(-gamma t)|x-y|",
        "stationary_statistics": "moments are (alpha)_n/beta^n, cumulants alpha(n-1)!/beta^n, and covariance is alpha exp(-gamma|t|)/beta^2",
        "polynomial_filtration": "P_m is invariant and the restriction has exactly the simple eigenvalues 0,-gamma,...,-m gamma",
        "spectral_boundary": "the filtration theorem makes no assertion about the full L2 spectrum, completeness, normality, or reversibility",
    }
    boundary = [
        {"face": "kappa=0,gamma>0", "status": "deterministic exponential decay with unique invariant delta_0"},
        {"face": "gamma=0,kappa>0", "status": "compound-Poisson subordinator with no invariant probability"},
        {"face": "gamma=kappa=0", "status": "static process and every initial law is invariant"},
        {"face": "beta=0", "status": "outside the model because an exponential probability law of rate zero does not exist"},
        {"face": "beta to infinity", "status": "a weak zero-jump-size limit, not an included parameter"},
        {"face": "finite filtration", "status": "only each fixed P_m spectrum is claimed, never a full L2 spectrum"},
    ]
    data = {
        "schema": "hcs-c335-shot-noise-ou-v1", "candidate_id": "HCS-C335", "obstruction_id": "HEN-O319",
        "evaluation_date": "2026-09-03", "fixed_epoch": EPOCH, "source_commit": SOURCE, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_lock": {"relative_path": "evaluations/route_a/HCS-C335/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC},
        "model": model, "theorem_contract": theorem,
        "parameter_rows": parameter_rows, "transition_rows": transform_rows,
        "semigroup_rows": semigroup_rows, "polynomial_rows": polynomial_rows,
        "boundary_atlas": boundary,
        "collision_boundary": {
            "C229": "CIR has diffusive square-root noise rather than finite-activity positive jumps",
            "C233": "M/M/infinity is discrete-state immigration-death rather than continuous shot noise",
            "C265": "Hawkes has self-exciting intensity rather than exogenous Poisson arrivals",
            "C328": "run-and-tumble has dichotomous velocities and compact support rather than positive jumps and a Gamma law",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "No priority is claimed for Lévy-driven OU stationarity or exponential shot-noise formulas.",
            "The polynomial filtration is not asserted to exhaust any full L2 spectrum.",
            "Finite grids are regression receipts and do not replace the all-time analytic proof.",
            "No target arithmetic local data, Euler factors, root numbers, automorphy, divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
        ],
        "references": [
            {"url": "https://www.sciencedirect.com/science/article/abs/pii/S0165168498002266", "doi": "10.1016/S0165-1684(98)00226-6", "role": "primary Markov exponential-shot-noise and stationary-Gamma source"},
            {"url": "https://www.sciencedirect.com/science/article/pii/0304414984903120", "doi": "10.1016/0304-4149(84)90312-0", "role": "primary operator-selfdecomposable OU limit-law source"},
            {"url": "https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/1467-9868.00282", "doi": "10.1111/1467-9868.00282", "role": "primary non-Gaussian OU source and modeling boundary"},
        ],
    }
    data["enumeration"] = {
        "parameter_rows": len(parameter_rows), "transition_rows": len(transform_rows),
        "semigroup_rows": len(semigroup_rows), "polynomial_rows": len(polynomial_rows),
        "moment_entries": sum(len(row["stationary_moments_0_to_12"]) for row in parameter_rows),
        "generator_coefficients": sum(len(row["coefficients_low_to_high"]) for row in polynomial_rows),
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data)+1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(f"C335_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
