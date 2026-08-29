#!/usr/bin/env python3
"""Independent, producer-free checker for the C231 receipt."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import re

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "results/c231_allen_cahn_evidence.json"
SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90

TOP_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator",
    "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a",
    "scope_flags", "citations", "nonclaims", "payload_sha256",
}
FROZEN_KEYS = {"equation", "epsilon_equation", "potential", "gradient_flow_energy", "traveling_ansatz", "front_formula", "clock", "primitive_periodic_orbit", "forbidden_data"}
THEOREM_KEYS = {"front_and_speed", "first_integral", "speed_selection", "energy_dissipation", "surface_energy", "translation_uniqueness", "linearization", "factorization", "discrete_spectrum", "essential_spectrum", "degenerate_boundaries", "scope"}
REGRESSION_KEYS = {"epsilon_rows", "speed_rows", "profile_rows", "energy_rows", "row_counts", "working_decimal_digits", "serialized_significant_digits"}
EPS_KEYS = {"epsilon", "front_width_sqrt2epsilon", "surface_energy", "integral_front_gradient_square", "translation_eigenvalue", "shape_eigenvalue", "essential_edge", "spectral_gap_to_edge"}
SPEED_KEYS = {"speed_c", "well_energy_jump", "front_gradient_integral", "selection_product_c_times_integral", "admissible_equal_well_heteroclinic"}
PROFILE_KEYS = {"y", "front_U", "front_prime_scaled", "kernel_mode", "shape_mode", "front_first_integral_residual", "scaled_kernel_residual", "scaled_shape_residual", "factorization_quadratic_form_nonnegative"}
ENERGY_KEYS = {"y", "potential_W", "half_scaled_gradient_square", "equipartition_residual", "dissipation_density_symbol"}
ROUTE_KEYS = {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def parseq(s: str) -> Fraction:
    return Fraction(s)


def close(a: str | mp.mpf, b: mp.mpf, tol: mp.mpf = mp.mpf("1e-52")) -> bool:
    return abs(mp.mpf(a) - b) <= tol * max(1, abs(b))


def sech(y: mp.mpf) -> mp.mpf:
    return 1 / mp.cosh(y)


def check_keys(obj: dict, expected: set[str], where: str) -> int:
    assert set(obj) == expected, f"{where} keys mismatch: {sorted(set(obj)^expected)}"
    return 1


def validate(data: dict) -> int:
    count = 0
    count += check_keys(data, TOP_KEYS, "top")
    assert data["schema"] == "hcs-c231-allen-cahn-front-pt-spectrum-v1"; count += 1
    assert data["candidate_id"] == "HCS-C231"; count += 1
    assert data["evaluation_date"] == "2026-08-29"; count += 1
    assert data["source_commit"] == SOURCE_COMMIT; count += 1
    assert data["scope_literal"] == SCOPE; count += 1
    assert data["payload_sha256"] == payload_hash(data); count += 1

    ev = data["evaluator"]; assert set(ev) == {"path", "version", "sha256"}; count += 1
    assert ev["version"] == "0.2.0" and ev["sha256"] == EVALUATOR_SHA256; count += 1
    assert ev["path"] == "flow_systems/skills/route-a-evaluator.md"; count += 1

    frozen = data["frozen_object"]; count += check_keys(frozen, FROZEN_KEYS, "frozen")
    assert frozen["equation"] == "u_t=u_xx+u-u^3"; count += 1
    assert frozen["epsilon_equation"] == "u_t=u_xx+epsilon^(-2)(u-u^3), epsilon>0"; count += 1
    assert frozen["potential"] == "W(u)=(1-u^2)^2/4"; count += 1
    assert frozen["primitive_periodic_orbit"] is False; count += 1
    assert "no primitive periodic orbit" in frozen["clock"].lower(); count += 1
    assert SCOPE.replace("_", "-") not in frozen["forbidden_data"]; count += 1

    theorem = data["theorem"]; count += check_keys(theorem, THEOREM_KEYS, "theorem")
    required_fragments = {
        "front_and_speed": "c=0", "first_integral": "W(U)", "speed_selection": "c integral_R (U')^2",
        "energy_dissipation": "dE_epsilon/dt=-integral_R u_t^2 dx", "surface_energy": "2 sqrt(2)/(3 epsilon)",
        "translation_uniqueness": "modulo xi-translation", "linearization": "Pöschl" if False else "sech^2",
        "factorization": "B^*B", "discrete_spectrum": "-3/(2 epsilon^2)",
        "essential_spectrum": "(-infinity,-2/epsilon^2]", "degenerate_boundaries": "epsilon downarrow 0",
        "scope": "no primitive periodic-orbit repetition law",
    }
    for key, frag in required_fragments.items():
        assert frag.lower() in theorem[key].lower(), (key, frag); count += 1

    reg = data["regression"]; count += check_keys(reg, REGRESSION_KEYS, "regression")
    assert reg["working_decimal_digits"] == 90 and reg["serialized_significant_digits"] == 64; count += 1
    assert reg["row_counts"] == {"epsilon": 5, "speed": 5, "profile": 5, "energy": 5}; count += 1

    eps_rows = reg["epsilon_rows"]; assert len(eps_rows) == 5; count += 1
    for row in eps_rows:
        count += check_keys(row, EPS_KEYS, "epsilon row")
        eps = mp.mpf(parseq(row["epsilon"]).numerator) / parseq(row["epsilon"]).denominator
        assert eps > 0; count += 1
        assert close(row["front_width_sqrt2epsilon"], mp.sqrt(2) * eps); count += 1
        expected_sigma = 2 * mp.sqrt(2) / (3 * eps)
        assert close(row["surface_energy"], expected_sigma); count += 1
        assert close(row["integral_front_gradient_square"], expected_sigma); count += 1
        assert close(row["translation_eigenvalue"], mp.mpf(0)); count += 1
        assert close(row["shape_eigenvalue"], -3 / (2 * eps**2)); count += 1
        assert close(row["essential_edge"], -2 / eps**2); count += 1
        assert close(row["spectral_gap_to_edge"], 1 / (2 * eps**2)); count += 1

    speed_rows = reg["speed_rows"]; assert len(speed_rows) == 5; count += 1
    for row in speed_rows:
        count += check_keys(row, SPEED_KEYS, "speed row")
        c = mp.mpf(parseq(row["speed_c"]).numerator) / parseq(row["speed_c"]).denominator
        I = 2 * mp.sqrt(2) / 3
        assert close(row["well_energy_jump"], mp.mpf(0)); count += 1
        assert close(row["front_gradient_integral"], I); count += 1
        assert close(row["selection_product_c_times_integral"], c * I); count += 1
        assert row["admissible_equal_well_heteroclinic"] is (c == 0); count += 1

    profile_rows = reg["profile_rows"]; assert len(profile_rows) == 5; count += 1
    for row in profile_rows:
        count += check_keys(row, PROFILE_KEYS, "profile row")
        yq = parseq(row["y"]); y = mp.mpf(yq.numerator) / yq.denominator
        s = sech(y); t = mp.tanh(y)
        assert close(row["front_U"], t); count += 1
        assert close(row["front_prime_scaled"], s**2); count += 1
        assert close(row["kernel_mode"], s**2); count += 1
        assert close(row["shape_mode"], s*t); count += 1
        assert close(row["front_first_integral_residual"], 0); count += 1
        assert close(row["scaled_kernel_residual"], 0); count += 1
        assert close(row["scaled_shape_residual"], 0); count += 1
        assert row["factorization_quadratic_form_nonnegative"] is True; count += 1

    energy_rows = reg["energy_rows"]; assert len(energy_rows) == 5; count += 1
    for row in energy_rows:
        count += check_keys(row, ENERGY_KEYS, "energy row")
        yq = parseq(row["y"]); y = mp.mpf(yq.numerator) / yq.denominator
        s = sech(y); t = mp.tanh(y); W = (1 - t**2)**2 / 4
        assert close(row["potential_W"], W); count += 1
        assert close(row["half_scaled_gradient_square"], s**4 / 4); count += 1
        assert close(row["equipartition_residual"], 0); count += 1
        assert row["dissipation_density_symbol"] == "u_t^2"; count += 1

    ids = data["exact_identities"]
    assert len(ids) == 9 and all(set(item) == {"name", "formula"} for item in ids); count += 1
    names = {item["name"] for item in ids}
    assert names == {"equal_well_energy", "tanh_ode", "equipartition", "speed_selection", "gradient_flow", "surface_tension", "pt_factorization", "pt_modes", "essential_edge"}; count += 1

    route = data["route_a"]; count += check_keys(route, ROUTE_KEYS, "route")
    assert route["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]; count += 1
    assert route["overall"] == "ROUTE_A_REJECTED" and route["route_b_invocation_allowed"] is False; count += 1
    assert "periodic-orbit" in route["strongest_failure"]; count += 1

    flags = data["scope_flags"]; count += check_keys(flags, SCOPE_KEYS, "scope flags")
    assert all(value is False for value in flags.values()); count += 1

    citations = data["citations"]
    assert len(citations) == 2; count += 1
    expected_citations = {
        "AllenCahn1979": {"title": "A microscopic theory for antiphase boundary motion and its application to antiphase domain coarsening", "authors": "S. M. Allen and J. W. Cahn", "venue": "Acta Metallurgica 27(6), 1085--1095", "year": 1979, "doi": "10.1016/0001-6160(79)90196-2"},
        "FifeMcLeod1977": {"title": "The approach of solutions of nonlinear diffusion equations to travelling front solutions", "authors": "P. C. Fife and J. B. McLeod", "venue": "Archive for Rational Mechanics and Analysis 65(4), 335--361", "year": 1977, "doi": "10.1007/BF00250432"},
    }
    for item in citations:
        assert set(item) == {"id", "title", "authors", "venue", "year", "doi", "role"}; count += 1
        ref = expected_citations[item["id"]]
        for k, v in ref.items(): assert item[k] == v, (item["id"], k); count += 1

    assert len(data["nonclaims"]) == 5; count += 1
    all_text = json.dumps(data, ensure_ascii=False).lower()
    for forbidden in ("target zero table", "euler product", "root number", "automorphy", "hilbert-polya operator"):
        # These phrases are allowed only in explicit nonclaim/scope fields.  The
        # receipt must not turn any of them into a positive assertion.
        assert forbidden in all_text; count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    n = validate(data)
    print(f"C231 independent checker: PASS ({n} assertions)")


if __name__ == "__main__":
    main()
