#!/usr/bin/env python3
"""Independent symbolic derivation checks for HCS-C274."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    c, z, lam, t = sp.symbols("c z lambda t", real=True)
    J = sp.zeros(6)
    for i in range(3):
        J[i, i+3], J[i+3, i] = 1, -1
    K = sp.zeros(6)
    K[0, 0] = K[1, 1] = c**2/sp.Integer(4)-z**2/sp.Integer(2)
    K[2, 2] = z**2
    K[3, 3] = K[4, 4] = K[5, 5] = 1
    K[1, 3] = K[3, 1] = c/2
    K[0, 4] = K[4, 0] = -c/2
    A = J*K
    tests = []
    tests.append(K == K.T)
    ham = sp.simplify(A.T*J+J*A)
    tests.extend(ham[i, j] == 0 for i in range(6) for j in range(6))

    expected_char = (lam**2+z**2)*(lam**4+(c**2-z**2)*lam**2+z**4/sp.Integer(4))
    cp = A.charpoly()
    tests.append(sp.expand(cp.as_expr().subs(cp.gen, lam)-expected_char) == 0)

    # The canonical-to-velocity gauge map reproduces the Lorentz-force ODE.
    T = sp.eye(6)
    T[3, 1], T[4, 0] = c/2, -c/2
    Av = sp.simplify(T*A*T.inv())
    expected_v = sp.zeros(6)
    expected_v[0, 3] = expected_v[1, 4] = expected_v[2, 5] = 1
    expected_v[3, 0], expected_v[3, 4] = z**2/2, c
    expected_v[4, 1], expected_v[4, 3] = z**2/2, -c
    expected_v[5, 2] = -z**2
    tests.extend(sp.simplify(Av[i, j]-expected_v[i, j]) == 0 for i in range(6) for j in range(6))

    # Signed-field reversal is a canonical conjugacy.
    R = sp.diag(1, -1, 1, 1, -1, 1)
    tests.append(sp.simplify(R.T*J*R-J) == sp.zeros(6))
    tests.append(sp.simplify(R*A*R-A.subs(c, -c)) == sp.zeros(6))

    # Frequency and signed-action identities in the stable chamber.
    wp, wm = sp.symbols("omega_plus omega_minus", positive=True)
    cc, zz2, root = wp+wm, 2*wp*wm, wp-wm
    tests.extend([
        sp.expand(cc**2-2*zz2-root**2) == 0,
        sp.expand((cc+root)/2-wp) == 0,
        sp.expand((cc-root)/2-wm) == 0,
        sp.expand(wp*wm-zz2/2) == 0,
    ])
    ap, bp, am, bm = sp.symbols("a_plus b_plus a_minus b_minus", real=True)
    x, y = ap+am, bp+bm
    vx, vy = wp*bp+wm*bm, -wp*ap-wm*am
    Hr = (vx**2+vy**2)/2-zz2*(x**2+y**2)/4
    Ip = root*(ap**2+bp**2)/2
    Im = root*(am**2+bm**2)/2
    tests.append(sp.expand(Hr-(wp*Ip-wm*Im)) == 0)
    tests.append(sp.expand(Hr.subs({am: 0, bm: 0})-wp*Ip) == 0)
    tests.append(sp.expand(Hr.subs({ap: 0, bp: 0})+wm*Im) == 0)

    # Entire rotating-frame flow solves the radial equation.
    r = sp.symbols("r", nonzero=True, real=True)
    u0, v0 = sp.symbols("u0 v0")
    C = sp.cos(r*t/2)
    S = 2*sp.sin(r*t/2)/r
    w = C*u0+S*(v0+sp.I*c*u0/2)
    u = sp.exp(-sp.I*c*t/2)*w
    tests.append(sp.trigsimp(sp.diff(w, t, 2)+r**2*w/4) == 0)
    wf = sp.Function("w")(t)
    uf = sp.exp(-sp.I*c*t/2)*wf
    transformed = sp.simplify(
        sp.exp(sp.I*c*t/2)*(sp.diff(uf, t, 2)+sp.I*c*sp.diff(uf, t)-z**2*uf/2)
    )
    tests.append(sp.simplify(transformed-(sp.diff(wf, t, 2)+(c**2-2*z**2)*wf/4)) == 0)
    tests.append(sp.simplify(u.subs(t, 0)-u0) == 0)
    tests.append(sp.simplify(sp.diff(u, t).subs(t, 0)-v0) == 0)
    tests.append(sp.trigsimp(C**2+r**2*S**2/4-1) == 0)
    tests.append(sp.simplify(sp.diff(S, t)-C) == 0)
    tests.append(sp.simplify(sp.diff(C, t)+r**2*S/4) == 0)
    tests.append(sp.limit(C, r, 0) == 1)
    tests.append(sp.limit(S, r, 0) == t)

    # Critical and zero-axial boundary formulas are true limits, not new models.
    critical = sp.simplify(sp.limit(u, r, 0))
    expected_critical = sp.exp(-sp.I*c*t/2)*(u0+t*(v0+sp.I*c*u0/2))
    tests.append(sp.simplify(critical-expected_critical) == 0)
    tests.append(sp.limit(sp.sin(z*t)/z, z, 0) == t)
    tests.append(sp.limit(sp.cos(z*t), z, 0) == 1)

    # Radial spectral factors agree with the two circular frequencies.
    radial_modes = sp.expand((lam**2+wp**2)*(lam**2+wm**2))
    radial_expected = lam**4+(cc**2-zz2)*lam**2+zz2**2/4
    tests.append(sp.expand(radial_modes-radial_expected) == 0)

    assert all(tests), [i for i, value in enumerate(tests) if not value]
    print(f"C274_SYMPY_PASS ({len(tests)} symbolic identities; Hamiltonian flow, gauge, spectrum, actions, boundaries)")


if __name__ == "__main__":
    main()
