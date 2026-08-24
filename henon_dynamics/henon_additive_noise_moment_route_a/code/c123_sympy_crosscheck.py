#!/usr/bin/env python3
"""Independent symbolic checks for the C123 polynomial Markov operator."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "results" / "c123_noise_evidence.json").read_text())
parse = lambda v: sp.sympify(v, locals={"sqrt": sp.sqrt})
pmat = lambda M: sp.Matrix([[parse(x) for x in row] for row in M])
pvec = lambda v: sp.Matrix([parse(x) for x in v])
x, y = sp.symbols("x y")
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
    for row, b in enumerate(basis):
        K[row, col] = poly.coeff_monomial(b)
recorded = pmat(data["degree_four_markov_operator"]["matrix"])
checks = [recorded[i, j] == K[i, j] for i in range(15) for j in range(15)]
mu = pvec(data["stationary_moments_through_degree_four"]["moments"])
checks += [sp.simplify(v) == 0 for v in (K.T - sp.eye(15)) * mu]
checks.append(mu[0] == 1)
A = sp.Matrix([[sp.Rational(1, 2), sp.Rational(-1, 4)], [sp.Rational(1, 4), 0]])
Sigma = sp.Matrix([[mu[3], mu[4]], [mu[4], mu[5]]])
checks += [sp.simplify(v) == 0 for v in Sigma - A * Sigma * A.T - sp.diag(sp.Rational(1, 4), 0)]
checks.append(sp.factor(mu[10] - 3 * mu[3] ** 2) == sp.Rational(-47789203456, 359401303125))
atlas = data["periodic_noise_word_atlas"]
checks.append(
    atlas["row_probability_semantics"]
    == "chosen rooted length-n block probability under the iid law; not necklace total mass; not infinite periodic-orbit probability"
)
checks += [
    parse(row["chosen_rooted_block_probability"]) == sp.Rational(1, 2) ** row["period"]
    for row in atlas["rows"]
]
verdict = data["route_a_verdict"]
checks += [
    verdict["A1"] == "A1_WEAK",
    verdict["A2"] == "A2_FAIL",
    verdict["A3"] == "A3_FAIL",
    verdict["A4"] == "A4_FAIL",
    verdict["overall"] == "ROUTE_A_EXPLORATORY",
    data["claims"]["prime_like_target_correspondence"] is False,
    data["claims"]["target_divisor_match"] is False,
    data["claims"]["analytic_bridge"] is False,
]
assert all(checks)
print(json.dumps({"status": "C123_SYMPY_CROSSCHECK_PASS", "checks": len(checks)}, sort_keys=True))
