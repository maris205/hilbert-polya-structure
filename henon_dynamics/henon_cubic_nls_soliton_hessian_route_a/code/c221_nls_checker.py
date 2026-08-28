#!/usr/bin/env python3
"""Independent recursive/value checker for the C221 NLS receipt."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c221_nls_evidence.json"
SOURCE_COMMIT = "86c7bb8a39cdd1b8e941e45833b068170ca06287"
EVAL = {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
OMEGA_VALUES = [F(1, 4), F(1), F(4)]
X_VALUES = [F(-2), F(-1), F(0), F(1), F(2)]
Y_VALUES = [F(-2), F(-1), F(0), F(1), F(2)]
WORKING_DECIMAL_DIGITS = 100


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def q(value: F) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def parse(value: str) -> mp.mpf:
    return mp.mpf(value)


def arg(value):
    return q(value) if isinstance(value, F) else mp.mpf(value)


def sech(x):
    return 1 / mp.cosh(x)


def Q(w: F, x) -> mp.mpf:
    ww, xx = q(w), arg(x)
    return mp.sqrt(ww) * sech(mp.sqrt(ww) * xx)


def Qp(w: F, x) -> mp.mpf:
    ww, xx = q(w), arg(x)
    y = mp.sqrt(ww) * xx
    return -ww * sech(y) * mp.tanh(y)


def qres(w: F, x) -> mp.mpf:
    ww, xx = q(w), arg(x)
    y = mp.sqrt(ww) * xx
    s = sech(y)
    return -(ww ** mp.mpf("1.5") * (s - 2 * s ** 3)) + ww * (mp.sqrt(ww) * s) - 2 * (mp.sqrt(ww) * s) ** 3


def phi2(w: F, x) -> mp.mpf:
    return sech(mp.sqrt(q(w)) * arg(x)) ** 2


def second(fun, x):
    return mp.diff(fun, x, 2)


def Lp(w: F, fun, x) -> mp.mpf:
    ww, xx = q(w), arg(x)
    return -second(lambda z: fun(w, z), xx) + (ww - 6 * ww * sech(mp.sqrt(ww) * xx) ** 2) * fun(w, xx)


def Lm(w: F, fun, x) -> mp.mpf:
    ww, xx = q(w), arg(x)
    return -second(lambda z: fun(w, z), xx) + (ww - 2 * ww * sech(mp.sqrt(ww) * xx) ** 2) * fun(w, xx)


def check_keys(obj, expected, where, check):
    check(isinstance(obj, dict), where + " mapping")
    check(set(obj) == set(expected), where + " keys")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(ap.parse_args().evidence.read_text())
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    assertions = 0

    def check(condition, message):
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    top = ["schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "summary", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"]
    check_keys(data, top, "top", check)
    check_keys(data["evaluator"], ["path", "version", "sha256"], "evaluator", check)
    frozen_keys = ["phase_space", "equation", "standing_wave", "parameters", "clock", "normalization", "determinant_convention", "arithmetic_origin", "allowed_data", "forbidden_data"]
    check_keys(data["frozen_object"], frozen_keys, "frozen", check)
    theorem_keys = ["profile_equation", "integrals", "vk", "hessian", "spectrum", "morse", "factorization", "boundaries"]
    check_keys(data["theorem"], theorem_keys, "theorem", check)
    reg_keys = ["omega_values", "x_values", "y_values", "profile_rows", "integral_rows", "spectrum_rows", "factorization_rows", "boundary_rows"]
    check_keys(data["regression"], reg_keys, "regression", check)
    summary_keys = ["profile_row_count", "integral_row_count", "spectrum_row_count", "factorization_row_count", "boundary_row_count", "serialized_decimal_digits"]
    check_keys(data["summary"], summary_keys, "summary", check)
    check_keys(data["route_a"], ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"], "route", check)
    flags = ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]
    check_keys(data["scope_flags"], flags, "scope_flags", check)

    check(data["schema"] == "hcs-c221-focusing-cubic-nls-hessian-v1", "schema")
    check(data["candidate_id"] == "HCS-C221", "candidate")
    check(data["evaluation_date"] == "2026-08-28", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator"] == EVAL, "evaluator")
    expected_frozen = {
        "phase_space": "H^1(R;C) with the one-dimensional focusing cubic NLS flow; the spectral owner is the real Hessian at the standing wave",
        "equation": "i psi_t + psi_xx + 2|psi|^2 psi = 0",
        "standing_wave": "psi(t,x)=exp(i*omega*t) Q_omega(x), Q_omega(x)=sqrt(omega) sech(sqrt(omega)*x)",
        "parameters": "omega>0; physical t and x; no fitted scale",
        "clock": "physical NLS time t; no logarithmic or target-fitted clock",
        "normalization": "M(u)=integral_R |u|^2 dx; H(u)=1/2 integral |u_x|^2 dx - 1/2 integral |u|^4 dx; S_omega=H+(omega/2)M",
        "determinant_convention": "none; continuous-spectrum Hessians are not called dynamical zeta or Fredholm determinants",
        "arithmetic_origin": "none; this is a scope-locked non-arithmetic Hamiltonian PDE certificate",
        "allowed_data": "exact rational omega,x,y sentinels and source-local sech/Pöschl–Teller algebra",
        "forbidden_data": "prime/zero tables, target labels, fitted frequencies, Euler factors, root numbers, and external spectral fits",
    }
    expected_theorem = {
        "profile_equation": "-Q_omega''+omega Q_omega-2 Q_omega^3=0, Q_omega=sqrt(omega) sech(sqrt(omega)x)",
        "integrals": "M(Q)=2 sqrt(omega), ||Q'||_2^2=(2/3)omega^(3/2), ||Q||_4^4=(4/3)omega^(3/2), H(Q)=-(1/3)omega^(3/2), S_omega(Q)=(2/3)omega^(3/2)",
        "vk": "dM(Q_omega)/domega=omega^(-1/2)>0",
        "hessian": "L_+=-d_x^2+omega-6omega sech^2(sqrt(omega)x), L_-=-d_x^2+omega-2omega sech^2(sqrt(omega)x)",
        "spectrum": "sigma_ess(L_+)=sigma_ess(L_-)=[omega,infinity); L_+ has simple eigenvalues -3omega (sech^2) and 0 (Q_prime), L_- has simple eigenvalue 0 (Q), with no other discrete eigenvalues",
        "morse": "L_+ has Morse index one and ker L_+=span{Q_prime}; L_- is nonnegative with ker L_-=span{Q}",
        "factorization": "in y=sqrt(omega)x, A_l=d_y+l tanh(y), A_l*=−d_y+l tanh(y): P_2=A_2* A_2−3 and P_1=A_1* A_1",
        "boundaries": "omega↓0 collapses the branch and threshold; defocusing sign has no bright H1 sech soliton; finite periodic and d≥2 branches are outside scope",
    }
    check(data["frozen_object"] == expected_frozen, "frozen values")
    check(data["theorem"] == expected_theorem, "theorem values")
    check(data["headline"] == "The one-dimensional focusing cubic NLS soliton has an exact Hessian spectrum, Morse index, VK slope, and Pöschl–Teller factorization", "headline")
    check(data["regression"]["omega_values"] == [str(v) for v in OMEGA_VALUES], "omega grid")
    check(data["regression"]["x_values"] == [str(v) for v in X_VALUES], "x grid")
    check(data["regression"]["y_values"] == [str(v) for v in Y_VALUES], "y grid")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(v is False for v in data["scope_flags"].values()), "scope flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")

    tol = mp.mpf("1e-70")
    reg = data["regression"]
    pkeys = ["case_id", "omega", "x", "Q", "Q_prime", "standing_wave_residual"]
    seen = set()
    for i, row in enumerate(reg["profile_rows"]):
        check_keys(row, pkeys, f"profile[{i}]", check)
        w, x = F(row["omega"]), F(row["x"])
        check(w in OMEGA_VALUES and x in X_VALUES, f"profile[{i}] domain")
        ident = (str(w), str(x))
        check(ident not in seen, f"profile[{i}] duplicate")
        seen.add(ident)
        check(row["case_id"] == f"w{w}_x{x}", f"profile[{i}] id")
        check(abs(parse(row["Q"]) - Q(w, x)) < tol, f"profile[{i}] Q")
        check(abs(parse(row["Q_prime"]) - Qp(w, x)) < tol, f"profile[{i}] Qp")
        check(abs(parse(row["standing_wave_residual"]) - qres(w, x)) < tol, f"profile[{i}] residual")
    check(len(seen) == 15, "profile count")

    ikeys = ["case_id", "omega", "mass", "grad_norm_sq", "quartic_norm_4", "hamiltonian", "action", "vk_slope"]
    seen = set()
    for i, row in enumerate(reg["integral_rows"]):
        check_keys(row, ikeys, f"integral[{i}]", check)
        w = F(row["omega"]); ww = q(w)
        check(w in OMEGA_VALUES, f"integral[{i}] domain")
        check(row["case_id"] == f"w{w}", f"integral[{i}] id")
        check(str(w) not in seen, f"integral[{i}] duplicate"); seen.add(str(w))
        vals = {
            "mass": 2 * mp.sqrt(ww),
            "grad_norm_sq": mp.mpf(2) / 3 * ww ** mp.mpf("1.5"),
            "quartic_norm_4": mp.mpf(4) / 3 * ww ** mp.mpf("1.5"),
        }
        vals["hamiltonian"] = (vals["grad_norm_sq"] - vals["quartic_norm_4"]) / 2
        vals["action"] = vals["hamiltonian"] + ww * vals["mass"] / 2
        vals["vk_slope"] = 1 / mp.sqrt(ww)
        for key, value in vals.items():
            check(abs(parse(row[key]) - value) < tol, f"integral[{i}] {key}")
    check(len(seen) == 3, "integral count")

    skeys = ["case_id", "omega", "x", "Lplus_phi2_residual", "Lplus_Qprime_residual", "Lminus_Q_residual", "essential_threshold", "Lplus_phi2_eigenvalue", "Lplus_Qprime_eigenvalue", "Lminus_Q_eigenvalue"]
    seen = set()
    for i, row in enumerate(reg["spectrum_rows"]):
        check_keys(row, skeys, f"spectrum[{i}]", check)
        w, x = F(row["omega"]), F(row["x"]); ident = (str(w), str(x))
        check(w in OMEGA_VALUES and x in X_VALUES, f"spectrum[{i}] domain")
        check(ident not in seen, f"spectrum[{i}] duplicate"); seen.add(ident)
        check(row["case_id"] == f"w{w}_x{x}", f"spectrum[{i}] id")
        check(abs(parse(row["Lplus_phi2_residual"]) - (Lp(w, phi2, x) + 3*q(w)*phi2(w, x))) < tol, f"spectrum[{i}] phi2")
        check(abs(parse(row["Lplus_Qprime_residual"]) - Lp(w, Qp, x)) < tol, f"spectrum[{i}] Qp")
        check(abs(parse(row["Lminus_Q_residual"]) - Lm(w, Q, x)) < tol, f"spectrum[{i}] Q")
        check(parse(row["essential_threshold"]) == q(w), f"spectrum[{i}] threshold")
        check(parse(row["Lplus_phi2_eigenvalue"]) == -3*q(w), f"spectrum[{i}] eigenvalue")
        check(row["Lplus_Qprime_eigenvalue"] == "0" and row["Lminus_Q_eigenvalue"] == "0", f"spectrum[{i}] zero labels")
    check(len(seen) == 15, "spectrum count")

    fkeys = ["case_id", "omega", "y", "P2_minus_A2starA2_plus3", "P1_minus_A1starA1"]
    seen = set()
    for i, row in enumerate(reg["factorization_rows"]):
        check_keys(row, fkeys, f"factorization[{i}]", check)
        w, y = F(row["omega"]), F(row["y"]); ident = (str(w), str(y))
        check(w in OMEGA_VALUES and y in Y_VALUES, f"factorization[{i}] domain")
        check(ident not in seen, f"factorization[{i}] duplicate"); seen.add(ident)
        check(row["case_id"] == f"w{w}_y{y}", f"factorization[{i}] id")
        yy = q(y) if isinstance(y, F) else mp.mpf(y)
        s2 = 1 / mp.cosh(yy) ** 2
        r2 = (1 - 6*s2) - ((4 - 6*s2) - 3)
        r1 = (1 - 2*s2) - (1 - 2*s2)
        check(abs(parse(row["P2_minus_A2starA2_plus3"]) - r2) < tol, f"factorization[{i}] P2")
        check(abs(parse(row["P1_minus_A1starA1"]) - r1) < tol, f"factorization[{i}] P1")
    check(len(seen) == 15, "factorization count")

    bkeys = ["boundary_id", "parameter", "statement"]
    expected_b = {"omega_zero", "defocusing", "periodic_domain", "higher_dimension"}
    check(len(reg["boundary_rows"]) == 4, "boundary count")
    for i, row in enumerate(reg["boundary_rows"]):
        check_keys(row, bkeys, f"boundary[{i}]", check)
        check(row["boundary_id"] in expected_b, f"boundary[{i}] id")

    check(data["summary"]["profile_row_count"] == 15, "summary profile")
    check(data["summary"]["integral_row_count"] == 3, "summary integral")
    check(data["summary"]["spectrum_row_count"] == 15, "summary spectrum")
    check(data["summary"]["factorization_row_count"] == 15, "summary factorization")
    check(data["summary"]["boundary_row_count"] == 4, "summary boundaries")
    check(data["summary"]["serialized_decimal_digits"] == 82, "summary digits")
    check(len(data["citations"]) == 3, "citations")
    for i, citation in enumerate(data["citations"]):
        check_keys(citation, ["key", "claim", "title", "authors", "venue", "date", "url", "persistent_url"], f"citation[{i}]", check)
        check(citation["url"] == citation["persistent_url"], f"citation[{i}] url")
    check("Weinstein" in data["citations"][1]["authors"], "Weinstein source")
    pt = data["citations"][2]
    check(pt["key"] == "PoschlTeller1933", "Pöschl–Teller key")
    check(pt["claim"] == "original solvable Pöschl–Teller potential and ladder source; historical attribution only", "Pöschl–Teller claim boundary")
    check(pt["title"] == "Bemerkungen zur Quantenmechanik des anharmonischen Oszillators", "Pöschl–Teller title")
    check(pt["authors"] == "G. Pöschl and E. Teller", "Pöschl–Teller authors")
    check(pt["venue"] == "Zeitschrift für Physik 83, 143–151", "Pöschl–Teller venue")
    check(pt["date"] == "1933", "Pöschl–Teller date")
    check(pt["url"] == "https://doi.org/10.1007/BF01331132", "Pöschl–Teller DOI")
    print(json.dumps({"status": "C221_CHECKER_PASS", "assertions": assertions, "profile_rows": 15, "spectrum_rows": 15, "factorization_rows": 15}, sort_keys=True))


if __name__ == "__main__":
    main()
