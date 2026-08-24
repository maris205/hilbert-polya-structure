#!/usr/bin/env python3
"""Independent numerical and integer checker for C128."""
import cmath
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results" / "c128_metaplectic_evidence.json"


def mobius(n):
    primes, x, d = 0, n, 2
    while d * d <= x:
        if x % d == 0:
            x //= d; primes += 1
            if x % d == 0: return 0
            while x % d == 0: x //= d
        d += 1
    if x > 1: primes += 1
    return -1 if primes % 2 else 1


def validate(data):
    digest = data.pop("payload_sha256")
    payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(payload).hexdigest() == digest
    data["payload_sha256"] = digest
    assert data["schema"] == "HCS-C128-v1" and data["quantum_level"] == 7
    assert data["candidate_id"] == "HCS-C128" and data["date_utc"] == "2026-08-24"
    assert data["classical_matrix"] == [[3, -1], [1, 0]]
    assert data["reversor_matrix"] == [[0, 1], [1, 0]]
    assert data["phase_conventions"] == {
        "omega": "exp(2*pi*i/7)",
        "inverse_of_2_mod_7": 4,
        "fourier": "F_xy=7^(-1/2)*omega^(x*y)",
        "chirp": "C_xx=omega^((3/2)*x^2)",
        "unitary": "U=C*F^(-1)",
        "weyl": "W(q,p)=omega^(-q*p/2)*Q^q*P^p",
        "antiunitary": "Theta=F*K",
    }

    n = 7; inv2 = 4; w = cmath.exp(2j * cmath.pi / n)
    xs = np.arange(n)
    fourier = w ** np.outer(xs, xs) / np.sqrt(n)
    chirp = np.diag([w ** ((3 * inv2 * x * x) % n) for x in xs])
    U = chirp @ fourier.conj().T
    Q = np.diag([w**x for x in xs])
    P = np.zeros((n, n), complex)
    for x in xs: P[(x + 1) % n, x] = 1

    def W(q, p):
        return w ** ((-q * p * inv2) % n) * np.linalg.matrix_power(Q, int(q)) @ np.linalg.matrix_power(P, int(p))

    assert np.max(np.abs(U @ U.conj().T - np.eye(n))) < 1e-12
    A = np.array([[3, -1], [1, 0]], int)
    for q in xs:
        for p in xs:
            q2, p2 = A @ np.array([q, p])
            assert np.max(np.abs(U @ W(q, p) @ U.conj().T - W(q2 % n, p2 % n))) < 1e-12
    assert np.max(np.abs(np.linalg.matrix_power(U, 8) - np.eye(n))) < 1e-12
    assert np.max(np.abs(fourier @ fourier.conj() - np.eye(n))) < 1e-12
    assert np.max(np.abs(fourier @ U.conj() @ fourier.conj().T - U.conj().T)) < 1e-12
    expected = [1j, 1, -1j, -1, 1j, 1, -1j, 7]
    for k, value in enumerate(expected, 1):
        assert abs(np.trace(np.linalg.matrix_power(U, k)) - value) < 1e-11
    expected_char = np.array([1, -1j, -1, 1j, 1, -1j, -1, 1j], complex)
    assert np.max(np.abs(np.poly(U) - expected_char)) < 1e-10

    t0, t1 = 2, 3
    traces = [t0, t1]
    for _ in range(2, 17): traces.append(3 * traces[-1] - traces[-2])
    for row in data["classical_quantum_clock"]:
        k = row["n"]; fixed = traces[k] - 2
        primitive = sum(mobius(d) * (traces[k // d] - 2) for d in range(1, k + 1) if k % d == 0) // k
        assert row["matrix_trace"] == traces[k]
        assert row["fixed_points"] == fixed and row["primitive_cycles"] == primitive
        expected_qtrace = ["i", "1", "-i", "-1", "i", "1", "-i", "7"][(k - 1) % 8]
        assert row["quantum_trace_N7"] == expected_qtrace
    assert data["quantum_traces_n1_to_n8"] == ["i", "1", "-i", "-1", "i", "1", "-i", "7"]
    assert data["exact_certificate"] == {
        "field": "Q(zeta_7,sqrt(7))",
        "unitarity_entries": 49,
        "egorov_cases": 49,
        "theta_square_entries": 49,
        "time_reversal_entries": 49,
        "u_power_8_entries": 49,
        "all_exact_checks_pass": True,
    }
    assert data["characteristic_polynomial"] == "t^7-i*t^6-t^5+i*t^4+t^3-i*t^2-t+i"
    assert data["fredholm_determinant"] == "1-i*z-z^2+i*z^3+z^4-i*z^5-z^6+i*z^7"
    assert data["spectrum"] == "all eighth roots of unity except -i"
    assert data["action_sum"] == {
        "phase": "sum_j((3/2)*x_j^2-x_j*x_(j-1)) mod 7",
        "stationary_equation": "3*x_j-x_(j-1)-x_(j+1)=0 mod 7",
    }
    assert data["even_modulus_control"] == {
        "test_modulus": 8,
        "inverse_of_2_exists": False,
        "same_half_phase_formula_directly_defined": False,
        "scope": "only the frozen qp/2 convention; doubled-phase or other even-N Weil conventions are not excluded",
    }
    assert not any((2 * x) % data["even_modulus_control"]["test_modulus"] == 1 for x in range(data["even_modulus_control"]["test_modulus"]))
    assert data["progress"] == {
        "finite_level_aliasing_obstruction": "PROVED_EXACT",
        "natural_quantization_gate": "PASS_EXACT",
        "even_modulus_same_convention_obstruction": "PROVED_EXACT",
    }
    assert data["route_a"]["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    assert data["route_a"]["route_b_invocation_allowed"] is False
    flags = data["scope_flags"]
    assert flags["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert not any(v for k, v in flags.items() if k != "scope")


if __name__ == "__main__":
    validate(json.loads(EVIDENCE.read_text()))
    print("C128 independent checker: PASS")
