#!/usr/bin/env python3
"""Produce the exact HCS-C137 uniform Möbius--Bergman receipt."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c137_uniform_mobius_evidence.json"
A_VALUES = (Fraction(3), Fraction(13, 4), Fraction(7, 2))
B_VALUES = (Fraction(6), Fraction(13, 2), Fraction(7))
CUTOFF = 10


def fs(x: Fraction | int) -> str:
    q = Fraction(x)
    return f"{q.numerator}/{q.denominator}"


def mmul(x, y):
    return tuple(tuple(sum(x[i][k] * y[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def word_matrix(word: tuple[int, ...], a: Fraction, b: Fraction):
    out = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    mats = (((Fraction(0), Fraction(1)), (Fraction(1), a)),
            ((Fraction(0), Fraction(1)), (Fraction(1), b)))
    for letter in word:
        out = mmul(out, mats[letter])
    return out


def mobius(n: int) -> int:
    x, count, d = n, 0, 2
    while d * d <= x:
        if x % d == 0:
            x //= d
            count += 1
            if x % d == 0:
                return 0
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def primitive_cycles(n: int) -> int:
    return sum(mobius(d) * 2 ** (n // d) for d in range(1, n + 1) if n % d == 0) // n


def case_token(word: tuple[int, ...], a: Fraction, b: Fraction) -> str:
    (A, B), (C, D) = word_matrix(word, a, b)
    determinant = A * D - B * C
    trace = A + D
    disc = trace * trace - 4 * determinant
    assert determinant == (-1) ** len(word) and C > 0 and disc > 0
    name = "".join("a" if x == 0 else "b" for x in word)
    return (
        f"a={fs(a)}:b={fs(b)}:{name}:M={fs(A)},{fs(B)},{fs(C)},{fs(D)}:"
        f"det={fs(determinant)}:tr={fs(trace)}:disc={fs(disc)}:"
        f"fixed=({fs(A-D)}+sqrt({fs(disc)}))/(2*{fs(C)}):"
        f"lambda=({fs(trace)}-sqrt({fs(disc)}))/({fs(trace)}+sqrt({fs(disc)}))"
    )


def digest(lines: list[str]) -> str:
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def trace_formula(a: Fraction, b: Fraction, first: bool) -> Fraction:
    if first:
        return a**3 * b**2 + a**3 + 2*a**2*b + 2*a*b**2 + 3*a + 2*b
    return a**3 * b**2 + 4*a**2*b + a*b**2 + 3*a + 2*b


def build() -> dict:
    grid = []
    total_words = 0
    for a, b in product(A_VALUES, B_VALUES):
        periods = []
        for n in range(1, CUTOFF + 1):
            lines = [case_token(word, a, b) for word in product((0, 1), repeat=n)]
            periods.append({
                "n": n,
                "rooted_words": len(lines),
                "primitive_cycles": primitive_cycles(n),
                "trace_case_count": len(lines),
                "trace_case_sha256": digest(lines),
            })
            total_words += len(lines)
        t1, t2 = trace_formula(a, b, True), trace_formula(a, b, False)
        grid.append({
            "a": fs(a),
            "b": fs(b),
            "closed_image_gap": fs(Fraction(1, 1) / (a + 1) - Fraction(1, 1) / (b - 1)),
            "period_receipts_through_10": periods,
            "aaabb_trace": fs(t1),
            "aabab_trace": fs(t2),
            "trace_gap": fs(t1 - t2),
        })

    assert total_words == 9 * (2 ** 11 - 2) == 18414
    trace_values = [trace_formula(a, b, True) for a, b in product(A_VALUES, B_VALUES)]
    gap_values = [a * (b-a)**2 for a, b in product(A_VALUES, B_VALUES)]
    assert min(gap_values) == Fraction(175, 8)
    assert max(trace_values) == Fraction(10731, 4)

    data = {
        "schema": "HCS-C137-uniform-mobius-bergman-v1",
        "candidate_id": "HCS-C137",
        "date_utc": "2026-08-24",
        "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "family": {
            "branches": "phi_x(z)=1/(x+z)",
            "parameter_rectangle": {"a": ["3/1", "7/2"], "b": ["6/1", "7/1"]},
            "space": "normalized Bergman A^2(unit disk)",
            "operator": "L_(a,b)=C_phi_a+C_phi_b",
        },
        "uniform_geometry": {
            "image_disk": "center=x/(x^2-1), radius=1/(x^2-1)",
            "closed_image_gap_formula": "g(a,b)=1/(a+1)-1/(b-1)",
            "minimum_gap": "1/45",
            "minimum_corner": ["7/2", "6/1"],
            "strong_separation_uniform": True,
            "negative_rectangle": {"a": ["3/1", "4/1"], "b": ["6/1", "7/1"], "minimum_gap": "0/1", "tangent_corner": ["4/1", "6/1"], "positive_closed_gap": False},
        },
        "uniform_operator_bounds": {
            "trace_class": True,
            "trace_norm_upper_bound": "89/16",
            "trace_norm_lipschitz": "||L_(a,b)-L_(a',b')||_1 <= 4|a-a'|+(5/32)|b-b'|",
            "a_lipschitz_constant": "4/1",
            "b_lipschitz_constant": "5/32",
            "proof_majorant": "sum_(n>=1) (n+1)n r^(n-1) delta = 2 delta/(1-r)^3",
        },
        "all_word_theorem": {
            "matrix": "M_x=[[0,1],[1,x]]",
            "fixed_point": "(A-D+sqrt(Delta))/(2C)",
            "multiplier": "(t-sqrt(Delta))/(t+sqrt(Delta))",
            "composition_trace": "1/2+t/(2sqrt(Delta))",
            "power_trace": "Tr(L_(a,b)^n)=sum_(|w|=n) 1/(1-lambda_w)",
            "fredholm_product": "det(I-zL)=product_[p primitive] product_(k>=0)(1-z^|p| lambda_p^k)",
            "raw_absolute_convergence": "|z|<1/2",
            "determinant_global_domain": "entire by trace class; no raw-product claim outside |z|<1/2",
        },
        "order_sensitive_uniform_control": {
            "words": ["aaabb", "aabab"],
            "not_cyclic_rotations": True,
            "first_trace_formula": "a^3*b^2+a^3+2*a^2*b+2*a*b^2+3*a+2*b",
            "second_trace_formula": "a^3*b^2+4*a^2*b+a*b^2+3*a+2*b",
            "trace_gap_identity": "t_aaabb-t_aabab=a*(b-a)^2",
            "uniform_trace_gap_lower_bound": "175/8",
            "first_trace_upper_bound": "10731/4",
            "composition_trace_gap_lower_bound": "2800/(10731^2+64)^(3/2)",
            "composition_trace_gap_positive": True,
        },
        "grid_receipts": grid,
        "receipt_summary": {
            "parameter_points": 9,
            "rooted_word_receipts_through_10": total_words,
            "primitive_classes_per_parameter_through_10": sum(primitive_cycles(n) for n in range(1, 11)),
            "primitive_parameter_receipts_through_10": 9 * sum(primitive_cycles(n) for n in range(1, 11)),
            "theorem_parameter_domain": "entire frozen rectangle; grid is replay only",
        },
        "progress": {
            "uniform_separation": "PASS_EXACT",
            "uniform_nuclearity_and_lipschitz": "PASS_ANALYTIC",
            "all_word_trace_product": "PASS_ANALYTIC",
            "uniform_order_sensitivity": "PASS_EXACT",
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
            "no prime-like target correspondence",
            "no target divisor or zero census",
            "no target functional equation or counting law",
            "no natural unitary, scattering, or self-adjoint lift",
            "no Euler-factor, root-number, automorphy, or Hilbert--Polya claim",
        ],
    }
    payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    data["payload_sha256"] = hashlib.sha256(payload).hexdigest()
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
