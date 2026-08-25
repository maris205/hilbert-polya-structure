#!/usr/bin/env python3
"""Independent exact checker for C141; this file never imports the producer."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c141_quadratic_ruelle_evidence.json"
CHECKS = 0


def expect(condition: bool, message: str) -> None:
    global CHECKS
    assert condition, message
    CHECKS += 1


def trim(p):
    p = [Fraction(x) for x in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return trim(out)


def sub(a, b):
    return add(a, [-Fraction(x) for x in b])


def mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return trim(out)


def divmod_poly(a, b):
    a, b = trim(a), trim(b)
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        degree = len(a) - len(b)
        scale = a[-1] / b[-1]
        q[degree] += scale
        a = sub(a, [Fraction(0)] * degree + [scale * x for x in b])
    return trim(q), trim(a)


def mod(a, p):
    return divmod_poly(a, p)[1]


def xgcd(a, b):
    old_r, r = trim(a), trim(b)
    old_s, s = [Fraction(1)], [Fraction(0)]
    old_t, t = [Fraction(0)], [Fraction(1)]
    while r != [0]:
        q, new_r = divmod_poly(old_r, r)
        old_r, r = r, new_r
        old_s, s = s, sub(old_s, mul(q, s))
        old_t, t = t, sub(old_t, mul(q, t))
    scale = old_r[-1]
    return [x / scale for x in old_r], [x / scale for x in old_s], [x / scale for x in old_t]


def derivative(p):
    return trim([Fraction(i) * p[i] for i in range(1, len(p))] or [0])


def trace_inverse(denominator, modulus):
    gcd, inverse, _ = xgcd(denominator, modulus)
    assert gcd == [Fraction(1)]
    inverse = mod(inverse, modulus)
    degree = len(modulus) - 1
    total = Fraction(0)
    for j in range(degree):
        image = mod([Fraction(0)] * j + inverse, modulus)
        if j < len(image): total += image[j]
    return total


def fs(q):
    q = Fraction(q)
    return f"{q.numerator}/{q.denominator}"


def mu(n):
    x, count, d = n, 0, 2
    while d * d <= x:
        if x % d == 0:
            x //= d; count += 1
            if x % d == 0: return 0
            while x % d == 0: x //= d
        d += 1
    if x > 1: count += 1
    return -1 if count % 2 else 1


def primitive(n):
    return sum(mu(d) * 2 ** (n // d) for d in range(1, n + 1) if n % d == 0) // n


def validate(data: dict, recompute_core: bool = True) -> int:
    receipt = data.pop("payload_sha256")
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    expect(hashlib.sha256(canonical).hexdigest() == receipt, "payload hash")
    data["payload_sha256"] = receipt
    expect(set(data) == {"all_period_theorem", "candidate_id", "date_utc", "geometry_and_nuclearity", "headline_exact_prefix", "negative_control", "nonclaims", "payload_sha256", "primitive_product", "progress", "receipt_summary", "route_a", "schema", "scope", "scope_flags", "source_lock", "weight_ladder_controls"}, "top-level schema")
    expect(data["schema"] == "HCS-C141-quadratic-inverse-branch-ruelle-v1", "schema literal")
    expect(data["candidate_id"] == "HCS-C141" and data["date_utc"] == "2026-08-25", "identity/date")
    expect(data["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    source = data["source_lock"]
    expect(set(source) == {"clock", "cutoff", "determinant_convention", "domain", "forward_map", "headline_weight", "inverse_branches", "operator_family", "precision", "space", "square_root_convention"}, "source-lock keys")
    expect(source["forward_map"] == "F(z)=z^2-6", "forward map")
    expect(source["domain"] == "D_4={z:|z|<4}", "domain")
    expect(source["inverse_branches"] == "psi_+(z)=sqrt(z+6), psi_-(z)=-sqrt(z+6)", "branches")
    expect(source["square_root_convention"] == "principal square root on D(6,4), contained in Re(w)>0", "root convention")
    expect(source["space"] == "Hardy H^2(D_4), normalized basis e_j(z)=(z/4)^j", "space")
    expect(source["operator_family"] == "(L_m f)(z)=sum_(epsilon=+,-) (psi_epsilon'(z))^m f(psi_epsilon(z))", "operator")
    expect(source["headline_weight"] == "m=2", "headline weight")
    expect(source["clock"] == "one inverse branch per iterate", "clock")
    expect(source["determinant_convention"] == "D_2(u)=det(I-u L_2)", "determinant convention")
    expect(source["cutoff"] == "no theorem cutoff; n=1..6 is an exact replay prefix", "cutoff")
    expect(source["precision"] == "exact integer and rational quotient-algebra arithmetic", "precision")

    geometry = data["geometry_and_nuclearity"]
    expect(geometry == {
        "branch_real_part_separation": "Re(psi_+)>=sqrt(2), Re(psi_-)<=-sqrt(2)",
        "derivative_bound": "q=1/(2*sqrt(2))",
        "image_radius_upper_bound": "sqrt(10)<4",
        "nuclear_decomposition": "sum_(epsilon,j) [(psi_epsilon')^2 (psi_epsilon/4)^j] tensor e_j^*",
        "squared_weight_bound": "sup|psi_epsilon'|^2<=1/8",
        "trace_class": True,
        "trace_norm_upper_bound": "1/(4-sqrt(10))",
    }, "geometry/nuclearity block")

    theorem = data["all_period_theorem"]
    expect(set(theorem) == {"escape_bound", "headline_trace_formula", "periodic_points_exhausted", "periodic_polynomial", "power_trace_formula", "primitive_count_formula", "simple_roots", "unique_word_fixed_points"}, "theorem keys")
    expect(theorem["periodic_points_exhausted"] is True, "point exhaustion")
    expect(theorem["escape_bound"] == "|z|>3 implies |F(z)|>|z|; hence every periodic point lies in D_4", "escape bound")
    expect(theorem["unique_word_fixed_points"] == "every length-n inverse word is a q^n contraction and has one fixed point", "word fixed points")
    expect(theorem["simple_roots"] == "all roots of F^n(z)-z are simple because inverse multipliers have modulus <1", "simple roots")
    expect(theorem["power_trace_formula"] == "Tr(L_m^n)=sum_(F^n(p)=p) Lambda_n(p)^(-m)/(1-Lambda_n(p)^(-1))", "all-m trace")
    expect(theorem["headline_trace_formula"] == "Tr(L_2^n)=sum_(F^n(p)=p) 1/(Lambda_n(p)*(Lambda_n(p)-1))", "headline trace")
    expect(theorem["periodic_polynomial"] == "P_n(z)=F^n(z)-z is monic of degree 2^n", "periodic polynomial")
    expect(theorem["primitive_count_formula"] == "P_n=(1/n) sum_(d|n) mu(d) 2^(n/d)", "primitive count")

    expected_traces = ["1/12", "7/720", "239/257472", "1255703/13810694400", "235072563599/26491011084499968", "655398850662090042240821783/756396676602907446734765701632000"]
    prefix = data["headline_exact_prefix"]
    expect(set(prefix) == {"fredholm_coefficients_c0_through_c6", "newton_recurrence", "periods", "trace_prefix"}, "prefix keys")
    expect(prefix["trace_prefix"] == expected_traces, "trace vector")
    iterate = [Fraction(0), Fraction(1)]
    recomputed = []
    for n, row in enumerate(prefix["periods"], 1):
        iterate = add(mul(iterate, iterate), [-6])
        periodic = iterate[:]; periodic[1] -= 1; periodic = trim(periodic)
        lam = derivative(iterate); lm1 = lam[:]; lm1[0] -= 1
        trace = trace_inverse(mul(lam, lm1), periodic) if recompute_core else Fraction(expected_traces[n - 1])
        recomputed.append(trace)
        expect(set(row) == {"degree", "n", "periodic_polynomial_coefficients_low_to_high", "periodic_polynomial_sha256", "primitive_orbits", "rooted_inverse_words", "trace_L2_power"}, f"row {n} keys")
        expect(row["n"] == n and row["degree"] == 2 ** n, f"row {n} identity")
        expect(row["rooted_inverse_words"] == 2 ** n and row["primitive_orbits"] == primitive(n), f"row {n} counts")
        expect(row["periodic_polynomial_coefficients_low_to_high"] == [int(x) for x in periodic], f"row {n} polynomial")
        token = ",".join(str(int(x)) for x in periodic).encode()
        expect(row["periodic_polynomial_sha256"] == hashlib.sha256(token).hexdigest(), f"row {n} polynomial hash")
        expect(row["trace_L2_power"] == fs(trace) == expected_traces[n - 1], f"row {n} quotient trace")
    expect(len(prefix["periods"]) == 6, "six period rows")
    coefficients = [Fraction(1)]
    for n in range(1, 7):
        coefficients.append(-sum(coefficients[n-j] * recomputed[j-1] for j in range(1, n+1)) / n)
    expect(prefix["fredholm_coefficients_c0_through_c6"] == [fs(x) for x in coefficients], "Newton coefficients")
    expect(prefix["newton_recurrence"] == "c_0=1; c_n=-(1/n) sum_(j=1)^n c_(n-j) Tr(L_2^j)", "Newton recurrence")

    controls = data["weight_ladder_controls"]
    expect(controls == {
        "first_nontrivial_stability_weight": "m=2",
        "lagrange_identity": "sum_(P_n(p)=0) 1/P_n'(p)=0 for deg(P_n)>=2",
        "m0_determinant": "det(I-u L_0)=1-2u",
        "m0_trace_formula": "Tr(L_0^n)=2^n",
        "m0_trace_prefix": [2, 4, 8, 16, 32, 64],
        "m1_determinant": "det(I-u L_1)=1",
        "m1_trace_formula": "Tr(L_1^n)=0",
        "m1_trace_prefix": [0, 0, 0, 0, 0, 0],
    }, "m=0/1 controls")

    product = data["primitive_product"]
    expect(set(product) == {"absolute_majorant", "formula", "global_statement", "index_reason", "inner_index_starts_at", "raw_product_absolute_convergence_domain"}, "product keys")
    expect(product["formula"] == "D_2(u)=product_[p primitive] product_(k>=2) (1-u^ell(p)*Lambda_p^(-k))", "product formula")
    expect(product["inner_index_starts_at"] == 2, "product start")
    expect(product["index_reason"] == "mu^(2r)/(1-mu^r)=sum_(k>=2) mu^(kr), with mu=Lambda_p^(-1)", "product index proof")
    expect(product["raw_product_absolute_convergence_domain"] == "|u|<4", "product disk")
    expect(product["absolute_majorant"] == "sum_(n>=1) |u|^n*4^(-n)/(n*(1-q^n))", "product majorant")
    expect(product["global_statement"] == "D_2 is entire by trace class; no raw-product convergence is claimed outside |u|<4", "global/product boundary")

    expect(data["negative_control"] == {"boundary": "this rejects only the same D_4 branch construction, not every possible operator space", "map": "F_control(z)=z^2-2", "reason": "the branch point -2 lies inside D_4, so z+2 has no global holomorphic square root on D_4", "same_D4_branch_model_valid": False}, "negative control")
    expect(data["receipt_summary"] == {"fredholm_taylor_degree": 6, "primitive_orbits_through_6": 23, "rooted_periodic_points_through_6": 126, "theorem_period_cutoff": "none", "trace_prefix_length": 6}, "summary")
    expect(data["progress"] == {"all_period_trace": "PASS_EXACT", "geometry": "PASS_ANALYTIC", "headline": "first unconditional nonlinear polynomial inverse-branch Hardy trace-class package in this series, with all-period exhaustion and a stability-weight control ladder", "m0_m1_controls": "PASS_EXACT", "over_prior_gate": "advances beyond finite polynomial matrices, real count models, and Möbius word matrices to a single nonlinear complex polynomial with intrinsic inverse branches and exact m=2 stability traces", "primitive_product": "PASS_IN_PROVED_DISK", "trace_class": "PASS_ANALYTIC"}, "progress")
    expect(data["route_a"] == {"overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False, "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]}, "Route-A verdict")
    expect(data["scope_flags"] == {"claims_automorphy": False, "claims_euler_factors": False, "claims_hilbert_polya": False, "claims_root_number": False, "claims_target_divisor": False, "uses_prime_table": False, "uses_zero_table": False}, "scope flags")
    expect(data["nonclaims"] == ["no prime-like target correspondence or target zero census", "no target functional equation, counting law, or divisor match", "no arithmetic/local data, Euler factor, root number, or automorphy claim", "no natural unitary, self-adjoint, metaplectic, or Hilbert--Polya operator", "no raw primitive-product convergence claim outside |u|<4", "no novelty claim for general Ruelle or weighted-composition theory"], "nonclaims")
    return CHECKS


def main() -> None:
    fast = "--fast" in sys.argv[1:]
    positional = [arg for arg in sys.argv[1:] if arg != "--fast"]
    path = Path(positional[0]) if positional else DEFAULT
    checks = validate(json.loads(path.read_text()), recompute_core=not fast)
    mode = "semantic-fast" if fast else "full-exact"
    print(f"C141 independent checker: PASS ({checks} assertions; {mode})")


if __name__ == "__main__":
    main()
