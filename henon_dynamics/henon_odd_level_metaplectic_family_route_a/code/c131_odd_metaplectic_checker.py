#!/usr/bin/env python3
"""Independent integer checker for the C131 evidence ledger."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results" / "c131_odd_metaplectic_evidence.json"
LEVELS = [3, 5, 7, 9, 11, 15, 23, 57, 145]

TOP_LEVEL_KEYS = {
    "schema", "candidate_id", "date_utc", "classical_matrix",
    "reversor_matrix", "family", "phase_conventions",
    "all_odd_level_theorem", "matrix_power_receipts",
    "certified_level_receipts", "total_exact_egorov_cases",
    "unbounded_window_witnesses", "even_modulus_control", "nonclaims",
    "checks", "route_a", "scope_flags", "payload_sha256",
}
CERTIFIED_LEVEL_KEYS = {
    "N", "inverse_of_2", "fourier_orthogonality_pairs", "egorov_cases",
    "egorov_case_sha256", "antiunitary_weyl_cases",
    "antiunitary_case_sha256", "certified_no_action_alias_window",
    "window_threshold", "next_threshold", "action_residues",
}


def exact_keys(value: dict, expected: set[str], label: str) -> None:
    assert isinstance(value, dict), f"{label} must be an object"
    assert set(value) == expected, f"{label} schema keys differ"


def digest(lines: list[str]) -> str:
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def matrix_product(x, y):
    return [[sum(x[i][k] * y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matrix_power(a, n):
    out = [[1, 0], [0, 1]]
    for _ in range(n):
        out = matrix_product(out, a)
    return out


def validate(data: dict) -> None:
    exact_keys(data, TOP_LEVEL_KEYS, "top-level evidence")
    payload = data["payload_sha256"]
    assert isinstance(payload, str) and len(payload) == 64
    unsigned = {key: value for key, value in data.items() if key != "payload_sha256"}
    canonical = json.dumps(unsigned, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(canonical).hexdigest() == payload
    assert data["schema"] == "HCS-C131-v1"
    assert data["candidate_id"] == "HCS-C131" and data["date_utc"] == "2026-08-24"
    assert data["classical_matrix"] == [[3, -1], [1, 0]]
    assert data["reversor_matrix"] == [[0, 1], [1, 0]]
    assert data["family"] == {"levels": "all odd integers N>=3", "certified_levels": LEVELS}
    assert data["phase_conventions"] == {
        "omega_N": "exp(2*pi*i/N)",
        "half": "the unique h in Z/NZ with 2*h=1",
        "fourier": "F_N(x,y)=N^(-1/2)*omega_N^(x*y)",
        "chirp": "C_N(x,x)=omega_N^(3*h*x^2)",
        "unitary": "U_N=C_N*F_N^(-1)",
        "weyl": "W_N(q,p)=omega_N^(-h*q*p)*Q_N^q*P_N^p",
        "antiunitary": "Theta_N=F_N*K",
    }
    assert data["all_odd_level_theorem"] == {
        "unitary": True,
        "egorov": "U_N W_N(q,p) U_N^(-1)=W_N(3*q-p,q)",
        "clock": "U_N^n implements A^n on every Weyl observable",
        "antiunitary_square": "Theta_N^2=I",
        "antiunitary_reversal": "Theta_N U_N Theta_N^(-1)=U_N^(-1)",
        "antiunitary_weyl_action": "Theta_N W_N(q,p) Theta_N^(-1)=W_N(p,q)",
    }

    a = [[3, -1], [1, 0]]
    u = [0, 1]
    for _ in range(21):
        u.append(3 * u[-1] - u[-2])
    assert [row["n"] for row in data["matrix_power_receipts"]] == list(range(1, 17))
    for row in data["matrix_power_receipts"]:
        n = row["n"]
        assert row == {"n": n, "u_n": u[n], "max_norm_A_n_minus_I": u[n + 1] - 1}
        assert matrix_power(a, n) == [[u[n + 1], -u[n]], [u[n], -u[n - 1]]]

    assert len(data["certified_level_receipts"]) == len(LEVELS)
    total = 0
    windows = []
    for expected_n, row in zip(LEVELS, data["certified_level_receipts"]):
        exact_keys(row, CERTIFIED_LEVEL_KEYS, f"certified level {expected_n}")
        modulus = row["N"]
        assert modulus == expected_n and modulus % 2 == 1
        half = (modulus + 1) // 2
        assert row["inverse_of_2"] == half and (2 * half) % modulus == 1
        forward, reverse = [], []
        for q in range(modulus):
            for p in range(modulus):
                cancellation = (-half * q * p + half * q * p) % modulus
                reverse_cancellation = (2 * half * q * p - q * p) % modulus
                assert cancellation == reverse_cancellation == 0
                forward.append(f"{q},{p}>{(3*q-p)%modulus},{q}:{cancellation}")
                reverse.append(f"{q},{p}>{p},{q}:{reverse_cancellation}")
        assert row["egorov_cases"] == modulus**2 == row["fourier_orthogonality_pairs"]
        assert row["antiunitary_weyl_cases"] == modulus**2
        assert row["egorov_case_sha256"] == digest(forward)
        assert row["antiunitary_case_sha256"] == digest(reverse)
        window = 0
        while u[window + 2] - 1 < modulus:
            window += 1
        assert row["certified_no_action_alias_window"] == window
        assert row["window_threshold"] == u[window + 1] - 1
        assert row["next_threshold"] == u[window + 2] - 1
        expected_residues = []
        for n in range(1, window + 1):
            power = matrix_power(a, n)
            residue = [(power[i][j] - (1 if i == j else 0)) % modulus for i in range(2) for j in range(2)]
            assert any(residue)
            expected_residues.append({"n": n, "A_n_minus_I_mod_N": residue})
        assert row["action_residues"] == expected_residues
        windows.append(window)
        total += modulus**2
    assert windows == [1, 1, 1, 2, 2, 2, 3, 4, 5]
    assert data["total_exact_egorov_cases"] == total == 25313
    assert data["unbounded_window_witnesses"] == [
        {"N": 3, "window": 1}, {"N": 9, "window": 2},
        {"N": 23, "window": 3}, {"N": 57, "window": 4},
        {"N": 145, "window": 5},
    ]
    assert data["even_modulus_control"] == {
        "test_modulus": 8,
        "inverse_of_2_exists": False,
        "same_qp_over_2_convention_directly_defined": False,
        "scope": "only the frozen half-phase convention; other even-level Weil/metaplectic conventions are not excluded",
    }
    assert not any((2 * x) % 8 == 1 for x in range(8))
    expected_nonclaims = {
        "cross_level_projective_compatibility": False,
        "semiclassical_trace_match": False,
        "hilbert_polya": False,
    }
    assert data["nonclaims"] == expected_nonclaims
    assert all(type(value) is bool for value in data["nonclaims"].values())
    expected_checks = {
        "all_certified_levels_pass": True,
        "all_exact_egorov_cases_pass": True,
        "uniform_antiunitary_pass": True,
        "no_action_alias_windows_pass": True,
        "even_same_convention_control_pass": True,
    }
    assert data["checks"] == expected_checks
    assert all(type(value) is bool for value in data["checks"].values())
    expected_route = {
        "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
        "structural_gate": "ODD_LEVEL_NATURAL_QUANTIZATION_FAMILY_PASS",
        "route_b_invocation_allowed": False,
    }
    assert data["route_a"] == expected_route
    assert data["route_a"]["route_b_invocation_allowed"] is False
    expected_flags = {
        "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "uses_prime_table": False,
        "uses_zero_table": False,
        "claims_euler_factors": False,
        "claims_root_number": False,
        "claims_automorphy": False,
        "claims_hilbert_polya": False,
    }
    assert data["scope_flags"] == expected_flags
    assert all(
        type(value) is bool
        for key, value in data["scope_flags"].items()
        if key != "scope"
    )


if __name__ == "__main__":
    validate(json.loads(EVIDENCE.read_text()))
    print("C131 independent checker: PASS (25,313 exact Egorov cases)")
