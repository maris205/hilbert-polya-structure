"""One bounded exact scalar-transfer diagnostic, not an all-layer theorem.

Reuse only the earlier pure graph constructors, never their main/analyze.
Output is stdout only. The input/terminal scalar sequence is certified by
an exact dimension-sufficient Cayley--Hamilton recurrence test, and then
the numerator and denominator are reduced over Q. No floating roots.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import hashlib
import json
import platform
import time

import sympy as sp


SOURCE = (Path(__file__).resolve().parents[2] / "continuation_round2"
          / "solenoid_boundary" / "semigroup_probe.py")
spec = spec_from_file_location("prior_pure_graph", SOURCE)
prior = module_from_spec(spec)
spec.loader.exec_module(prior)
x, t = sp.symbols("x t")


def berlekamp_massey(sequence):
    """Field algorithm; returns order L and q with q[0]=1."""
    q, old = [Fraction(1)], [Fraction(1)]
    order, shift, last = 0, 1, Fraction(1)
    for n, value in enumerate(sequence):
        discrepancy = Fraction(value) + sum(
            q[j] * sequence[n-j] for j in range(1, order+1))
        if not discrepancy:
            shift += 1
            continue
        saved = q[:]
        coefficient = -discrepancy / last
        q.extend([Fraction(0)] * max(0, len(old)+shift-len(q)))
        for j, value_old in enumerate(old):
            q[j+shift] += coefficient * value_old
        if 2*order <= n:
            order = n+1-order
            old, last, shift = saved, discrepancy, 1
        else:
            shift += 1
    q.extend([Fraction(0)] * max(0, order+1-len(q)))
    return order, q[:order+1]


def transfer_matrix(group, edges):
    positions = {node: i for i, node in enumerate(group)}
    matrix = sp.zeros(len(group))
    for node, i in positions.items():
        for target in edges[node]:
            if target in positions:
                matrix[i, positions[target]] += 1
    return matrix


def polynomial(coefficients):
    return sp.Poly(sum(sp.Rational(c.numerator, c.denominator)*t**j
                       for j, c in enumerate(coefficients)), t, domain=sp.QQ)


def run_layer(k):
    start = time.monotonic()
    states, edges, failure = prior.graph(k, 250_000)
    if failure:
        raise RuntimeError(json.dumps(failure, sort_keys=True))
    dimension = len(states)
    groups, labels = prior.components(edges)
    all_factors = sp.Poly(1, x)
    closed = []
    for label, group in enumerate(groups):
        characteristic = transfer_matrix(group, edges).charpoly(x).as_poly()
        all_factors *= characteristic
        if all(labels[target] == label for node in group for target in edges[node]):
            closed.append({"size": len(group),
                           "characteristic": str(sp.factor(characteristic.as_expr()))})

    terminal = [int((state[0]+state[3]-1) % (2**k) == 0) for state in states]
    moments = []
    current = terminal
    for unused in range(3*dimension+1):
        moments.append(current[0])
        current = [sum(current[target] for target in row) for row in edges]
    order, q = berlekamp_massey(moments[:2*dimension+1])
    if order > dimension or q[0] != 1:
        raise RuntimeError("Invalid recurrence dimension or normalization")
    residual_count = 0
    for n in range(order, len(moments)):
        residual = sum(q[j]*moments[n-j] for j in range(order+1))
        if residual:
            raise RuntimeError(f"Exact recurrence fails at k={k}, n={n}")
        residual_count += 1
    if residual_count < dimension:
        raise RuntimeError("Insufficient Cayley--Hamilton certificate")

    numerator = polynomial([sum(q[j]*moments[n-j] for j in range(min(n, order)+1))
                            for n in range(order)])
    denominator = polynomial(q)
    common = sp.gcd(numerator, denominator)
    numerator = numerator.exquo(common)
    denominator = denominator.exquo(common)
    normalization = denominator.eval(0)
    numerator = numerator.mul_ground(1/normalization)
    denominator = denominator.mul_ground(1/normalization)
    if sp.gcd(numerator, denominator).degree() != 0 or denominator.eval(0) != 1:
        raise RuntimeError("Reduced rational function normalization failed")
    return {"k": k, "dimension": dimension, "status": "EXACT_FINITE_LAYER",
            "characteristic": str(sp.factor(all_factors.as_expr())),
            "closed_components": closed, "recurrence_order": order,
            "certificate_consecutive_residuals": residual_count,
            "numerator": str(sp.factor(numerator.as_expr())),
            "denominator": str(sp.factor(denominator.as_expr())),
            "denominator_degree": denominator.degree(),
            "first_moments": moments[:16],
            "elapsed_seconds": round(time.monotonic()-start, 6)}


def main():
    print(json.dumps({"python": platform.python_version(), "sympy": sp.__version__,
                      "graph_source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                      "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      "meaning": "Exact trace-one observable at k<=6; no all-layer conclusion"},
                     sort_keys=True), flush=True)
    for k in range(1, 7):
        print(json.dumps(run_layer(k), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
