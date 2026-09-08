"""Exact bounded oldform-block falsifier; not an all-level proof.

E(p**j z,s) at a width-one cusp of denominator p**a has incoming
coefficient p**(s * h(e,j,a)), h=e-min(2*a,e)+2*min(a,j)-j.
This follows by reducing the rational cusp p**j * u/p**a and
using the level-one modular invariance; its outgoing coefficient is
phi(s) times the same expression at 1-s.
The class-constant reduced block therefore satisfies C(s) P(s)=C(1-s).
No s-dependent similarity is used to compare P(s) and P(t).
"""

import json
import platform

import sympy as sp


def incoming(p, e, s):
    return sp.Matrix([
        [
            sp.Integer(p) ** (
                s * (e - min(2 * a, e) + 2 * min(a, j) - j)
            )
            for a in range(e + 1)
        ]
        for j in range(e + 1)
    ])


def block(p, e, s):
    return incoming(p, e, s).inv() * incoming(p, e, 1 - s)


def main():
    rows = []
    for p in (2, 3, 5, 7):
        for e in range(1, 11):
            p2 = block(p, e, 2)
            p3 = block(p, e, 3)
            commutator = p2 * p3 - p3 * p2
            support = [
                (i, j, str(commutator[i, j]))
                for i in range(e + 1)
                for j in range(e + 1)
                if commutator[i, j] != 0
            ]
            rows.append({
                "prime": p,
                "exponent": e,
                "parameters": [2, 3],
                "dimension": e + 1,
                "commutator_nonzero_entries": len(support),
                "first_nonzero": support[0] if support else None,
            })
    print(json.dumps({
        "kind": "bounded_exact_oldform_block_falsifier",
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "cells": len(rows),
        "rows": rows,
        "scope": "Exact finite diagnostics conditional on the stated constant-term reduction; not a proof of all-level commutativity."
    }, indent=2))


if __name__ == "__main__":
    main()
