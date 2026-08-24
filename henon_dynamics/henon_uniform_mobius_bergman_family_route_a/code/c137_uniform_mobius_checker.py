#!/usr/bin/env python3
"""Independent exact checker for C137; never imports the producer."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c137_uniform_mobius_evidence.json"
A_VALUES = (Fraction(3), Fraction(13, 4), Fraction(7, 2))
B_VALUES = (Fraction(6), Fraction(13, 2), Fraction(7))


def fs(x) -> str:
    q = Fraction(x)
    return f"{q.numerator}/{q.denominator}"


def mul(x, y):
    return [[sum(x[i][k] * y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matrix(word, a, b):
    out = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    mats = ([[Fraction(0), Fraction(1)], [Fraction(1), a]],
            [[Fraction(0), Fraction(1)], [Fraction(1), b]])
    for letter in word:
        out = mul(out, mats[letter])
    return out


def mu(n):
    x, count, d = n, 0, 2
    while d*d <= x:
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


def primitive(n):
    return sum(mu(d) * 2**(n//d) for d in range(1, n+1) if n % d == 0) // n


def token(word, a, b):
    (A, B), (C, D) = matrix(word, a, b)
    determinant = A*D-B*C
    trace = A+D
    disc = trace*trace-4*determinant
    name = "".join("a" if x == 0 else "b" for x in word)
    return (f"a={fs(a)}:b={fs(b)}:{name}:M={fs(A)},{fs(B)},{fs(C)},{fs(D)}:"
            f"det={fs(determinant)}:tr={fs(trace)}:disc={fs(disc)}:"
            f"fixed=({fs(A-D)}+sqrt({fs(disc)}))/(2*{fs(C)}):"
            f"lambda=({fs(trace)}-sqrt({fs(disc)}))/({fs(trace)}+sqrt({fs(disc)}))")


def tformula(a, b, first):
    if first:
        return a**3*b**2+a**3+2*a**2*b+2*a*b**2+3*a+2*b
    return a**3*b**2+4*a**2*b+a*b**2+3*a+2*b


def validate(data: dict) -> None:
    receipt = data.pop("payload_sha256")
    assert hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":")).encode()).hexdigest() == receipt
    data["payload_sha256"] = receipt
    assert set(data) == {"all_word_theorem", "candidate_id", "date_utc", "family", "grid_receipts", "nonclaims", "order_sensitive_uniform_control", "payload_sha256", "progress", "receipt_summary", "route_a", "schema", "scope", "scope_flags", "uniform_geometry", "uniform_operator_bounds"}
    assert data["schema"] == "HCS-C137-uniform-mobius-bergman-v1"
    assert data["candidate_id"] == "HCS-C137" and data["date_utc"] == "2026-08-24"
    assert data["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert data["family"] == {"branches": "phi_x(z)=1/(x+z)", "operator": "L_(a,b)=C_phi_a+C_phi_b", "parameter_rectangle": {"a": ["3/1", "7/2"], "b": ["6/1", "7/1"]}, "space": "normalized Bergman A^2(unit disk)"}
    assert data["uniform_geometry"] == {
        "image_disk": "center=x/(x^2-1), radius=1/(x^2-1)",
        "closed_image_gap_formula": "g(a,b)=1/(a+1)-1/(b-1)",
        "minimum_gap": "1/45", "minimum_corner": ["7/2", "6/1"],
        "strong_separation_uniform": True,
        "negative_rectangle": {"a": ["3/1", "4/1"], "b": ["6/1", "7/1"], "minimum_gap": "0/1", "tangent_corner": ["4/1", "6/1"], "positive_closed_gap": False},
    }
    assert data["uniform_operator_bounds"] == {
        "trace_class": True, "trace_norm_upper_bound": "89/16",
        "trace_norm_lipschitz": "||L_(a,b)-L_(a',b')||_1 <= 4|a-a'|+(5/32)|b-b'|",
        "a_lipschitz_constant": "4/1", "b_lipschitz_constant": "5/32",
        "proof_majorant": "sum_(n>=1) (n+1)n r^(n-1) delta = 2 delta/(1-r)^3",
    }
    assert set(data["all_word_theorem"]) == {"composition_trace", "determinant_global_domain", "fixed_point", "fredholm_product", "matrix", "multiplier", "power_trace", "raw_absolute_convergence"}
    assert data["all_word_theorem"]["matrix"] == "M_x=[[0,1],[1,x]]"
    assert data["all_word_theorem"]["fixed_point"] == "(A-D+sqrt(Delta))/(2C)"
    assert data["all_word_theorem"]["multiplier"] == "(t-sqrt(Delta))/(t+sqrt(Delta))"
    assert data["all_word_theorem"]["composition_trace"] == "1/2+t/(2sqrt(Delta))"
    assert data["all_word_theorem"]["power_trace"] == "Tr(L_(a,b)^n)=sum_(|w|=n) 1/(1-lambda_w)"
    assert data["all_word_theorem"]["fredholm_product"] == "det(I-zL)=product_[p primitive] product_(k>=0)(1-z^|p| lambda_p^k)"
    assert data["all_word_theorem"]["raw_absolute_convergence"] == "|z|<1/2"
    assert data["all_word_theorem"]["determinant_global_domain"] == "entire by trace class; no raw-product claim outside |z|<1/2"
    total = 0
    assert len(data["grid_receipts"]) == 9
    for record, (a, b) in zip(data["grid_receipts"], product(A_VALUES, B_VALUES)):
        assert set(record) == {"a", "aaabb_trace", "aabab_trace", "b", "closed_image_gap", "period_receipts_through_10", "trace_gap"}
        assert record["a"] == fs(a) and record["b"] == fs(b)
        assert record["closed_image_gap"] == fs(1/(a+1)-1/(b-1))
        for n, row in enumerate(record["period_receipts_through_10"], 1):
            lines = [token(word, a, b) for word in product((0, 1), repeat=n)]
            expected = {"n": n, "rooted_words": 2**n, "primitive_cycles": primitive(n), "trace_case_count": 2**n, "trace_case_sha256": hashlib.sha256("\n".join(lines).encode()).hexdigest()}
            assert row == expected
            total += len(lines)
        t1, t2 = tformula(a, b, True), tformula(a, b, False)
        assert record["aaabb_trace"] == fs(t1) and record["aabab_trace"] == fs(t2)
        assert record["trace_gap"] == fs(t1-t2) == fs(a*(b-a)**2)
    assert total == 18414
    assert data["receipt_summary"] == {"parameter_points": 9, "primitive_classes_per_parameter_through_10": 226, "primitive_parameter_receipts_through_10": 2034, "rooted_word_receipts_through_10": 18414, "theorem_parameter_domain": "entire frozen rectangle; grid is replay only"}
    control = data["order_sensitive_uniform_control"]
    assert set(control) == {"composition_trace_gap_lower_bound", "composition_trace_gap_positive", "first_trace_formula", "first_trace_upper_bound", "not_cyclic_rotations", "second_trace_formula", "trace_gap_identity", "uniform_trace_gap_lower_bound", "words"}
    assert control == {
        "words": ["aaabb", "aabab"], "not_cyclic_rotations": True,
        "first_trace_formula": "a^3*b^2+a^3+2*a^2*b+2*a*b^2+3*a+2*b",
        "second_trace_formula": "a^3*b^2+4*a^2*b+a*b^2+3*a+2*b",
        "trace_gap_identity": "t_aaabb-t_aabab=a*(b-a)^2",
        "uniform_trace_gap_lower_bound": "175/8", "first_trace_upper_bound": "10731/4",
        "composition_trace_gap_lower_bound": "2800/(10731^2+64)^(3/2)", "composition_trace_gap_positive": True,
    }
    assert data["progress"] == {"all_word_trace_product": "PASS_ANALYTIC", "uniform_nuclearity_and_lipschitz": "PASS_ANALYTIC", "uniform_order_sensitivity": "PASS_EXACT", "uniform_separation": "PASS_EXACT"}
    assert data["route_a"] == {"overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False, "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]}
    assert data["scope_flags"] == {"claims_automorphy": False, "claims_euler_factors": False, "claims_hilbert_polya": False, "claims_root_number": False, "claims_target_divisor": False, "uses_prime_table": False, "uses_zero_table": False}
    assert data["nonclaims"] == ["no prime-like target correspondence", "no target divisor or zero census", "no target functional equation or counting law", "no natural unitary, scattering, or self-adjoint lift", "no Euler-factor, root-number, automorphy, or Hilbert--Polya claim"]


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    validate(json.loads(path.read_text()))
    print("C137 independent checker: PASS (18,414 exact word receipts)")


if __name__ == "__main__":
    main()
