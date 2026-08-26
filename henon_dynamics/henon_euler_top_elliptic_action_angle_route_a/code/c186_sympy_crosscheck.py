#!/usr/bin/env python3
"""Separate symbolic reconstruction of the C186 coefficient identities."""
import json
import sympy as s


def main() -> None:
    a, b, c, e, G = s.symbols("a b c e G", positive=True)
    checks = []

    A2=(e-c)/(a-c); B2=(e-c)/(b-c); C2=(a-e)/(a-c)
    k2=(a-b)*(e-c)/((b-c)*(a-e)); w2=G**2*(b-c)*(a-e)
    checks += [A2+C2-1, -A2+B2-C2*k2, a*A2+c*C2-e,
               -a*A2+b*B2-c*C2*k2,
               w2*A2-G**2*(b-c)**2*B2*C2,
               w2*B2-G**2*(a-c)**2*A2*C2,
               w2*k2**2*C2-G**2*(a-b)**2*A2*B2]

    A2=(e-c)/(a-c); B2=(a-e)/(a-b); C2=(a-e)/(a-c)
    k2=(b-c)*(a-e)/((a-b)*(e-c)); w2=G**2*(a-b)*(e-c)
    checks += [A2+C2-1, -A2*k2+B2-C2, a*A2+c*C2-e,
               -a*A2*k2+b*B2-c*C2,
               w2*A2*k2**2-G**2*(b-c)**2*B2*C2,
               w2*B2-G**2*(a-c)**2*A2*C2,
               w2*C2-G**2*(a-b)**2*A2*B2]

    As=(b-c)/(a-c); Cs=(a-b)/(a-c); rs=G**2*(a-b)*(b-c)
    checks += [As+Cs-1, a*As+c*Cs-b,
               rs*As-G**2*(b-c)**2*Cs,
               rs*Cs-G**2*(a-b)**2*As]

    linear = [-G**2*(a-b)*(a-c), G**2*(a-b)*(b-c), -G**2*(a-c)*(b-c)]
    checks += [linear[0]+G**2*(a-b)*(a-c), linear[1]-G**2*(a-b)*(b-c), linear[2]+G**2*(a-c)*(b-c)]

    M1, M2, M3 = s.symbols("M1 M2 M3", real=True)
    M = s.Matrix([M1, M2, M3])
    variables = (M1, M2, M3)
    radius = s.sqrt(M1**2 + M2**2 + M3**2)

    def bracket(f, h):
        grad_f = s.Matrix([s.diff(f, x) for x in variables])
        grad_h = s.Matrix([s.diff(h, x) for x in variables])
        return -M.dot(grad_f.cross(grad_h))

    q3 = s.atan(M2 / M1)
    q1 = s.atan(M3 / M2)
    checks += [bracket(q3, M3) + 1, bracket(q3, radius - M3) - 1,
               bracket(q1, M1) + 1, bracket(q1, radius - M1) - 1]
    for i, expr in enumerate(checks, 1):
        if s.factor(s.cancel(expr)) != 0:
            raise AssertionError(f"symbolic identity {i} failed: {expr}")
    print(json.dumps({"status": "C186_SYMPY_PASS", "symbolic_checks": len(checks)}, sort_keys=True))


if __name__ == "__main__":
    main()
