#!/usr/bin/env python3
"""Direct symbolic identity cross-check for C120."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c120_variational_period3_evidence.json").read_text())
q, p, Q, z = sp.symbols("q p Q z")

F = sp.Matrix([q**3-2*q-p, q])
B = F.jacobian([q, p])
predicates: list[bool] = [sp.factor(B.det()) == 1]

Finv = sp.Matrix([p, p**3-2*p-q])
Q0, P0 = sp.symbols("Q0 P0")
forward_after_inverse = F.subs({q: P0, p: P0**3-2*P0-Q0})
inverse_after_forward = sp.Matrix([
    F[1], F[1]**3-2*F[1]-F[0],
])
RFR = sp.Matrix([p, p**3-2*p-q])
predicates.extend([
    forward_after_inverse == sp.Matrix([Q0, P0]),
    sp.simplify(inverse_after_forward-sp.Matrix([q, p])) == sp.zeros(2, 1),
    RFR == Finv,
])

fixed_polynomial = sp.factor(q**3-4*q)
predicates.append(fixed_polynomial == q*(q-2)*(q+2))

states = [sp.Matrix([0, -1]), sp.Matrix([1, 0]), sp.Matrix([-1, 1])]
for index, state in enumerate(states):
    image = F.subs({q: state[0], p: state[1]})
    predicates.append(image == states[(index+1) % 3])

def b(value: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[3*value**2-2, -1], [1, 0]])

M = b(-1)*b(1)*b(0)
predicates.extend([
    M == sp.Matrix([[-1, 0], [-3, -1]]),
    sp.trace(M) == -2,
    M.det() == 1,
    sp.factor((sp.eye(2)-z*M).det()) == (1+z)**2,
])

q0, q1, q2 = sp.symbols("q0 q1 q2")
word = [q0, q1, q2]
V = lambda x: x**4/sp.Integer(4)-x**2
action = sum(word[i]*word[(i+1) % 3]-V(word[i]) for i in range(3))
gradient = sp.Matrix([sp.diff(action, x) for x in word])
point = {q0: 0, q1: 1, q2: -1}
H = sp.hessian(action, word).subs(point)
lam = sp.symbols("lambda")
predicates.extend([
    gradient.subs(point) == sp.zeros(3, 1),
    H == sp.Matrix([[2, 1, 1], [1, -1, 1], [1, 1, -1]]),
    H.det() == 4,
    sp.factor(H.charpoly(lam).as_expr()) == (lam+2)*(lam**2-2*lam-2),
    sp.simplify(action.subs(point)-sp.Rational(1, 2)) == 0,
])

S = q*Q-(q**4/sp.Integer(4)-q**2)
predicates.extend([
    sp.expand(-sp.diff(S, q)-(q**3-2*q-Q)) == 0,
    sp.diff(S, Q) == q,
    DATA["primitive_period_three"]["monodromy"] == [["-1", "0"], ["-3", "-1"]],
    DATA["discrete_action_certificate"]["morse_index"] == 2,
    DATA["route_a_evaluator_audit"]["canonical_tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
    DATA["route_a_verdict"]["A1"] == "A1_WEAK",
    DATA["route_a_verdict"]["A2"] == "A2_FAIL",
    DATA["route_a_verdict"]["A3"] == "A3_FAIL",
    DATA["route_a_verdict"]["A4"] == "A4_FORMAL_HINT",
    DATA["route_a_evaluator_audit"]["a1"]["target_prime_correspondence"] is False,
    DATA["route_a_evaluator_audit"]["a2"]["source_owned_dynamical_zeta_or_fredholm_object"] is False,
    DATA["route_a_evaluator_audit"]["a2"]["target_divisor_match"] is False,
])
assert all(predicates)
assert len(predicates) == 29
print(json.dumps({"status": "C120_SYMPY_CROSSCHECK_PASS", "checks": len(predicates)}, sort_keys=True))
