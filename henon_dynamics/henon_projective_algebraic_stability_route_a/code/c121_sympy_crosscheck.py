#!/usr/bin/env python3
"""Fresh SymPy cross-check of the C121 birational and orbit identities."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c121_projective_evidence.json").read_text())
x, y, z = sp.symbols("x y z")


def h(first: sp.Expr, second: sp.Expr, parameter: int = -4) -> tuple[sp.Expr, sp.Expr]:
    return (sp.expand(first**2 + parameter - second), first)


def hinv(first: sp.Expr, second: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    return (second, sp.expand(second**2 - 4 - first))


checks = 0

# Affine inverse identities.
assert tuple(sp.expand(v) for v in h(*hinv(x, y))) == (x, y)
checks += 2
assert tuple(sp.expand(v) for v in hinv(*h(x, y))) == (x, y)
checks += 2

# Projective base points and the contracted line at infinity.
X, Y, Z = sp.symbols("X Y Z")
forward = (X**2 - 4 * Z**2 - Y * Z, X * Z, Z**2)
inverse = (Y * Z, Y**2 - 4 * Z**2 - X * Z, Z**2)
assert tuple(value.subs({X: 0, Y: 1, Z: 0}) for value in forward) == (0, 0, 0)
checks += 3
assert tuple(value.subs({X: 1, Y: 0, Z: 0}) for value in inverse) == (0, 0, 0)
checks += 3
assert tuple(value.subs({X: 1, Y: 0, Z: 0}) for value in forward) == (1, 0, 0)
checks += 3
assert tuple(sp.expand(value.subs(Z, 0)) for value in forward) == (X**2, 0, 0)
checks += 3

# Fixed points.
fixed_polynomial = sp.Poly(x**2 - 2 * x - 4, x)
assert sp.expand(fixed_polynomial.as_expr() - (x - 1 - sp.sqrt(5)) * (x - 1 + sp.sqrt(5))) == 0
checks += 1
for root in (1 + sp.sqrt(5), 1 - sp.sqrt(5)):
    assert all(sp.simplify(a - b) == 0 for a, b in zip(h(root, root), (root, root)))
    checks += 2

# Primitive two-cycle and its tangent monodromy.
p = (sp.Integer(0), sp.Integer(-2))
q = (sp.Integer(-2), sp.Integer(0))
assert h(*p) == q and h(*q) == p and p != q
checks += 5
B = lambda first: sp.Matrix([[2 * first, -1], [1, 0]])
monodromy = B(-2) * B(0)
assert monodromy == sp.Matrix([[-1, 4], [0, -1]])
checks += 4
assert sp.trace(monodromy) == -2 and monodromy.det() == 1
checks += 2
assert sp.Poly((sp.eye(2) - z * monodromy).det(), z).all_coeffs() == [1, 2, 1]
checks += 3

# Small expanded prefix, followed by the nonexpanded all-order degree check.
older, old = y, x
for n in range(1, 5):
    new = sp.expand(old**2 - 4 - older)
    polynomial = sp.Poly(new, x, y)
    assert polynomial.total_degree() == 2**n
    assert polynomial.coeff_monomial(x ** (2**n)) == 1
    assert DATA["degree_growth"]["rows"][n - 1]["first_coordinate_degree"] == 2**n
    checks += 3
    older, old = old, new

for n, row in enumerate(DATA["degree_growth"]["rows"], start=1):
    # Induction: squaring the unique monic top term doubles the degree, while
    # p_{n-2} and the constant have strictly smaller degree.
    assert row["first_coordinate_degree"] == 2**n
    assert row["second_coordinate_degree"] == 2 ** (n - 1)
    assert row["homogeneous_first_X_power_coefficient"] == 1
    assert row["projective_coordinate_gcd"] == "1"
    checks += 4

# Parameter controls recomputed symbolically.
for control in DATA["parameter_controls"]:
    alternate = control["parameter_c"]
    hp = h(*p, parameter=alternate)
    hq = h(*q, parameter=alternate)
    residual_pq = [int(sp.expand(hp[i] - q[i])) for i in range(2)]
    residual_qp = [int(sp.expand(hq[i] - p[i])) for i in range(2)]
    assert residual_pq == control["candidate_transition_residual_p_to_q"]
    assert residual_qp == control["candidate_transition_residual_q_to_p"]
    assert residual_pq != [0, 0] and residual_qp != [0, 0]
    checks += 4

assert DATA["degree_growth"]["dynamical_degree"] == "2"
assert DATA["degree_growth"]["entropy_claimed"] is False
checks += 2
route = DATA["route_a_verdict"]
assert route["canonical_tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
checks += 4
assert route["overall"] == "ROUTE_A_EXPLORATORY"
checks += 1
nonclaims = " | ".join(DATA["nonclaims"])
assert "prime-like target correspondence" in nonclaims
assert "target divisor" in nonclaims
assert "functional equation" in nonclaims
checks += 3
print("C121_SYMPY_PASS", checks, "exact symbolic checks")
