#!/usr/bin/env python3
"""Independent exact checker for C132; it does not import the producer."""
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c132_mobius_bergman_evidence.json"
getcontext().prec = 60


def multiply(x, y):
    return [[sum(x[i][k] * y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matrix(word):
    out = [[1, 0], [0, 1]]
    for digit in word:
        out = multiply(out, [[0, 1], [1, digit]])
    return out


def mu(n):
    count, x, d = 0, n, 2
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


def primitive(n):
    return sum(mu(d) * 2 ** (n // d) for d in range(1, n + 1) if n % d == 0) // n


def token_weight(word):
    (a, b), (c, d) = matrix(word)
    determinant = a * d - b * c
    trace = a + d
    disc = trace * trace - 4 * determinant
    contraction = 1
    for digit in word:
        contraction *= (digit - 1) ** 2
    token = (
        f"{''.join(map(str, word))}:{a},{b},{c},{d}:det={determinant}:tr={trace}:disc={disc}:"
        f"fixed=({a-d}+sqrt({disc}))/(2*{c}):"
        f"lambda=({trace}-sqrt({disc}))/({trace}+sqrt({disc})):"
        f"weight=1/2+{trace}/(2*sqrt({disc})):deriv_bound=1/{contraction}"
    )
    weight = Decimal(1) / 2 + Decimal(trace) / (Decimal(2) * Decimal(disc).sqrt())
    return token, weight


def anagram(word):
    (a, b), (c, d) = matrix(word)
    determinant, trace = a * d - b * c, a + d
    disc = trace * trace - 4 * determinant
    return {
        "word": "".join(map(str, word)), "matrix": [[a, b], [c, d]],
        "trace": trace, "determinant": determinant, "discriminant": disc,
        "fixed_point": f"({a-d}+sqrt({disc}))/(2*{c})",
        "multiplier": f"({trace}-sqrt({disc}))/({trace}+sqrt({disc}))",
        "composition_trace": f"1/2+{trace}/(2*sqrt({disc}))",
    }


def validate(data: dict) -> None:
    receipt = data.pop("payload_sha256")
    payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(payload).hexdigest() == receipt
    data["payload_sha256"] = receipt
    assert set(data) == {
        "all_word_theorem",
        "branches",
        "candidate_id",
        "checks",
        "date_utc",
        "digits",
        "geometry",
        "mobius_matrices",
        "operator",
        "order_sensitive_anagram_control",
        "payload_sha256",
        "period_receipts_through_10",
        "primitive_fredholm_product",
        "progress",
        "route_a",
        "schema",
        "scope_flags",
        "total_rooted_word_receipts",
    }
    assert data["schema"] == "HCS-C132-v1"
    assert data["candidate_id"] == "HCS-C132" and data["date_utc"] == "2026-08-24"
    assert data["digits"] == [3, 6] and data["branches"] == "phi_a(z)=1/(a+z)"
    assert data["mobius_matrices"] == {"3": [[0, 1], [1, 3]], "6": [[0, 1], [1, 6]]}
    expected_geometry = {
        "ambient_domain": "unit disk",
        "branch_images": [
            {"digit": 3, "image_center": "3/8", "image_radius": "1/8", "max_image_modulus": "1/2", "max_derivative_on_unit_disk": "1/4"},
            {"digit": 6, "image_center": "6/35", "image_radius": "1/35", "max_image_modulus": "1/5", "max_derivative_on_unit_disk": "1/25"},
        ],
        "closed_image_separation_gap": "1/20", "strong_separation": True,
    }
    assert data["geometry"] == expected_geometry
    assert data["operator"] == {
        "space": "normalized Bergman A^2(unit disk)",
        "definition": "L f = f(phi_3)+f(phi_6)",
        "trace_class": True,
        "trace_norm_upper_bound": "89/16",
        "bound_method": "sum_n (n+1) r_a^n = (1-r_a)^(-2)",
    }
    assert data["all_word_theorem"] == {
        "unique_fixed_point": True,
        "fixed_polynomial": "C*z^2+(D-A)*z-B=0 for M_w=[[A,B],[C,D]]",
        "multiplier": "(tr(M_w)-sqrt(discriminant))/(tr(M_w)+sqrt(discriminant))",
        "composition_trace": "1/2+tr(M_w)/(2*sqrt(discriminant))",
        "all_n_trace": "Tr(L^n)=sum_{|w|=n} 1/(1-Phi_w'(z_w))",
    }
    total = 0
    for n, row in enumerate(data["period_receipts_through_10"], 1):
        lines, trace_total = [], Decimal(0)
        for word in product((3, 6), repeat=n):
            case, weight = token_weight(word)
            lines.append(case)
            trace_total += weight
        assert row == {
            "n": n, "rooted_words": 2**n, "primitive_cycles": primitive(n),
            "orientation": "reversing" if n % 2 else "preserving",
            "trace_case_count": len(lines),
            "trace_case_sha256": hashlib.sha256("\n".join(lines).encode()).hexdigest(),
            "trace_sum_decimal_30": format(trace_total, ".30f"),
        }
        total += len(lines)
    assert data["total_rooted_word_receipts"] == total == 2046
    assert data["primitive_fredholm_product"] == {
        "formula": "det(I-zL)=product_[p primitive] product_k>=0 (1-z^|p|*lambda_p^k)",
        "raw_absolute_convergence": "|z|<1/2",
        "global_statement": "the trace-class determinant is entire; no raw Euler-product convergence beyond its proved disk is claimed",
    }
    control = data["order_sensitive_anagram_control"]
    assert control["same_digit_multiset"] == {"3": 3, "6": 2}
    assert control["not_cyclic_rotations"] is True
    assert control["first"] == anagram((3, 3, 3, 6, 6))
    assert control["second"] == anagram((3, 3, 6, 3, 6))
    first_word, second_word = (3, 3, 3, 6, 6), (3, 3, 6, 3, 6)
    assert second_word not in {
        first_word[shift:] + first_word[:shift] for shift in range(len(first_word))
    }
    assert control["first"]["trace"] == 1344 and control["second"]["trace"] == 1317
    assert control["first"]["matrix"] != control["second"]["matrix"]
    assert control["first"]["multiplier"] != control["second"]["multiplier"]
    assert control["first"]["composition_trace"] != control["second"]["composition_trace"]
    assert all(control[key] for key in ["matrix_differs", "multiplier_differs", "composition_trace_differs"])
    assert data["progress"] == {
        "intrinsic_order_sensitive_geometry": "PASS_EXACT",
        "global_trace_class_owner": "PASS_ANALYTIC",
        "all_period_trace_and_primitive_product": "PASS_ANALYTIC",
        "common_linear_location_blindness_repaired": "INTERNAL_NONLINEAR_ORDER_SENSITIVITY",
    }
    assert data["checks"] == {
        "all_2046_word_receipts_pass": True,
        "anagram_control_pass": True,
        "geometry_pass": True,
        "trace_class_bound_pass": True,
    }
    assert data["route_a"] == {
        "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        "structural_gate": "MOBIUS_ORDER_SENSITIVE_TRACE_OWNER_PASS",
        "route_b_invocation_allowed": False,
    }
    assert data["scope_flags"] == {
        "claims_automorphy": False,
        "claims_euler_factors": False,
        "claims_hilbert_polya": False,
        "claims_root_number": False,
        "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "uses_prime_table": False,
        "uses_zero_table": False,
    }


if __name__ == "__main__":
    validate(json.loads(EVIDENCE.read_text()))
    print("C132 independent checker: PASS (2,046 exact word receipts)")
