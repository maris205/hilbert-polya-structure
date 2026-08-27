#!/usr/bin/env python3
"""Separate symbolic derivation of the C189 Riccati and Möbius identities."""
import json
import sympy as s


def main() -> None:
    f, hr, hi = s.symbols("f hr hi", real=True)
    z, zb = s.symbols("z zb", nonzero=True)
    h, hb = hr + s.I * hi, hr - s.I * hi
    zdot = s.I * f * z + (h - hb * z**2) / 2
    zbdot = -s.I * f * zb + (hb - h * zb**2) / 2
    checks = []

    # Circle tangency and the phase-to-Riccati conversion on z*zb=1.
    checks.append(s.simplify((zdot * zb + z * zbdot).subs(zb, 1 / z)))
    phase_rhs = f + (h * zb - hb * z) / (2 * s.I)
    checks.append(s.simplify((zdot / (s.I * z) - phase_rhs).subs(zb, 1 / z)))

    # su(1,1) lift and its scalar square.
    A = s.Matrix([[s.I * f, h], [hb, -s.I * f]]) / 2
    J = s.diag(1, -1)
    checks.extend(list(A.conjugate().T * J + J * A))
    checks.append(s.trace(A))
    delta = f**2 - hr**2 - hi**2
    checks.extend(list(s.simplify(A * A + delta * s.eye(2) / 4)))

    # Direct projectivization gives the common Riccati vector field.
    projective = A[0, 0] * z + A[0, 1] - z * (A[1, 0] * z + A[1, 1])
    checks.append(s.simplify(projective - zdot))

    # SU(1,1) maps the unit circle to itself.
    aa, aac, bb, bbc = s.symbols("aa aac bb bbc")
    circle_numerator = (aa*z+bb)*(aac*zb+bbc) - (bbc*z+aac)*(bb*zb+aa)
    checks.append(s.expand(circle_numerator - (aa*aac-bb*bbc)*(z*zb-1)))

    # A general fractional-linear map preserves the selected cross ratio.
    ma, mb, mc, md = s.symbols("ma mb mc md")
    x1, x2, x3, x4 = s.symbols("x1 x2 x3 x4")
    def mob(x):
        return (ma*x+mb)/(mc*x+md)
    def cross(a, b, c, d):
        return (a-c)*(b-d)/((a-d)*(b-c))
    checks.append(s.cancel(cross(mob(x1), mob(x2), mob(x3), mob(x4)) - cross(x1, x2, x3, x4)))

    # The stationary quadratic has the stated discriminant normalization.
    sigma = s.symbols("sigma")
    root = (s.I*f + sigma) / hb
    polynomial = hb*root**2 - 2*s.I*f*root - h
    checks.append(s.simplify(polynomial - (sigma**2 + f**2 - h*hb)/hb))

    # Hyperbolic/parabolic boundary-root modulus identities.
    kappa = s.symbols("kappa", real=True)
    hyper_modulus = (kappa**2 + f**2) / (hr**2 + hi**2)
    checks.append(s.factor((hr**2+hi**2)*(hyper_modulus-1) - (kappa**2+f**2-hr**2-hi**2)))
    parabolic_modulus = f**2 / (hr**2 + hi**2)
    checks.append(s.factor((hr**2+hi**2)*(parabolic_modulus-1) - (f**2-hr**2-hi**2)))

    # The disk-automorphism coefficient normalization agrees projectively.
    rho, alpha, alphac = s.symbols("rho alpha alphac", nonzero=True)
    direct = rho * (z + alpha) / (1 + alphac*z)
    coefficient_form = (rho*z + rho*alpha) / (alphac*z + 1)
    checks.append(s.cancel(direct - coefficient_form))

    simplified = [s.simplify(value) for value in checks]
    failures = [index for index, value in enumerate(simplified, start=1) if value != 0]
    if failures:
        raise AssertionError({"failed_checks": failures, "values": [str(simplified[index-1]) for index in failures]})
    print(json.dumps({"status": "C189_SYMPY_PASS", "checks": len(checks)}, sort_keys=True))


if __name__ == "__main__":
    main()
