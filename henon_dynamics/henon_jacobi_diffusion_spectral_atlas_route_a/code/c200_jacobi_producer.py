#!/usr/bin/env python3
"""Produce the deterministic exact C200 Jacobi-diffusion certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c200_jacobi_evidence.json"
PARAMETERS = [F(1, 2), F(1), F(3, 2)]
MAX_DEGREE = 8


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def boundary(value: F) -> str:
    return "regular_reflecting" if value < 1 else "entrance"


def eigenvalue(n: int, alpha: F, beta: F) -> F:
    return F(n) * (F(n - 1) + alpha + beta)


def lower(n: int, alpha: F) -> F:
    return F(n) * (F(n - 1) + alpha)


def monic_eigenpolynomial(n: int, alpha: F, beta: F) -> list[F]:
    if n == 0:
        return [F(1)]
    coefficients = [F(0) for _ in range(n + 1)]
    coefficients[n] = F(1)
    top = eigenvalue(n, alpha, beta)
    for j in range(n - 1, -1, -1):
        coefficients[j] = -coefficients[j + 1] * lower(j + 1, alpha) / (
            top - eigenvalue(j, alpha, beta)
        )
    return coefficients


def apply_generator(coefficients: list[F], alpha: F, beta: F) -> list[F]:
    out = [F(0) for _ in coefficients]
    for k, coefficient in enumerate(coefficients):
        out[k] -= coefficient * eigenvalue(k, alpha, beta)
        if k:
            out[k - 1] += coefficient * lower(k, alpha)
    return out


def stationary_moment(k: int, alpha: F, beta: F) -> F:
    value = F(1)
    for j in range(k):
        value *= (alpha + j) / (alpha + beta + j)
    return value


def matrices(alpha: F, beta: F) -> tuple[list[list[F]], list[list[F]]]:
    size = MAX_DEGREE + 1
    generator = [[F(0) for _ in range(size)] for _ in range(size)]
    gram = [[stationary_moment(i + j, alpha, beta) for j in range(size)] for i in range(size)]
    for k in range(size):
        generator[k][k] = -eigenvalue(k, alpha, beta)
        if k:
            generator[k - 1][k] = lower(k, alpha)
    return generator, gram


def multiply(left: list[list[F]], right: list[list[F]]) -> list[list[F]]:
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def transpose(matrix: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*matrix)]


def build() -> dict:
    cases = []
    coefficient_identities = 0
    moment_identities = 0
    gram_identities = 0
    for alpha in PARAMETERS:
        for beta in PARAMETERS:
            polynomial_rows = []
            for n in range(MAX_DEGREE + 1):
                coefficients = monic_eigenpolynomial(n, alpha, beta)
                residual = apply_generator(coefficients, alpha, beta)
                lam = eigenvalue(n, alpha, beta)
                residual = [residual[j] + lam * coefficients[j] for j in range(n + 1)]
                assert all(value == 0 for value in residual)
                coefficient_identities += len(residual)
                polynomial_rows.append({
                    "degree": n,
                    "eigenvalue": str(lam),
                    "coefficients_ascending": [str(value) for value in coefficients],
                    "ode_residual_zero": True,
                })
            moments = [stationary_moment(k, alpha, beta) for k in range(MAX_DEGREE + 1)]
            for k in range(1, MAX_DEGREE + 1):
                assert lower(k, alpha) * moments[k - 1] == eigenvalue(k, alpha, beta) * moments[k]
                moment_identities += 1
            generator, gram = matrices(alpha, beta)
            left = multiply(gram, generator)
            right = multiply(transpose(generator), gram)
            assert left == right
            gram_identities += len(left) * len(left)
            cases.append({
                "case_id": f"alpha_{alpha}_beta_{beta}",
                "alpha": str(alpha),
                "beta": str(beta),
                "left_boundary": boundary(alpha),
                "right_boundary": boundary(beta),
                "stationary_moments_0_to_8": [str(value) for value in moments],
                "polynomial_rows": polynomial_rows,
                "gram_generator_symmetry_zero": True,
            })

    data = {
        "schema": "hcs-c200-jacobi-v1",
        "candidate_id": "HCS-C200",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": (
            "Every positive-mutation canonical Jacobi diffusion has an exact "
            "boundary atlas, Beta-reversible Jacobi spectrum, heat determinant, "
            "and closed moment hierarchy"
        ),
        "frozen_object": {
            "sde": "dX=[alpha-(alpha+beta)X]dt+sqrt(2X(1-X))dW",
            "generator": "L=x(1-x)d2+[alpha-(alpha+beta)x]d",
            "parameters": "alpha>0, beta>0",
            "realization": "canonical conservative no-flux Jacobi diffusion on [0,1]",
            "clock": "physical diffusion time t; twice the common one-half Wright-Fisher convention",
            "normalization": "Beta(alpha,beta) probability and full L2(pi) semigroup",
            "determinant_convention": "D_t(z)=det_L2(pi)(I-z P_t), t>0",
            "allowed_data": "exact rational mutation sentinels and source-local polynomial algebra",
            "forbidden_data": "prime tables, target zeros, fitted arithmetic or biological observations",
        },
        "theorem": {
            "scale_density": "x^(-alpha)(1-x)^(-beta)",
            "speed_and_invariant_density": "x^(alpha-1)(1-x)^(beta-1)/B(alpha,beta)",
            "boundary_at_zero": "regular reflecting for 0<alpha<1; entrance for alpha>=1",
            "boundary_at_one": "regular reflecting for 0<beta<1; entrance for beta>=1",
            "divergence_form": "L f=pi^(-1) d/dx[x(1-x)pi f']",
            "eigenbasis": "P_n^(beta-1,alpha-1)(2x-1)",
            "eigenvalues": "-n(n+alpha+beta-1)",
            "spectral_gap": "alpha+beta",
            "heat_kernel": "k_t(x,y)=sum_n exp(-n(n+alpha+beta-1)t) phi_n(x)phi_n(y) relative to pi",
            "trace_class_determinant": "prod_n>=0 [1-z exp(-n(n+alpha+beta-1)t)]",
            "moment_closure": "m_k'=k(k+alpha-1)m_(k-1)-k(k+alpha+beta-1)m_k",
            "stationary_moments": "(alpha)_k/(alpha+beta)_k",
            "semigroup_periodicity": "P_T f=f in L2(pi), T>0, implies f is constant",
            "path_recurrence": "the irreducible positive-recurrent sample process revisits interior neighborhoods; this is not semigroup periodicity",
        },
        "regression": {
            "maximum_degree": MAX_DEGREE,
            "parameter_cases": cases,
        },
        "summary": {
            "parameter_case_count": len(cases),
            "boundary_decision_count": 2 * len(cases),
            "eigenpolynomial_count": len(cases) * (MAX_DEGREE + 1),
            "coefficient_identity_count": coefficient_identities,
            "moment_identity_count": moment_identities,
            "gram_symmetry_identity_count": gram_identities,
            "exact_scalar_identity_count": coefficient_identities + moment_identities + gram_identities,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "The conservative diffusion has a canonical reversible self-adjoint realization and a complete source-local trace-class semigroup spectrum.",
            "strongest_failure": "There is no intrinsic rational-prime carrier, deterministic primitive-orbit owner, target determinant, or same-clock quantization.",
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
            {"key": "EpsteinMazzeo2010", "claim": "canonical zero-flux Wright-Fisher semigroups", "doi": "10.1137/090766152"},
            {"key": "SongSteinrucken2012", "claim": "Beta weight and Jacobi spectral representation in the one-half clock", "doi": "10.1534/genetics.111.136929"},
            {"key": "Griffiths1979", "claim": "neutral Wright-Fisher transition-density expansion", "doi": "10.2307/1426842"},
        ],
        "nonclaims": [
            "priority for the Jacobi diffusion, Wright-Fisher model, Jacobi polynomials, or their spectral expansion",
            "absence of probabilistic sample-path recurrence",
            "uniqueness of a Markov realization from the interior differential expression without the no-flux source lock",
            "that finite exact regression proves the continuum-parameter theorem",
            "a rational-prime orbit law, target divisor, Hilbert--Polya operator, external review, acceptance score, or Route-B authorization",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C200_PRODUCER_PASS",
        "cases": data["summary"]["parameter_case_count"],
        "exact_identities": data["summary"]["exact_scalar_identity_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
