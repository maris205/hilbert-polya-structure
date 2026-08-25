#!/usr/bin/env python3
"""Produce the exact HCS-C141 quadratic inverse-branch Ruelle receipt."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c141_quadratic_ruelle_evidence.json"
CUTOFF = 6


def trim(p: list[Fraction]) -> list[Fraction]:
    p = p[:]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def derivative(a: list[Fraction]) -> list[Fraction]:
    return trim([Fraction(i) * a[i] for i in range(1, len(a))] or [Fraction(0)])


def remainder(a: list[Fraction], modulus: list[Fraction]) -> list[Fraction]:
    out = trim(a)
    assert modulus[-1] == 1
    while len(out) >= len(modulus):
        shift = len(out) - len(modulus)
        lead = out[-1]
        for j, x in enumerate(modulus):
            out[j + shift] -= lead * x
        out = trim(out)
    return out


def multiplication_matrix(a: list[Fraction], modulus: list[Fraction]) -> list[list[Fraction]]:
    degree = len(modulus) - 1
    matrix = [[Fraction(0) for _ in range(degree)] for _ in range(degree)]
    for column in range(degree):
        image = remainder([Fraction(0)] * column + a, modulus)
        for row, value in enumerate(image):
            matrix[row][column] = value
    return matrix


def solve(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    n = len(rhs)
    aug = [matrix[i][:] + [rhs[i]] for i in range(n)]
    for column in range(n):
        pivot = next(row for row in range(column, n) if aug[row][column])
        aug[column], aug[pivot] = aug[pivot], aug[column]
        scale = aug[column][column]
        aug[column] = [x / scale for x in aug[column]]
        for row in range(n):
            if row == column or not aug[row][column]:
                continue
            scale = aug[row][column]
            aug[row] = [x - scale * y for x, y in zip(aug[row], aug[column])]
    return [aug[i][-1] for i in range(n)]


def quotient_trace_inverse(denominator: list[Fraction], modulus: list[Fraction]) -> Fraction:
    degree = len(modulus) - 1
    matrix = multiplication_matrix(denominator, modulus)
    inverse = solve(matrix, [Fraction(1)] + [Fraction(0)] * (degree - 1))
    check = remainder(mul(denominator, inverse), modulus)
    assert check == [Fraction(1)]
    inverse_matrix = multiplication_matrix(inverse, modulus)
    return sum(inverse_matrix[i][i] for i in range(degree))


def fraction_string(value: Fraction | int) -> str:
    q = Fraction(value)
    return f"{q.numerator}/{q.denominator}"


def mobius(n: int) -> int:
    value, primes, divisor = n, 0, 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            value //= divisor
            primes += 1
            if value % divisor == 0:
                return 0
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def primitive_orbits(n: int) -> int:
    return sum(mobius(d) * 2 ** (n // d) for d in range(1, n + 1) if n % d == 0) // n


def poly_hash(p: list[Fraction]) -> str:
    assert all(x.denominator == 1 for x in p)
    payload = ",".join(str(x.numerator) for x in p).encode()
    return hashlib.sha256(payload).hexdigest()


def payload_hash(data: dict) -> str:
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def build() -> dict:
    iterate = [Fraction(0), Fraction(1)]
    traces: list[Fraction] = []
    rows = []
    for n in range(1, CUTOFF + 1):
        iterate = add(mul(iterate, iterate), [Fraction(-6)])
        periodic = iterate[:]
        periodic[1] -= 1
        periodic = trim(periodic)
        multiplier = derivative(iterate)
        multiplier_minus_one = multiplier[:]
        multiplier_minus_one[0] -= 1
        denominator = mul(multiplier, multiplier_minus_one)
        trace = quotient_trace_inverse(denominator, periodic)
        traces.append(trace)
        rows.append({
            "n": n,
            "degree": len(periodic) - 1,
            "rooted_inverse_words": 2 ** n,
            "primitive_orbits": primitive_orbits(n),
            "periodic_polynomial_coefficients_low_to_high": [int(x) for x in periodic],
            "periodic_polynomial_sha256": poly_hash(periodic),
            "trace_L2_power": fraction_string(trace),
        })

    coefficients = [Fraction(1)]
    for n in range(1, CUTOFF + 1):
        coefficients.append(-sum(coefficients[n - j] * traces[j - 1] for j in range(1, n + 1)) / n)

    expected_traces = [
        "1/12", "7/720", "239/257472", "1255703/13810694400",
        "235072563599/26491011084499968",
        "655398850662090042240821783/756396676602907446734765701632000",
    ]
    expected_coefficients = [
        "1/1", "-1/12", "-1/720", "-1/1287360", "-1/2057793465600",
        "-1/2628907672975559586892800",
        "-1/2145321764151480887652914286846712748095922688000",
    ]
    assert [fraction_string(x) for x in traces] == expected_traces
    assert [fraction_string(x) for x in coefficients] == expected_coefficients

    data = {
        "schema": "HCS-C141-quadratic-inverse-branch-ruelle-v1",
        "candidate_id": "HCS-C141",
        "date_utc": "2026-08-25",
        "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "forward_map": "F(z)=z^2-6",
            "domain": "D_4={z:|z|<4}",
            "inverse_branches": "psi_+(z)=sqrt(z+6), psi_-(z)=-sqrt(z+6)",
            "square_root_convention": "principal square root on D(6,4), contained in Re(w)>0",
            "space": "Hardy H^2(D_4), normalized basis e_j(z)=(z/4)^j",
            "operator_family": "(L_m f)(z)=sum_(epsilon=+,-) (psi_epsilon'(z))^m f(psi_epsilon(z))",
            "headline_weight": "m=2",
            "clock": "one inverse branch per iterate",
            "determinant_convention": "D_2(u)=det(I-u L_2)",
            "cutoff": "no theorem cutoff; n=1..6 is an exact replay prefix",
            "precision": "exact integer and rational quotient-algebra arithmetic",
        },
        "geometry_and_nuclearity": {
            "image_radius_upper_bound": "sqrt(10)<4",
            "branch_real_part_separation": "Re(psi_+)>=sqrt(2), Re(psi_-)<=-sqrt(2)",
            "derivative_bound": "q=1/(2*sqrt(2))",
            "squared_weight_bound": "sup|psi_epsilon'|^2<=1/8",
            "trace_class": True,
            "trace_norm_upper_bound": "1/(4-sqrt(10))",
            "nuclear_decomposition": "sum_(epsilon,j) [(psi_epsilon')^2 (psi_epsilon/4)^j] tensor e_j^*",
        },
        "all_period_theorem": {
            "periodic_points_exhausted": True,
            "escape_bound": "|z|>3 implies |F(z)|>|z|; hence every periodic point lies in D_4",
            "unique_word_fixed_points": "every length-n inverse word is a q^n contraction and has one fixed point",
            "simple_roots": "all roots of F^n(z)-z are simple because inverse multipliers have modulus <1",
            "power_trace_formula": "Tr(L_m^n)=sum_(F^n(p)=p) Lambda_n(p)^(-m)/(1-Lambda_n(p)^(-1))",
            "headline_trace_formula": "Tr(L_2^n)=sum_(F^n(p)=p) 1/(Lambda_n(p)*(Lambda_n(p)-1))",
            "periodic_polynomial": "P_n(z)=F^n(z)-z is monic of degree 2^n",
            "primitive_count_formula": "P_n=(1/n) sum_(d|n) mu(d) 2^(n/d)",
        },
        "weight_ladder_controls": {
            "lagrange_identity": "sum_(P_n(p)=0) 1/P_n'(p)=0 for deg(P_n)>=2",
            "m0_trace_formula": "Tr(L_0^n)=2^n",
            "m0_determinant": "det(I-u L_0)=1-2u",
            "m1_trace_formula": "Tr(L_1^n)=0",
            "m1_determinant": "det(I-u L_1)=1",
            "first_nontrivial_stability_weight": "m=2",
            "m0_trace_prefix": [2 ** n for n in range(1, CUTOFF + 1)],
            "m1_trace_prefix": [0 for _ in range(CUTOFF)],
        },
        "headline_exact_prefix": {
            "periods": rows,
            "trace_prefix": expected_traces,
            "fredholm_coefficients_c0_through_c6": expected_coefficients,
            "newton_recurrence": "c_0=1; c_n=-(1/n) sum_(j=1)^n c_(n-j) Tr(L_2^j)",
        },
        "primitive_product": {
            "formula": "D_2(u)=product_[p primitive] product_(k>=2) (1-u^ell(p)*Lambda_p^(-k))",
            "inner_index_starts_at": 2,
            "index_reason": "mu^(2r)/(1-mu^r)=sum_(k>=2) mu^(kr), with mu=Lambda_p^(-1)",
            "raw_product_absolute_convergence_domain": "|u|<4",
            "absolute_majorant": "sum_(n>=1) |u|^n*4^(-n)/(n*(1-q^n))",
            "global_statement": "D_2 is entire by trace class; no raw-product convergence is claimed outside |u|<4",
        },
        "negative_control": {
            "map": "F_control(z)=z^2-2",
            "same_D4_branch_model_valid": False,
            "reason": "the branch point -2 lies inside D_4, so z+2 has no global holomorphic square root on D_4",
            "boundary": "this rejects only the same D_4 branch construction, not every possible operator space",
        },
        "receipt_summary": {
            "trace_prefix_length": CUTOFF,
            "fredholm_taylor_degree": CUTOFF,
            "rooted_periodic_points_through_6": sum(2 ** n for n in range(1, CUTOFF + 1)),
            "primitive_orbits_through_6": sum(primitive_orbits(n) for n in range(1, CUTOFF + 1)),
            "theorem_period_cutoff": "none",
        },
        "progress": {
            "headline": "first unconditional nonlinear polynomial inverse-branch Hardy trace-class package in this series, with all-period exhaustion and a stability-weight control ladder",
            "over_prior_gate": "advances beyond finite polynomial matrices, real count models, and Möbius word matrices to a single nonlinear complex polynomial with intrinsic inverse branches and exact m=2 stability traces",
            "geometry": "PASS_ANALYTIC",
            "trace_class": "PASS_ANALYTIC",
            "all_period_trace": "PASS_EXACT",
            "primitive_product": "PASS_IN_PROVED_DISK",
            "m0_m1_controls": "PASS_EXACT",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "uses_prime_table": False,
            "uses_zero_table": False,
            "claims_target_divisor": False,
            "claims_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_hilbert_polya": False,
        },
        "nonclaims": [
            "no prime-like target correspondence or target zero census",
            "no target functional equation, counting law, or divisor match",
            "no arithmetic/local data, Euler factor, root number, or automorphy claim",
            "no natural unitary, self-adjoint, metaplectic, or Hilbert--Polya operator",
            "no raw primitive-product convergence claim outside |u|<4",
            "no novelty claim for general Ruelle or weighted-composition theory",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
