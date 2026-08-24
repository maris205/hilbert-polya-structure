#!/usr/bin/env python3
"""Independent standard-library checker for C134; imports no producer code."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c134_character_evidence.json"


def fs(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def add(a, b):
    out = dict(a)
    for exponent, coefficient in b.items():
        out[exponent] = out.get(exponent, Fraction(0)) + coefficient
    return {e: c for e, c in out.items() if c}


def mul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            out[ea + eb] = out.get(ea + eb, Fraction(0)) + ca * cb
    return {e: c for e, c in out.items() if c}


def scale(a, value):
    return {e: Fraction(value) * c for e, c in a.items() if value * c}


def mono(exponent, coefficient=1):
    return {exponent: Fraction(coefficient)} if coefficient else {}


def scalar(value):
    return mono(0, value)


def receipt(poly):
    return {str(e): fs(poly[e]) for e in sorted(poly)}


def eye(n):
    return [[scalar(i == j) for j in range(n)] for i in range(n)]


def mmul(a, b):
    rows = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            total = {}
            for k in range(len(b)):
                total = add(total, mul(a[i][k], b[k][j]))
            row.append(total)
        rows.append(row)
    return rows


def mpow(matrix, n):
    out = eye(len(matrix))
    base = matrix
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def trace(matrix):
    out = {}
    for i in range(len(matrix)):
        out = add(out, matrix[i][i])
    return out


def matrix(B, weights, translations):
    return [[mono(translations[j], weights[j] * B[i][j]) for j in range(3)] for i in range(3)]


def coefficients(traces, degree):
    out = [scalar(1)]
    for n in range(1, degree + 1):
        total = {}
        for k in range(1, n + 1):
            total = add(total, mul(traces[k], out[n - k]))
        out.append(scale(total, Fraction(-1, n)))
    return out


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def qpow(n):
    base = (Fraction(3, 5), Fraction(4, 5))
    if n < 0:
        base = (base[0], -base[1])
        n = -n
    out = (Fraction(1), Fraction(0))
    while n:
        if n & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        n //= 2
    return out


def greceipt(value):
    return {"real": fs(value[0]), "imag": fs(value[1])}


def eval_q(poly):
    total = (Fraction(0), Fraction(0))
    for exponent, coefficient in poly.items():
        value = qpow(exponent)
        total = (total[0] + coefficient * value[0], total[1] + coefficient * value[1])
    return total


def mod5(poly):
    row = [Fraction(0)] * 5
    for exponent, coefficient in poly.items():
        row[exponent % 5] += coefficient
    return [fs(value) for value in row]


def delta(t):
    return [scalar(1), mono(t[0], Fraction(-1, 2)), mono(t[0] + t[1], Fraction(-1, 6)), mono(sum(t), Fraction(-1, 30))]


def primitive(word):
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least(word):
    return min(word[k:] + word[:k] for k in range(len(word)))


def admissible(word, B):
    return all(B[word[k]][word[(k + 1) % len(word)]] for k in range(len(word)))


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    data = json.loads(path.read_text())
    checks = 0

    def ck(condition, label):
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    def keys(mapping, expected, label):
        ck(set(mapping) == set(expected), label)

    keys(data, {"schema", "candidate_id", "date_utc", "scope_literal", "source_lock", "frozen_family", "all_order_operator", "universal_recovery", "controls", "replay_prefix", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "payload keys")
    ck(data["schema"] == "HCS-C134-v1", "schema")
    ck(data["candidate_id"] == "HCS-C134", "candidate")
    ck(data["date_utc"] == "2026-08-24", "date")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")

    lock = data["source_lock"]
    keys(lock, {"linear_part_A", "adjacency_B", "weights", "scaled_family", "clock", "normalization", "determinant_convention", "precision", "cutoff", "forbidden_data"}, "source lock keys")
    ck(lock["linear_part_A"] == [["3/16", "-1/32"], ["1/4", "0"]], "A lock")
    ck(lock["adjacency_B"] == [[1, 1, 0], [1, 0, 1], [1, 0, 0]], "B lock")
    ck(lock["weights"] == ["1/2", "1/3", "1/5"], "weights lock")
    ck(lock["scaled_family"] == "k>=1, translations are any branch permutation of (-2k,0,2k), Hardy bidisc radius 3k", "family lock")
    ck(lock["clock"] == "one admissible graph edge per iterate", "clock lock")
    ck(lock["normalization"] == "chi_u(m)=u^m on the integer translation lattice; u is a labelled U(1) parameter", "normalization lock")
    ck(lock["determinant_convention"] == "D_t,u(z)=det(I-z*L_t,u)", "det convention")
    ck(lock["precision"] == "exact Laurent polynomials over Q and Gaussian rationals at q=(3+4i)/5", "precision lock")
    ck(lock["cutoff"] == "none in theorem; periods and Taylor orders 1 through 8 are replay only", "cutoff lock")
    ck("prime or zero tables" in lock["forbidden_data"], "forbidden data")

    family = data["frozen_family"]
    keys(family, {"A_eigenvalues", "A_infinity_norm", "universal_character_ring", "faithful_anchor_q", "q_inverse", "faithfulness_certificate", "operator", "geometry_theorem", "examples"}, "family keys")
    ck(family["A_eigenvalues"] == ["1/8", "1/16"], "eigenvalues")
    ck(family["A_infinity_norm"] == "1/4", "norm")
    ck(family["faithful_anchor_q"] == {"real": "3/5", "imag": "4/5"}, "q")
    ck(family["q_inverse"] == {"real": "3/5", "imag": "-4/5"}, "q inverse")
    ck(family["faithfulness_certificate"] == "q has quadratic trace 6/5, hence is not an algebraic integer or a root of unity; q^m=q^n implies m=n", "faithfulness headline")
    ck(family["operator"] == "(L_t,u f)_i=sum_j B_ij*c_j*u^(t_j)*f_j(Az+(t_j,0))", "operator")
    ck(family["geometry_theorem"] == "for every k>=1 and every branch permutation: radii=(21k/32,3k/4), strict first-coordinate margin=11k/32, and minimum gap=11k/16", "geometry theorem")

    B = [[1, 1, 0], [1, 0, 1], [1, 0, 0]]
    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)]
    rebuilt = {}
    for k in (1, 6):
        t = [-2 * k, 0, 2 * k]
        W = matrix(B, weights, t)
        symbolic = {n: trace(mpow(W, n)) for n in range(1, 9)}
        hardy = {n: scale(symbolic[n], 1 / ((1 - Fraction(1, 8) ** n) * (1 - Fraction(1, 16) ** n))) for n in range(1, 9)}
        coeff = coefficients(hardy, 8)
        expected = {
            "translations": [str(v) for v in t],
            "domain_radius": str(3 * k),
            "first_coordinate_radius": fs(Fraction(21 * k, 32)),
            "second_coordinate_radius": fs(Fraction(3 * k, 4)),
            "pairwise_minimum_gap": fs(Fraction(11 * k, 16)),
            "strict_interior_margin_first_coordinate": fs(Fraction(11 * k, 32)),
            "partial_sum_exponents": [t[0], t[0] + t[1], sum(t)],
            "decoded_translations": [str(v) for v in t],
            "symbolic_delta_z0_to_z3": [receipt(value) for value in delta(t)],
            "q_delta_z0_to_z3": [greceipt(eval_q(value)) for value in delta(t)],
            "universal_hardy_traces_n1_to_8": {str(n): receipt(hardy[n]) for n in range(1, 9)},
            "universal_fredholm_coefficients_z0_to_z8": [receipt(value) for value in coeff],
            "z5_symbolic_traces_n1_to_8": {str(n): mod5(symbolic[n]) for n in range(1, 9)},
        }
        ck(family["examples"][str(k)] == expected, f"complete k={k} example")
        rebuilt[str(k)] = expected
    ck(rebuilt["1"]["z5_symbolic_traces_n1_to_8"] == rebuilt["6"]["z5_symbolic_traces_n1_to_8"], "z5 alias reconstruction")
    ck(rebuilt["1"]["q_delta_z0_to_z3"] != rebuilt["6"]["q_delta_z0_to_z3"], "q separation reconstruction")
    ck(qpow(-2) == (Fraction(-7, 25), Fraction(-24, 25)), "q^-2")
    ck(qpow(-12) != qpow(-2), "faithful witness")

    operator = data["all_order_operator"]
    keys(operator, {"trace_class", "trace_formula", "lattice_product", "primitive_product", "uniform_character_bound", "all_period"}, "operator keys")
    ck(operator["trace_class"] is True and operator["all_period"] is True, "all-period trace class")
    ck(operator["trace_formula"] == "Tr(L_t,u^n)=Tr(W_t,u^n)/((1-8^(-n))*(1-16^(-n))) for every n>=1", "trace headline")
    ck(operator["lattice_product"] == "D_t,u(z)=product_(r,s>=0) det(I-z*8^(-r)*16^(-s)*W_t,u)", "lattice headline")
    ck(operator["primitive_product"] == "log D_t,u=-sum_[gamma]sum_m (c_gamma*u^(M_gamma)*z^ell)^m/(m*det(I-A^(m*ell)))", "primitive headline")

    recovery = data["universal_recovery"]
    keys(recovery, {"symbolic_delta_general", "normalized_log_jet", "newton_E1", "newton_E2", "newton_E3", "monomial_recovery", "decode", "strongest_theorem", "permutation_receipts"}, "recovery keys")
    ck(recovery["symbolic_delta_general"] == "1-(1/2)X^(t0)z-(1/6)X^(t0+t1)z^2-(1/30)X^(t0+t1+t2)z^3", "delta headline")
    ck(recovery["normalized_log_jet"] == "P_n(X)=-n*(1-8^(-n))*(1-16^(-n))*[z^n]log D_t,X=Tr(W_t,X^n)", "jet headline")
    ck(recovery["newton_E1"] == "E1=P1", "Newton E1")
    ck(recovery["newton_E2"] == "E2=(P1^2-P2)/2", "Newton E2")
    ck(recovery["newton_E3"] == "E3=(P1^3-3*P1*P2+2*P3)/6", "Newton E3")
    ck(recovery["monomial_recovery"] == ["2*E1=X^t0", "-6*E2=X^(t0+t1)", "30*E3=X^(t0+t1+t2)"], "monomial recovery")
    ck(recovery["decode"] == "t0=S0, t1=S01-S0, t2=S012-S01", "decode")
    ck(recovery["strongest_theorem"] == "the first three labelled universal log jets, or their exact evaluation at any known faithful character, determine the branch-labelled integer translation triple", "recovery theorem")
    expected_permutations = []
    for k in (1, 6):
        for t in sorted(set(itertools.permutations((-2 * k, 0, 2 * k)))):
            partial = [t[0], t[0] + t[1], sum(t)]
            expected_permutations.append({"k": k, "translations": [str(v) for v in t], "partial_sum_exponents": partial, "decoded_translations": [str(partial[0]), str(partial[1] - partial[0]), str(partial[2] - partial[1])]})
    ck(recovery["permutation_receipts"] == expected_permutations, "all permutation recoveries")

    controls = data["controls"]
    keys(controls, {"k1_vs_k6_z5_alias", "alias_reason", "k1_vs_k6_q_separated", "q_separation_witness", "labelled_parameter_boundary", "torsion_boundary", "finite_precision_boundary", "geometry_boundary"}, "controls keys")
    ck(controls["k1_vs_k6_z5_alias"] is True, "alias flag")
    ck(controls["k1_vs_k6_q_separated"] is True, "q separation flag")
    ck(controls["alias_reason"] == "(-12,0,12) is componentwise congruent to (-2,0,2) modulo 5, so every Z/5 twisted trace and determinant agrees", "alias reason")
    ck(controls["q_separation_witness"] == "the linear symbolic coefficients are -(1/2)q^(-2) and -(1/2)q^(-12), which differ because q is faithful", "q witness")
    ck(controls["labelled_parameter_boundary"] == "without the orientation-labelled character parameter, t and -t obey D_{-t,u}(z)=D_{t,u^{-1}}(z)", "labelled parameter boundary")
    ck("not a stable finite-precision" in controls["finite_precision_boundary"], "precision boundary")
    ck("only for integer x-translations" in controls["geometry_boundary"], "geometry boundary")

    prefix = data["replay_prefix"]
    keys(prefix, {"period_limit", "rooted_counts_n1_to_8", "primitive_representatives_n1_to_8", "primitive_holonomy_histograms", "rooted_closed_words_total", "primitive_cycles_total"}, "prefix keys")
    rooted_counts = {}
    reps_by_n = {}
    hist = {"1": {}, "6": {}}
    for n in range(1, 9):
        rooted = [w for w in itertools.product(range(3), repeat=n) if admissible(w, B)]
        reps = sorted({least(w) for w in rooted if primitive(w)})
        rooted_counts[str(n)] = len(rooted)
        reps_by_n[str(n)] = ["".join(map(str, w)) for w in reps]
        for k in (1, 6):
            t = [-2 * k, 0, 2 * k]
            row = {}
            for word in reps:
                exponent = sum(t[symbol] for symbol in word)
                row[str(exponent)] = row.get(str(exponent), 0) + 1
            hist[str(k)][str(n)] = row
    ck(prefix["period_limit"] == 8, "prefix limit")
    ck(prefix["rooted_counts_n1_to_8"] == rooted_counts, "rooted counts")
    ck(prefix["primitive_representatives_n1_to_8"] == reps_by_n, "primitive reps")
    ck(prefix["primitive_holonomy_histograms"] == hist, "histograms")
    ck(prefix["rooted_closed_words_total"] == 284, "rooted total")
    ck(prefix["primitive_cycles_total"] == 40, "primitive total")

    progress = data["progress_and_boundary"]
    keys(progress, {"progress_over_C129", "remaining_internal_obstruction", "target_obstruction"}, "progress keys")
    ck(progress["progress_over_C129"] == "replaces one mod-5 quotient character by the labelled universal character torus and proves exact recovery of every branch-labelled integer translation in the frozen family", "progress headline")
    ck("floating-point stability" in progress["remaining_internal_obstruction"], "remaining boundary")
    route = data["route_a"]
    keys(route, {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route keys")
    ck(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "tuple")
    ck(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    ck(route["route_b_invocation_allowed"] is False, "route B")
    flags = data["scope_flags"]
    keys(flags, {"scope", "uses_prime_table", "uses_zero_table", "claims_arithmetic_euler_factors", "claims_root_number", "claims_automorphy", "claims_hilbert_polya", "uses_route_b_inputs"}, "scope flag keys")
    ck(flags == {"scope": "NO_BAD_EULER_OR_ROOT_NUMBER", "uses_prime_table": False, "uses_zero_table": False, "claims_arithmetic_euler_factors": False, "claims_root_number": False, "claims_automorphy": False, "claims_hilbert_polya": False, "uses_route_b_inputs": False}, "scope flags")
    ck(data["nonclaims"] == ["stable recovery from finite-precision character samples", "recovery of arbitrary real or higher-dimensional geometry", "recovery when the character parameter orientation or the frozen graph and weights are unknown", "a target-facing zero or divisor match", "prime-like information, arithmetic/local data, Euler factors, root numbers, or automorphy", "a self-adjoint Hilbert--Polya operator, natural unitary quantization, or Route-B authorization"], "nonclaims")

    print(json.dumps({"status": "C134_INDEPENDENT_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
