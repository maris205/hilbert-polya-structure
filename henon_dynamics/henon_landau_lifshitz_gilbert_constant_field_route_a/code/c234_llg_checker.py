#!/usr/bin/env python3
"""Producer-independent checker for the C234 LLG certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import re

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "results/c234_llg_evidence.json"
SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
FROZEN_KEYS = {"equation", "phase_space", "parameters", "stereographic_coordinate", "exact_stereographic_flow", "m3_formula", "energy", "clock", "primitive_periodic_orbit", "forbidden_data"}
THEOREM_KEYS = {"stereographic_solution", "sphere_reconstruction", "m3_solution", "energy_dissipation", "stability", "periodic_face", "identity_face", "sampled_fixed_sets", "degenerate_boundaries", "scope"}
REGRESSION_KEYS = {"flow_rows", "stability_rows", "boundary_rows", "sampled_rows", "row_counts", "working_decimal_digits", "serialized_significant_digits"}
FLOW_KEYS = {"alpha", "omega", "time", "m3_initial", "damping_rate_alpha_omega", "m3_exact", "transverse_radius", "z_real", "z_imag", "z_modulus", "phase_unwrapped", "energy_one_minus_m3", "energy_derivative", "norm_residual", "stereographic_residual"}
STAB_KEYS = {"alpha", "omega", "north_real_eigenvalue", "north_imaginary_frequency", "south_real_eigenvalue", "south_imaginary_frequency", "north_class", "south_class"}
BOUNDARY_KEYS = {"face", "condition", "flow", "energy_change", "fixed_set"}
BOUNDARY_EXPECTED = [
    {"face": "omega_zero", "condition": "omega=0", "flow": "identity", "energy_change": "0", "fixed_set": "whole_sphere"},
    {"face": "alpha_zero", "condition": "alpha=0,omega>0", "flow": "rigid_rotation", "energy_change": "0", "fixed_set": "resonant_or_two_poles"},
    {"face": "positive_damping", "condition": "alpha>0,omega>0", "flow": "north_attractor_south_repeller", "energy_change": "nonpositive", "fixed_set": "two_poles_for_tau>0"},
    {"face": "north_pole", "condition": "m=e3", "flow": "equilibrium", "energy_change": "0", "fixed_set": "north_pole"},
    {"face": "south_pole", "condition": "m=-e3", "flow": "equilibrium", "energy_change": "0", "fixed_set": "south_pole"},
]
SAMPLED_KEYS = {"alpha", "omega", "tau_over_2pi_over_omega", "fixed_set_class", "fixed_set_dimension", "latitude_family"}
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


def close(a: str | mp.mpf, b: mp.mpf, tol: mp.mpf = mp.mpf("1e-51")) -> bool:
    return abs(mp.mpf(a) - b) <= tol * max(mp.mpf(1), abs(b))


def keys(obj: dict, expected: set[str], where: str) -> int:
    assert set(obj) == expected, f"{where} keys mismatch: {sorted(set(obj)^expected)}"
    return 1


def classify(alpha: Fraction, omega: Fraction, turns: Fraction) -> tuple[str, int]:
    if omega == 0 or turns == 0:
        return "identity_whole_sphere", 2
    if alpha == 0 and turns.denominator == 1:
        return "resonant_whole_sphere", 2
    if alpha == 0:
        return "nonresonant_two_poles", 0
    return "damped_two_poles", 0


def validate(data: dict) -> int:
    count = 0
    count += keys(data, TOP_KEYS, "top")
    assert data["schema"] == "hcs-c234-llg-constant-field-v1"; count += 1
    assert data["candidate_id"] == "HCS-C234"; count += 1
    assert data["evaluation_date"] == "2026-08-29"; count += 1
    assert data["source_commit"] == SOURCE_COMMIT; count += 1
    assert data["scope_literal"] == SCOPE; count += 1
    assert data["payload_sha256"] == payload_hash(data); count += 1

    ev = data["evaluator"]
    assert set(ev) == {"path", "version", "sha256"}; count += 1
    assert ev["path"] == "flow_systems/skills/route-a-evaluator.md" and ev["version"] == "0.2.0" and ev["sha256"] == EVALUATOR_SHA256; count += 1

    frozen = data["frozen_object"]
    count += keys(frozen, FROZEN_KEYS, "frozen")
    assert frozen["equation"] == "m_dot=-omega m cross e3-alpha omega m cross (m cross e3)"; count += 1
    assert "(1+alpha^2)" in frozen["parameters"] and "absorbs" in frozen["parameters"]; count += 1
    assert frozen["stereographic_coordinate"] == "z=(m1+i m2)/(1+m3)"; count += 1
    assert frozen["exact_stereographic_flow"] == "z_dot=(-alpha omega+i omega)z"; count += 1
    assert frozen["primitive_periodic_orbit"] is False; count += 1
    assert "continuous latitude" in frozen["clock"]; count += 1

    theorem = data["theorem"]
    count += keys(theorem, THEOREM_KEYS, "theorem")
    fragments = {
        "stereographic_solution": "exp((-alpha omega+i omega)t)",
        "sphere_reconstruction": "2z/(1+|z|^2)",
        "m3_solution": "tanh(alpha omega t",
        "energy_dissipation": "-alpha omega(1-m3^2)",
        "stability": "north is asymptotically stable",
        "periodic_face": "period 2pi/omega",
        "identity_face": "identity",
        "sampled_fixed_sets": "whole sphere iff",
        "degenerate_boundaries": "alpha=0",
        "scope": "no arithmetic divisor",
    }
    for name, fragment in fragments.items():
        assert fragment.lower() in theorem[name].lower(), (name, fragment); count += 1

    reg = data["regression"]
    count += keys(reg, REGRESSION_KEYS, "regression")
    assert reg["working_decimal_digits"] == 90 and reg["serialized_significant_digits"] == 64; count += 1
    assert reg["row_counts"] == {"flow": 6, "stability": 4, "boundary": 5, "sampled": 6}; count += 1

    flow_rows = reg["flow_rows"]
    assert len(flow_rows) == 6; count += 1
    for row in flow_rows:
        count += keys(row, FLOW_KEYS, "flow row")
        aa, ww, tt, m0 = map(q, (row["alpha"], row["omega"], row["time"], row["m3_initial"]))
        assert aa >= 0 and ww >= 0 and -1 < m0 < 1 and tt >= 0; count += 1
        a, tm, m0m = mpq(aa) * mpq(ww), mpq(tt), mpq(m0)
        m3 = mp.tanh(a * tm + mp.atanh(m0m))
        z = mp.sqrt((1 - m0m) / (1 + m0m)) * mp.exp((-a + 1j * mpq(ww)) * tm)
        assert close(row["damping_rate_alpha_omega"], a); count += 1
        assert close(row["m3_exact"], m3); count += 1
        assert close(row["transverse_radius"], mp.sqrt(1 - m3*m3)); count += 1
        assert close(row["z_real"], mp.re(z)); count += 1
        assert close(row["z_imag"], mp.im(z)); count += 1
        assert close(row["z_modulus"], abs(z)); count += 1
        assert close(row["phase_unwrapped"], mpq(ww)*tm); count += 1
        assert close(row["energy_one_minus_m3"], 1-m3); count += 1
        assert close(row["energy_derivative"], -a*(1-m3*m3)); count += 1
        assert close(row["norm_residual"], 0); count += 1
        assert close(row["stereographic_residual"], 0); count += 1

    stability = reg["stability_rows"]
    assert len(stability) == 4; count += 1
    for row in stability:
        count += keys(row, STAB_KEYS, "stability row")
        aa, ww = q(row["alpha"]), q(row["omega"]); a, w = mpq(aa)*mpq(ww), mpq(ww)
        assert close(row["north_real_eigenvalue"], -a); count += 1
        assert close(row["south_real_eigenvalue"], a); count += 1
        assert close(row["north_imaginary_frequency"], w) and close(row["south_imaginary_frequency"], w); count += 1
        assert row["north_class"] == ("asymptotically_stable" if a > 0 else "center_neutral"); count += 1
        assert row["south_class"] == ("unstable" if a > 0 else "center_neutral"); count += 1

    # Boundary rows are a semantic atlas, not just a key/face inventory.
    # Lock every source-defined condition and its resulting flow, energy and
    # fixed-set classification so repaired-hash mutations cannot hide in an
    # unchecked row.
    boundary = reg["boundary_rows"]
    assert len(boundary) == len(BOUNDARY_EXPECTED); count += 1
    for idx, (row, expected) in enumerate(zip(boundary, BOUNDARY_EXPECTED)):
        count += keys(row, BOUNDARY_KEYS, f"boundary row {idx}")
        assert row == expected, f"boundary row {idx} semantic mismatch"
        count += 1

    sampled = reg["sampled_rows"]
    assert len(sampled) == 6; count += 1
    for row in sampled:
        count += keys(row, SAMPLED_KEYS, "sampled row")
        aa, ww, turns = q(row["alpha"]), q(row["omega"]), q(row["tau_over_2pi_over_omega"])
        expected, dim = classify(aa, ww, turns)
        assert row["fixed_set_class"] == expected and row["fixed_set_dimension"] == dim; count += 1
        assert row["latitude_family"] is (aa == 0 and ww > 0); count += 1

    ids = data["exact_identities"]
    assert len(ids) == 9 and all(set(item) == {"name", "formula"} for item in ids); count += 1
    assert {item["name"] for item in ids} == {"stereographic_linearization", "m3_logistic", "sphere_reconstruction", "norm_constraint", "energy_law", "north_linear_mode", "south_linear_mode", "latitude_period", "sample_resonance"}; count += 1

    route = data["route_a"]
    count += keys(route, ROUTE_KEYS, "route")
    assert route["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]; count += 1
    assert route["overall"] == "ROUTE_A_REJECTED" and route["route_b_invocation_allowed"] is False; count += 1
    assert "nonisolated" in route["strongest_failure"]; count += 1

    flags = data["scope_flags"]
    count += keys(flags, SCOPE_KEYS, "scope flags")
    assert all(value is False for value in flags.values()); count += 1

    citations = data["citations"]
    assert len(citations) == 1; count += 1
    item = citations[0]
    expected = {"id": "Lakshmanan2011", "title": "The fascinating world of the Landau--Lifshitz--Gilbert equation: an overview", "authors": "M. Lakshmanan", "venue": "Philosophical Transactions of the Royal Society A 369(1939), 1280--1300", "year": 2011, "doi": "10.1098/rsta.2010.0319"}
    assert set(item) == set(expected) | {"role"}; count += 1
    for key, value in expected.items():
        assert item[key] == value, (key, item[key]); count += 1
    assert len(data["nonclaims"]) == 5; count += 1
    text = json.dumps(data, ensure_ascii=False).lower()
    for phrase in ("target primes", "euler factors", "root numbers", "hilbert-polya", "route-b"):
        assert phrase in text; count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()
    n = validate(json.loads(args.input.read_text()))
    print(f"C234 independent checker: PASS ({n} assertions)")


if __name__ == "__main__":
    main()
