#!/usr/bin/env python3
"""Exact C128 certificate in Q(zeta_7,sqrt(7))."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

N = 7
INV2 = 4
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results" / "c128_metaplectic_evidence.json"
CZ = tuple(Fraction(0) for _ in range(6))


def ca(a, b): return tuple(x + y for x, y in zip(a, b))
def cs(a, s): return tuple(s * x for x in a)


def zeta(k: int):
    k %= 7
    if k == 6:
        return tuple(Fraction(-1) for _ in range(6))
    out = list(CZ)
    out[k] = Fraction(1)
    return tuple(out)


def cm(a, b):
    raw = [Fraction(0) for _ in range(7)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            raw[(i + j) % 7] += x * y
    return tuple(raw[k] - raw[6] for k in range(6))


def cc(a):
    out = CZ
    for k, value in enumerate(a):
        out = ca(out, cs(zeta(-k), value))
    return out


# Elements are a+b*sqrt(7), with a,b in Q(zeta_7).
EZ = (CZ, CZ)
EO = (zeta(0), CZ)


def ea(x, y): return ca(x[0], y[0]), ca(x[1], y[1])
def es(x, s): return cs(x[0], s), cs(x[1], s)
def em(x, y): return ca(cm(x[0], y[0]), cs(cm(x[1], y[1]), 7)), ca(cm(x[0], y[1]), cm(x[1], y[0]))
def ec(x): return cc(x[0]), cc(x[1])
def ez(k): return zeta(k), CZ
def normalized_root(k): return CZ, cs(zeta(k), Fraction(1, 7))


def madd(A, B): return [[ea(x, y) for x, y in zip(rx, ry)] for rx, ry in zip(A, B)]


def mmul(A, B):
    rows, inner, cols = len(A), len(B), len(B[0])
    out = [[EZ for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for k in range(inner):
            if A[i][k] == EZ:
                continue
            for j in range(cols):
                out[i][j] = ea(out[i][j], em(A[i][k], B[k][j]))
    return out


def madj(A): return [[ec(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def mconj(A): return [[ec(x) for x in row] for row in A]


def mid(n):
    return [[EO if i == j else EZ for j in range(n)] for i in range(n)]


def mpow(A, n):
    out = mid(len(A))
    base = A
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def mscale(A, s): return [[es(x, s) for x in row] for row in A]
def mtrace(A):
    out = EZ
    for i in range(len(A)):
        out = ea(out, A[i][i])
    return out


def phase_matrix(kind: str):
    if kind == "F":
        return [[normalized_root(x * y) for y in range(N)] for x in range(N)]
    if kind == "U":
        return [[normalized_root(3 * INV2 * x * x - x * y) for y in range(N)] for x in range(N)]
    raise ValueError(kind)


def weyl(q: int, p: int):
    out = [[EZ for _ in range(N)] for _ in range(N)]
    for x in range(N):
        out[(x + p) % N][x] = ez(q * x + q * p * INV2)
    return out


def classical_rows(limit: int):
    traces = [2, 3]
    for _ in range(2, limit + 1):
        traces.append(3 * traces[-1] - traces[-2])
    fixed = {n: traces[n] - 2 for n in range(1, limit + 1)}

    def mobius(n):
        factors, d, x = 0, 2, n
        while d * d <= x:
            if x % d == 0:
                x //= d; factors += 1
                if x % d == 0: return 0
                while x % d == 0: x //= d
            d += 1
        if x > 1: factors += 1
        return -1 if factors % 2 else 1

    rows = []
    for n in range(1, limit + 1):
        primitive = sum(mobius(d) * fixed[n // d] for d in range(1, n + 1) if n % d == 0) // n
        rows.append({"n": n, "matrix_trace": traces[n], "fixed_points": fixed[n], "primitive_cycles": primitive})
    return rows


def build():
    F = phase_matrix("F")
    U = phase_matrix("U")
    assert mmul(U, madj(U)) == mid(N)
    assert mpow(U, 8) == mid(N)
    egorov = 0
    for q in range(N):
        for p in range(N):
            lhs = mmul(mmul(U, weyl(q, p)), madj(U))
            rhs = weyl((3 * q - p) % N, q)
            assert lhs == rhs
            egorov += 1
    assert mmul(F, mconj(F)) == mid(N)
    assert mmul(mmul(F, mconj(U)), madj(F)) == madj(U)

    gauss = CZ
    for x in range(N):
        gauss = ca(gauss, zeta(x * x))
    iext = (CZ, cs(gauss, Fraction(1, 7)))
    assert em(iext, iext) == es(EO, -1)
    expected = [iext, EO, es(iext, -1), es(EO, -1), iext, EO, es(iext, -1), es(EO, 7)]
    for n, value in enumerate(expected, 1):
        assert mtrace(mpow(U, n)) == value

    qnames = ["i", "1", "-i", "-1", "i", "1", "-i", "7"]
    classical = classical_rows(16)
    for row in classical:
        row["quantum_trace_N7"] = qnames[(row["n"] - 1) % 8] if row["n"] % 8 else "7"

    # Negative convention control: the frozen qp/2 phase uses the inverse of
    # 2.  It therefore has no literal extension to an even residue ring.
    # This does not rule out separately defined doubled-phase even-N Weil
    # conventions.
    assert not any((2 * x) % 8 == 1 for x in range(8))

    data = {
        "schema": "HCS-C128-v1",
        "candidate_id": "HCS-C128",
        "date_utc": "2026-08-24",
        "classical_matrix": [[3, -1], [1, 0]],
        "reversor_matrix": [[0, 1], [1, 0]],
        "quantum_level": 7,
        "phase_conventions": {
            "omega": "exp(2*pi*i/7)", "inverse_of_2_mod_7": 4,
            "fourier": "F_xy=7^(-1/2)*omega^(x*y)",
            "chirp": "C_xx=omega^((3/2)*x^2)", "unitary": "U=C*F^(-1)",
            "weyl": "W(q,p)=omega^(-q*p/2)*Q^q*P^p", "antiunitary": "Theta=F*K",
        },
        "exact_certificate": {
            "field": "Q(zeta_7,sqrt(7))", "unitarity_entries": 49,
            "egorov_cases": egorov, "theta_square_entries": 49,
            "time_reversal_entries": 49, "u_power_8_entries": 49,
            "all_exact_checks_pass": True,
        },
        "quantum_traces_n1_to_n8": qnames,
        "characteristic_polynomial": "t^7-i*t^6-t^5+i*t^4+t^3-i*t^2-t+i",
        "fredholm_determinant": "1-i*z-z^2+i*z^3+z^4-i*z^5-z^6+i*z^7",
        "spectrum": "all eighth roots of unity except -i",
        "action_sum": {
            "phase": "sum_j((3/2)*x_j^2-x_j*x_(j-1)) mod 7",
            "stationary_equation": "3*x_j-x_(j-1)-x_(j+1)=0 mod 7",
        },
        "even_modulus_control": {
            "test_modulus": 8,
            "inverse_of_2_exists": False,
            "same_half_phase_formula_directly_defined": False,
            "scope": "only the frozen qp/2 convention; doubled-phase or other even-N Weil conventions are not excluded",
        },
        "classical_quantum_clock": classical,
        "progress": {
            "natural_quantization_gate": "PASS_EXACT",
            "finite_level_aliasing_obstruction": "PROVED_EXACT",
            "even_modulus_same_convention_obstruction": "PROVED_EXACT",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "scope": "NO_BAD_EULER_OR_ROOT_NUMBER", "uses_prime_table": False,
            "uses_zero_table": False, "claims_euler_factors": False,
            "claims_root_number": False, "claims_automorphy": False,
            "claims_hilbert_polya": False,
        },
    }
    payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    data["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = ap.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n")
    print(args.output)


if __name__ == "__main__": main()
