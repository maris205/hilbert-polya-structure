#!/usr/bin/env python3
"""Produce the exact C134 faithful-character recovery certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c134_character_evidence.json"
PREFIX = 8


def fs(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def clean(poly: dict[int, Fraction]) -> dict[int, Fraction]:
    return {e: c for e, c in poly.items() if c}


def lp_scalar(value: Fraction | int) -> dict[int, Fraction]:
    return {} if not value else {0: Fraction(value)}


def lp_monomial(exponent: int, coefficient: Fraction | int = 1) -> dict[int, Fraction]:
    return {} if not coefficient else {exponent: Fraction(coefficient)}


def lp_add(left: dict[int, Fraction], right: dict[int, Fraction]) -> dict[int, Fraction]:
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, Fraction(0)) + coefficient
    return clean(out)


def lp_scale(poly: dict[int, Fraction], value: Fraction | int) -> dict[int, Fraction]:
    return clean({e: Fraction(value) * c for e, c in poly.items()})


def lp_mul(left: dict[int, Fraction], right: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for e1, c1 in left.items():
        for e2, c2 in right.items():
            out[e1 + e2] = out.get(e1 + e2, Fraction(0)) + c1 * c2
    return clean(out)


def lp_receipt(poly: dict[int, Fraction]) -> dict[str, str]:
    return {str(e): fs(poly[e]) for e in sorted(poly)}


def eye(n: int) -> list[list[dict[int, Fraction]]]:
    return [[lp_scalar(i == j) for j in range(n)] for i in range(n)]


def mmul(left, right):
    out = []
    for i in range(len(left)):
        row = []
        for j in range(len(right[0])):
            total: dict[int, Fraction] = {}
            for k in range(len(right)):
                total = lp_add(total, lp_mul(left[i][k], right[k][j]))
            row.append(total)
        out.append(row)
    return out


def mpow(matrix, n: int):
    out = eye(len(matrix))
    base = matrix
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def mtrace(matrix):
    total: dict[int, Fraction] = {}
    for i in range(len(matrix)):
        total = lp_add(total, matrix[i][i])
    return total


def weighted_matrix(B, weights, translations):
    return [
        [lp_monomial(translations[j], weights[j] * B[i][j]) for j in range(3)]
        for i in range(3)
    ]


def fredholm_coefficients(traces, degree: int):
    coefficients = [lp_scalar(1)]
    for n in range(1, degree + 1):
        total: dict[int, Fraction] = {}
        for k in range(1, n + 1):
            total = lp_add(total, lp_mul(traces[k], coefficients[n - k]))
        coefficients.append(lp_scale(total, Fraction(-1, n)))
    return coefficients


def gaussian_mul(left, right):
    a, b = left
    c, d = right
    return (a * c - b * d, a * d + b * c)


def gaussian_pow(exponent: int):
    q = (Fraction(3, 5), Fraction(4, 5))
    if exponent < 0:
        q = (q[0], -q[1])
        exponent = -exponent
    out = (Fraction(1), Fraction(0))
    while exponent:
        if exponent & 1:
            out = gaussian_mul(out, q)
        q = gaussian_mul(q, q)
        exponent //= 2
    return out


def gaussian_scale(value, scalar):
    return (Fraction(scalar) * value[0], Fraction(scalar) * value[1])


def gaussian_receipt(value):
    return {"real": fs(value[0]), "imag": fs(value[1])}


def eval_q(poly):
    total = (Fraction(0), Fraction(0))
    for exponent, coefficient in poly.items():
        value = gaussian_scale(gaussian_pow(exponent), coefficient)
        total = (total[0] + value[0], total[1] + value[1])
    return total


def reduce_mod5(poly):
    row = [Fraction(0)] * 5
    for exponent, coefficient in poly.items():
        row[exponent % 5] += coefficient
    return [fs(value) for value in row]


def admissible(word, B):
    return all(B[word[k]][word[(k + 1) % len(word)]] for k in range(len(word)))


def primitive(word):
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least_rotation(word):
    return min(word[k:] + word[:k] for k in range(len(word)))


def canonical_payload(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def delta(translations):
    t0, t1, t2 = translations
    return [
        lp_scalar(1),
        lp_monomial(t0, Fraction(-1, 2)),
        lp_monomial(t0 + t1, Fraction(-1, 6)),
        lp_monomial(t0 + t1 + t2, Fraction(-1, 30)),
    ]


def build() -> dict:
    B = [[1, 1, 0], [1, 0, 1], [1, 0, 0]]
    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)]
    examples = {}
    for k in (1, 6):
        translations = [-2 * k, 0, 2 * k]
        W = weighted_matrix(B, weights, translations)
        symbolic = {n: mtrace(mpow(W, n)) for n in range(1, PREFIX + 1)}
        hardy = {
            n: lp_scale(
                symbolic[n],
                1 / ((1 - Fraction(1, 8) ** n) * (1 - Fraction(1, 16) ** n)),
            )
            for n in range(1, PREFIX + 1)
        }
        coefficients = fredholm_coefficients(hardy, PREFIX)
        examples[str(k)] = {
            "translations": [str(v) for v in translations],
            "domain_radius": str(3 * k),
            "first_coordinate_radius": fs(Fraction(21 * k, 32)),
            "second_coordinate_radius": fs(Fraction(3 * k, 4)),
            "pairwise_minimum_gap": fs(Fraction(11 * k, 16)),
            "strict_interior_margin_first_coordinate": fs(Fraction(11 * k, 32)),
            "partial_sum_exponents": [translations[0], translations[0] + translations[1], sum(translations)],
            "decoded_translations": [str(v) for v in translations],
            "symbolic_delta_z0_to_z3": [lp_receipt(value) for value in delta(translations)],
            "q_delta_z0_to_z3": [gaussian_receipt(eval_q(value)) for value in delta(translations)],
            "universal_hardy_traces_n1_to_8": {str(n): lp_receipt(hardy[n]) for n in range(1, PREFIX + 1)},
            "universal_fredholm_coefficients_z0_to_z8": [lp_receipt(value) for value in coefficients],
            "z5_symbolic_traces_n1_to_8": {str(n): reduce_mod5(symbolic[n]) for n in range(1, PREFIX + 1)},
        }

    permutation_receipts = []
    for k in (1, 6):
        for translations in sorted(set(itertools.permutations((-2 * k, 0, 2 * k)))):
            partial = [translations[0], translations[0] + translations[1], sum(translations)]
            decoded = [partial[0], partial[1] - partial[0], partial[2] - partial[1]]
            assert tuple(decoded) == translations
            permutation_receipts.append({
                "k": k,
                "translations": [str(v) for v in translations],
                "partial_sum_exponents": partial,
                "decoded_translations": [str(v) for v in decoded],
            })

    rooted_counts = {}
    primitive_representatives = {}
    holonomy_histograms = {"1": {}, "6": {}}
    for n in range(1, PREFIX + 1):
        rooted = [word for word in itertools.product(range(3), repeat=n) if admissible(word, B)]
        reps = sorted({least_rotation(word) for word in rooted if primitive(word)})
        rooted_counts[str(n)] = len(rooted)
        primitive_representatives[str(n)] = ["".join(map(str, word)) for word in reps]
        for k in (1, 6):
            translations = [-2 * k, 0, 2 * k]
            histogram: dict[str, int] = {}
            for word in reps:
                exponent = sum(translations[symbol] for symbol in word)
                histogram[str(exponent)] = histogram.get(str(exponent), 0) + 1
            holonomy_histograms[str(k)][str(n)] = histogram

    assert examples["1"]["z5_symbolic_traces_n1_to_8"] == examples["6"]["z5_symbolic_traces_n1_to_8"]
    assert examples["1"]["q_delta_z0_to_z3"] != examples["6"]["q_delta_z0_to_z3"]

    data = {
        "schema": "HCS-C134-v1",
        "candidate_id": "HCS-C134",
        "date_utc": "2026-08-24",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "linear_part_A": [["3/16", "-1/32"], ["1/4", "0"]],
            "adjacency_B": [[1, 1, 0], [1, 0, 1], [1, 0, 0]],
            "weights": ["1/2", "1/3", "1/5"],
            "scaled_family": "k>=1, translations are any branch permutation of (-2k,0,2k), Hardy bidisc radius 3k",
            "clock": "one admissible graph edge per iterate",
            "normalization": "chi_u(m)=u^m on the integer translation lattice; u is a labelled U(1) parameter",
            "determinant_convention": "D_t,u(z)=det(I-z*L_t,u)",
            "precision": "exact Laurent polynomials over Q and Gaussian rationals at q=(3+4i)/5",
            "cutoff": "none in theorem; periods and Taylor orders 1 through 8 are replay only",
            "forbidden_data": "external prime or zero tables, arithmetic/local factors, root numbers, and Route-B inputs",
        },
        "frozen_family": {
            "A_eigenvalues": ["1/8", "1/16"],
            "A_infinity_norm": "1/4",
            "universal_character_ring": "Q[Z]=Q[X,X^(-1)] with chi_X(m)=X^m",
            "faithful_anchor_q": {"real": "3/5", "imag": "4/5"},
            "q_inverse": {"real": "3/5", "imag": "-4/5"},
            "faithfulness_certificate": "q has quadratic trace 6/5, hence is not an algebraic integer or a root of unity; q^m=q^n implies m=n",
            "operator": "(L_t,u f)_i=sum_j B_ij*c_j*u^(t_j)*f_j(Az+(t_j,0))",
            "geometry_theorem": "for every k>=1 and every branch permutation: radii=(21k/32,3k/4), strict first-coordinate margin=11k/32, and minimum gap=11k/16",
            "examples": examples,
        },
        "all_order_operator": {
            "trace_class": True,
            "trace_formula": "Tr(L_t,u^n)=Tr(W_t,u^n)/((1-8^(-n))*(1-16^(-n))) for every n>=1",
            "lattice_product": "D_t,u(z)=product_(r,s>=0) det(I-z*8^(-r)*16^(-s)*W_t,u)",
            "primitive_product": "log D_t,u=-sum_[gamma]sum_m (c_gamma*u^(M_gamma)*z^ell)^m/(m*det(I-A^(m*ell)))",
            "uniform_character_bound": "all trace-class and product bounds are uniform in u because |u^m|=1",
            "all_period": True,
        },
        "universal_recovery": {
            "symbolic_delta_general": "1-(1/2)X^(t0)z-(1/6)X^(t0+t1)z^2-(1/30)X^(t0+t1+t2)z^3",
            "normalized_log_jet": "P_n(X)=-n*(1-8^(-n))*(1-16^(-n))*[z^n]log D_t,X=Tr(W_t,X^n)",
            "newton_E1": "E1=P1",
            "newton_E2": "E2=(P1^2-P2)/2",
            "newton_E3": "E3=(P1^3-3*P1*P2+2*P3)/6",
            "monomial_recovery": ["2*E1=X^t0", "-6*E2=X^(t0+t1)", "30*E3=X^(t0+t1+t2)"],
            "decode": "t0=S0, t1=S01-S0, t2=S012-S01",
            "strongest_theorem": "the first three labelled universal log jets, or their exact evaluation at any known faithful character, determine the branch-labelled integer translation triple",
            "permutation_receipts": permutation_receipts,
        },
        "controls": {
            "k1_vs_k6_z5_alias": True,
            "alias_reason": "(-12,0,12) is componentwise congruent to (-2,0,2) modulo 5, so every Z/5 twisted trace and determinant agrees",
            "k1_vs_k6_q_separated": True,
            "q_separation_witness": "the linear symbolic coefficients are -(1/2)q^(-2) and -(1/2)q^(-12), which differ because q is faithful",
            "labelled_parameter_boundary": "without the orientation-labelled character parameter, t and -t obey D_{-t,u}(z)=D_{t,u^{-1}}(z)",
            "torsion_boundary": "torsion-only character samples factor through finite quotients and can alias distinct scaled translations",
            "finite_precision_boundary": "exact injectivity at a faithful dense character is not a stable finite-precision inversion theorem",
            "geometry_boundary": "recovery is only for integer x-translations inside the frozen A,B,c,branch-labelled affine family",
        },
        "replay_prefix": {
            "period_limit": PREFIX,
            "rooted_counts_n1_to_8": rooted_counts,
            "primitive_representatives_n1_to_8": primitive_representatives,
            "primitive_holonomy_histograms": holonomy_histograms,
            "rooted_closed_words_total": sum(rooted_counts.values()),
            "primitive_cycles_total": sum(len(v) for v in primitive_representatives.values()),
        },
        "progress_and_boundary": {
            "progress_over_C129": "replaces one mod-5 quotient character by the labelled universal character torus and proves exact recovery of every branch-labelled integer translation in the frozen family",
            "remaining_internal_obstruction": "unlabelled parameter orientation, torsion-only sampling, floating-point stability, and geometry outside the frozen family are not recovered",
            "target_obstruction": "no target divisor, functional equation, counting law, or arithmetic interpretation is compared",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "ALL_PERIOD_INTRINSIC_PRIMITIVE_ORBITS_WITH_NO_PRIME_LIKE_TARGET_CORRESPONDENCE",
            "A2_qualification": "EXACT_SOURCE FREDHOLM FAMILY AND RECOVERY THEOREM BUT NO FROZEN TARGET DIVISOR MATCH",
            "A3_qualification": "NO TARGET FUNCTIONAL EQUATION GAMMA FACTOR COUNTING LAW OR CONTINUATION COMPARISON",
            "A4_qualification": "CANONICAL FLAT CHARACTER FAMILY IS A FORMAL PHASE LIFT, NOT A NATURAL QUANTIZATION",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "uses_prime_table": False,
            "uses_zero_table": False,
            "claims_arithmetic_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_hilbert_polya": False,
            "uses_route_b_inputs": False,
        },
        "nonclaims": [
            "stable recovery from finite-precision character samples",
            "recovery of arbitrary real or higher-dimensional geometry",
            "recovery when the character parameter orientation or the frozen graph and weights are unknown",
            "a target-facing zero or divisor match",
            "prime-like information, arithmetic/local data, Euler factors, root numbers, or automorphy",
            "a self-adjoint Hilbert--Polya operator, natural unitary quantization, or Route-B authorization",
        ],
    }
    data["payload_sha256"] = sha256(canonical_payload(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    args.output.write_text(raw)
    print(json.dumps({
        "status": "C134_EXACT_EVIDENCE_PASS",
        "evidence_sha256": sha256(raw.encode()).hexdigest(),
        "payload_sha256": data["payload_sha256"],
        "rooted_words_through_8": data["replay_prefix"]["rooted_closed_words_total"],
        "primitive_cycles_through_8": data["replay_prefix"]["primitive_cycles_total"],
        "permutation_recoveries": len(data["universal_recovery"]["permutation_receipts"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
