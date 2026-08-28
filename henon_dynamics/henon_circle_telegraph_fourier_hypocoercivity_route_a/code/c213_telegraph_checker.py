#!/usr/bin/env python3
"""Producer-independent recursive checker for the C213 telegraph certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c213_telegraph_evidence.json"
SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVAL = {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
HEADLINE = "The circular telegraph process has exact Fourier blocks, a sharp spectral-gap atlas and a noncompactness boundary"
C_VALUES = [F(0), F(1, 2), F(1), F(2), F(3)]
LAMBDA_VALUES = [F(0), F(1, 2), F(1), F(2), F(3)]
K_VALUES = list(range(-3, 4))
TIMES = [F(0), F(1, 3), F(1), F(2)]
WORKING_DECIMAL_DIGITS = 100
SERIALIZED_SIGNIFICANT_DIGITS = 82


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(x: F) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def significant_digits(value: str) -> int:
    mantissa = str(value).lower().split("e", 1)[0].lstrip("+-").replace(".", "")
    sig = mantissa.lstrip("0")
    return len(sig) if sig else 1


def pair_value(pair: list[str]) -> mp.mpc:
    return mp.mpc(mp.mpf(pair[0]), mp.mpf(pair[1]))


def expected_mode(c: F, lam: F) -> str:
    if c == 0 and lam == 0:
        return "static_all_modes"
    if c == 0:
        return "velocity_mixing_no_spatial_decay"
    if lam == 0:
        return "ballistic_unitary"
    if lam <= c:
        return "oscillatory_or_critical_gap_lambda"
    return "hypocoercive_diffusive_gap"


def expected_gap(c: F, lam: F) -> str:
    if c == 0 or lam == 0:
        return "0"
    if lam <= c:
        return str(lam)
    return f"{lam}-sqrt({lam * lam - c * c})"


def expected_stationary(c: F, lam: F) -> str:
    if c == 0:
        return "infinite"
    if lam == 0:
        return "2"
    return "1"


def expected_block(c: F, lam: F, k: int, t: F):
    """Independent 2x2 exponential calculation at high precision."""
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    ck = c * k
    d2 = lam * lam - ck * ck
    delta = mp.sqrt(mpq(d2))
    tt = mpq(t)
    if d2 == 0:
        h, q = mp.mpf(1), tt
    else:
        h, q = mp.cosh(delta * tt), mp.sinh(delta * tt) / delta
    e = mp.exp(-mpq(lam) * tt)
    ik = mp.j * mpq(ck)
    n = [[ik, mpq(lam)], [mpq(lam), -ik]]
    matrix = [[e * (h + q * n[0][0]), e * q * n[0][1]],
              [e * q * n[1][0], e * (h + q * n[1][1])]]
    roots = [-mpq(lam) + delta, -mpq(lam) - delta]
    return d2, roots, matrix


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(ap.parse_args().evidence.read_text())
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    assertions = 0

    def check(cond, msg):
        nonlocal assertions
        assertions += 1
        if not cond:
            raise AssertionError(msg)

    def keys(obj, expected, where):
        check(isinstance(obj, dict), where + " mapping")
        check(set(obj) == set(expected), where + " keys")

    keys(data, ["schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "summary", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"], "top")
    keys(data["evaluator"], ["path", "version", "sha256"], "evaluator")
    keys(data["frozen_object"], ["phase_space", "process", "generator", "parameters", "clock", "normalization", "determinant_convention", "arithmetic_origin", "allowed_data", "forbidden_data"], "frozen")
    keys(data["theorem"], ["fourier_block", "nilpotent_square", "matrix_exponential", "eigenvalues", "telegraph_equation", "spectral_gap", "critical_blocks", "stationary_boundary", "essential_boundary", "ballistic_boundary"], "theorem")
    keys(data["regression"], ["c_values", "lambda_values", "k_values", "time_values", "block_rows", "gap_rows"], "regression")
    keys(data["summary"], ["block_row_count", "gap_row_count", "matrix_entry_count", "parameter_pair_count"], "summary")
    keys(data["route_a"], ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"], "route")
    flag_keys = ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]
    keys(data["scope_flags"], flag_keys, "scope_flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c213-circle-telegraph-v1", "schema")
    check(data["candidate_id"] == "HCS-C213", "candidate")
    check(data["evaluation_date"] == "2026-08-28", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator"] == EVAL, "evaluator lock")
    check(data["headline"] == HEADLINE, "headline")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    expected_route = {
        "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "strongest_positive": "The source Markov semigroup has an exact all-mode Fourier matrix exponential, sharp gap regimes, Jordan boundaries and an essential-spectrum obstruction.",
        "strongest_failure": "There is no intrinsic rational-prime carrier, isolated primitive-orbit owner, target divisor or nontrivial same-clock self-adjoint lift.",
    }
    check(data["route_a"] == expected_route, "route lock")
    check(all(v is False for v in data["scope_flags"].values()), "scope flags")
    check(data["frozen_object"]["arithmetic_origin"] == "none; this is a scope-locked non-arithmetic control", "arithmetic boundary")
    check(data["frozen_object"]["determinant_convention"].startswith("finite 2x2 Fourier characteristic"), "determinant boundary")
    expected_frozen = {
        "phase_space": "L2(T_{2pi} x {+1,-1}, dx/(2pi) times uniform velocity law)",
        "process": "dx/dt=c*v modulo 2pi; velocity flips sign at Poisson rate lambda",
        "generator": "L f(x,v)=c*v*partial_x f(x,v)+lambda*(f(x,-v)-f(x,v))",
        "parameters": "c>=0, lambda>=0, physical t>=0",
        "clock": "physical elapsed time; no fitted or logarithmic clock",
        "normalization": "uniform invariant measure on the circle and two velocities",
        "determinant_convention": "finite 2x2 Fourier characteristic polynomial only; no Fredholm or target determinant",
        "arithmetic_origin": "none; this is a scope-locked non-arithmetic control",
        "allowed_data": "exact rational c,lambda,k,t sentinels and source-local Fourier algebra",
        "forbidden_data": "prime/zero tables, target labels, fitted phases and external observations",
    }
    check(data["frozen_object"] == expected_frozen, "frozen object lock")
    expected_theorem = {
        "fourier_block": "G_k=[[-lambda+i*c*k,lambda],[lambda,-lambda-i*c*k]]",
        "nilpotent_square": "(G_k+lambda I)^2=(lambda^2-c^2*k^2)I",
        "matrix_exponential": "exp(tG_k)=exp(-lambda*t)[cosh(delta_k*t)I+sinh(delta_k*t)(G_k+lambda I)/delta_k], delta_k^2=lambda^2-c^2*k^2; delta=0 uses I+tN",
        "eigenvalues": "rho_{k,+/-}=-lambda +/- sqrt(lambda^2-c^2*k^2)",
        "telegraph_equation": "rho_tt+2*lambda*rho_t=c^2*rho_xx for rho=f_++f_-",
        "spectral_gap": "sharp spectral-abscissa gap (not a constant-free L2 operator-norm decay): for c>0,lambda>0 gap=lambda when lambda<=c and gap=lambda-sqrt(lambda^2-c^2) when lambda>c; gap=0 when c=0 or lambda=0",
        "critical_blocks": "lambda=c*|k|>0 gives a single Jordan block at -lambda; k=0 has eigenvalues 0 and -2lambda",
        "stationary_boundary": "c>0,lambda>0 has only constants; c=0,lambda>0 has an infinite spatial stationary subspace; lambda=0 has two velocity constants",
        "essential_boundary": "for c>0,lambda>0 the essential norm of P_t on the complement of constants is the |k|->infinity block limit exp(-lambda*t), still nonzero; for c=0 or lambda=0 it is 1",
        "ballistic_boundary": "lambda=0 is the same-clock unitary pair of translations; c=0 is velocity-only mixing with no spatial decay",
    }
    check(data["theorem"] == expected_theorem, "theorem lock")
    check("sharp spectral-abscissa gap" in data["theorem"]["spectral_gap"], "gap wording")
    check("not a constant-free L2 operator-norm decay" in data["theorem"]["spectral_gap"], "operator norm boundary")
    check("|k|" in data["theorem"]["essential_boundary"], "essential high-frequency boundary")
    expected_citation = {"key": "Kac1974", "claim": "telegraph-process origin and velocity-switching framework", "title": "A stochastic model related to the telegrapher's equation", "authors": "Mark Kac", "report_number": "Rocky Mountain Journal of Mathematics 4(3), 497--509", "date": "1974", "url": "https://doi.org/10.1216/RMJ-1974-4-3-497", "persistent_url": "https://doi.org/10.1216/RMJ-1974-4-3-497"}
    check(data["citations"] == [expected_citation], "citation lock")

    reg = data["regression"]
    check(reg["c_values"] == [str(x) for x in C_VALUES], "c grid")
    check(reg["lambda_values"] == [str(x) for x in LAMBDA_VALUES], "lambda grid")
    check(reg["k_values"] == K_VALUES, "k grid")
    check(reg["time_values"] == [str(x) for x in TIMES], "time grid")
    rows = reg["block_rows"]
    check(len(rows) == 700, "block count")
    row_keys = ["case_id", "c", "lambda", "k", "t", "delta_square", "generator_trace", "generator_determinant", "mode", "eigenvalues", "exponential_matrix"]
    seen = set()
    tol = mp.mpf("3e-75")
    matrix_entries = 0
    for idx, row in enumerate(rows):
        keys(row, row_keys, f"block[{idx}]")
        c, lam, k, t = F(row["c"]), F(row["lambda"]), int(row["k"]), F(row["t"])
        check(c in C_VALUES and lam in LAMBDA_VALUES and k in K_VALUES and t in TIMES, f"block[{idx}] domain")
        ident = (str(c), str(lam), k, str(t))
        check(ident not in seen, f"duplicate block {ident}")
        seen.add(ident)
        check(row["case_id"] == f"c{c}_lambda{lam}_k{k}_t{t}", f"block[{idx}] id")
        d2, roots, matrix = expected_block(c, lam, k, t)
        check(F(row["delta_square"]) == d2, f"block[{idx}] delta")
        check(F(row["generator_trace"]) == -2 * lam, f"block[{idx}] trace")
        check(F(row["generator_determinant"]) == c * c * k * k, f"block[{idx}] determinant")
        check(row["mode"] == expected_mode(c, lam), f"block[{idx}] mode")
        check(isinstance(row["eigenvalues"], list) and len(row["eigenvalues"]) == 2, f"block[{idx}] roots shape")
        for j in range(2):
            pair = row["eigenvalues"][j]
            check(isinstance(pair, list) and len(pair) == 2, f"block[{idx}] root pair")
            z = pair_value(pair)
            check(abs(z - roots[j]) < tol, f"block[{idx}] root value")
            for component in pair:
                if mp.mpf(component) != 0:
                    check(significant_digits(component) == SERIALIZED_SIGNIFICANT_DIGITS, f"block[{idx}] root precision")
        mat = row["exponential_matrix"]
        check(isinstance(mat, list) and len(mat) == 2 and all(isinstance(x, list) and len(x) == 2 for x in mat), f"block[{idx}] matrix shape")
        for i in range(2):
            for j in range(2):
                pair = mat[i][j]
                check(isinstance(pair, list) and len(pair) == 2, f"block[{idx}] matrix pair")
                z = pair_value(pair)
                check(abs(z - matrix[i][j]) < tol, f"block[{idx}] matrix value")
                for component in pair:
                    if mp.mpf(component) != 0:
                        check(significant_digits(component) == SERIALIZED_SIGNIFICANT_DIGITS, f"block[{idx}] matrix precision")
                matrix_entries += 1
    check(len(seen) == len(rows), "block uniqueness")

    gaps = reg["gap_rows"]
    check(len(gaps) == 25, "gap count")
    gap_keys = ["case_id", "c", "lambda", "gap_expression", "stationary_dimension", "essential_norm_expression", "mode"]
    seen_gaps = set()
    for idx, row in enumerate(gaps):
        keys(row, gap_keys, f"gap[{idx}]")
        c, lam = F(row["c"]), F(row["lambda"])
        ident = (str(c), str(lam))
        check(ident not in seen_gaps, f"duplicate gap {ident}")
        seen_gaps.add(ident)
        check(row["case_id"] == f"c{c}_lambda{lam}", f"gap[{idx}] id")
        check(row["gap_expression"] == expected_gap(c, lam), f"gap[{idx}] expression")
        check(row["stationary_dimension"] == expected_stationary(c, lam), f"gap[{idx}] stationary")
        check(row["essential_norm_expression"] == ("1" if c == 0 else "exp(-lambda*t)"), f"gap[{idx}] essential")
        check(row["mode"] == expected_mode(c, lam), f"gap[{idx}] mode")
    check(len(seen_gaps) == len(gaps), "gap uniqueness")
    check(data["summary"] == {"block_row_count": 700, "gap_row_count": 25, "matrix_entry_count": 2800, "parameter_pair_count": 25}, "summary")
    expected_nonclaims = ["priority for the telegraph process or its Fourier solution", "a finite block ledger proves the infinite semigroup theorem", "Fourier characteristic polynomials are Fredholm determinants or dynamical zeta functions", "any spectral value is an arithmetic or target zero", "a Hilbert-Polya operator, target divisor, Euler factor, root number, automorphy, external review or Route-B authorization"]
    check(data["nonclaims"] == expected_nonclaims, "nonclaims lock")
    print(json.dumps({"status": "C213_CHECKER_PASS", "assertions": assertions, "block_rows": len(rows), "gap_rows": len(gaps), "matrix_entries": matrix_entries, "recursive_key_sets": 10 + len(rows) + len(gaps), "producer_imported": False}, sort_keys=True))


if __name__ == "__main__":
    main()
