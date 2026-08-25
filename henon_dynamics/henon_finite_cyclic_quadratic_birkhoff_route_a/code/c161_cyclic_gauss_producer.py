#!/usr/bin/env python3
"""Produce every-iterate quadratic Birkhoff amplitudes for HCS-C161."""
from __future__ import annotations

import argparse
import cmath
from hashlib import sha256
import json
from math import gcd, pi, sqrt
from pathlib import Path


Q_MAX = 31
SOURCE_COMMIT = "63f75cf476711de93e6096ef74ac16969e1127d0"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
REJECTED_UPSTREAM_SHA = "06791bf5734a48d0fe84d0e752e5d156172e637fe9a6a5e29792dfb3b2637b40"


def canonical_hash(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def jacobi(numerator, denominator):
    assert denominator > 0 and denominator % 2 == 1
    numerator %= denominator
    answer = 1
    while numerator:
        while numerator % 2 == 0:
            numerator //= 2
            if denominator % 8 in (3, 5):
                answer = -answer
        numerator, denominator = denominator, numerator
        if numerator % 4 == denominator % 4 == 3:
            answer = -answer
        numerator %= denominator
    return answer if denominator == 1 else 0


def coefficients(a, b, n):
    return (a * n,
            a * n * (n - 1) + b * n,
            a * n * (n - 1) * (2 * n - 1) // 6 + b * n * (n - 1) // 2)


def gauss_descriptor(q, a, b, n):
    quadratic, linear, constant = coefficients(a, b, n)
    divisor = gcd(quadratic, q)
    if linear % divisor:
        return {
            "status": "VANISHING_GCD_OBSTRUCTION", "gcd_A_q": divisor,
            "A_n": quadratic, "B_n": linear, "C_n": constant,
        }
    reduced_modulus = q // divisor
    if reduced_modulus == 1:
        return {
            "status": "CONSTANT_PHASE", "gcd_A_q": divisor,
            "A_n": quadratic, "B_n": linear, "C_n": constant,
            "reduced_modulus": 1, "scale": q, "radical": 1,
            "jacobi_sign": 1, "epsilon": "ONE", "phase_numerator_mod_q": constant % q,
        }
    reduced_a = quadratic // divisor
    reduced_b = linear // divisor
    inverse = pow((4 * reduced_a) % reduced_modulus, -1, reduced_modulus)
    completion = (-inverse * reduced_b * reduced_b) % reduced_modulus
    phase = (constant + divisor * completion) % q
    return {
        "status": "PRIMITIVE_GAUSS_EVALUATION", "gcd_A_q": divisor,
        "A_n": quadratic, "B_n": linear, "C_n": constant,
        "reduced_modulus": reduced_modulus, "reduced_A": reduced_a,
        "reduced_B": reduced_b, "completion_square_residue": completion,
        "scale": divisor, "radical": reduced_modulus,
        "jacobi_sign": jacobi(reduced_a, reduced_modulus),
        "epsilon": "ONE" if reduced_modulus % 4 == 1 else "I",
        "phase_numerator_mod_q": phase,
    }


def descriptor_value(q, descriptor):
    if descriptor["status"] == "VANISHING_GCD_OBSTRUCTION":
        return 0j
    epsilon = 1 if descriptor["epsilon"] == "ONE" else 1j
    phase = cmath.exp(2j * pi * descriptor["phase_numerator_mod_q"] / q)
    return (descriptor["scale"] * descriptor["jacobi_sign"] * epsilon *
            sqrt(descriptor["radical"]) * phase)


def direct_value(q, a, b, n):
    quadratic, linear, constant = coefficients(a, b, n)
    return sum(cmath.exp(2j * pi * ((quadratic * x * x + linear * x + constant) % q) / q)
               for x in range(q))


def is_prime(value):
    return value >= 2 and all(value % divisor for divisor in range(2, int(sqrt(value)) + 1))


def legendre(value, prime):
    value %= prime
    if value == 0:
        return 0
    residue = pow(value, (prime - 1) // 2, prime)
    return 1 if residue == 1 else -1


def prime_zero_count(prime, a, b, n):
    quadratic, linear, constant = (value % prime for value in coefficients(a, b, n))
    if quadratic:
        discriminant = (linear * linear - 4 * quadratic * constant) % prime
        return 1 + legendre(discriminant, prime), discriminant, "QUADRATIC_DISCRIMINANT"
    if linear:
        return 1, None, "LINEAR_UNIQUE_ROOT"
    return (prime if constant == 0 else 0), None, "CONSTANT_LEVEL"


def exhaustive_certificate():
    cases = vanish = nonzero = zero_cases = 0
    maximum_error = 0.0
    for q in range(3, Q_MAX + 1, 2):
        for a in range(q):
            for b in range(q):
                for n in range(1, 2 * q + 1):
                    descriptor = gauss_descriptor(q, a, b, n)
                    direct = direct_value(q, a, b, n)
                    predicted = descriptor_value(q, descriptor)
                    error = abs(direct - predicted)
                    assert error < 3e-10 * q
                    maximum_error = max(maximum_error, error)
                    cases += 1
                    if descriptor["status"] == "VANISHING_GCD_OBSTRUCTION":
                        vanish += 1
                    else:
                        nonzero += 1
                    if is_prime(q):
                        expected, _, _ = prime_zero_count(q, a, b, n)
                        direct_zeros = sum(1 for x in range(q)
                                           if sum((a * ((x + j) % q) ** 2 +
                                                   b * ((x + j) % q)) for j in range(n)) % q == 0)
                        assert expected == direct_zeros
                        zero_cases += 1
    return cases, vanish, nonzero, zero_cases, maximum_error


def build_evidence():
    cases, vanish, nonzero, zero_cases, maximum_error = exhaustive_certificate()
    sentinels = []
    for q, a, b, n in ((9, 1, 0, 1), (9, 3, 1, 1), (9, 3, 0, 1),
                       (9, 1, 0, 9), (15, 2, 3, 4), (21, 5, 2, 7),
                       (25, 5, 0, 3), (27, 4, 8, 18), (31, 7, 11, 13)):
        descriptor = gauss_descriptor(q, a, b, n)
        direct = direct_value(q, a, b, n)
        row = {"q": q, "a": a, "b": b, "n": n, "formula": descriptor,
               "direct_real": format(direct.real, ".17g"),
               "direct_imag": format(direct.imag, ".17g")}
        if is_prime(q):
            count, discriminant, branch = prime_zero_count(q, a, b, n)
            row["prime_zero_level"] = {"count": count, "discriminant_mod_p": discriminant,
                                       "branch": branch}
        sentinels.append(row)
    payload = {
        "schema": "hcs-c161-finite-cyclic-quadratic-birkhoff-evidence-v1",
        "candidate_id": "HCS-C161",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "object": "finite cyclic rotation R_q(x)=x+1 on Z/qZ, q odd, with phi_(a,b)(x)=a*x^2+b*x",
            "clock": "the exact Birkhoff iterate n>=1",
            "normalization": "unscaled complete orbit average numerator sum_(x mod q) exp(2*pi*i*S_n phi(x)/q)",
            "determinant_convention": "none; the object is a finite source dynamical amplitude",
            "cutoff": {"all_parameter_theorem": True, "exhaustive_q_odd_at_most": Q_MAX,
                       "n_at_most_twice_q": True},
            "precision": "exact modular formula; double-complex exhaustive sentinels with a 3e-10*q envelope",
            "training_data": "none",
            "forbidden_data": "target zero/prime tables, target divisors/counting laws, arithmetic local or Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "hard_gate": {
            "required": "a strict all-iterate evaluation rather than another finite Heisenberg table",
            "rejected_candidate": "the C156 Heisenberg all-n local-product draft",
            "rejection_reason": "discriminant evidence did not independently establish uniform quotient coordinates, translation removal, or the 2-adic and 5-adic equivalences",
            "rejected_upstream_evidence_sha256": REJECTED_UPSTREAM_SHA,
            "pivot": "finite cyclic quadratic Birkhoff dynamics",
            "status": "PASS_BY_MODEL_PIVOT",
        },
        "all_iterate_theorem": {
            "birkhoff_polynomial": "for n>=1, S_n phi(x)=A_n*x^2+B_n*x+C_n with A_n=a*n, B_n=a*n(n-1)+b*n, C_n=a*n(n-1)(2n-1)/6+b*n(n-1)/2",
            "vanishing_gate": "d=gcd(A_n,q); the amplitude is zero exactly when d does not divide B_n",
            "nonzero_formula": "if d|B_n and Q=q/d>1: d*(A_n/d|Q)*epsilon_Q*sqrt(Q)*exp(2*pi*i*(C_n+d*(-B'^2*(4A')^-1 mod Q))/q)",
            "constant_branch": "if Q=1 the amplitude is q*exp(2*pi*i*C_n/q)",
            "epsilon": "epsilon_Q=1 for Q=1 mod 4 and i for Q=3 mod 4",
            "prime_zero_law": "for q=p prime: 1+(Delta|p) in the quadratic branch, one in the linear branch, and p or zero in the constant branch",
            "pure_quadratic_specialization": "for p>=5, a=1, b=0 and n nonzero mod p, Delta=n^2*(1-n^2)/3 and the zero count is 1+(Delta|p); n=0 mod p gives p roots, while n congruent to plus_or_minus 1 mod p gives the single double root",
            "prime_zero_or_euler_interpretation": False,
        },
        "formal_lift": {
            "hilbert_space": "H_q=ell^2(Z/qZ)",
            "koopman_shift": "(K_q f)(x)=f(x+1)",
            "phase_multiplier": "(M_phi f)(x)=exp(2*pi*i*phi_(a,b)(x)/q)*f(x)",
            "weighted_unitary": "U_phi=M_phi*K_q",
            "same_clock_identity": "G_(q,n)(a,b)=Tr(U_phi^n*K_q^(-n))",
            "ordinary_trace_warning": "G_(q,n) is not asserted to equal Tr(U_phi^n); the compensating K_q^(-n) is essential",
            "time_reversal_antiunitary": "Theta=D_g*P*J with (P f)(x)=f(-x), J complex conjugation, and g(x)=(a-b)*x^2",
            "time_reversal_identity": "Theta*U_phi*Theta^(-1)=U_phi^(-1)",
            "time_reversal_involution": True,
            "finite_dimensional_unitary": True,
            "target_operator_claimed": False,
        },
        "exhaustive_validation": {
            "formula_cases": cases, "vanishing_cases": vanish, "nonzero_cases": nonzero,
            "prime_zero_count_cases": zero_cases,
            "maximum_complex_absolute_error": format(maximum_error, ".17g"),
        },
        "sentinels": sentinels,
        "route_a": {"tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
                    "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False},
        "claim_boundary": {
            "target_trace_identity": False, "target_divisor_matching": False,
            "target_functional_equation": False, "target_counting_law": False,
            "arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
            "automorphy": False, "hilbert_polya_operator": False,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] /
                        "results/c161_cyclic_gauss_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "C161_PRODUCER_PASS",
                      "payload_sha256": payload["payload_sha256"],
                      **payload["exhaustive_validation"]}, sort_keys=True))


if __name__ == "__main__":
    main()
