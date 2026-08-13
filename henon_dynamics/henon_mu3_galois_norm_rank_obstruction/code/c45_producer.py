#!/usr/bin/env python3
"""Exact certificate producer for HCS-C45.

C45 tests two canonical rational descents of the C44 paired Hénon factor:
the ordinary Galois norm and its normalized Log_0 root.  The first is a
rational function but has growing virtual degree; the second has a stronger
Euler half-plane but is not automatically a rational/Fredholm determinant.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "hcs-c45-certificate-v1"
TRACE_CONTROL_BOUND = 499
N2_CONTROL_PRIMES = (7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97)
N2_EXPECTED_TRACES = (-6, -6, -6, -30, 18, -54, 18, 42, -30, 42, -30)
PREFIX_DEGREE_BUDGETS = (0, 2, 4, 6, 8, 16, 32)


def canonical_json(obj: Any) -> bytes:
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def prime_divisors(n: int) -> list[int]:
    answer: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            answer.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        answer.append(n)
    return answer


def primitive_root(p: int) -> int:
    factors = prime_divisors(p - 1)
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // q, p) != 1 for q in factors):
            return candidate
    raise AssertionError("primitive root not found")


def split_primes_through(bound: int) -> tuple[int, ...]:
    return tuple(p for p in range(5, bound + 1) if p % 3 == 1 and is_prime(p))


def reduced_fraction(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def phase_zero_count_n1(p: int, rho: int) -> int:
    """Count 2*x^3+2*y^3+(1+rho)*x*y=0 exactly."""
    coefficient = (1 + rho) % p
    cubes = [2 * x * x * x % p for x in range(p)]
    count = 0
    for x in range(p):
        for y in range(p):
            if (cubes[x] + cubes[y] + coefficient * x * y) % p == 0:
                count += 1
    return count


def phase_zero_count_n2(p: int, rho: int) -> int:
    """Count the genuine four-step chronological rho-twisted phase zeroes.

    The phase is
      x0*x1+x1*x2+x2*x3+rho*x3*x0 + 2*sum_j xj^3.
    Root histograms for 2*x3^3+a*x3 reduce the enumeration from p^4 to p^3
    without changing chronology or replacing the transition by an average.
    """
    root_counts: list[list[int]] = []
    for linear in range(p):
        row = [0] * p
        for x3 in range(p):
            row[(2 * x3 * x3 * x3 + linear * x3) % p] += 1
        root_counts.append(row)
    cubes = [2 * x * x * x % p for x in range(p)]
    count = 0
    for x0 in range(p):
        for x1 in range(p):
            prefix = (x0 * x1 + cubes[x0] + cubes[x1]) % p
            for x2 in range(p):
                target = (-prefix - x1 * x2 - cubes[x2]) % p
                count += root_counts[(x2 + rho * x0) % p][target]
    return count


def build_trace_control(p: int) -> dict[str, Any]:
    assert is_prime(p) and p % 3 == 1
    generator = primitive_root(p)
    rho = pow(generator, (p - 1) // 3, p)
    assert rho != 1 and pow(rho, 3, p) == 1
    zero_count = phase_zero_count_n1(p, rho)
    assert zero_count == p - 3
    trace_c1 = 2 * zero_count - 2 * p
    assert trace_c1 == -6
    field_degree = (p - 1) // 2
    norm_virtual_degree = 4 * field_degree
    assert norm_virtual_degree == 2 * (p - 1)
    return {
        "prime": p,
        "least_primitive_root": generator,
        "rho_order_3": rho,
        "real_cyclotomic_degree": field_degree,
        "chronological_n1_zero_count": zero_count,
        "ordinary_norm_first_log_moment_C_p_1": trace_c1,
        "normalized_first_log_moment_c_p_1": reduced_fraction(
            Fraction(trace_c1, field_degree)
        ),
        "ordinary_norm_virtual_degree": norm_virtual_degree,
        "prefactor_lower_bounds": [
            {
                "bounded_absolute_virtual_degree_M": budget,
                "triangle_inequality_rhs": norm_virtual_degree - budget,
            }
            for budget in PREFIX_DEGREE_BUDGETS
        ],
    }


def build_n2_control(p: int) -> dict[str, Any]:
    generator = primitive_root(p)
    rho = pow(generator, (p - 1) // 3, p)
    zero_count = phase_zero_count_n2(p, rho)
    numerator = 2 * zero_count
    assert numerator % p == 0
    trace_c2 = numerator // p - 2 * p * p
    field_degree = (p - 1) // 2
    normalized = Fraction(trace_c2, field_degree)
    # Multiplication by (1-z)^6 cancels C_1 only.  In logarithmic-moment
    # notation its next moment is C_2+6, which is not identically zero.
    return {
        "prime": p,
        "rho_order_3": rho,
        "chronological_phase": "x0*x1+x1*x2+x2*x3+rho*x3*x0+2*(x0^3+x1^3+x2^3+x3^3)",
        "chronological_n2_zero_count": zero_count,
        "ordinary_norm_second_log_moment_C_p_2": trace_c2,
        "normalized_second_log_moment_c_p_2": reduced_fraction(normalized),
        "after_multiply_by_one_minus_z_power_6_second_log_moment": trace_c2
        + 6,
    }


def source_lock(project_root: Path) -> list[dict[str, str]]:
    henon_root = project_root.parent
    relative_paths = (
        "henon_mu3_augmented_euler_superproduct/results/c43_certificate.json",
        "henon_mu3_fixed_coefficient_field_obstruction/results/c44_certificate.json",
    )
    answer: list[dict[str, str]] = []
    for relative in relative_paths:
        source = henon_root / relative
        if not source.is_file():
            raise FileNotFoundError(source)
        answer.append(
            {"path": f"henon_dynamics/{relative}", "sha256": sha256_file(source)}
        )
    return answer


def build_payload(project_root: Path) -> dict[str, Any]:
    trace_primes = split_primes_through(TRACE_CONTROL_BOUND)
    trace_controls = [build_trace_control(p) for p in trace_primes]
    n2_controls = [build_n2_control(p) for p in N2_CONTROL_PRIMES]
    assert tuple(
        row["ordinary_norm_second_log_moment_C_p_2"] for row in n2_controls
    ) == N2_EXPECTED_TRACES
    return {
        "material_passport": {
            "candidate_id": "HCS-C45",
            "project": "henon_mu3_galois_norm_rank_obstruction",
            "ai_assistance_disclosed": True,
            "evidence_policy": "exact all-prime degree argument plus exact chronological finite controls; no zero-table data",
        },
        "source_lock": source_lock(project_root),
        "definitions": {
            "coefficient_field": "L_p=Q(zeta_p)^+ with d_p=(p-1)/2",
            "paired_local_factor": "E_p(z)=D_p(z;psi)*D_p(z;psi^-1) in L_p(z)",
            "ordinary_galois_norm": "N_p(z)=Norm_(L_p/Q)(E_p(z)) in Q(z)",
            "ordinary_norm_log": "Log N_p(z)=-sum_(n>=1) C_p,n*z^n/n with C_p,n=Tr_(L_p/Q)(B_p,n)",
            "normalized_log_norm": "G_p(z)=exp((1/d_p)*Log_0 N_p(z)) near z=0",
            "normalized_log": "Log G_p(z)=-sum_(n>=1) c_p,n*z^n/n with c_p,n=C_p,n/d_p",
            "split_prime_clock": "z=p^(-s)=Norm(mathfrak_p)^(-s)",
            "chronology": "all B_p,n retain the rho-twisted ordered 2n-step Henon phase",
        },
        "all_prime_theorems": {
            "first_trace": "C_p,1=Tr_(L_p/Q)(B_p,1)=-6",
            "ordinary_norm_virtual_degree": "vdeg N_p=4*d_p=2*(p-1)",
            "ordinary_norm_leading_coefficient": "nonzero",
            "bounded_prefactor_no_go": "if Q_p in Q(z) and abs(vdeg Q_p)<=M independent of p, then abs(vdeg(Q_p*N_p))>=2*(p-1)-M",
            "fixed_rank_conclusion": "no uniformly bounded finite-rank graded determinant can realize Q_p*N_p",
            "ordinary_norm_euler_germ": "product_p N_p(p^(-s)) converges locally uniformly and is nonzero for Re(s)>1",
            "normalized_first_moment": "c_p,1=-12/(p-1)",
            "normalized_higher_moment_bound": "abs(c_p,n)<=4*4^n for n>=2",
            "normalized_euler_germ": "product_p G_p(p^(-s)) converges locally uniformly and is nonzero for Re(s)>1/2",
            "normalized_root_determinant_gate": "G_p is an ordinary rational determinant only if every divisor multiplicity of N_p is divisible by d_p",
        },
        "exact_trace_controls": trace_controls,
        "exact_chronological_n2_controls": n2_controls,
        "aggregate_control": {
            "trace_control_bound_inclusive": TRACE_CONTROL_BOUND,
            "trace_control_primes": list(trace_primes),
            "number_of_trace_controls": len(trace_controls),
            "all_n1_zero_counts_equal_p_minus_3": all(
                row["chronological_n1_zero_count"] == row["prime"] - 3
                for row in trace_controls
            ),
            "all_first_traces_equal_minus_6": all(
                row["ordinary_norm_first_log_moment_C_p_1"] == -6
                for row in trace_controls
            ),
            "all_norm_virtual_degrees_equal_2_times_p_minus_1": all(
                row["ordinary_norm_virtual_degree"] == 2 * (row["prime"] - 1)
                for row in trace_controls
            ),
            "maximum_certified_norm_virtual_degree": max(
                row["ordinary_norm_virtual_degree"] for row in trace_controls
            ),
            "n2_control_primes": list(N2_CONTROL_PRIMES),
            "n2_trace_ledger": [
                row["ordinary_norm_second_log_moment_C_p_2"] for row in n2_controls
            ],
            "normalized_n2_moments_are_not_constant": len(
                {
                    (
                        row["normalized_second_log_moment_c_p_2"]["numerator"],
                        row["normalized_second_log_moment_c_p_2"]["denominator"],
                    )
                    for row in n2_controls
                }
            )
            > 1,
            "one_minus_z_power_6_is_only_first_order_normalization": any(
                row[
                    "after_multiply_by_one_minus_z_power_6_second_log_moment"
                ]
                != 0
                for row in n2_controls
            ),
        },
        "decisions": {
            "ordinary_galois_norm_rational_descent": "EXACT_BUT_UNBOUNDED_LOCAL_RANK",
            "bounded_degree_rational_prefactor_repair": "REFUTED_ALL_SPLIT_PRIMES",
            "normalized_log_norm_analytic_acceleration": "PROVED_RE_S_GREATER_THAN_ONE_HALF",
            "normalized_log_norm_as_rational_fredholm_determinant": "OPEN_DIVISOR_MULTIPLICITY_GATE",
            "one_minus_z_power_6_tate_cancellation": "NOT_CLAIMED_BEYOND_FIRST_LOG_COEFFICIENT",
            "next_large_gate": "TEST_DIVISOR_MULTIPLICITIES_OF_N_p_MOD_d_p_AND_LOCAL_MONODROMY",
        },
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_ANALYTIC_DETERMINANT",
            "A2_reason": "ordinary norm is rational and gives an Euler germ on Re(s)>1; normalized root improves to Re(s)>1/2 but is not yet an ordinary determinant",
            "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A3_reason": "normalized Log_0 norm reaches the critical-boundary half-plane, while continuation, functional equation, and divisor integrality remain open",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_EXPLORATORY",
            "scoped_status": "ROUTE_A_EXPLORATORY_CRITICAL_BOUNDARY_GERM",
            "route_b_invocation_allowed": False,
        },
        "scope": {
            "rh_proved": False,
            "hilbert_polya_operator_constructed": False,
            "global_meromorphic_continuation_claimed": False,
            "gamma_factor_claimed": False,
            "riemann_zero_data_used": False,
            "normalized_root_claimed_rational": False,
            "normalized_root_claimed_fredholm_determinant": False,
            "bounded_rank_claimed_for_ordinary_norm": False,
            "inert_prime_factor_constructed": False,
        },
    }


def build_certificate(project_root: Path) -> dict[str, Any]:
    payload = build_payload(project_root)
    return {
        "schema": SCHEMA,
        "payload": payload,
        "payload_sha256": hashlib.sha256(canonical_json(payload)).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()
    project_root = Path(__file__).resolve().parents[1]
    certificate = build_certificate(project_root)
    output = Path(arguments.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {output}")
    print(f"payload_sha256={certificate['payload_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
