#!/usr/bin/env python3
"""Producer-independent checker for the HCS-C229 CIR certificate."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import math
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c229_cir_evidence.json"
SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
HEADLINE = "The Cox--Ingersoll--Ross square-root diffusion has a closed all-parameter Feller boundary atlas, an exact affine Laplace transform, and—on the nondegenerate face—a Gamma reversible law with an explicit Laguerre semigroup and sharp spectral gap."
FROZEN = {"sde": "dX_t=kappa(theta-X_t)dt+sigma sqrt(X_t)dW_t, X_0=x>=0", "generator": "L f=kappa(theta-x)f' +(sigma^2/2)x f''", "parameter_domain": "kappa,theta,sigma>=0; x>=0", "clock": "physical diffusion time t>=0", "feller_index": "alpha=2 kappa theta/sigma^2 when sigma>0; compare 2 kappa theta with sigma^2", "normalization": "Gamma scale beta=sigma^2/(2 kappa), Laguerre variable z=x/beta", "semigroup_convention": "P_t f(x)=E_x[f(X_t)] and p_t(x,y)=pi(y) K_t(x,y)", "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert-Polya operators"}
THEOREM = {"existence": "For every nonnegative parameter triple and x>=0 there is a unique nonnegative strong CIR solution; the boundary behavior below is canonical (instantaneous reflection on the regular face and absorption when dimension is zero).", "feller_atlas": "For kappa>0,theta>0,sigma>0, 2 kappa theta>=sigma^2 makes 0 an entrance/inaccessible boundary, while 0<2 kappa theta<sigma^2 makes it regular and instantaneously reflecting. If theta=0 or kappa=0 with sigma>0, dimension is zero and 0 is absorbing. If sigma=0 the process is deterministic and must be treated on separate faces.", "affine_transform": "E_x exp(-u X_t)=exp[-phi_t(u)-psi_t(u)x], psi'=-kappa psi-(sigma^2/2)psi^2, phi'=kappa theta psi, psi_0=u; closed forms are given separately for kappa sigma>0, kappa=0, sigma>0, sigma=0,kappa>0, and both zero.", "noncentral_chisquare": "When kappa,sigma>0, X_t=c_t chi2prime_{4 kappa theta/sigma^2}(lambda_t), c_t=sigma^2(1-e^-kappa t)/(4 kappa), lambda_t=4 kappa e^-kappa t x/[sigma^2(1-e^-kappa t)].", "gamma_stationary": "When kappa,theta,sigma>0, pi is Gamma(alpha=2 kappa theta/sigma^2, scale beta=sigma^2/(2 kappa)); it is the unique invariant probability law, with mean theta and variance theta sigma^2/(2 kappa).", "laguerre_spectrum": "After z=x/beta, L=kappa[z d2 +(alpha-z)d], and L_n^(alpha-1)(z) has eigenvalue -kappa n. The exact reversible kernel ratio is K_t=sum_{n>=0}e^-kappa nt n! Gamma(alpha)/Gamma(n+alpha) L_n(z_x)L_n(z_y).", "gap_ergodicity": "The L2(pi) spectral gap is exactly kappa; Var_pi(P_t f)<=e^-2 kappa t Var_pi(f), and chi2/TV contract with factors e^-2 kappa t and e^-kappa t for L2 initial densities. Equality is attained by the first Laguerre mode.", "degenerate_faces": "sigma=0 gives X_t=theta+(x-theta)e^-kappa t for kappa>0; theta=0 gives deterministic decay. kappa=theta=0,sigma>0 is squared Bessel dimension zero with an absorbing atom at 0. kappa=sigma=0 is the constant process. These faces have no nontrivial Gamma/Laguerre stationary theorem.", "zeta_boundary": "The stochastic semigroup and its Laguerre kernel are not a primitive-orbit zeta, Fredholm determinant matched to an analytic target, or Hilbert--Polya operator."}
IDENTITIES = [{"name": "riccati_affine", "formula": "psi'=-kappa psi-(sigma^2/2)psi^2 and phi'=kappa theta psi"}, {"name": "interior_closed_form", "formula": "h=sigma^2(1-e^-kappa t)/(2kappa), psi=u e^-kappa t/(1+h u), phi=alpha log(1+h u)"}, {"name": "noncentral_chisquare_laplace", "formula": "c=sigma^2(1-e^-kappa t)/(4kappa), d=2alpha, lambda=4kappa e^-kappa t x/[sigma^2(1-e^-kappa t)]"}, {"name": "feller_index", "formula": "delta=4kappa theta/sigma^2 and 0 is inaccessible iff delta>=2"}, {"name": "gamma_invariance", "formula": "pi(dx)=x^(alpha-1)e^-x/beta dx/[Gamma(alpha) beta^alpha], alpha beta=theta"}, {"name": "laguerre_eigen_equation", "formula": "z L_n''+(alpha-z)L_n'+n L_n=0"}, {"name": "laguerre_orthogonality", "formula": "int L_n L_m z^(alpha-1)e^-z dz=Gamma(n+alpha)/n! delta_nm"}, {"name": "poincare_gap", "formula": "E_pi[(f-pi f)^2]<=kappa^-1 E_pi[(sigma^2/2)x(f')^2]"}, {"name": "zero_dimension_atom", "formula": "P_x(X_t=0)=exp[-x e^-kappa t/h_t] for theta=0,kappa>0,sigma>0; h_t=sigma^2(1-e^-kappa t)/(2kappa)"}]


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def frac(s: str | int) -> Fraction:
    return Fraction(s)


def mpfrac(s: str | int) -> mp.mpf:
    z = frac(s); return mp.mpf(z.numerator) / z.denominator


def dec(v: mp.mpf, digits: int = 64) -> str:
    if abs(v) < mp.mpf("1e-82"): return "0.0"
    return mp.nstr(v, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def bclass(k: Fraction, th: Fraction, s: Fraction) -> str:
    if s == 0:
        if k == 0: return "constant_every_point_absorbing"
        if th == 0: return "deterministic_zero_absorbing_asymptotic"
        return "deterministic_entrance_to_positive_theta"
    if k == 0 or th == 0: return "absorbing_zero_dimension"
    return "entrance_inaccessible" if 2 * k * th >= s * s else "regular_instantaneously_reflecting"


def sreg(k: Fraction, th: Fraction, s: Fraction) -> str:
    if k > 0 and th > 0 and s > 0: return "unique_gamma"
    if s == 0 and k > 0 and th > 0: return "delta_theta_deterministic"
    if th == 0 and (k > 0 or s > 0): return "delta_zero_absorbing"
    return "no_unique_probability_stationary_law"


def branch(k: Fraction, th: Fraction, s: Fraction) -> str:
    if k > 0 and s > 0: return "mean_reverting_cir"
    if k == 0 and s > 0: return "squared_bessel_dimension_zero"
    if s == 0 and k > 0: return "deterministic_ode"
    return "constant_process"


def transform(k: Fraction, th: Fraction, s: Fraction, t: Fraction, u: Fraction) -> tuple[mp.mpf, mp.mpf]:
    km, tm, sm, tt, um = [mpfrac(v) for v in (k, th, s, t, u)]
    if km > 0 and sm > 0:
        e = mp.exp(-km * tt); h = sm * sm / (2 * km) * (1 - e)
        return (2 * km * tm / (sm * sm)) * mp.log(1 + h * um), um * e / (1 + h * um)
    if km == 0 and sm > 0:
        h = sm * sm * tt / 2; return mp.mpf(0), um / (1 + h * um)
    if sm == 0 and km > 0:
        e = mp.exp(-km * tt); return tm * um * (1 - e), um * e
    return mp.mpf(0), um


def laguerre(n: int, a: mp.mpf, z: mp.mpf) -> mp.mpf:
    return mp.fsum(((-1) ** j) * mp.binomial(n + a, n - j) * z ** j / mp.factorial(j) for j in range(n + 1))


class Audit:
    def __init__(self) -> None: self.count = 0
    def check(self, ok: bool, msg: str) -> None:
        self.count += 1
        if not ok: raise AssertionError(msg)


def validate(d: dict) -> int:
    a = Audit()
    a.check(set(d) == TOP_KEYS, "top-level schema closure")
    a.check(d["schema"] == "hcs-c229-cir-affine-laguerre-v1", "schema")
    a.check(d["candidate_id"] == "HCS-C229", "candidate")
    a.check(d["evaluation_date"] == "2026-08-29", "date")
    a.check(d["source_commit"] == SOURCE_COMMIT, "source lock")
    a.check(d["scope_literal"] == SCOPE, "scope")
    a.check(d["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator lock")
    a.check(d["headline"] == HEADLINE, "headline")
    a.check(d["frozen_object"] == FROZEN, "frozen object")
    a.check(d["payload_sha256"] == payload_hash(d), "payload hash")
    a.check(set(d["theorem"]) == set(THEOREM), "theorem keys")
    a.check(d["theorem"] == THEOREM, "theorem lock")
    r = d["regression"]
    a.check(set(r) == {"boundary_rows", "boundary_row_count", "transform_rows", "transform_row_count", "stationary_rows", "stationary_row_count", "laguerre_rows", "gap_rows", "atom_rows", "working_decimal_digits", "serialized_significant_digits"}, "regression keys")
    a.check(r["boundary_row_count"] == 8 == len(r["boundary_rows"]), "boundary count")
    expected_boundary = [("strict_feller_entrance", Fraction(3), Fraction(2), Fraction(2)), ("feller_equality_entrance", Fraction(1), Fraction(2), Fraction(2)), ("regular_reflecting", Fraction(1), Fraction(1), Fraction(2)), ("theta_zero_absorbing", Fraction(2), Fraction(0), Fraction(1)), ("kappa_zero_squared_bessel", Fraction(0), Fraction(5), Fraction(2)), ("sigma_zero_deterministic_positive", Fraction(2), Fraction(3), Fraction(0)), ("sigma_zero_theta_zero", Fraction(2), Fraction(0), Fraction(0)), ("all_rates_zero_constant", Fraction(0), Fraction(5), Fraction(0))]
    bkeys = {"case_id", "kappa", "theta", "sigma", "feller_left_2kappa_theta", "feller_right_sigma_squared", "alpha_2kappa_theta_over_sigma2", "boundary_class", "stationary_regime", "transform_branch"}
    for row, (cid, k, th, s) in zip(r["boundary_rows"], expected_boundary):
        a.check(set(row) == bkeys, f"boundary keys {cid}")
        a.check(row["case_id"] == cid, f"boundary id {cid}")
        a.check((frac(row["kappa"]), frac(row["theta"]), frac(row["sigma"])) == (k, th, s), f"boundary params {cid}")
        a.check(frac(row["feller_left_2kappa_theta"]) == 2*k*th, f"left {cid}")
        a.check(frac(row["feller_right_sigma_squared"]) == s*s, f"right {cid}")
        expected_alpha = None if s == 0 else 2*k*th/(s*s)
        a.check((None if row["alpha_2kappa_theta_over_sigma2"] is None else frac(row["alpha_2kappa_theta_over_sigma2"])) == expected_alpha, f"alpha {cid}")
        a.check(row["boundary_class"] == bclass(k, th, s), f"class {cid}")
        a.check(row["stationary_regime"] == sreg(k, th, s), f"stationary {cid}")
        a.check(row["transform_branch"] == branch(k, th, s), f"branch {cid}")
    a.check(r["transform_row_count"] == 7 == len(r["transform_rows"]), "transform count")
    tkeys = {"case_id", "kappa", "theta", "sigma", "time", "u", "x", "phi", "psi", "laplace"}
    expected_transform = [("interior_short", Fraction(3), Fraction(2), Fraction(2), Fraction(1,5), Fraction(3,7), Fraction(5,2)), ("interior_long", Fraction(3), Fraction(2), Fraction(2), Fraction(7,3), Fraction(4,5), Fraction(1,3)), ("equality_face", Fraction(1), Fraction(2), Fraction(2), Fraction(1,2), Fraction(2,3), Fraction(4)), ("regular_face", Fraction(1), Fraction(1), Fraction(2), Fraction(3,2), Fraction(1,2), Fraction(1)), ("kappa_zero", Fraction(0), Fraction(5), Fraction(2), Fraction(4,3), Fraction(3,5), Fraction(2)), ("sigma_zero", Fraction(2), Fraction(3), Fraction(0), Fraction(2,3), Fraction(7,8), Fraction(5,2)), ("all_zero", Fraction(0), Fraction(5), Fraction(0), Fraction(11,6), Fraction(2,5), Fraction(9))]
    for row, (cid, k, th, s, t, u, x) in zip(r["transform_rows"], expected_transform):
        a.check(set(row) == tkeys, f"transform keys {cid}")
        a.check(row["case_id"] == cid, f"transform id {cid}")
        a.check(tuple(frac(row[z]) for z in ("kappa", "theta", "sigma", "time", "u", "x")) == (k, th, s, t, u, x), f"transform params {cid}")
        ph, ps = transform(k, th, s, t, u)
        a.check(row["phi"] == dec(ph), f"phi {cid}"); a.check(row["psi"] == dec(ps), f"psi {cid}")
        a.check(row["laplace"] == dec(mp.exp(-ph-ps*mpfrac(x))), f"laplace {cid}")
        a.check(mp.mpf(row["laplace"]) > 0 and mp.mpf(row["laplace"]) <= 1, f"laplace range {cid}")
    a.check(r["stationary_row_count"] == 3 == len(r["stationary_rows"]), "stationary count")
    skeys = {"case_id", "kappa", "theta", "sigma", "u", "alpha", "beta_scale", "mean", "variance", "laplace_gamma"}
    expected_stationary = [("gamma_alpha6", Fraction(3), Fraction(2), Fraction(2), Fraction(3,5)), ("gamma_alpha_half", Fraction(1), Fraction(1), Fraction(2), Fraction(4,7)), ("gamma_alpha2", Fraction(2), Fraction(1), Fraction(2), Fraction(5,6))]
    for row, (cid, k, th, s, u) in zip(r["stationary_rows"], expected_stationary):
        a.check(set(row) == skeys, f"stationary keys {cid}")
        a.check(row["case_id"] == cid, f"stationary id {cid}")
        aa, bb = 2*k*th/(s*s), s*s/(2*k)
        a.check(frac(row["alpha"]) == aa and frac(row["beta_scale"]) == bb, f"gamma params {cid}")
        a.check(row["mean"] == dec(mpfrac(aa)*mpfrac(bb)), f"mean {cid}")
        a.check(row["variance"] == dec(mpfrac(aa)*mpfrac(bb)**2), f"variance {cid}")
        a.check(row["laplace_gamma"] == dec((1+mpfrac(bb)*mpfrac(u))**(-mpfrac(aa))), f"gamma laplace {cid}")
    lrows = r["laguerre_rows"]
    a.check(len(lrows) == 12, "laguerre row count")
    for n, row in enumerate(lrows[:9]):
        a.check(set(row) == {"n", "eigenvalue", "normalized_norm", "kernel_coefficient"}, f"laguerre keys {n}")
        a.check(row["n"] == n and frac(row["eigenvalue"]) == -3*n, f"laguerre eigen {n}")
        norm = mp.gamma(n+6)/(mp.factorial(n)*mp.gamma(6))
        a.check(row["normalized_norm"] == dec(norm), f"norm {n}"); a.check(row["kernel_coefficient"] == dec(1/norm), f"coef {n}")
    for row in lrows[9:]:
        a.check(set(row) == {"n", "time", "x", "y", "kernel_ratio_N80", "kernel_terms"}, "kernel row keys")
        a.check(row["n"] == -1 and row["kernel_terms"] == 80, "kernel metadata")
        a.check(mp.mpf(row["kernel_ratio_N80"]) > 0, "kernel positivity")
    grows = r["gap_rows"]; a.check(len(grows) == 5, "gap rows")
    for row in grows:
        a.check(set(row) == {"kappa", "time", "variance_factor", "l2_factor", "n1_eigen_factor"}, "gap keys")
        fac = mp.exp(-mpfrac(row["kappa"])*mpfrac(row["time"]))
        a.check(row["l2_factor"] == dec(fac) and row["n1_eigen_factor"] == dec(fac), "gap factor")
        a.check(row["variance_factor"] == dec(fac*fac), "variance factor")
    arows = r["atom_rows"]; a.check(len(arows) == 3, "atom rows")
    for row in arows:
        a.check(set(row) == {"kappa", "sigma", "time", "x", "atom_at_zero"}, "atom keys")
        k, s, t, x = [mpfrac(row[z]) for z in ("kappa", "sigma", "time", "x")]
        if k > 0: h = s*s/(2*k)*(1-mp.exp(-k*t)); expected = mp.exp(-x*mp.exp(-k*t)/h)
        else: h = s*s*t/2; expected = mp.exp(-x/h)
        a.check(row["atom_at_zero"] == dec(expected), "atom value")
        a.check(0 < mp.mpf(row["atom_at_zero"]) < 1, "atom range")
    a.check(r["working_decimal_digits"] == 90 and r["serialized_significant_digits"] == 64, "precision lock")
    a.check(d["exact_identities"] == IDENTITIES, "identity ledger")
    route = d["route_a"]
    a.check(set(route) == {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}, "route keys")
    a.check(route["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    a.check(route["overall"] == "ROUTE_A_REJECTED" and route["route_b_invocation_allowed"] is False, "route verdict")
    a.check(set(d["scope_flags"]) == SCOPE_KEYS and all(v is False for v in d["scope_flags"].values()), "scope flags")
    expected_citations = [{"id": "CoxIngersollRoss1985", "doi": "10.2307/1911252", "role": "original affine term-structure/CIR model"}, {"id": "Feller1951", "doi": "10.2307/1969318", "role": "one-dimensional boundary classification framework"}, {"id": "Alfonsi2010", "doi": "10.1090/S0025-5718-09-02252-2", "role": "square-root diffusion schemes and boundary context"}, {"id": "Lepage2016", "doi": "10.1080/03610918.2015.1057222", "role": "CIR transition and noncentral chi-square formulas"}]
    a.check(d["citations"] == expected_citations, "citation ledger")
    a.check(len(d["nonclaims"]) == 5 and all(isinstance(x, str) for x in d["nonclaims"]), "nonclaims")
    return a.count


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    count = validate(data)
    print(f"C229 independent checker: PASS ({count} assertions; payload_sha256={data['payload_sha256']})")


if __name__ == "__main__": main()
