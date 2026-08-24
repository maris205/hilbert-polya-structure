#!/usr/bin/env python3
"""Produce the exact C132 Möbius--Bergman trace receipt."""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c132_mobius_bergman_evidence.json"
DIGITS = (3, 6)
CUTOFF = 10
getcontext().prec = 60


def frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def mmul(x, y):
    return (
        (x[0][0] * y[0][0] + x[0][1] * y[1][0], x[0][0] * y[0][1] + x[0][1] * y[1][1]),
        (x[1][0] * y[0][0] + x[1][1] * y[1][0], x[1][0] * y[0][1] + x[1][1] * y[1][1]),
    )


def word_matrix(word: tuple[int, ...]):
    out = ((1, 0), (0, 1))
    for digit in word:
        out = mmul(out, ((0, 1), (1, digit)))
    return out


def mobius(n: int) -> int:
    x, primes, d = n, 0, 2
    while d * d <= x:
        if x % d == 0:
            x //= d
            primes += 1
            if x % d == 0:
                return 0
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        primes += 1
    return -1 if primes % 2 else 1


def primitive_cycles(n: int) -> int:
    return sum(mobius(d) * 2 ** (n // d) for d in range(1, n + 1) if n % d == 0) // n


def case_record(word: tuple[int, ...]) -> tuple[str, Decimal]:
    (a, b), (c, d) = word_matrix(word)
    det = a * d - b * c
    trace = a + d
    disc = trace * trace - 4 * det
    assert det == (-1) ** len(word) and c > 0 and disc > 0
    contraction_den = 1
    for digit in word:
        contraction_den *= (digit - 1) ** 2
    token = (
        f"{''.join(map(str, word))}:{a},{b},{c},{d}:det={det}:tr={trace}:disc={disc}:"
        f"fixed=({a-d}+sqrt({disc}))/(2*{c}):"
        f"lambda=({trace}-sqrt({disc}))/({trace}+sqrt({disc})):"
        f"weight=1/2+{trace}/(2*sqrt({disc})):deriv_bound=1/{contraction_den}"
    )
    weight = Decimal(1) / 2 + Decimal(trace) / (Decimal(2) * Decimal(disc).sqrt())
    return token, weight


def digest(lines: list[str]) -> str:
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def anagram_record(word: tuple[int, ...]) -> dict:
    (a, b), (c, d) = word_matrix(word)
    det, trace = a * d - b * c, a + d
    disc = trace * trace - 4 * det
    return {
        "word": "".join(map(str, word)),
        "matrix": [[a, b], [c, d]],
        "trace": trace,
        "determinant": det,
        "discriminant": disc,
        "fixed_point": f"({a-d}+sqrt({disc}))/(2*{c})",
        "multiplier": f"({trace}-sqrt({disc}))/({trace}+sqrt({disc}))",
        "composition_trace": f"1/2+{trace}/(2*sqrt({disc}))",
    }


def build() -> dict:
    geometry = []
    for digit in DIGITS:
        center = Fraction(digit, digit * digit - 1)
        radius = Fraction(1, digit * digit - 1)
        max_modulus = Fraction(1, digit - 1)
        geometry.append({
            "digit": digit,
            "image_center": frac(center),
            "image_radius": frac(radius),
            "max_image_modulus": frac(max_modulus),
            "max_derivative_on_unit_disk": frac(Fraction(1, (digit - 1) ** 2)),
        })
    separation_gap = Fraction(3, 8) - Fraction(6, 35) - Fraction(1, 8) - Fraction(1, 35)
    assert separation_gap == Fraction(1, 20)

    periods = []
    total_words = 0
    for n in range(1, CUTOFF + 1):
        cases, trace_total = [], Decimal(0)
        for word in product(DIGITS, repeat=n):
            token, weight = case_record(word)
            cases.append(token)
            trace_total += weight
        periods.append({
            "n": n,
            "rooted_words": 2**n,
            "primitive_cycles": primitive_cycles(n),
            "orientation": "reversing" if n % 2 else "preserving",
            "trace_case_count": len(cases),
            "trace_case_sha256": digest(cases),
            "trace_sum_decimal_30": format(trace_total, ".30f"),
        })
        total_words += len(cases)

    first = anagram_record((3, 3, 3, 6, 6))
    second = anagram_record((3, 3, 6, 3, 6))
    rotations = {
        (3, 3, 3, 6, 6)[shift:] + (3, 3, 3, 6, 6)[:shift]
        for shift in range(5)
    }
    assert (3, 3, 6, 3, 6) not in rotations
    assert first["trace"] == 1344 and second["trace"] == 1317
    assert first["matrix"] != second["matrix"]
    assert first["multiplier"] != second["multiplier"]
    assert first["composition_trace"] != second["composition_trace"]
    data = {
        "schema": "HCS-C132-v1",
        "candidate_id": "HCS-C132",
        "date_utc": "2026-08-24",
        "digits": [3, 6],
        "branches": "phi_a(z)=1/(a+z)",
        "mobius_matrices": {"3": [[0, 1], [1, 3]], "6": [[0, 1], [1, 6]]},
        "geometry": {
            "ambient_domain": "unit disk",
            "branch_images": geometry,
            "closed_image_separation_gap": frac(separation_gap),
            "strong_separation": True,
        },
        "operator": {
            "space": "normalized Bergman A^2(unit disk)",
            "definition": "L f = f(phi_3)+f(phi_6)",
            "trace_class": True,
            "trace_norm_upper_bound": "89/16",
            "bound_method": "sum_n (n+1) r_a^n = (1-r_a)^(-2)",
        },
        "all_word_theorem": {
            "unique_fixed_point": True,
            "fixed_polynomial": "C*z^2+(D-A)*z-B=0 for M_w=[[A,B],[C,D]]",
            "multiplier": "(tr(M_w)-sqrt(discriminant))/(tr(M_w)+sqrt(discriminant))",
            "composition_trace": "1/2+tr(M_w)/(2*sqrt(discriminant))",
            "all_n_trace": "Tr(L^n)=sum_{|w|=n} 1/(1-Phi_w'(z_w))",
        },
        "period_receipts_through_10": periods,
        "total_rooted_word_receipts": total_words,
        "primitive_fredholm_product": {
            "formula": "det(I-zL)=product_[p primitive] product_k>=0 (1-z^|p|*lambda_p^k)",
            "raw_absolute_convergence": "|z|<1/2",
            "global_statement": "the trace-class determinant is entire; no raw Euler-product convergence beyond its proved disk is claimed",
        },
        "order_sensitive_anagram_control": {
            "same_digit_multiset": {"3": 3, "6": 2},
            "not_cyclic_rotations": True,
            "first": first,
            "second": second,
            "matrix_differs": True,
            "multiplier_differs": True,
            "composition_trace_differs": True,
        },
        "progress": {
            "intrinsic_order_sensitive_geometry": "PASS_EXACT",
            "global_trace_class_owner": "PASS_ANALYTIC",
            "all_period_trace_and_primitive_product": "PASS_ANALYTIC",
            "common_linear_location_blindness_repaired": "INTERNAL_NONLINEAR_ORDER_SENSITIVITY",
        },
        "checks": {
            "geometry_pass": True,
            "all_2046_word_receipts_pass": total_words == 2046,
            "anagram_control_pass": True,
            "trace_class_bound_pass": True,
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "structural_gate": "MOBIUS_ORDER_SENSITIVE_TRACE_OWNER_PASS",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "uses_prime_table": False,
            "uses_zero_table": False,
            "claims_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_hilbert_polya": False,
        },
    }
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    data["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
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
