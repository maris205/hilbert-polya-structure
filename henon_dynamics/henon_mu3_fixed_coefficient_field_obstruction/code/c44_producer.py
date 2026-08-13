#!/usr/bin/env python3
"""Exact certificate producer for HCS-C44.

The computation is deliberately elementary: all finite-field and cyclotomic
calculations use Python integers.  The certificate supports, but is not a
substitute for, the all-prime stabilizer proof in the paper.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd
from pathlib import Path
from typing import Any


SCHEMA = "hcs-c44-certificate-v1"
CONTROL_BOUND = 499


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


def factorial_mod(n: int, p: int) -> int:
    value = 1
    for integer in range(2, n + 1):
        value = value * integer % p
    return value


def split_primes_through(bound: int) -> tuple[int, ...]:
    return tuple(p for p in range(5, bound + 1) if p % 3 == 1 and is_prime(p))


def phase_histogram(p: int, rho: int) -> list[int]:
    """N_p(r)=#{(x,y): 2x^3+2y^3+(1+rho)xy=r}."""
    cubes = [2 * x * x * x % p for x in range(p)]
    coefficient = (1 + rho) % p
    histogram = [0] * p
    for x in range(p):
        for y in range(p):
            residue = (cubes[x] + cubes[y] + coefficient * x * y) % p
            histogram[residue] += 1
    assert sum(histogram) == p * p
    return histogram


def paired_histogram(histogram: list[int]) -> list[int]:
    p = len(histogram)
    return [histogram[r] + histogram[-r % p] for r in range(p)]


def scaling_stabilizer(values: list[int]) -> list[int]:
    p = len(values)
    return [
        scalar
        for scalar in range(1, p)
        if all(values[scalar * r % p] == values[r] for r in range(p))
    ]


def power_moment(values: list[int], exponent: int) -> int:
    p = len(values)
    return sum(pow(r, exponent, p) * values[r] for r in range(p)) % p


def circular_product(left: list[int], right: list[int]) -> list[int]:
    p = len(left)
    output = [0] * p
    for i, a in enumerate(left):
        if a == 0:
            continue
        for j, b in enumerate(right):
            if b:
                output[(i + j) % p] += a * b
    return output


