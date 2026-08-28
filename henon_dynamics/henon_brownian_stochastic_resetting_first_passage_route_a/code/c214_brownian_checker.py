#!/usr/bin/env python3
"""Producer-independent recursive audit for the C214 certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c214_brownian_evidence.json"
SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVAL = {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
HEADLINE = "Brownian resetting has an exact renewal propagator, first-passage transform and universal optimal reset rate"
D_VALUES = [F(1, 2), F(1), F(2)]
R_VALUES = [F(1, 4), F(1), F(4)]
A_VALUES = [F(1, 2), F(1), F(2)]
X_VALUES = [F(-1), F(0), F(1)]
T_VALUES = [F(1, 5), F(1), F(2)]
S_VALUES = [F(0), F(1, 5), F(1), F(3)]
WORKING_DECIMAL_DIGITS = 100


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(value: F) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def parsed(value: str) -> mp.mpf:
    return mp.mpf(value)


def free_kernel(D: F, x: F, t: F) -> mp.mpf:
    dd, xx, tt = mpq(D), mpq(x), mpq(t)
    return mp.exp(-xx * xx / (4 * dd * tt)) / mp.sqrt(4 * mp.pi * dd * tt)


def independent_reset_integral(D: F, r: F, x: F, t: F) -> mp.mpf:
    """Numerical quadrature after u=y^2 removes the heat-kernel singularity."""
    dd, rr, xx, tt = mpq(D), mpq(r), mpq(x), mpq(t)
    scale = 2 / mp.sqrt(4 * mp.pi * dd)
    upper = mp.sqrt(tt)
    return mp.quad(lambda y: scale * mp.exp(-rr * y * y - xx * xx / (4 * dd * y * y)) if y != 0 else (scale if xx == 0 else mp.mpf(0)), [0, upper])


def stationary(D: F, r: F, x: F) -> mp.mpf:
    root = mp.sqrt(mpq(r) / mpq(D))
    return root * mp.exp(-abs(mpq(x)) * root) / 2


def transforms(D: F, r: F, a: F, s: F) -> tuple[mp.mpf, mp.mpf]:
    dd, rr, aa, ss = mpq(D), mpq(r), mpq(a), mpq(s)
    e = mp.exp(-aa * mp.sqrt((ss + rr) / dd))
    den = ss + rr * e
    return (ss + rr) * e / den, (1 - e) / den


def mean_hitting(D: F, r: F, a: F) -> mp.mpf:
    z = mpq(a) * mp.sqrt(mpq(r) / mpq(D))
    return mp.expm1(z) / mpq(r)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(ap.parse_args().evidence.read_text())
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    assertions = 0

    def check(condition, message: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    def keys(obj, expected, where: str) -> None:
        check(isinstance(obj, dict), where + " mapping")
        check(set(obj) == set(expected), where + " keys")

    top_keys = ["schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "summary", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"]
    keys(data, top_keys, "top")
    keys(data["evaluator"], ["path", "version", "sha256"], "evaluator")
    frozen_keys = ["phase_space", "process", "generator", "parameters", "clock", "normalization", "determinant_convention", "arithmetic_origin", "allowed_data", "forbidden_data"]
    keys(data["frozen_object"], frozen_keys, "frozen")
    theorem_keys = ["free_kernel", "renewal_propagator", "reset_integral", "stationary_laplace", "fpt_laplace", "survival_laplace", "mfpt", "optimality", "moments", "boundaries"]
    keys(data["theorem"], theorem_keys, "theorem")
    reg_keys = ["D_values", "r_values", "a_values", "x_values", "t_values", "s_values", "propagator_rows", "stationary_rows", "normalization_rows", "fpt_rows", "mfpt_rows", "boundary_rows", "optimality"]
    keys(data["regression"], reg_keys, "regression")
    keys(data["regression"]["optimality"], ["equation", "z_star", "equation_residual", "scaled_optimal_rate"], "optimality")
    keys(data["summary"], ["propagator_row_count", "stationary_row_count", "normalization_row_count", "fpt_row_count", "mfpt_row_count", "boundary_row_count", "serialized_decimal_digits"], "summary")
    route_keys = ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"]
    keys(data["route_a"], route_keys, "route")
    flag_keys = ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]
    keys(data["scope_flags"], flag_keys, "scope_flags")

    expected_frozen = {
        "phase_space": "free realization on R; killed-search realization on (-infinity,a) with absorbing boundary a and reset point 0",
        "process": "free: dX_t=sqrt(2D)dW_t with rate-r resets to 0; search: same dynamics on (-infinity,a), started at 0 and killed at a",
        "generator": "L f(x)=D f''(x)+r(f(0)-f(x)) on R for the free process, with Dirichlet killing at a for the search realization",
        "parameters": "D>0, r>0, a>0; physical t>=0",
        "clock": "physical elapsed time; no fitted or logarithmic clock",
        "normalization": "for t>0 the free propagator and stationary law are absolutely continuous Lebesgue densities on R; the killed search is sub-Markov on (-infinity,a)",
        "determinant_convention": "none; Laplace denominators are renewal resolvents, never dynamical zeta or Fredholm determinants",
        "arithmetic_origin": "none; this is a scope-locked non-arithmetic stochastic control",
        "allowed_data": "exact rational D,r,a,s,x,t sentinels and source-local heat-kernel/renewal algebra",
        "forbidden_data": "prime/zero tables, target labels, fitted rates, Euler factors and external observations",
    }
    check(data["schema"] == "hcs-c214-brownian-resetting-v1", "schema")
    check(data["candidate_id"] == "HCS-C214", "candidate")
    check(data["evaluation_date"] == "2026-08-28", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator"] == EVAL, "evaluator lock")
    check(data["headline"] == HEADLINE, "headline")
    check(data["frozen_object"] == expected_frozen, "frozen object")
    expected_theorem = {
        "free_kernel": "G_D(x,t)=(4*pi*D*t)^(-1/2) exp(-x^2/(4*D*t))",
        "renewal_propagator": "p_r(x,t|0)=exp(-r*t)G_D(x,t)+r*integral_0^t exp(-r*u)G_D(x,u)du",
        "reset_integral": "I_t(x)=[exp(-|x|sqrt(r/D)) erfc(|x|/(2sqrt(Dt))-sqrt(rt))-exp(|x|sqrt(r/D)) erfc(|x|/(2sqrt(Dt))+sqrt(rt))]/(4sqrt(D*r)), with the continuous x=0 branch",
        "stationary_laplace": "p_st(x)=sqrt(r/D) exp(-|x|sqrt(r/D))/2 and integral_R p_st dx=1",
        "fpt_laplace": "F_r(s)=((s+r) exp(-a sqrt((s+r)/D)))/(s+r exp(-a sqrt((s+r)/D)))",
        "survival_laplace": "S_r(s)=(1-exp(-a sqrt((s+r)/D)))/(s+r exp(-a sqrt((s+r)/D)))",
        "mfpt": "E[T_a]=(exp(a sqrt(r/D))-1)/r",
        "optimality": "For z=a sqrt(r/D), (D/a^2)E[T_a]=(exp(z)-1)/z^2; its unique positive minimizer solves z=2(1-exp(-z)), z*=1.5936242600400400923... and r*=D(z*/a)^2",
        "moments": "All moments are finite for D,r,a>0; for every n>=0, (-1)^n F_r^(n)(0)=E[T_a^n] and (-1)^n S_r^(n)(0)=E[T_a^(n+1)]/(n+1)",
        "boundaries": "r=0 has no stationary law and infinite mean hitting time; a=0 gives T=0; D=0 cannot reach a>0 from the reset point",
    }
    check(data["theorem"] == expected_theorem, "theorem")
    expected_citations = [
        {"key": "EvansMajumdar2011PRL", "claim": "fixed-point stochastic resetting renewal framework and stationary density", "title": "Diffusion with Stochastic Resetting", "authors": "Martin R. Evans and Satya N. Majumdar", "venue": "Physical Review Letters 106, 160601", "date": "2011", "url": "https://doi.org/10.1103/PhysRevLett.106.160601", "persistent_url": "https://doi.org/10.1103/PhysRevLett.106.160601"},
        {"key": "EvansMajumdar2011JPA", "claim": "optimal resetting first-passage calculation", "title": "Diffusion with Optimal Resetting", "authors": "Martin R. Evans and Satya N. Majumdar", "venue": "Journal of Physics A: Mathematical and Theoretical 44, 435001", "date": "2011", "url": "https://doi.org/10.1088/1751-8113/44/43/435001", "persistent_url": "https://doi.org/10.1088/1751-8113/44/43/435001"},
        {"key": "EvansMajumdarSchehr2020", "claim": "review of resetting renewal and first-passage identities", "title": "Stochastic resetting and applications", "authors": "Martin R. Evans, Satya N. Majumdar and Grégory Schehr", "venue": "Journal of Physics A: Mathematical and Theoretical 53, 193001", "date": "2020", "url": "https://doi.org/10.1088/1751-8121/ab7cfe", "persistent_url": "https://doi.org/10.1088/1751-8121/ab7cfe"},
    ]
    for i, citation in enumerate(data["citations"]):
        keys(citation, ["key", "claim", "title", "authors", "venue", "date", "url", "persistent_url"], f"citation[{i}]")
    check(data["citations"] == expected_citations, "citations")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(v is False for v in data["scope_flags"].values()), "scope flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")

    reg = data["regression"]
    check(reg["D_values"] == [str(x) for x in D_VALUES], "D grid")
    check(reg["r_values"] == [str(x) for x in R_VALUES], "r grid")
    check(reg["a_values"] == [str(x) for x in A_VALUES], "a grid")
    check(reg["x_values"] == [str(x) for x in X_VALUES], "x grid")
    check(reg["t_values"] == [str(x) for x in T_VALUES], "t grid")
    check(reg["s_values"] == [str(x) for x in S_VALUES], "s grid")
    tol = mp.mpf("1e-64")
    seen = set()
    pkeys = ["case_id", "D", "r", "x", "t", "free_density", "reset_integral", "reset_density", "stationary_density"]
    for i, row in enumerate(reg["propagator_rows"]):
        keys(row, pkeys, f"propagator[{i}]")
        D, r, x, t = F(row["D"]), F(row["r"]), F(row["x"]), F(row["t"])
        check(D in D_VALUES and r in R_VALUES and x in X_VALUES and t in T_VALUES, f"propagator[{i}] domain")
        ident = (str(D), str(r), str(x), str(t))
        check(ident not in seen, f"duplicate propagator {ident}")
        seen.add(ident)
        check(row["case_id"] == f"D{D}_r{r}_x{x}_t{t}", f"propagator[{i}] id")
        free = free_kernel(D, x, t)
        integ = independent_reset_integral(D, r, x, t)
        dens = mp.exp(-mpq(r) * mpq(t)) * free + mpq(r) * integ
        check(abs(parsed(row["free_density"]) - free) < tol, f"propagator[{i}] free")
        check(abs(parsed(row["reset_integral"]) - integ) < tol, f"propagator[{i}] integral")
        check(abs(parsed(row["reset_density"]) - dens) < tol, f"propagator[{i}] density")
        check(abs(parsed(row["stationary_density"]) - stationary(D, r, x)) < tol, f"propagator[{i}] stationary")
        check(parsed(row["reset_density"]) > 0, f"propagator[{i}] positivity")
    check(len(seen) == 81, "propagator uniqueness/count")

    skeys = ["case_id", "D", "r", "x", "density"]
    seen = set()
    for i, row in enumerate(reg["stationary_rows"]):
        keys(row, skeys, f"stationary[{i}]")
        D, r, x = F(row["D"]), F(row["r"]), F(row["x"])
        check(D in D_VALUES and r in R_VALUES and x in X_VALUES, f"stationary[{i}] domain")
        ident = (str(D), str(r), str(x))
        check(ident not in seen, f"duplicate stationary {ident}")
        seen.add(ident)
        check(row["case_id"] == f"D{D}_r{r}_x{x}", f"stationary[{i}] id")
        check(abs(parsed(row["density"]) - stationary(D, r, x)) < tol, f"stationary[{i}] value")
    check(len(seen) == 27, "stationary count")

    nkeys = ["case_id", "D", "r", "integral"]
    seen = set()
    for i, row in enumerate(reg["normalization_rows"]):
        keys(row, nkeys, f"normalization[{i}]")
        D, r = F(row["D"]), F(row["r"])
        check(D in D_VALUES and r in R_VALUES, f"normalization[{i}] domain")
        ident = (str(D), str(r))
        check(ident not in seen, f"duplicate normalization {ident}")
        seen.add(ident)
        check(row["case_id"] == f"D{D}_r{r}", f"normalization[{i}] id")
        # Independent integration of the Laplace density over R.
        dd, rr = mpq(D), mpq(r)
        norm = mp.quad(lambda y: mp.sqrt(rr / dd) * mp.exp(-mp.sqrt(rr / dd) * abs(y)) / 2, [-mp.inf, 0, mp.inf])
        check(abs(norm - 1) < tol, f"normalization[{i}] integral")
        check(row["integral"] == "1", f"normalization[{i}] serialized")
    check(len(seen) == 9, "normalization count")

    fkeys = ["case_id", "D", "r", "a", "s", "shifted_free_fpt", "fpt_laplace", "survival_laplace"]
    seen = set()
    for i, row in enumerate(reg["fpt_rows"]):
        keys(row, fkeys, f"fpt[{i}]")
        D, r, a, s = F(row["D"]), F(row["r"]), F(row["a"]), F(row["s"])
        check(D in D_VALUES and r in R_VALUES and a in A_VALUES and s in S_VALUES, f"fpt[{i}] domain")
        ident = (str(D), str(r), str(a), str(s))
        check(ident not in seen, f"duplicate fpt {ident}")
        seen.add(ident)
        check(row["case_id"] == f"D{D}_r{r}_a{a}_s{s}", f"fpt[{i}] id")
        f, survival = transforms(D, r, a, s)
        shifted = mp.exp(-mpq(a) * mp.sqrt((mpq(s) + mpq(r)) / mpq(D)))
        check(abs(parsed(row["shifted_free_fpt"]) - shifted) < tol, f"fpt[{i}] shifted")
        check(abs(parsed(row["fpt_laplace"]) - f) < tol, f"fpt[{i}] f")
        check(abs(parsed(row["survival_laplace"]) - survival) < tol, f"fpt[{i}] survival")
        if s == 0:
            check(abs(parsed(row["fpt_laplace"]) - 1) < tol, f"fpt[{i}] mass")
            check(abs(parsed(row["survival_laplace"]) - mean_hitting(D, r, a)) < tol, f"fpt[{i}] mean limit")
        else:
            check(abs(parsed(row["survival_laplace"]) - (1 - parsed(row["fpt_laplace"])) / mpq(s)) < tol, f"fpt[{i}] renewal relation")
    check(len(seen) == 108, "fpt count")

    mkeys = ["case_id", "D", "r", "a", "z", "mfpt", "scaled_mfpt", "optimal_rate"]
    seen = set()
    for i, row in enumerate(reg["mfpt_rows"]):
        keys(row, mkeys, f"mfpt[{i}]")
        D, r, a = F(row["D"]), F(row["r"]), F(row["a"])
        check(D in D_VALUES and r in R_VALUES and a in A_VALUES, f"mfpt[{i}] domain")
        ident = (str(D), str(r), str(a))
        check(ident not in seen, f"duplicate mfpt {ident}")
        seen.add(ident)
        check(row["case_id"] == f"D{D}_r{r}_a{a}", f"mfpt[{i}] id")
        z = mpq(a) * mp.sqrt(mpq(r) / mpq(D))
        value = mean_hitting(D, r, a)
        check(abs(parsed(row["z"]) - z) < tol, f"mfpt[{i}] z")
        check(abs(parsed(row["mfpt"]) - value) < tol, f"mfpt[{i}] value")
        check(abs(parsed(row["scaled_mfpt"]) - value * mpq(D) / (mpq(a) ** 2)) < tol, f"mfpt[{i}] scale")
        zstar = parsed(reg["optimality"]["z_star"])
        check(abs(parsed(row["optimal_rate"]) - mpq(D) * zstar * zstar / (mpq(a) ** 2)) < tol, f"mfpt[{i}] optimum")
    check(len(seen) == 27, "mfpt count")

    bkeys = ["boundary_id", "parameter", "statement"]
    expected_boundaries = {
        "r_zero": ("r=0", "ordinary Brownian motion; no normalizable stationary density; E[T_a]=infinity for a>0"),
        "a_zero": ("a=0", "the start is already absorbed; T=0, F(s)=1 and the positive-target optimum is not applicable"),
        "D_zero": ("D=0", "deterministic reset-at-origin path cannot reach a>0; F(s)=0 and E[T_a]=infinity"),
        "all_zero_target": ("a=r=0", "absorbed at time zero; this is separate from the positive-parameter family"),
    }
    check(len(reg["boundary_rows"]) == 4, "boundary count")
    for i, row in enumerate(reg["boundary_rows"]):
        keys(row, bkeys, f"boundary[{i}]")
        check(row["boundary_id"] in expected_boundaries, f"boundary[{i}] id")
        check((row["parameter"], row["statement"]) == expected_boundaries[row["boundary_id"]], f"boundary[{i}] statement")

    opt = reg["optimality"]
    check(opt["equation"] == "z-2*(1-exp(-z))=0", "opt equation")
    zstar = parsed(opt["z_star"])
    residual = zstar - 2 * (1 - mp.exp(-zstar))
    check(abs(residual) < mp.mpf("1e-70"), "opt residual")
    check(abs(parsed(opt["equation_residual"]) - residual) < tol, "opt residual serialization")
    check(abs(parsed(opt["scaled_optimal_rate"]) - zstar * zstar) < tol, "opt scale")
    check(mp.mpf("1.5") < zstar < mp.mpf("1.7"), "positive root bracket")
    # The derivative of (e^z-1)/z^2 has the sign of h(z)=z-2(1-e^-z)
    # after multiplication by a positive factor; a sign change around z* is
    # a finite audit of the selected (nonzero) root.
    h = lambda z: z - 2 * (1 - mp.exp(-z))
    check(h(mp.mpf("1.0")) < 0 < h(mp.mpf("2.0")), "unique-root bracket")

    check(data["summary"] == {"propagator_row_count": 81, "stationary_row_count": 27, "normalization_row_count": 9, "fpt_row_count": 108, "mfpt_row_count": 27, "boundary_row_count": 4, "serialized_decimal_digits": 82}, "summary")
    expected_nonclaims = [
        "priority or novelty for stochastic resetting, its propagator, or its optimum",
        "a finite rational grid proves the all-parameter theorem",
        "the denominator s+r exp(-a sqrt((s+r)/D)) is a dynamical zeta, Fredholm determinant, or Euler factor",
        "any reset optimum or transform has arithmetic or target-zero meaning",
        "a Hilbert-Polya operator, target divisor, Euler factor, root number, automorphy, external review, or Route-B authorization",
    ]
    check(data["nonclaims"] == expected_nonclaims, "nonclaims")
    print(json.dumps({"status": "C214_CHECKER_PASS", "assertions": assertions, "propagator_rows": len(reg["propagator_rows"]), "stationary_rows": len(reg["stationary_rows"]), "fpt_rows": len(reg["fpt_rows"]), "mfpt_rows": len(reg["mfpt_rows"]), "producer_imported": False}, sort_keys=True))


if __name__ == "__main__":
    main()
