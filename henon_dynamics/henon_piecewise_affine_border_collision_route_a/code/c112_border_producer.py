#!/usr/bin/env python3
"""Exact finite pilot for a two-branch border-collision Hénon map (C112)."""
from __future__ import annotations
import itertools, json
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c112_border_evidence.json"
NMAX = 8
RHO = (Q(1, 2), Q(2, 3))
B = ((Q(-5), Q(-1)), (Q(1), Q(0)))
D = ((Q(-2), Q(0)), (Q(2), Q(0)))

def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mv(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(2)) for i in range(2))
def det(a): return a[0][0] * a[1][1] - a[0][1] * a[1][0]
def identity(): return ((Q(1), Q(0)), (Q(0), Q(1)))
def affine_step(m, t, symbol):
    return mm(B, m), tuple(x + y for x, y in zip(mv(B, t), D[symbol]))
def rotations(word): return [tuple(word[i:] + word[:i]) for i in range(len(word))]
def primitive(word):
    n = len(word)
    return all(tuple(word) != tuple(word[:d] * (n // d)) for d in range(1, n) if n % d == 0)
def qstr(x): return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
def qmat(m): return [[qstr(x) for x in row] for row in m]
def qvec(v): return [qstr(x) for x in v]

def fixed_point(word):
    m, t = identity(), (Q(0), Q(0))
    for symbol in word: m, t = affine_step(m, t, symbol)
    lhs = ((Q(1) - m[0][0], -m[0][1]), (-m[1][0], Q(1) - m[1][1]))
    dd = det(lhs)
    if dd == 0: raise AssertionError("singular affine return")
    z = ((t[0] * lhs[1][1] - lhs[0][1] * t[1]) / dd,
         (lhs[0][0] * t[1] - t[0] * lhs[1][0]) / dd)
    current = z
    for symbol in word:
        if current[0] == 0 or ((current[0] < 0) != (symbol == 0)):
            raise AssertionError((word, z, current, symbol))
        current = (B[0][0] * current[0] + B[0][1] * current[1] + D[symbol][0], current[0])
    if current != z: raise AssertionError((word, z, current))
    return m, z

def primitive_rows():
    rows = []
    for n in range(1, NMAX + 1):
        seen = set()
        for word in itertools.product((0, 1), repeat=n):
            if not primitive(list(word)): continue
            canon = min(rotations(list(word)))
            if canon in seen: continue
            seen.add(canon)
            m, z = fixed_point(canon)
            weight = Q(1)
            for symbol in canon: weight *= RHO[symbol]
            rows.append({"length": n, "word": "".join(map(str, canon)), "symbols": list(canon),
                         "canonical_rotation": list(canon), "fixed_point": qvec(z), "monodromy": qmat(m),
                         "monodromy_trace": qstr(m[0][0] + m[1][1]), "monodromy_determinant": qstr(det(m)),
                         "branch_weight": qstr(weight), "rooted_start_multiplicity": n,
                         "cyclic_stabilizer_size": 1, "orientation_sign": 1, "domain_check": True})
    return rows

def block_transfer():
    out = sp.zeros(4); b = sp.Matrix([[-5, -1], [1, 0]])
    for i in range(2):
        for j in range(2):
            out[2*i:2*i+2, 2*j:2*j+2] = sp.Rational(RHO[j].numerator, RHO[j].denominator) * b
    return out

def main():
    rows = primitive_rows(); transfer = block_transfer(); z = sp.Symbol("z")
    rooted = {str(n): 2**n for n in range(1, NMAX + 1)}
    prim = {str(n): sum(r["length"] == n for r in rows) for n in range(1, NMAX + 1)}
    determinant_poly = sp.factor((sp.eye(4) - z * transfer).det())
    traces = {str(n): str(sp.factor(sp.trace(transfer**n))) for n in range(1, NMAX + 1)}
    unweighted = sp.zeros(4); b = sp.Matrix([[-5, -1], [1, 0]])
    for i in range(2):
        for j in range(2): unweighted[2*i:2*i+2, 2*j:2*j+2] = b
    payload = {"schema": "hcs-c112-piecewise-affine-border-v1", "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
      "source_model": {"map": "P_s(x,y)=(-5*x+c_s-y,x), c_0=-2,c_1=2", "branch_domains": {"0":"x<0","1":"x>0"},
        "border":"x=0 excluded from the periodic ledger", "branch_jacobians":qmat(B),
        "branch_weights":[qstr(x) for x in RHO], "max_period":NMAX,
        "pilot":"all binary words with exact affine fixed-point/domain checks"},
      "primitive_rows": rows, "rooted_word_counts": rooted, "primitive_necklace_counts": prim,
      "weighted_transfer_matrix": [[str(transfer[i,j]) for j in range(4)] for i in range(4)],
      "weighted_transfer_determinant": str(determinant_poly), "weighted_transfer_traces": traces,
      "unweighted_control_determinant": str(sp.factor((sp.eye(4)-z*unweighted).det())),
      "verdict": {"A1":"A1_PARTIAL_CERTIFIED", "A2":"A2_CERTIFIED_PREFIX", "A3":"A3_NOT_ADDRESSED", "A4":"A4_FAIL",
        "qualification":"finite piecewise-affine branch pilot; no global Markov theorem or Fredholm owner"},
      "nonclaims":["complete border-collision repeller","analytic Fredholm determinant","arithmetic data","Route B"]}
    raw = json.dumps(payload, sort_keys=True, indent=2) + "\n"; OUT.write_text(raw)
    print(json.dumps({"evidence_sha256":sha256(raw.encode()).hexdigest(),"primitive_necklaces":len(rows),
      "determinant":str(determinant_poly),"status":"C112_PREFREEZE_G3_PASS"}, sort_keys=True))
if __name__ == "__main__": main()
