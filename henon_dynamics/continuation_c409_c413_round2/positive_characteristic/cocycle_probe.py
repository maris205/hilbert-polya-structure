#!/usr/bin/env python3
"""Fixed finite diagnostics for a new nonlinear additive cocycle; stdout only.

This does not rerun the frozen inverse-tower scripts. It computes the new
observables S_n(P)=sum(P(g^j(x))) for g=x+x^2 in truncated F_p[x].
No inferred formula for all p-powers is asserted by a successful run.
"""

import json
from math import comb

from flint import nmod_poly


def leading(poly, precision):
    terms = [(j, int(poly[j])) for j in range(min(len(poly), precision)) if poly[j]]
    return {"order": terms[0][0] if terms else None, "terms": terms[:4],
            "precision": precision}


def probe(p, precision):
    x = nmod_poly([0, 1], p)
    current = x
    forcings = tuple(range(1, p+3))
    sums = {k: nmod_poly([], p) for k in forcings}
    output = []
    for n in range(1, p*p+1):
        power = nmod_poly([1], p)
        for k in forcings:
            power = (power*current).truncate(precision)
            sums[k] = (sums[k]+power).truncate(precision)
        current = (current+current*current).truncate(precision)
        # x^2=g(x)-x is an exact telescoping control for the new observable.
        assert sums[2] == (current-x).truncate(precision)
        if n in (1, p, p*p):
            for k in forcings:
                output.append({"p": p, "n": n, "forcing_x_power": k,
                               **leading(sums[k], precision)})
    return output


def laurent_shear_obstruction(p, precision=64):
    """Test Q(g)-Q=x+c modulo x^precision with ord(Q)>=-1.

    A failed finite linear system refutes this restricted formal shear.
    Passing it would not establish an infinite compatible solution.
    """
    columns = []
    columns.append([(-1)**(i+1) % p for i in range(precision)])
    for k in range(1, precision):
        columns.append([comb(k, i-k) % p if k < i <= 2*k else 0
                        for i in range(precision)])
    columns.append([1]+[0]*(precision-1))  # free constant c
    rows = [[column[i] for column in columns]+[int(i == 1)] for i in range(precision)]
    rank = 0
    for col in range(len(columns)):
        pivot = next((i for i in range(rank, precision) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[pivot], rows[rank] = rows[rank], rows[pivot]
        inverse = pow(rows[rank][col], -1, p)
        rows[rank] = [(v*inverse) % p for v in rows[rank]]
        for i in range(precision):
            if i != rank and rows[i][col]:
                factor = rows[i][col]
                rows[i] = [(a-factor*b) % p for a, b in zip(rows[i], rows[rank])]
        rank += 1
    consistent = not any(not any(row[:-1]) and row[-1] for row in rows)
    return {"p": p, "precision": precision, "pole_order_at_most_one": True,
            "constant_allowed": True, "consistent_finite_system": consistent,
            "coefficient_rank": rank}


if __name__ == "__main__":
    print(json.dumps({"cases": probe(3, 128)+probe(5, 256),
                      "boundaries": {"all_height_proof": False,
                                     "truncated_zero_is_not_identity": True,
                                     "fixed_inputs_before_execution": True}}, indent=2))
