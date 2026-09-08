#!/usr/bin/env python3
"""Independent exact substitution of IR1's final classification table.

This does not execute/import either finite-core enumerator. It proves only
the stated polynomial identities, not exhaustion or least-period coverage.
No files are written; all failures raise explicitly even under python -O.
"""
import json
from hashlib import sha256
from pathlib import Path

import sympy as sp

a, t, u, v, r, m = sp.symbols("a t u v r m", integer=True)
families = [
    ("F1", 2*r-r*r, (r,), r*r*(2*r-3)),
    ("F2", u+v-u*v, (u, v), u*v*(u+v-3)),
    ("F3", 2*t-4, (-2, -2, t), 8-(t-4)**2),
    ("F4", a, (-1, t, -1, a+1-t), t*t-(a+1)*t+2*a+2),
    ("F5", -1, (-1, t, 0, 0, -1-t), t*(t+1)),
    ("E5", -13, (-4, -2, -3, -3, -2), -64),
    ("F6", 0, (0, 0, t, 0, 0, -t), t*t),
    ("F8", -1, (-1, t, 1, t, -1, -t-2, 1, -t-2), (t+1)**2+1),
    ("E9", -2, (-2, -1, 0, 0, -1, -2, 0, -1, 0), -1),
    ("F12", 0, (1, m, 1, m-1, -1, -m, 1, 1-m, 1, -m, -1, m-1),
     m*m-m+2),
]


def require_zero(expr, label):
    residual = sp.expand(expr)
    if residual != 0:
        raise ValueError(f"{label}: nonzero residual {residual}")


def run():
    rows = []
    for name, force, word, level in families:
        length = len(word)
        for i in range(length):
            x, y, z, following = (word[(i+j) % length] for j in range(4))
            require_zero(following-y*z-force+x, f"{name}: recurrence phase {i}")
            require_zero(x*x+y*y+z*z-x*y*z-force*(x+y+z)-level,
                         f"{name}: invariant phase {i}")
        rows.append({"family": name, "all_wraparound_phases": length,
                     "recurrence": "IDENTITY", "level": "IDENTITY"})
    # Independent invariant verification on the full polynomial phase space.
    x, y, z, force = sp.symbols("x y z force")
    invariant = lambda b, c, d: b*b+c*c+d*d-b*c*d-force*(b+c+d)
    require_zero(invariant(y, z, y*z+force-x)-invariant(x, y, z),
                 "global invariant")
    # The quadratic equations used to turn level membership into finite tests.
    P, S, k = sp.symbols("P S k")
    require_zero((P*(S-3)).subs(S, P+a)-(P*P+(a-3)*P), "F2 level reduction")
    require_zero((a+1)**2-4*(2*a+2-k)-((a+1)*(a-7)+4*k), "F4 discriminant")
    require_zero(4*t*(t+1)+1-(2*t+1)**2, "F5 discriminant")
    require_zero(4*(m*m-m+2)-7-(2*m-1)**2, "F12 discriminant")
    print(json.dumps({"sympy_version": sp.__version__, "families": rows,
                      "family_phase_checks_per_identity": sum(len(w) for _, _, w, _ in families),
                      "global_invariance": "IDENTITY", "count_reductions": "IDENTITY",
                      "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
                      "exhaustion_or_minimality_checked": False}, indent=2, sort_keys=True))


if __name__ == "__main__":
    run()
