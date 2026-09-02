#!/usr/bin/env python3
"""Producer-independent symbolic checks for the finite SSH theorem package."""
from __future__ import annotations

import sys

import sympy as sp


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C318 SymPy lane refuses optimized Python")
    y, v, w, z = sp.symbols("y v w z", real=True, nonzero=True)
    checks = 0

    def zero(expr, label):
        nonlocal checks
        entries = list(expr) if isinstance(expr, sp.MatrixBase) else [expr]
        for entry in entries:
            if sp.cancel(sp.factor(entry)) != 0:
                raise AssertionError(label)
            checks += 1

    # Two independent constructions: the Jacobi continuant in y and the
    # Chebyshev representation with the full (vw)^M prefactor.
    q0, q1 = sp.Integer(1), y - v**2
    for m in range(1, 13):
        if m == 1:
            qm = q1
        else:
            q0, q1 = q1, sp.expand((y - v**2 - w**2) * q1 - v**2 * w**2 * q0)
            qm = q1
        x = (y - v**2 - w**2) / (2 * v * w)
        cheb = (v * w) ** m * (sp.chebyshevu(m, x) + w * sp.chebyshevu(m - 1, x) / v)
        zero(qm - cheb, f"Chebyshev prefactor M={m}")
        zero(sp.Poly(qm, y).LC() - 1, f"monic M={m}")
        zero(qm.subs(y, 0) - (-1) ** m * v ** (2 * m), f"constant M={m}")

    # Direct 2M-site determinants guard the alternation and block convention.
    E = sp.symbols("E")
    for m in range(1, 7):
        h = sp.zeros(2 * m)
        for j in range(m):
            h[j, m + j] = h[m + j, j] = v
            if j + 1 < m:
                h[j + 1, m + j] = h[m + j, j + 1] = w
        direct = sp.det(E * sp.eye(2 * m) - h)
        q0m, q1m = sp.Integer(1), E**2 - v**2
        for _ in range(2, m + 1):
            q0m, q1m = q1m, sp.expand((E**2 - v**2 - w**2) * q1m - v**2 * w**2 * q0m)
        zero(direct - q1m, f"site determinant M={m}")
        gamma = sp.diag(*([1] * m + [-1] * m))
        zero(gamma * h * gamma + h, f"chiral block M={m}")

    # Rational z=e^{-kappa} witnesses: root equation, energy convention,
    # both block equations, normalization symmetry, and strict threshold.
    for m in range(2, 21):
        ratio = (1 - z ** (2 * m + 2)) / (z * (1 - z ** (2 * m)))
        xz = -(z + 1 / z) / 2
        energy = z ** (m - 1) * (1 - z**2) / (1 - z ** (2 * m))
        zero(sp.chebyshevu(m, xz) + ratio * sp.chebyshevu(m - 1, xz), f"hyperbolic secular M={m}")
        zero(energy - ratio * z**m * (1 - z**2) / (1 - z ** (2 * m + 2)), f"energy dual M={m}")
        zero(sp.limit(ratio, z, 1) - sp.Rational(m + 1, m), f"finite threshold M={m}")
        a = [(-1) ** (j - 1) * (z ** (-(m + 1 - j)) - z ** (m + 1 - j)) / 2 for j in range(1, m + 1)]
        b = [(-1) ** (j - 1) * (z ** (-j) - z**j) / 2 for j in range(1, m + 1)]
        for j in range(m):
            tb = b[j] + (ratio * b[j - 1] if j else 0)
            tstar_a = a[j] + (ratio * a[j + 1] if j + 1 < m else 0)
            zero(tb - energy * a[j], f"T b M={m},j={j}")
            zero(tstar_a - energy * b[j], f"Tstar a M={m},j={j}")
        zero(sum(u * u for u in a) - sum(u * u for u in b), f"edge norm symmetry M={m}")

    # The threshold is a genuine band-edge vector, not an exact zero mode.
    for m in range(2, 41):
        vm, wm = sp.Integer(m), sp.Integer(m + 1)
        a = [(-1) ** (j - 1) * (m + 1 - j) for j in range(1, m + 1)]
        b = [(-1) ** (j - 1) * j for j in range(1, m + 1)]
        for j in range(m):
            zero(vm * b[j] + (wm * b[j - 1] if j else 0) - a[j], f"threshold T M={m},j={j}")
            zero(vm * a[j] + (wm * a[j + 1] if j + 1 < m else 0) - b[j], f"threshold Tstar M={m},j={j}")

    # The raw hyperbolic vectors vanish as kappa tends to zero.  Their
    # common 1/kappa rescaling has the claimed nonzero linear-taper limit.
    kappa = sp.symbols("kappa", positive=True)
    for n in range(1, 41):
        zero(sp.limit(sp.sinh(n * kappa) / kappa, kappa, 0) - n, f"rescaled taper n={n}")

    # All hopping faces and the one-cell convention.
    for m in range(1, 31):
        q0, qm = sp.Integer(1), y - v**2
        for _ in range(2, m + 1):
            q0, qm = qm, sp.expand((y - v**2 - w**2) * qm - v**2 * w**2 * q0)
        zero(qm.subs(w, 0) - (y - v**2) ** m, f"w=0 face M={m}")
        zero(qm.subs(v, 0) - y * (y - w**2) ** (m - 1), f"v=0 face M={m}")
        zero(qm.subs({v: 0, w: 0}) - y**m, f"origin face M={m}")
    zero((E * sp.eye(2) - sp.Matrix([[0, v], [v, 0]])).det() - (E**2 - v**2), "M=1 open")
    zero((E * sp.eye(2) - sp.Matrix([[0, v + w], [v + w, 0]])).det() - (E**2 - (v + w) ** 2), "M=1 periodic")

    # Independent finite-matrix power identities underlying the entire sinc
    # propagator.  They remain valid when either hopping is zero.
    for m in range(2, 7):
        vm, wm = sp.Integer(m + 1), sp.Integer(m - 1)
        tmat = sp.zeros(m)
        for j in range(m):
            tmat[j, j] = vm
            if j:
                tmat[j, j - 1] = wm
        h = sp.Matrix.vstack(sp.Matrix.hstack(sp.zeros(m), tmat), sp.Matrix.hstack(tmat.T, sp.zeros(m)))
        for n in range(0, 9):
            even = sp.diag((tmat * tmat.T) ** n, (tmat.T * tmat) ** n)
            odd = sp.Matrix.vstack(
                sp.Matrix.hstack(sp.zeros(m), (tmat * tmat.T) ** n * tmat),
                sp.Matrix.hstack((tmat.T * tmat) ** n * tmat.T, sp.zeros(m)),
            )
            zero(h ** (2 * n) - even, f"even block power M={m},n={n}")
            zero(h ** (2 * n + 1) - odd, f"odd block power M={m},n={n}")

    # Bloch dispersion, winding orientation convention, parity point, and
    # mode-resolved quench orthogonality.
    k = sp.symbols("k", real=True)
    qk = v + w * sp.exp(sp.I * k)
    hk = sp.Matrix([[0, v + w * sp.exp(-sp.I * k)], [qk, 0]])
    zero(sp.det(E * sp.eye(2) - hk) - (E**2 - v**2 - w**2 - v * w * (sp.exp(sp.I * k) + sp.exp(-sp.I * k))), "Bloch determinant")
    zero(sp.trigsimp(sp.expand_complex(sp.exp(sp.I * k) + sp.exp(-sp.I * k))) - 2 * sp.cos(k), "Bloch cosine dispersion")
    zero(sp.im(sp.conjugate(qk) * sp.diff(qk, k)).subs(k, 0) - w * (v + w), "counterclockwise orientation")
    zero(qk.subs(k, sp.pi) - (v - w), "critical k=pi")
    for m in range(2, 16):
        if m % 2 == 0:
            zero(
                (v**2 + w**2 + 2 * v * w * sp.cos(sp.pi)) - (v - w) ** 2,
                f"even sampled gap square M={m}",
            )
        else:
            nearest_square = v**2 + w**2 + 2 * v * w * sp.cos(sp.pi - sp.pi / m)
            odd_formula = v**2 + w**2 - 2 * v * w * sp.cos(sp.pi / m)
            zero(sp.trigsimp(nearest_square - odd_formula), f"odd sampled gap square M={m}")
    theta = sp.symbols("theta", real=True)
    zero(
        sp.trigsimp(2 * (1 - sp.cos(theta)) - 4 * sp.sin(theta / 2) ** 2),
        "odd critical sampled-gap half-angle identity",
    )
    vi, wi, vf, wf = sp.symbols("v_i w_i v_f w_f", positive=True)
    ck = -(vi * vf + wi * wf) / (vi * wf + wi * vf)
    zero(vi * vf + wi * wf + (vi * wf + wi * vf) * ck, "quench orthogonality")
    zero(ck.subs({vi: 3, wi: 1, vf: 1, wf: 5}) + sp.Rational(1, 2), "grid-hit cosine")
    for multiple in range(1, 11):
        zero(sp.cos(2 * sp.pi * multiple / (3 * multiple)) + sp.Rational(1, 2), f"grid mode M={3*multiple}")

    print(f"C318 SymPy cross-check: PASS ({checks} identities; producer import forbidden)")


if __name__ == "__main__":
    main()
