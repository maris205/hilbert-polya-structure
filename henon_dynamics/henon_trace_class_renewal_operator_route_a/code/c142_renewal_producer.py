#!/usr/bin/env python3
"""Produce the exact HCS-C142 trace-class renewal evidence receipt."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


COEFFICIENT_CUTOFF = 16
TRACE_CUTOFF = 12
PRIMITIVE_CLOCK_CUTOFF = 10
FINITE_SECTION_SIZE = 14
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def q(x: Fraction | int) -> str:
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def renewal_coefficient(m: int) -> Fraction:
    return Fraction(1, 2 ** (m * (m + 1) // 2))


def zero_matrix(n: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    out = zero_matrix(n)
    for i in range(n):
        for k in range(n):
            if not a[i][k]:
                continue
            for j in range(n):
                if b[k][j]:
                    out[i][j] += a[i][k] * b[k][j]
    return out


def renewal_matrix(n: int) -> list[list[Fraction]]:
    """Matrix convention: column j is T e_j."""
    out = zero_matrix(n)
    for j in range(n):
        out[0][j] += Fraction(1, 2 ** (j + 1))
        if j + 1 < n:
            out[j + 1][j] += Fraction(1, 2 ** (j + 1))
    return out


def matrix_traces(n: int, cutoff: int) -> list[Fraction]:
    t = renewal_matrix(n)
    power = [row[:] for row in t]
    values = []
    for k in range(1, cutoff + 1):
        values.append(sum(power[i][i] for i in range(n)))
        if k != cutoff:
            power = matmul(power, t)
    return values


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[i:] + word[:i] for i in range(len(word)))


def is_primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(n % d or word != word[:d] * (n // d) for d in range(1, n))


def compositions(total: int) -> list[tuple[int, ...]]:
    if total == 0:
        return [()]
    ans: list[tuple[int, ...]] = []
    for mask in range(1 << (total - 1)):
        parts = []
        last = 0
        for j in range(total - 1):
            if mask & (1 << j):
                parts.append(j + 1 - last)
                last = j + 1
        parts.append(total - last)
        ans.append(tuple(parts))
    return ans


def primitive_necklaces(total: int) -> list[tuple[int, ...]]:
    return sorted({w for w in compositions(total) if is_primitive(w) and canonical_rotation(w) == w})


def word_weight(word: tuple[int, ...]) -> Fraction:
    ans = Fraction(1)
    for m in word:
        ans *= renewal_coefficient(m)
    return ans


def payload_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build_evidence() -> dict:
    traces = matrix_traces(FINITE_SECTION_SIZE, TRACE_CUTOFF)
    primitive_rows = []
    for clock in range(1, PRIMITIVE_CLOCK_CUTOFF + 1):
        words = primitive_necklaces(clock)
        primitive_rows.append({
            "clock": clock,
            "count": len(words),
            "weight_sum": q(sum((word_weight(w) for w in words), Fraction(0))),
            "words": ["-".join(map(str, w)) for w in words],
        })

    payload = {
        "schema": "hcs-c142-renewal-evidence-v1",
        "candidate_id": "HCS-C142",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_lock": {
            "object": "T=S+R on l2(N0), S e_n=2^(-(n+1))e_(n+1), R e_n=2^(-(n+1))e_0",
            "clock": "one directed graph edge; an excursion of length m has clock m",
            "normalization": "a_n=b_n=2^(-(n+1)); no fitted parameter",
            "determinant_convention": "D(z)=det_F(I-zT)",
            "cutoff": {
                "coefficient": COEFFICIENT_CUTOFF,
                "trace": TRACE_CUTOFF,
                "primitive_clock": PRIMITIVE_CLOCK_CUTOFF,
                "finite_section_size": FINITE_SECTION_SIZE,
            },
            "precision": "exact rational arithmetic",
            "allowed_data": "the frozen weighted renewal graph only",
            "forbidden_data": "prime tables, target zero tables, arithmetic local factors, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "operator_theorem": {
            "shift_trace_norm": "1",
            "return_trace_norm": "1/sqrt(3)",
            "operator_trace_norm_upper_bound": "1+1/sqrt(3)",
            "renewal_coefficient_formula": "c_m=2^(-m(m+1)/2)",
            "fredholm_determinant_formula": "D(z)=1-sum_(m>=1)c_m z^m",
            "entire_order": "0",
            "primitive_product_domain": "absolute on |z|<(1+1/sqrt(3))^(-1)",
        },
        "coefficient_ledger": [
            {"m": m, "triangular_exponent": m * (m + 1) // 2, "c_m": q(renewal_coefficient(m))}
            for m in range(1, COEFFICIENT_CUTOFF + 1)
        ],
        "trace_ledger": [{"n": n, "trace_Tn": q(v)} for n, v in enumerate(traces, 1)],
        "primitive_ledger": primitive_rows,
        "finite_section_certificate": {
            "size": FINITE_SECTION_SIZE,
            "determinant_prefix": "1-" + "-".join(
                f"({q(renewal_coefficient(m))})z^{m}" for m in range(1, FINITE_SECTION_SIZE + 1)
            ),
            "trace_exact_through": TRACE_CUTOFF,
        },
        "negative_control": {
            "object": "replace b_n by 1/2 while retaining a_n=2^(-(n+1))",
            "formal_first_return_coefficient": "2^(-(2m-1))",
            "formal_scalar_determinant": "(1-3z/4)/(1-z/4)",
            "operator_fact": "the weighted shift has singular value 1/2 with infinite multiplicity",
            "verdict": "NONCOMPACT_NOT_ORDINARY_FREDHOLM_DETERMINANT_CLASS",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "prime_like_correspondence": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
        },
    }
    payload["payload_sha256"] = payload_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results/c142_renewal_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "payload_sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
