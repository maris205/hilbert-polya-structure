#!/usr/bin/env python3
"""Independent root-mesh reconstruction for HCS-P76."""

from __future__ import annotations

import cmath
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT / "results/c76_independent_check.json"


def mu(n: int) -> int:
    value, sign, p = n, 1, 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            sign = -sign
            if value % p == 0:
                return 0
        p += 1
    return -sign if value > 1 else sign


def coeff(m: int) -> Fraction:
    return sum(Fraction(d * mu(d), m) for d in range(1, m + 1) if m % d == 0 and d % 2)


fibers = []
for q in (0.4, 1.0, 2.5):
    rows = []
    previous = Decimal(0)
    for m in range(1, 65):
        cm = coeff(m)
        if not cm:
            raise SystemExit(f"zero coefficient at {m}")
        with localcontext() as context:
            context.prec = 100
            qd = Decimal(str(q))
            rho_exact = (-(Decimal(1) + qd ** (2 * m)).ln() / Decimal(2 * m)).exp()
        rho = float(rho_exact)
        if not rho_exact > previous:
            raise SystemExit(f"nonincreasing radius at q={q}, m={m}")
        previous = rho_exact
        max_residual = 0.0
        for k in range(2 * m):
            alpha = rho * cmath.exp(1j * math.pi * k / m)
            max_residual = max(
                max_residual,
                abs(1 - (1 + q ** (2 * m)) * alpha ** (2 * m)),
            )
        rows.append(
            {
                "m": m,
                "c_m": str(cm),
                "rho_m": format(rho_exact, "f"),
                "root_count": 2 * m,
                "max_residual": format(max_residual, ".6e"),
                "mesh_gap": format(math.pi / m, ".17g"),
            }
        )
    limit = min(1.0, 1.0 / q)
    if not Decimal(rows[-1]["rho_m"]) < Decimal(str(limit)):
        raise SystemExit("wrong limiting side")
    fibers.append({"q": q, "limit": limit, "rows": rows})

out = {
    "candidate_id": "HCS-P76",
    "method": "independent divisor-sum coefficients and complex root meshes",
    "fibers": fibers,
    "all_channels_nonzero": True,
    "all_radius_ladders_strict": True,
    "mesh_gap_tends_to_zero": True,
    "check": True,
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"candidate_id": "HCS-P76", "fibers": len(fibers), "rows": 192, "check": True}, sort_keys=True))