def real_cyclotomic_minpoly_for_paired_moment(
    p: int, histogram: list[int]
) -> list[int]:
    """Primitive polynomial of B=(2/p) sum H(r) zeta_p^r.

    Coefficients are returned from highest degree to the constant term.  This
    routine is used only for the frozen p=7 anchor, but is valid whenever the
    scaling stabilizer of H is exactly {+1,-1}.
    """
    values = paired_histogram(histogram)
    degree = (p - 1) // 2
    group_element = [1] + [0] * (p - 1)
    power_sums: list[int] = []
    for _ in range(degree):
        group_element = circular_product(group_element, values)
        # Sum over all nonzero Galois automorphisms is p*c_0-sum(c_r).
        # H is even, hence each real conjugate is counted twice.
        doubled_trace = p * group_element[0] - sum(group_element)
        assert doubled_trace % 2 == 0
        power_sums.append(doubled_trace // 2)

    elementary = [1]
    for order in range(1, degree + 1):
        numerator = sum(
            (-1) ** (index - 1)
            * elementary[order - index]
            * power_sums[index - 1]
            for index in range(1, order + 1)
        )
        assert numerator % order == 0
        elementary.append(numerator // order)

    minpoly_alpha = [(-1) ** index * elementary[index] for index in range(degree + 1)]
    # If M(alpha)=0 and B=2*alpha/p, then 2^d M(pX/2) vanishes at B.
    transformed = [
        coefficient * p ** (degree - index) * 2**index
        for index, coefficient in enumerate(minpoly_alpha)
    ]
    content = 0
    for coefficient in transformed:
        content = gcd(content, abs(coefficient))
    primitive = [coefficient // content for coefficient in transformed]
    if primitive[0] < 0:
        primitive = [-coefficient for coefficient in primitive]
    return primitive


def moment_formula_k0(p: int, m: int) -> int:
    numerator = 2 * factorial_mod(2 * m, p) * pow(4, m, p)
    denominator = factorial_mod(m, p) ** 2
    return numerator * pow(denominator, -1, p) % p


def moment_formula_k1(p: int, m: int, coefficient: int) -> int:
    assert p >= 13 and m >= 4
    numerator = (
        2
        * factorial_mod(2 * m + 2, p)
        * pow(4, m - 2, p)
        * pow(coefficient, 6, p)
    )
    denominator = (
        factorial_mod(m - 2, p) ** 2 * factorial_mod(6, p)
    )
    return numerator * pow(denominator, -1, p) % p


def build_control(p: int) -> dict[str, Any]:
    assert is_prime(p) and p % 3 == 1
    m = (p - 1) // 3
    generator = primitive_root(p)
    rho = pow(generator, m, p)
    coefficient = (1 + rho) % p
    assert rho != 1 and pow(rho, 3, p) == 1
    assert coefficient != 0

    histogram = phase_histogram(p, rho)
    paired = paired_histogram(histogram)
    stabilizer = scaling_stabilizer(paired)
    k0 = 2 * m
    k0_direct = power_moment(paired, k0)
    k0_formula = moment_formula_k0(p, m)
    assert k0_direct == k0_formula != 0

    second_moment: dict[str, Any] | None
    if p == 7:
        second_moment = None
    else:
        k1 = k0 + 2
        k1_direct = power_moment(paired, k1)
        k1_formula = moment_formula_k1(p, m, coefficient)
        assert k1_direct == k1_formula != 0
        second_moment = {
            "exponent": k1,
            "direct_mod_p": k1_direct,
            "closed_formula_mod_p": k1_formula,
        }

    assert stabilizer == [1, p - 1]
    assert histogram[0] == p - 3
    trace_from_histogram = ((p - 1) * paired[0] - sum(paired[1:])) // p
    assert trace_from_histogram == -6

    return {
        "prime": p,
        "m_equals_p_minus_1_over_3": m,
        "least_primitive_root": generator,
        "rho_order_3": rho,
        "one_plus_rho": coefficient,
        "phase_histogram": histogram,
        "paired_scaling_stabilizer": stabilizer,
        "first_nonzero_power_moment": {
            "exponent": k0,
            "direct_mod_p": k0_direct,
            "closed_formula_mod_p": k0_formula,
        },
        "second_nonzero_power_moment": second_moment,
        "paired_moment_field_degree": (p - 1) // 2,
        "zero_fibre_count": histogram[0],
        "paired_moment_field_trace": trace_from_histogram,
    }


def source_lock(project_root: Path) -> list[dict[str, str]]:
    henon_root = project_root.parent
    relative = "henon_mu3_augmented_euler_superproduct/results/c43_certificate.json"
    source = henon_root / relative
    if not source.is_file():
        raise FileNotFoundError(source)
    return [{"path": f"henon_dynamics/{relative}", "sha256": sha256_file(source)}]


def build_payload(project_root: Path) -> dict[str, Any]:
    primes = split_primes_through(CONTROL_BOUND)
    controls = [build_control(p) for p in primes]
    p7_polynomial = real_cyclotomic_minpoly_for_paired_moment(
        7, controls[0]["phase_histogram"]
    )
    assert p7_polynomial == [7, 42, -168, -232]
    return {
        "material_passport": {
            "candidate_id": "HCS-C44",
            "project": "henon_mu3_fixed_coefficient_field_obstruction",
            "ai_assistance_disclosed": True,
            "evidence_policy": "all-prime proof plus exhaustive exact finite-field controls; no zero-table data",
        },
        "source_lock": source_lock(project_root),
        "conventions": {
            "phase": "F_p(x,y)=2*x^3+2*y^3+(1+rho_p)*x*y",
            "rho": "rho_p has exact order 3 in F_p^*",
            "raw_histogram": "N_p(r)=#{(x,y) in F_p^2:F_p(x,y)=r}",
            "paired_histogram": "H_p(r)=N_p(r)+N_p(-r)",
            "paired_first_moment": "B_p=(2/p)*sum_r H_p(r)*zeta_p^r=A_p,1(psi)+A_p,1(psi^-1)",
            "split_prime_clock": "z_mathfrak_p=(Norm mathfrak_p)^(-s)=p^(-s)",
            "inert_prime_clock_if_extended": "z_mathfrak_p=(Norm mathfrak_p)^(-s)=p^(-2s); no p-average substitution",
        },
        "all_prime_theorem": {
            "scope": "every prime p=1 mod 3, p>3",
            "stabilizer": "Stab_Gal(B_p)={+1,-1}",
            "field_identity": "Q(B_p)=Q(zeta_p+zeta_p^(-1))",
            "degree": "[Q(B_p):Q]=(p-1)/2",
            "proof_witness_k0": "k0=2m; M_k0=2*(2m)!/(m!^2)*4^m mod p is nonzero",
            "proof_witness_k1": "for p>=13, k1=2m+2; M_k1=2*(2m+2)!/((m-2)!^2*6!)*4^(m-2)*(1+rho)^6 mod p is nonzero",
            "stabilizer_deduction": "a^k0=a^k1=1 gives a^2=1; for p=7, gcd(k0,p-1)=2",
            "fixed_coefficient_number_field": "IMPOSSIBLE",
        },
        "exact_controls": controls,
        "aggregate_control": {
            "bound_inclusive": CONTROL_BOUND,
            "control_primes": list(primes),
            "complete_split_prime_list_through_bound": True,
            "number_of_control_primes": len(primes),
            "all_stabilizers_plus_minus_one": all(
                row["paired_scaling_stabilizer"] == [1, row["prime"] - 1]
                for row in controls
            ),
            "all_degrees_equal_p_minus_1_over_2": all(
                row["paired_moment_field_degree"] == (row["prime"] - 1) // 2
                for row in controls
            ),
            "all_zero_fibre_counts_equal_p_minus_3": all(
                row["zero_fibre_count"] == row["prime"] - 3 for row in controls
            ),
            "all_paired_field_traces_equal_minus_6": all(
                row["paired_moment_field_trace"] == -6 for row in controls
            ),
            "maximum_certified_field_degree": max(
                row["paired_moment_field_degree"] for row in controls
            ),
        },
        "all_prime_zero_fibre_theorem": {
            "formula": "N_p(0)=p-3 for every split prime p>3",
            "paired_field_trace": "Tr_Q(B_p)/Q=-6",
            "status": "PROVED_ALL_SPLIT_PRIMES",
        },
        "p7_anchor": {
            "paired_moment_primitive_minimal_polynomial_high_to_low": p7_polynomial,
            "polynomial": "7*X^3+42*X^2-168*X-232",
            "irreducible_over_Q": True,
        },
        "decisions": {
            "conjugate_pairing_repairs_real_type": "YES_LOCALLY",
            "descent_to_one_fixed_number_field": "REFUTED_ALL_SPLIT_PRIMES",
            "uniform_fixed_rank_compatible_system": "STOP_BEFORE_HANKEL_GATE",
            "finite_tate_cm_repair": "CLOSED_BY_HCS_C42",
            "next_large_gate": "CANONICAL_RATIONAL_GALOIS_NORM_OR_TRACE_ASSEMBLY_WITH_TRUE_NORM_CLOCK",
        },
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_ANALYTIC_DETERMINANT",
            "A2_reason": "inherited from the C43 raw Euler germ",
            "A3": "A3_FAIL",
            "A3_reason": "paired moments have unbounded coefficient-field degree",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope": {
            "rh_proved": False,
            "hilbert_polya_operator_constructed": False,
            "global_meromorphic_continuation_claimed": False,
            "gamma_factor_claimed": False,
            "riemann_zero_data_used": False,
            "inert_prime_operator_constructed": False,
            "zero_fibre_formula_used_as_route_a_promotion": False,
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
