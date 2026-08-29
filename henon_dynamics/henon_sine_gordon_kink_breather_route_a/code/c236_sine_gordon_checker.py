#!/usr/bin/env python3
"""Independent checker for the C236 sine--Gordon coherent-family receipt."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "results/c236_sine_gordon_evidence.json"
SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
FROZEN_KEYS = {"equation", "phase_space", "potential", "kink_ansatz", "kink_formula", "breather_formula", "boost_coordinates", "hessian", "clock", "primitive_periodic_orbit", "forbidden_data"}
THEOREM_KEYS = {"coherent_scope", "kink_classification", "kink_energy_momentum", "topological_charge", "breather_rest", "breather_boost", "energy_identity", "hessian_factorization", "hessian_spectrum", "limits", "scope"}
REG_KEYS = {"kink_rows", "breather_rows", "hessian_rows", "boundary_rows", "lorentz_rows", "row_counts", "working_decimal_digits", "serialized_significant_digits"}
KINK_KEYS = {"velocity", "orientation", "gamma", "inverse_width", "center_profile", "center_derivative", "energy", "momentum", "topological_charge", "mass_shell_residual", "traveling_ode_residual", "energy_density_integral_residual"}
BREATHER_KEYS = {"internal_frequency_Omega", "boost_velocity_V", "eta_sqrt_1_minus_Omega2", "rest_period", "rest_energy", "rest_momentum", "boost_gamma", "lab_energy", "lab_momentum", "center_quarter_amplitude", "mass_shell_residual", "topological_charge", "pde_residual", "lab_fixed_x_period_claimed"}
HESSIAN_KEYS = {"x", "kink_profile", "kink_derivative", "hessian_potential", "kernel_mode", "kernel_residual", "essential_edge", "factorization_quadratic_form_nonnegative"}
BOUNDARY_KEYS = {"face", "condition", "profile", "energy_limit", "period_statement"}
LORENTZ_KEYS = {"boost_velocity", "gamma", "rest_energy", "lab_energy", "lab_momentum", "lorentz_mass_shell_residual"}
EXPECTED_BOUNDARY_ROWS = [
    {"face": "rest_kink", "condition": "v=0", "profile": "static kink", "energy_limit": "8", "period_statement": "not periodic"},
    {"face": "subluminal_kink", "condition": "|v|<1", "profile": "Lorentz kink/antikink", "energy_limit": "8 gamma", "period_statement": "traveling heteroclinic"},
    {"face": "light_speed", "condition": "|v|->1", "profile": "width collapse", "energy_limit": "diverges", "period_statement": "excluded"},
    {"face": "breather_small_amplitude", "condition": "Omega->1", "profile": "vacuum limit", "energy_limit": "0", "period_statement": "2pi"},
    {"face": "breather_separatrix", "condition": "Omega->0", "profile": "long-period limit", "energy_limit": "16", "period_statement": "diverges"},
    {"face": "breather_rest", "condition": "V=0", "profile": "rest breather", "energy_limit": "16 eta", "period_statement": "2pi/Omega"},
    {"face": "breather_boost", "condition": "V!=0", "profile": "boosted breather", "energy_limit": "16 eta gamma_V", "period_statement": "comoving only"},
    {"face": "vacuum", "condition": "u=2pi k", "profile": "constant vacuum", "energy_limit": "0", "period_statement": "identity"},
]
ROUTE_KEYS = {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def q(s: str) -> Fraction:
    return Fraction(s)


def mpq(x: Fraction) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def close(a: str | mp.mpf, b: mp.mpf, tol: mp.mpf = mp.mpf("1e-50")) -> bool:
    return abs(mp.mpf(a) - b) <= tol * max(mp.mpf(1), abs(b))


def keys(obj: dict, expected: set[str], where: str) -> int:
    assert set(obj) == expected, f"{where} keys mismatch: {sorted(set(obj)^expected)}"
    return 1


def validate(data: dict) -> int:
    count = 0
    count += keys(data, TOP_KEYS, "top")
    assert data["schema"] == "hcs-c236-sine-gordon-kink-breather-v1"; count += 1
    assert data["candidate_id"] == "HCS-C236"; count += 1
    assert data["evaluation_date"] == "2026-08-29"; count += 1
    assert data["source_commit"] == SOURCE_COMMIT; count += 1
    assert data["scope_literal"] == SCOPE; count += 1
    assert data["payload_sha256"] == payload_hash(data); count += 1

    ev = data["evaluator"]
    assert set(ev) == {"path", "version", "sha256"}; count += 1
    assert ev["path"] == "flow_systems/skills/route-a-evaluator.md" and ev["version"] == "0.2.0" and ev["sha256"] == EVALUATOR_SHA256; count += 1

    frozen = data["frozen_object"]
    count += keys(frozen, FROZEN_KEYS, "frozen")
    assert frozen["equation"] == "u_tt-u_xx+sin(u)=0"; count += 1
    assert "2pi k" in frozen["kink_formula"] and "canonical k=0" in frozen["kink_formula"]; count += 1
    assert "rest/comoving internal period" in frozen["clock"]; count += 1
    assert "fixed-x period" in frozen["clock"]; count += 1
    assert frozen["primitive_periodic_orbit"] is False; count += 1

    theorem = data["theorem"]
    count += keys(theorem, THEOREM_KEYS, "theorem")
    fragments = {
        "coherent_scope": "not a classification of every finite-energy",
        "kink_classification": "2pi k+4 atan",
        "kink_energy_momentum": "E=8 gamma_v",
        "topological_charge": "Q=+1 and -1",
        "breather_rest": "rest energy 16 eta",
        "breather_boost": "comoving period",
        "energy_identity": "P=-integral u_t u_x",
        "hessian_factorization": "A^*A",
        "hessian_spectrum": "[1,infinity)",
        "limits": "Omega->1",
        "scope": "No all-finite-energy classification",
    }
    for name, fragment in fragments.items():
        assert fragment.lower() in theorem[name].lower(), (name, fragment); count += 1

    reg = data["regression"]
    count += keys(reg, REG_KEYS, "regression")
    assert reg["working_decimal_digits"] == 90 and reg["serialized_significant_digits"] == 64; count += 1
    assert reg["row_counts"] == {"kink": 6, "breather": 6, "hessian": 5, "boundary": 8, "lorentz": 4}; count += 1

    kink_rows = reg["kink_rows"]
    assert len(kink_rows) == 6; count += 1
    for row in kink_rows:
        count += keys(row, KINK_KEYS, "kink row")
        v, orientation = q(row["velocity"]), int(row["orientation"])
        assert -1 < v < 1 and orientation in (-1, 1); count += 1
        vm, g = mpq(v), 1/mp.sqrt(1-mpq(v)**2)
        assert close(row["gamma"], g); count += 1
        assert close(row["inverse_width"], g); count += 1
        assert close(row["center_profile"], mp.pi); count += 1
        assert close(row["center_derivative"], orientation*2*g); count += 1
        E, P = 8*g, 8*g*vm
        assert close(row["energy"], E); count += 1
        assert close(row["momentum"], P); count += 1
        assert row["topological_charge"] == orientation; count += 1
        assert close(row["mass_shell_residual"], 0); count += 1
        assert close(row["traveling_ode_residual"], 0); count += 1
        assert close(row["energy_density_integral_residual"], 0); count += 1

    breather_rows = reg["breather_rows"]
    assert len(breather_rows) == 6; count += 1
    for row in breather_rows:
        count += keys(row, BREATHER_KEYS, "breather row")
        Om, V = q(row["internal_frequency_Omega"]), q(row["boost_velocity_V"])
        assert 0 < Om < 1 and -1 < V < 1; count += 1
        Om_m, Vm = mpq(Om), mpq(V)
        eta = mp.sqrt(1-Om_m**2); gv = 1/mp.sqrt(1-Vm**2)
        rest = 16*eta; E, P = rest*gv, rest*gv*Vm
        assert close(row["eta_sqrt_1_minus_Omega2"], eta); count += 1
        assert close(row["rest_period"], 2*mp.pi/Om_m); count += 1
        assert close(row["rest_energy"], rest); count += 1
        assert close(row["rest_momentum"], 0); count += 1
        assert close(row["boost_gamma"], gv); count += 1
        assert close(row["lab_energy"], E); count += 1
        assert close(row["lab_momentum"], P); count += 1
        assert close(row["center_quarter_amplitude"], 4*mp.atan(eta/Om_m)); count += 1
        assert close(row["mass_shell_residual"], 0); count += 1
        assert row["topological_charge"] == 0; count += 1
        assert close(row["pde_residual"], 0); count += 1
        assert row["lab_fixed_x_period_claimed"] is (V == 0); count += 1

    hrows = reg["hessian_rows"]
    assert len(hrows) == 5; count += 1
    for row in hrows:
        count += keys(row, HESSIAN_KEYS, "hessian row")
        xq = q(row["x"]); x = mpq(xq); sech = 1/mp.cosh(x)
        assert close(row["kink_profile"], 4*mp.atan(mp.exp(x))); count += 1
        assert close(row["kink_derivative"], 2*sech); count += 1
        assert close(row["hessian_potential"], 1-2*sech**2); count += 1
        assert close(row["kernel_mode"], 2*sech); count += 1
        assert close(row["kernel_residual"], 0); count += 1
        assert close(row["essential_edge"], 1); count += 1
        assert row["factorization_quadratic_form_nonnegative"] is True; count += 1

    brows = reg["boundary_rows"]
    assert len(brows) == len(EXPECTED_BOUNDARY_ROWS); count += 1
    for idx, (row, expected) in enumerate(zip(brows, EXPECTED_BOUNDARY_ROWS)):
        count += keys(row, BOUNDARY_KEYS, f"boundary row {idx}")
        assert row == expected, f"boundary row {idx} semantic drift"; count += 1

    lrows = reg["lorentz_rows"]
    assert len(lrows) == 4; count += 1
    for row in lrows:
        count += keys(row, LORENTZ_KEYS, "Lorentz row")
        V = q(row["boost_velocity"]); vm = mpq(V); rest = mp.mpf(row["rest_energy"]); gv = 1/mp.sqrt(1-vm**2)
        E, P = rest*gv, rest*gv*vm
        assert close(row["gamma"], gv); count += 1
        assert close(row["lab_energy"], E); count += 1
        assert close(row["lab_momentum"], P); count += 1
        assert close(row["lorentz_mass_shell_residual"], 0); count += 1

    ids = data["exact_identities"]
    assert len(ids) == 13 and all(set(item) == {"name", "formula"} for item in ids); count += 1
    assert {item["name"] for item in ids} == {"sine_gordon_pde", "kink_profile", "antikink_profile", "kink_speed_domain", "kink_energy", "kink_momentum", "topological_charge", "breather_profile", "breather_dispersion", "breather_energy", "lorentz_energy_momentum", "hessian_factorization", "hessian_spectrum"}; count += 1

    route = data["route_a"]
    count += keys(route, ROUTE_KEYS, "route")
    assert route["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]; count += 1
    assert route["overall"] == "ROUTE_A_REJECTED" and route["route_b_invocation_allowed"] is False; count += 1
    assert "continuous family" in route["strongest_failure"]; count += 1

    flags = data["scope_flags"]
    count += keys(flags, SCOPE_KEYS, "scope flags")
    assert all(value is False for value in flags.values()); count += 1

    citations = data["citations"]
    assert len(citations) == 1; count += 1
    item = citations[0]
    expected = {"id": "McLaughlinScott1978", "title": "Perturbation analysis of fluxon dynamics", "authors": "J. M. McLaughlin and A. C. Scott", "venue": "Physical Review A 18(4), 1652--1680", "year": 1978, "doi": "10.1103/PhysRevA.18.1652"}
    assert set(item) == set(expected) | {"role"}; count += 1
    for key, value in expected.items():
        assert item[key] == value, (key, item[key]); count += 1
    assert len(data["nonclaims"]) == 5; count += 1
    all_text = json.dumps(data, ensure_ascii=False).lower()
    for phrase in ("target primes", "euler factors", "root numbers", "hilbert-polya", "route-b"):
        assert phrase in all_text; count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()
    n = validate(json.loads(args.input.read_text()))
    print(f"C236 independent checker: PASS ({n} assertions)")


if __name__ == "__main__":
    main()
