#!/usr/bin/env python3
"""Produce the deterministic exact C208 linear birth--death certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import comb
from pathlib import Path


SOURCE_COMMIT = "d108ef46fea7a8f62490a69071a83fcbda7c113b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c208_branching_evidence.json"
MAX_INITIAL = 4
MAX_STATE = 12


CASE_SPECS = [
    ("super_2_1_delta_1_2", "off_critical", F(2), F(1), F(1, 2), "finite positive time"),
    ("super_3_1_delta_1_4", "off_critical", F(3), F(1), F(1, 4), "finite positive time"),
    ("sub_1_2_delta_2", "off_critical", F(1), F(2), F(2), "finite positive time"),
    ("sub_1_3_delta_4", "off_critical", F(1), F(3), F(4), "finite positive time"),
    ("pure_birth_1_0_delta_1_3", "off_critical", F(1), F(0), F(1, 3), "finite positive time"),
    ("pure_death_0_1_delta_2", "off_critical", F(0), F(1), F(2), "finite positive time"),
    ("super_time_zero_2_1", "off_critical", F(2), F(1), F(1), "t=0"),
    ("sub_time_zero_1_2", "off_critical", F(1), F(2), F(1), "t=0"),
    ("critical_half_tau_half", "critical", F(1, 2), F(1, 2), F(1, 2), "finite positive time"),
    ("critical_one_tau_one", "critical", F(1), F(1), F(1), "finite positive time"),
    ("critical_two_tau_two", "critical", F(2), F(2), F(2), "finite positive time"),
    ("critical_time_zero", "critical", F(1), F(1), F(0), "t=0"),
    ("zero_rates_all_times", "zero_rates", F(0), F(0), F(0), "arbitrary t>=0"),
]

SEMIGROUP_SPECS = [
    ("super_2_1", "off_critical", F(2), F(1), F(1, 2), F(1, 4)),
    ("super_3_1", "off_critical", F(3), F(1), F(1, 2), F(1, 3)),
    ("sub_1_2", "off_critical", F(1), F(2), F(2), F(3)),
    ("sub_1_3", "off_critical", F(1), F(3), F(2), F(4)),
    ("pure_birth", "off_critical", F(1), F(0), F(1, 2), F(1, 3)),
    ("pure_death", "off_critical", F(0), F(1), F(2), F(3)),
    ("critical_small", "critical", F(1), F(1), F(1, 2), F(1, 3)),
    ("critical_large", "critical", F(2), F(2), F(1), F(2)),
    ("zero_rates", "zero_rates", F(0), F(0), F(0), F(0)),
]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def q(value: F) -> str:
    return str(value)


def pgf_parameters(mode: str, lam: F, mu: F, coordinate: F) -> tuple[F, F]:
    if mode == "off_critical":
        delta = coordinate
        denominator = lam - mu * delta
        if denominator == 0:
            raise AssertionError("inadmissible off-critical coordinate")
        return mu * (1 - delta) / denominator, lam * (1 - delta) / denominator
    if mode == "critical":
        tau = coordinate
        return tau / (1 + tau), tau / (1 + tau)
    if mode == "zero_rates":
        return F(0), F(0)
    raise AssertionError(mode)


def mobius_coefficients(p0: F, beta: F) -> tuple[F, F, F, F]:
    """Return (a,b,c,d) for F(s)=(a+b*s)/(c+d*s), normalized by c=1."""
    return p0, 1 - p0 - beta, F(1), -beta


def compose(left: tuple[F, F, F, F], right: tuple[F, F, F, F]) -> tuple[F, F, F, F]:
    """Coefficients of left(right(s)), normalized to denominator constant one."""
    a1, b1, c1, d1 = left
    a2, b2, c2, d2 = right
    numerator_constant = a1 * c2 + b1 * a2
    numerator_linear = a1 * d2 + b1 * b2
    denominator_constant = c1 * c2 + d1 * a2
    denominator_linear = c1 * d2 + d1 * b2
    return (
        numerator_constant / denominator_constant,
        numerator_linear / denominator_constant,
        F(1),
        denominator_linear / denominator_constant,
    )


def one_ancestor_probability(n: int, p0: F, beta: F) -> F:
    if n == 0:
        return p0
    return (1 - p0) * (1 - beta) * beta ** (n - 1)


def survivor_weight(z: int, k: int, p0: F) -> F:
    return F(comb(z, k)) * (1 - p0) ** k * p0 ** (z - k)


def transition_probability(z: int, n: int, p0: F, beta: F) -> F:
    if z == 0:
        return F(int(n == 0))
    if n == 0:
        return p0 ** z
    answer = F(0)
    for k in range(1, min(z, n) + 1):
        answer += (
            survivor_weight(z, k, p0)
            * F(comb(n - 1, k - 1))
            * (1 - beta) ** k
            * beta ** (n - k)
        )
    return answer


def moments(z: int, p0: F, beta: F) -> tuple[F, F]:
    mean_one = (1 - p0) / (1 - beta)
    second_one = (1 - p0) * (1 + beta) / (1 - beta) ** 2
    variance_one = second_one - mean_one ** 2
    return F(z) * mean_one, F(z) * variance_one


def build_case(spec) -> dict:
    case_id, mode, lam, mu, coordinate, time_descriptor = spec
    p0, beta = pgf_parameters(mode, lam, mu, coordinate)
    assert 0 <= p0 <= 1 and 0 <= beta < 1
    coeff = mobius_coefficients(p0, beta)
    population_rows = []
    for z in range(MAX_INITIAL + 1):
        probabilities = [transition_probability(z, n, p0, beta) for n in range(MAX_STATE + 1)]
        mean, variance = moments(z, p0, beta)
        population_rows.append({
            "initial_population": z,
            "survivor_weights_k_0_to_z": [q(survivor_weight(z, k, p0)) for k in range(z + 1)],
            "transition_probabilities_n_0_to_12": [q(value) for value in probabilities],
            "prefix_probability_n_0_to_12": q(sum(probabilities)),
            "tail_probability_after_12": q(1 - sum(probabilities)),
            "mean": q(mean),
            "variance": q(variance),
            "transition_structure": "binomial surviving lineages mixed with conditional negative-binomial sums",
        })
    one_probabilities = [one_ancestor_probability(n, p0, beta) for n in range(MAX_STATE + 1)]
    coordinate_name = "delta=exp(-(lambda-mu)t)" if mode == "off_critical" else "tau=lambda*t"
    if mode == "zero_rates":
        coordinate_name = "tau=lambda*t=0 for every t"
    return {
        "case_id": case_id,
        "regime": mode,
        "lambda": q(lam),
        "mu": q(mu),
        "clock_coordinate_name": coordinate_name,
        "clock_coordinate": q(coordinate),
        "time_descriptor": time_descriptor,
        "p0": q(p0),
        "beta": q(beta),
        "mobius_coefficients_a_b_c_d": [q(value) for value in coeff],
        "mobius_determinant_bc_minus_ad": q(coeff[1] * coeff[2] - coeff[0] * coeff[3]),
        "one_ancestor_probabilities_n_0_to_12": [q(value) for value in one_probabilities],
        "one_ancestor_prefix_probability_n_0_to_12": q(sum(one_probabilities)),
        "population_rows": population_rows,
    }


def build_semigroup(spec) -> dict:
    case_id, mode, lam, mu, first, second = spec
    target = first * second if mode == "off_critical" else first + second
    left = mobius_coefficients(*pgf_parameters(mode, lam, mu, first))
    right = mobius_coefficients(*pgf_parameters(mode, lam, mu, second))
    combined = compose(left, right)
    expected = mobius_coefficients(*pgf_parameters(mode, lam, mu, target))
    assert combined == expected
    coordinate_rule = "multiplication" if mode == "off_critical" else "addition"
    if mode == "zero_rates":
        coordinate_rule = "identity"
    return {
        "case_id": case_id,
        "regime": mode,
        "lambda": q(lam),
        "mu": q(mu),
        "first_coordinate": q(first),
        "second_coordinate": q(second),
        "combined_coordinate": q(target),
        "coordinate_rule": coordinate_rule,
        "composed_coefficients_a_b_c_d": [q(value) for value in combined],
        "target_coefficients_a_b_c_d": [q(value) for value in expected],
        "four_coefficient_residuals_zero": True,
    }


def build() -> dict:
    cases = [build_case(spec) for spec in CASE_SPECS]
    semigroup = [build_semigroup(spec) for spec in SEMIGROUP_SPECS]
    case_count = len(cases)
    transition_count = case_count * (MAX_INITIAL + 1) * (MAX_STATE + 1)
    survivor_count = case_count * sum(z + 1 for z in range(MAX_INITIAL + 1))
    moment_count = case_count * (MAX_INITIAL + 1) * 2
    one_ancestor_parameter_count = case_count * 2
    semigroup_count = len(semigroup) * 4
    data = {
        "schema": "hcs-c208-linear-birth-death-v1",
        "candidate_id": "HCS-C208",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": (
            "The linear birth--death branching process has an all-parameter Mobius PGF semigroup, "
            "exact survivor-mixture transitions, and a three-regime limit atlas"
        ),
        "frozen_object": {
            "process": "continuous-time Markov branching chain Z on nonnegative integers",
            "generator": "Gf(n)=lambda*n[f(n+1)-f(n)]+mu*n[f(n-1)-f(n)]",
            "parameters": "lambda>=0, mu>=0, initial z in nonnegative integers, t>=0",
            "clock": "physical continuous time; delta=exp(-(lambda-mu)t) off criticality and tau=lambda*t at criticality",
            "normalization": "one initial particle has PGF F_t(s); z particles have PGF F_t(s)^z",
            "determinant_convention": "none; the probability generating function is not called a zeta or determinant",
            "allowed_data": "exact rational delta or tau sentinels and source-local branching algebra",
            "forbidden_data": "prime tables, target zeros, fitted arithmetic or population observations",
        },
        "theorem": {
            "backward_equation": "d_t F=(F-1)(lambda*F-mu), F_0(s)=s",
            "off_critical_mobius": "F=[mu(1-s)-delta(mu-lambda*s)]/[lambda(1-s)-delta(mu-lambda*s)]",
            "critical_mobius": "F=[tau+(1-tau)s]/[1+tau-tau*s]",
            "semigroup": "F_t o F_u=F_(t+u); delta multiplies and tau adds",
            "one_ancestor_law": "P(0)=p0; P(n)=(1-p0)(1-beta)beta^(n-1), n>=1",
            "off_critical_parameters": "p0=mu(1-delta)/(lambda-mu*delta), beta=lambda(1-delta)/(lambda-mu*delta)",
            "critical_parameters": "p0=beta=tau/(1+tau)",
            "arbitrary_z_transition": "P_z(0)=p0^z; for n>=1 sum_k binom(z,k)p0^(z-k)(1-p0)^k binom(n-1,k-1)(1-beta)^k beta^(n-k)",
            "mixture_warning": "the all-parameter family is a binomial-survivor mixture, not uniformly one negative-binomial law; special parameters can collapse the mixture",
            "mean": "z*exp((lambda-mu)t)",
            "variance_off_critical": "z*(lambda+mu)/(lambda-mu)*exp((lambda-mu)t)*(exp((lambda-mu)t)-1)",
            "variance_critical": "2*z*lambda*t",
            "subcritical_qsd": "given survival, Z_t converges to geometric success 1-lambda/mu on {1,2,...}",
            "subcritical_qsd_invariance": "for rho=lambda/mu and g(s)=(1-rho)s/(1-rho*s), [g(F_t(s))-g(F_t(0))]/[1-g(F_t(0))]=g(s)",
            "critical_yaglom": "for lambda=mu>0, Z_t/(lambda*t) given survival converges to Exp(rate 1)",
            "supercritical_limit": "delta*Z_t converges; K~Binomial(z,(lambda-mu)/lambda), and conditional on K=k>=1 the limit is Gamma(k,rate (lambda-mu)/lambda)",
            "boundary_ledger": "z=0 and zero rates are absorbing identities; t=0 is identity; pure birth and pure death are included; criticality uses tau",
        },
        "asymptotics": {
            "proof_status": "symbolic limits proved separately from the finite exact regression",
            "subcritical_conditional_pgf_limit": "(1-lambda/mu)*s/(1-(lambda/mu)*s)",
            "critical_scaled_laplace_limit": "1/(1+theta)",
            "supercritical_one_ancestor_laplace_limit": "mu/lambda+(lambda-mu)^2/[lambda*(lambda-mu+lambda*theta)]",
            "supercritical_z_ancestor_laplace_limit": "the z-th power of the one-ancestor transform",
            "supercritical_atom_at_zero": "(mu/lambda)^z",
            "supercritical_conditional_components": "Gamma(k,rate (lambda-mu)/lambda), mixed by K conditional on K>=1",
        },
        "regression": {
            "maximum_initial_population": MAX_INITIAL,
            "maximum_reported_state": MAX_STATE,
            "parameter_cases": cases,
            "semigroup_cases": semigroup,
        },
        "summary": {
            "parameter_case_count": case_count,
            "semigroup_case_count": len(semigroup),
            "population_row_count": case_count * (MAX_INITIAL + 1),
            "transition_probability_count": transition_count,
            "survivor_weight_count": survivor_count,
            "moment_identity_count": moment_count,
            "one_ancestor_parameter_identity_count": one_ancestor_parameter_count,
            "semigroup_coefficient_identity_count": semigroup_count,
            "exact_scalar_identity_count": transition_count + survivor_count + moment_count + one_ancestor_parameter_count + semigroup_count,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "The source has an exact Markov composition law, branching decomposition, martingale scaling and complete extinction/survival atlas.",
            "strongest_failure": "It has no intrinsic rational-prime carrier, deterministic primitive-orbit owner, target determinant, analytic target match or same-clock self-adjoint quantization.",
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
            {
                "key": "KarlinMcGregor1958",
                "claim": "classical linear growth, birth and death source lock",
                "title": "Linear Growth, Birth and Death Processes",
                "authors": "S. Karlin and J. McGregor",
                "report_number": "KAR ONR 3",
                "date": "January 1958",
                "url": "https://statistics.stanford.edu/technical-reports/linear-growth-birth-and-death-processes",
                "persistent_url": "https://purl.stanford.edu/fx071vs8733",
            }
        ],
        "nonclaims": [
            "priority for the linear birth--death process, its branching law, or its limit theorems",
            "that a finite rational regression proves the all-parameter theorem",
            "that the PGF is a dynamical zeta, determinant, or arithmetic generating object",
            "that the arbitrary-z transition is a single negative-binomial law when extinction mixing is present",
            "population-data inference, prime or target-zero data, arithmetic local data, Euler factors, root numbers, automorphy, a target functional equation, a Hilbert--Polya operator, external review, acceptance score, or Route-B authorization",
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
        "status": "C208_PRODUCER_PASS",
        "cases": data["summary"]["parameter_case_count"],
        "semigroup_cases": data["summary"]["semigroup_case_count"],
        "exact_identities": data["summary"]["exact_scalar_identity_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
