#!/usr/bin/env python3
"""Independent symbolic Jaynes--Cummings block reconstruction for C223."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c223_jaynes_cummings_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text())
    checks = 0

    def zero(expr, message: str) -> None:
        nonlocal checks
        checks += 1
        if isinstance(expr, sp.MatrixBase):
            valid = all(sp.simplify(value) == 0 for value in expr)
        else:
            valid = sp.simplify(expr) == 0
        if not valid:
            raise AssertionError(message)

    wc, wq, g, n, lam = sp.symbols("omega_c omega_q g n lambda", real=True)
    npos = sp.symbols("n_pos", positive=True, real=True)
    delta = wq - wc
    center = (npos - sp.Rational(1, 2)) * wc
    sx = sp.Matrix([[0, 1], [1, 0]])
    sz = sp.diag(1, -1)
    ident = sp.eye(2)
    B = delta * sz / 2 + g * sp.sqrt(npos) * sx
    omega_sq = delta**2 + 4 * g**2 * npos
    zero(B * B - omega_sq * ident / 4, "traceless block square")
    H = center * ident + B
    zero(sp.trace(H) - 2 * center, "block trace")
    zero(H.det() - (center**2 - omega_sq / 4), "block determinant")
    zero(sp.factor((lam * ident - H).det()) - ((lam - center)**2 - omega_sq / 4), "characteristic polynomial")

    c, s = sp.symbols("c s", real=True)
    omega = sp.symbols("Omega", positive=True, real=True)
    # Replace B by a generic real Pauli vector with b_x^2+b_z^2=1.
    bx, bz = sp.symbols("b_x b_z", real=True)
    A = bx * sx + bz * sz
    U0 = c * ident - sp.I * s * A
    gram = (U0.conjugate().T * U0 - ident).applyfunc(
        lambda expr: sp.simplify(sp.expand(expr).subs(bz**2, 1 - bx**2).subs(s**2, 1 - c**2))
    )
    zero(gram, "unitarity from Pauli square")
    zero(sp.trace(U0) - 2 * c, "reduced propagator trace")
    det_reduced = sp.expand(U0.det()).subs(bz**2, 1 - bx**2).subs(s**2, 1 - c**2)
    zero(det_reduced - 1, "reduced propagator determinant")
    zero(sp.expand(U0[1, 0] * sp.conjugate(U0[1, 0])) - s**2 * bx**2, "transition probability")

    gauge = sz
    zero(gauge * (delta * sz / 2 + g * sp.sqrt(npos) * sx) * gauge - (delta * sz / 2 - g * sp.sqrt(npos) * sx), "coupling sign gauge")

    # Bare diagonal entries reconstruct the center/detuning convention.
    excited = (npos - 1) * wc + wq / 2
    ground = npos * wc - wq / 2
    zero((excited + ground) / 2 - center, "center from bare energies")
    zero(excited - ground - delta, "detuning from bare energies")

    # At Omega*T=2*pi*k the reduced propagator is (-1)^k I.
    k = sp.symbols("k", integer=True)
    checks += 1
    if sp.simplify(sp.sin(sp.pi * k)) != 0:
        raise AssertionError("revival sine")
    checks += 1
    if sp.simplify(sp.cos(sp.pi * k) - (-1) ** k) != 0:
        raise AssertionError("revival parity")

    rows = data["regression"]["block_rows"] + data["regression"]["dynamics_rows"]
    for i, row in enumerate(rows):
        checks += 1
        if "n" not in row or row["n"] < 1:
            raise AssertionError(f"row block index {i}")
    print(json.dumps({"status": "C223_SYMPY_PASS", "checks": checks, "generic_symbolic_checks": checks - len(rows), "evidence_row_checks": len(rows)}, sort_keys=True))


if __name__ == "__main__":
    main()
