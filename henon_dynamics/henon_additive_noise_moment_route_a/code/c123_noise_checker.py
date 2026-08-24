#!/usr/bin/env python3
"""Independent validator for C123; it never imports the producer."""
from __future__ import annotations

from itertools import product
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results" / "c123_noise_evidence.json"
A = sp.Matrix([[sp.Rational(1, 2), sp.Rational(-1, 4)], [sp.Rational(1, 4), 0]])


class CheckFailure(AssertionError):
    pass


def parse(x: str) -> sp.Expr:
    return sp.sympify(x, locals={"sqrt": sp.sqrt})


def pvec(v) -> sp.Matrix:
    return sp.Matrix([parse(x) for x in v])


def pmat(M) -> sp.Matrix:
    return sp.Matrix([[parse(x) for x in row] for row in M])


def minrot(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def primitive(w):
    n = len(w)
    return all(w != w[:d] * (n // d) for d in range(1, n) if n % d == 0)


def expected_operator():
    x, y, z = sp.symbols("x y z")
    basis, exps = [], []
    for d in range(5):
        for i in range(d, -1, -1):
            basis.append(x**i * y ** (d - i))
            exps.append((i, d - i))
    xp, yp = x / 2 - y / 4, x / 4
    K = sp.zeros(15)
    for col, (i, j) in enumerate(exps):
        image = sp.expand(((xp + sp.Rational(1, 2)) ** i * yp**j + (xp - sp.Rational(1, 2)) ** i * yp**j) / 2)
        poly = sp.Poly(image, x, y)
        for row, monomial in enumerate(basis):
            K[row, col] = poly.coeff_monomial(monomial)
    coeffs = list(reversed(sp.Poly((sp.eye(15) - z * K).det(), z).all_coeffs()))
    m = sp.symbols("m0:15")
    solution = sp.solve(list((K.T - sp.eye(15)) * sp.Matrix(m)) + [m[0] - 1], m, dict=True)[0]
    mu = sp.Matrix([solution[t] for t in m])
    return basis, K, coeffs, mu


def validate(data: dict) -> int:
    checks = 0

    def req(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise CheckFailure(message)

    req(data["schema_id"] == "hcs-c123-additive-noise-henon-moment-prefreeze-v1", "schema")
    req(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    req(pmat(data["source_model"]["linear_part"]) == A, "linear part")
    req(data["source_model"]["noise_support"] == ["-1/2", "1/2"], "noise support")
    req(data["source_model"]["noise_probabilities"] == ["1/2", "1/2"], "probabilities")
    req(A.eigenvals() == {sp.Rational(1, 4): 2} and A.det() == sp.Rational(1, 16), "linear spectrum")
    svals = sorted((A.T * A).eigenvals(), key=sp.default_sort_key)
    req([parse(v) for v in data["source_model"]["singular_value_squares"]] == svals, "singular values")
    req(all(v < 1 for v in svals), "strict contraction")

    atlas = data["periodic_noise_word_atlas"]
    req(atlas["maximum_period"] == 6 and atlas["rooted_words_tested"] == 126, "atlas cutoff")
    expected_counts, expected_words = {}, []
    for n in range(1, 7):
        ws = [w for w in product((-1, 1), repeat=n) if primitive(w) and w == minrot(w)]
        expected_counts[str(n)] = len(ws)
        expected_words.extend(ws)
    req(expected_counts == {"1": 2, "2": 1, "3": 2, "4": 3, "5": 6, "6": 9}, "necklace counts")
    req(atlas["primitive_necklace_counts"] == expected_counts and atlas["primitive_necklace_total"] == 23, "recorded counts")
    req(
        atlas["row_probability_semantics"]
        == "chosen rooted length-n block probability under the iid law; not necklace total mass; not infinite periodic-orbit probability",
        "probability semantics",
    )
    rows = atlas["rows"]
    req(len(rows) == 23, "row count")
    observed_words = []
    for row in rows:
        word = tuple(-1 if s == "-" else 1 for s in row["canonical_word"])
        observed_words.append(word)
        req(row["period"] == len(word) and primitive(word) and word == minrot(word), "word primitive/canonical")
        req(parse(row["chosen_rooted_block_probability"]) == sp.Rational(1, 2) ** len(word), "rooted block probability")
        req("word_probability" not in row, "ambiguous probability field absent")
        states = [pvec(v) for v in row["states"]]
        req(len(states) == len(word), "state count")
        for i, symbol in enumerate(word):
            nxt = A * states[i] + sp.Matrix([sp.Rational(symbol, 2), 0])
            req(sp.simplify(nxt - states[(i + 1) % len(states)]) == sp.zeros(2, 1), "cycle closure")
        req(row["primitive"] is True and row["cycle_closes"] is True, "cycle flags")
        req(pmat(row["composition_linear_part"]) == A ** len(word), "composition linear")
        req(parse(row["composition_determinant"]) == A.det() ** len(word), "composition determinant")
    req(observed_words == expected_words, "word ordering")

    basis, K, coeffs, mu = expected_operator()
    op = data["degree_four_markov_operator"]
    req(op["basis"] == [sp.sstr(b) for b in basis] and op["dimension"] == 15, "operator basis")
    req(pmat(op["matrix"]) == K, "operator matrix")
    req(parse(op["trace"]) == sp.Rational(453, 256), "operator trace")
    req(parse(op["determinant"]) == sp.Rational(1, 2**80), "operator determinant")
    req([parse(v) for v in op["det_I_minus_z"]] == coeffs, "det polynomial")
    moments = data["stationary_moments_through_degree_four"]
    req(pvec(moments["moments"]) == mu, "stationary moments")
    Sigma = sp.Matrix([[mu[3], mu[4]], [mu[4], mu[5]]])
    req(pmat(moments["covariance"]) == Sigma, "covariance")
    req(Sigma == sp.Matrix([[sp.Rational(1088, 3375), sp.Rational(128, 3375)], [sp.Rational(128, 3375), sp.Rational(68, 3375)]]), "covariance values")
    req(parse(moments["covariance_determinant"]) == sp.Rational(256, 50625), "covariance determinant")
    req(pmat(moments["lyapunov_residual"]) == sp.zeros(2), "Lyapunov residual")
    req(parse(moments["x_fourth_cumulant"]) == sp.Rational(-47789203456, 359401303125), "fourth cumulant")
    req(pmat(moments["noise_ablated_stationary_covariance"]) == sp.zeros(2), "ablation")
    verdict = data["route_a_verdict"]
    req(
        (verdict["A1"], verdict["A2"], verdict["A3"], verdict["A4"], verdict["overall"])
        == ("A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL", "ROUTE_A_EXPLORATORY"),
        "canonical route verdict",
    )
    req("NO_PRIME_LIKE_TARGET_CORRESPONDENCE" in verdict["A1_qualification"], "A1 target boundary")
    req("NO_TARGET_DIVISOR_MATCH_OR_ANALYTIC_BRIDGE" in verdict["A2_qualification"], "A2 target boundary")
    req(verdict["A3_qualification"] == "NO_GLOBAL_ANALYTIC_STRUCTURE_OR_CONTINUATION_THEOREM", "A3 boundary")
    for key in ("complete_random_orbit_atlas", "global_nuclear_or_fredholm_owner", "prime_like_target_correspondence", "target_divisor_match", "analytic_bridge", "arithmetic_local_data", "euler_factors", "root_numbers", "automorphy", "hilbert_polya_operator", "route_b_authorized"):
        req(data["claims"][key] is False, f"nonclaim {key}")
    return checks


def main():
    data = json.loads(EVIDENCE.read_text())
    print(json.dumps({"status": "C123_INDEPENDENT_CHECK_PASS", "checks": validate(data)}, sort_keys=True))


if __name__ == "__main__":
    main()
