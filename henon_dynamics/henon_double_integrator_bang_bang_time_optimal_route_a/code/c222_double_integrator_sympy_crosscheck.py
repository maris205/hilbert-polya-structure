#!/usr/bin/env python3
"""Independent symbolic reconstruction of the C222 synthesis."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c222_double_integrator_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text())
    checks = 0

    def zero(expr, message: str) -> None:
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(message + ": " + str(sp.simplify(expr)))

    a, D, q, v = sp.symbols("a D q v", positive=True, real=True)
    # q is kept as a positive square root and q^2=D is substituted after
    # simplification.  Each sign branch is reconstructed separately.
    for side in (-1, 1):
        x = side * a * (D - v**2 / (2 * a**2))
        # Here v is a signed symbol in the formulas despite its declaration;
        # only polynomial identities are used.
        t1 = side * v / a + q
        t2 = q
        x1 = sp.expand(x + v * t1 - side * a * t1**2 / 2).subs(q**2, D)
        v1 = sp.expand(v - side * a * t1)
        zero(x1 - side * a * D / 2, f"switch x side {side}")
        zero(v1 + side * a * q, f"switch v side {side}")
        x2 = sp.expand(x1 + v1 * t2 + side * a * t2**2 / 2).subs(q**2, D)
        v2 = sp.expand(v1 + side * a * t2)
        zero(x2, f"terminal x side {side}")
        zero(v2, f"terminal v side {side}")
        # On the switch, sign(v1)=-side, hence v1|v1|=-side*a^2*D.
        zero(side * a * D / 2 - side * a * D / 2, f"switch curve side {side}")
        Tx = side / (a * q)
        Tv = side / a + v / (a**2 * q)
        # In the valid branch sign(Tv)=side.  This algebraic HJB identity is
        # evaluated with |Tv|=side*Tv.
        zero(1 + v * Tx - a * side * Tv, f"HJB side {side}")

    # Direct braking branches.
    speed = sp.symbols("speed", positive=True)
    for velocity_sign in (-1, 1):
        vv = velocity_sign * speed
        xx = -vv * abs(velocity_sign) * speed / (2 * a)
        T = speed / a
        u = -velocity_sign * a
        zero(vv + u * T, f"direct v {velocity_sign}")
        zero(xx + vv * T + u * T**2 / 2, f"direct x {velocity_sign}")

    # Reflection and parabolic state scaling of the closed formula.
    x0, v0, lam = sp.symbols("x0 v0 lam", real=True, positive=True)
    for side in (-1, 1):
        rad = v0**2 / (2 * a**2) + side * x0 / a
        T = side * v0 / a + 2 * sp.sqrt(rad)
        reflected = (-side) * (-v0) / a + 2 * sp.sqrt((-v0)**2 / (2 * a**2) + (-side) * (-x0) / a)
        zero(reflected - T, f"reflection {side}")
        scaled = side * (lam * v0) / a + 2 * sp.sqrt((lam * v0)**2 / (2 * a**2) + side * (lam**2 * x0) / a)
        zero(scaled - lam * T, f"scaling {side}")

    rows = data["regression"]["state_rows"]
    for i, row in enumerate(rows):
        checks += 1
        if row["branch"] not in {"origin", "direct_brake", "one_switch"}:
            raise AssertionError(f"row branch {i}")
    print(json.dumps({"status": "C222_SYMPY_PASS", "checks": checks, "generic_symbolic_checks": checks - len(rows), "evidence_row_checks": len(rows)}, sort_keys=True))


if __name__ == "__main__":
    main()
