#!/usr/bin/env python3
"""Produce the deterministic HCS-C229 CIR theorem certificate.

The certificate is source-local.  It records the exact affine transform, the
Feller boundary split (including degenerate faces), and the Gamma/Laguerre
semigroup theorem.  It never reads arithmetic targets.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c229_cir_evidence.json"
mp.mp.dps = 90


def ftext(v: Fraction) -> str:
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"


def q(v: str | int | Fraction) -> Fraction:
    return v if isinstance(v, Fraction) else Fraction(v)


def mpq(v: str | Fraction | int) -> mp.mpf:
    z = q(v)
    return mp.mpf(z.numerator) / z.denominator


def dec(v: mp.mpf, digits: int = 64) -> str:
    if abs(v) < mp.mpf("1e-82"):
        return "0.0"
    return mp.nstr(v, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def alpha(kappa: Fraction, theta: Fraction, sigma: Fraction) -> Fraction | None:
    if sigma == 0:
        return None
    return 2 * kappa * theta / (sigma * sigma)


def boundary_class(kappa: Fraction, theta: Fraction, sigma: Fraction) -> str:
    if sigma == 0:
        if kappa == 0:
            return "constant_every_point_absorbing"
        if theta == 0:
            return "deterministic_zero_absorbing_asymptotic"
        return "deterministic_entrance_to_positive_theta"
    if kappa == 0 or theta == 0:
        return "absorbing_zero_dimension"
    left, right = 2 * kappa * theta, sigma * sigma
    return "entrance_inaccessible" if left >= right else "regular_instantaneously_reflecting"


def stationary_regime(kappa: Fraction, theta: Fraction, sigma: Fraction) -> str:
    if kappa > 0 and theta > 0 and sigma > 0:
        return "unique_gamma"
    if sigma == 0 and kappa > 0 and theta > 0:
        return "delta_theta_deterministic"
    if theta == 0 and (kappa > 0 or sigma > 0):
        return "delta_zero_absorbing"
    return "no_unique_probability_stationary_law"


def branch_name(kappa: Fraction, theta: Fraction, sigma: Fraction) -> str:
    if kappa > 0 and sigma > 0:
        return "mean_reverting_cir"
    if kappa == 0 and sigma > 0:
        return "squared_bessel_dimension_zero"
    if sigma == 0 and kappa > 0:
        return "deterministic_ode"
    return "constant_process"


def transform(kappa: Fraction, theta: Fraction, sigma: Fraction, t: Fraction, u: Fraction) -> tuple[mp.mpf, mp.mpf]:
    """Return (phi, psi) in E exp(-phi-psi*x)."""
    km, tm, sm, tt, um = map(mpq, (kappa, theta, sigma, t, u))
    if km > 0 and sm > 0:
        e = mp.exp(-km * tt)
        h = sm * sm / (2 * km) * (1 - e)
        psi = um * e / (1 + h * um)
        phi = (2 * km * tm / (sm * sm)) * mp.log(1 + h * um)
        return phi, psi
    if km == 0 and sm > 0:
        h = sm * sm * tt / 2
        return mp.mpf(0), um / (1 + h * um)
    if sm == 0 and km > 0:
        e = mp.exp(-km * tt)
        return tm * um * (1 - e), um * e
    return mp.mpf(0), um


def laplace_value(kappa: Fraction, theta: Fraction, sigma: Fraction, t: Fraction, u: Fraction, x: Fraction) -> mp.mpf:
    phi, psi = transform(kappa, theta, sigma, t, u)
    return mp.exp(-phi - psi * mpq(x))


def laguerre(n: int, a: mp.mpf, z: mp.mpf) -> mp.mpf:
    return mp.fsum(((-1) ** j) * mp.binomial(n + a, n - j) * z ** j / mp.factorial(j) for j in range(n + 1))


def gamma_kernel_ratio(alpha_m: mp.mpf, beta_m: mp.mpf, kappa_m: mp.mpf, t_m: mp.mpf, x_m: mp.mpf, y_m: mp.mpf, n_terms: int = 80) -> mp.mpf:
    zx, zy = x_m / beta_m, y_m / beta_m
    return mp.fsum(mp.exp(-kappa_m * t_m * n) * mp.factorial(n) * mp.gamma(alpha_m) / mp.gamma(n + alpha_m)
                   * laguerre(n, alpha_m - 1, zx) * laguerre(n, alpha_m - 1, zy)
                   for n in range(n_terms))


BOUNDARY_CASES = [
    ("strict_feller_entrance", Fraction(3), Fraction(2), Fraction(2)),
    ("feller_equality_entrance", Fraction(1), Fraction(2), Fraction(2)),
    ("regular_reflecting", Fraction(1), Fraction(1), Fraction(2)),
    ("theta_zero_absorbing", Fraction(2), Fraction(0), Fraction(1)),
    ("kappa_zero_squared_bessel", Fraction(0), Fraction(5), Fraction(2)),
    ("sigma_zero_deterministic_positive", Fraction(2), Fraction(3), Fraction(0)),
    ("sigma_zero_theta_zero", Fraction(2), Fraction(0), Fraction(0)),
    ("all_rates_zero_constant", Fraction(0), Fraction(5), Fraction(0)),
]


def boundary_row(case_id: str, kappa: Fraction, theta: Fraction, sigma: Fraction) -> dict:
    a = alpha(kappa, theta, sigma)
    return {
        "case_id": case_id, "kappa": ftext(kappa), "theta": ftext(theta), "sigma": ftext(sigma),
        "feller_left_2kappa_theta": ftext(2 * kappa * theta),
        "feller_right_sigma_squared": ftext(sigma * sigma),
        "alpha_2kappa_theta_over_sigma2": ftext(a) if a is not None else None,
        "boundary_class": boundary_class(kappa, theta, sigma),
        "stationary_regime": stationary_regime(kappa, theta, sigma),
        "transform_branch": branch_name(kappa, theta, sigma),
    }


TRANSFORM_CASES = [
    ("interior_short", Fraction(3), Fraction(2), Fraction(2), Fraction(1, 5), Fraction(3, 7), Fraction(5, 2)),
    ("interior_long", Fraction(3), Fraction(2), Fraction(2), Fraction(7, 3), Fraction(4, 5), Fraction(1, 3)),
    ("equality_face", Fraction(1), Fraction(2), Fraction(2), Fraction(1, 2), Fraction(2, 3), Fraction(4)),
    ("regular_face", Fraction(1), Fraction(1), Fraction(2), Fraction(3, 2), Fraction(1, 2), Fraction(1)),
    ("kappa_zero", Fraction(0), Fraction(5), Fraction(2), Fraction(4, 3), Fraction(3, 5), Fraction(2)),
    ("sigma_zero", Fraction(2), Fraction(3), Fraction(0), Fraction(2, 3), Fraction(7, 8), Fraction(5, 2)),
    ("all_zero", Fraction(0), Fraction(5), Fraction(0), Fraction(11, 6), Fraction(2, 5), Fraction(9)),
]


def transform_row(spec: tuple) -> dict:
    case_id, k, th, s, t, u, x = spec
    phi, psi = transform(k, th, s, t, u)
    return {"case_id": case_id, "kappa": ftext(k), "theta": ftext(th), "sigma": ftext(s),
            "time": ftext(t), "u": ftext(u), "x": ftext(x), "phi": dec(phi), "psi": dec(psi),
            "laplace": dec(mp.exp(-phi - psi * mpq(x)))}


STATIONARY_CASES = [
    ("gamma_alpha6", Fraction(3), Fraction(2), Fraction(2), Fraction(3, 5)),
    ("gamma_alpha_half", Fraction(1), Fraction(1), Fraction(2), Fraction(4, 7)),
    ("gamma_alpha2", Fraction(2), Fraction(1), Fraction(2), Fraction(5, 6)),
]


def stationary_row(case_id: str, k: Fraction, th: Fraction, s: Fraction, u: Fraction) -> dict:
    am, bm, um = mpq(2 * k * th / (s * s)), mpq(s * s / (2 * k)), mpq(u)
    return {"case_id": case_id, "kappa": ftext(k), "theta": ftext(th), "sigma": ftext(s), "u": ftext(u),
            "alpha": ftext(2 * k * th / (s * s)), "beta_scale": ftext(s * s / (2 * k)),
            "mean": dec(am * bm), "variance": dec(am * bm * bm),
            "laplace_gamma": dec((1 + bm * um) ** (-am))}


def laguerre_rows() -> list[dict]:
    k, th, s = Fraction(3), Fraction(2), Fraction(2)
    am, bm, km = mpq(6), mpq(Fraction(2, 3)), mpq(3)
    rows = []
    for n in range(9):
        norm = mp.gamma(n + am) / (mp.factorial(n) * mp.gamma(am))
        rows.append({"n": n, "eigenvalue": ftext(-k * n), "normalized_norm": dec(norm), "kernel_coefficient": dec(1 / norm)})
    for t, x, y in [(Fraction(1, 3), Fraction(2), Fraction(5, 3)), (Fraction(2), Fraction(1, 2), Fraction(7, 4)), (Fraction(5, 2), Fraction(4), Fraction(3, 5))]:
        ratio = gamma_kernel_ratio(am, bm, km, mpq(t), mpq(x), mpq(y), 80)
        rows.append({"n": -1, "time": ftext(t), "x": ftext(x), "y": ftext(y), "kernel_ratio_N80": dec(ratio), "kernel_terms": 80})
    return rows


def gap_rows() -> list[dict]:
    rows = []
    for k, t in [(Fraction(3), Fraction(1, 3)), (Fraction(3), Fraction(2)), (Fraction(1), Fraction(5, 4)), (Fraction(2), Fraction(7, 5)), (Fraction(5), Fraction(1, 2))]:
        factor = mp.exp(-mpq(k) * mpq(t))
        rows.append({"kappa": ftext(k), "time": ftext(t), "variance_factor": dec(factor * factor), "l2_factor": dec(factor), "n1_eigen_factor": dec(factor)})
    return rows


def atom_rows() -> list[dict]:
    rows = []
    for k, s, t, x in [(Fraction(2), Fraction(1), Fraction(1, 2), Fraction(3)), (Fraction(2), Fraction(3), Fraction(2), Fraction(5, 2)), (Fraction(0), Fraction(2), Fraction(4, 3), Fraction(2))]:
        km, sm, tm, xm = map(mpq, (k, s, t, x))
        if km > 0:
            h = sm * sm / (2 * km) * (1 - mp.exp(-km * tm))
            mass = mp.exp(-xm * mp.exp(-km * tm) / h)
        else:
            h = sm * sm * tm / 2
            mass = mp.exp(-xm / h)
        rows.append({"kappa": ftext(k), "sigma": ftext(s), "time": ftext(t), "x": ftext(x), "atom_at_zero": dec(mass)})
    return rows


def build() -> dict:
    data = {
        "schema": "hcs-c229-cir-affine-laguerre-v1", "candidate_id": "HCS-C229", "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The Cox--Ingersoll--Ross square-root diffusion has a closed all-parameter Feller boundary atlas, an exact affine Laplace transform, and—on the nondegenerate face—a Gamma reversible law with an explicit Laguerre semigroup and sharp spectral gap.",
        "frozen_object": {
            "sde": "dX_t=kappa(theta-X_t)dt+sigma sqrt(X_t)dW_t, X_0=x>=0",
            "generator": "L f=kappa(theta-x)f' +(sigma^2/2)x f''",
            "parameter_domain": "kappa,theta,sigma>=0; x>=0",
            "clock": "physical diffusion time t>=0",
            "feller_index": "alpha=2 kappa theta/sigma^2 when sigma>0; compare 2 kappa theta with sigma^2",
            "normalization": "Gamma scale beta=sigma^2/(2 kappa), Laguerre variable z=x/beta",
            "semigroup_convention": "P_t f(x)=E_x[f(X_t)] and p_t(x,y)=pi(y) K_t(x,y)",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert-Polya operators",
        },
        "theorem": {
            "existence": "For every nonnegative parameter triple and x>=0 there is a unique nonnegative strong CIR solution; the boundary behavior below is canonical (instantaneous reflection on the regular face and absorption when dimension is zero).",
            "feller_atlas": "For kappa>0,theta>0,sigma>0, 2 kappa theta>=sigma^2 makes 0 an entrance/inaccessible boundary, while 0<2 kappa theta<sigma^2 makes it regular and instantaneously reflecting. If theta=0 or kappa=0 with sigma>0, dimension is zero and 0 is absorbing. If sigma=0 the process is deterministic and must be treated on separate faces.",
            "affine_transform": "E_x exp(-u X_t)=exp[-phi_t(u)-psi_t(u)x], psi'=-kappa psi-(sigma^2/2)psi^2, phi'=kappa theta psi, psi_0=u; closed forms are given separately for kappa sigma>0, kappa=0, sigma>0, sigma=0,kappa>0, and both zero.",
            "noncentral_chisquare": "When kappa,sigma>0, X_t=c_t chi2prime_{4 kappa theta/sigma^2}(lambda_t), c_t=sigma^2(1-e^-kappa t)/(4 kappa), lambda_t=4 kappa e^-kappa t x/[sigma^2(1-e^-kappa t)].",
            "gamma_stationary": "When kappa,theta,sigma>0, pi is Gamma(alpha=2 kappa theta/sigma^2, scale beta=sigma^2/(2 kappa)); it is the unique invariant probability law, with mean theta and variance theta sigma^2/(2 kappa).",
            "laguerre_spectrum": "After z=x/beta, L=kappa[z d2 +(alpha-z)d], and L_n^(alpha-1)(z) has eigenvalue -kappa n. The exact reversible kernel ratio is K_t=sum_{n>=0}e^-kappa nt n! Gamma(alpha)/Gamma(n+alpha) L_n(z_x)L_n(z_y).",
            "gap_ergodicity": "The L2(pi) spectral gap is exactly kappa; Var_pi(P_t f)<=e^-2 kappa t Var_pi(f), and chi2/TV contract with factors e^-2 kappa t and e^-kappa t for L2 initial densities. Equality is attained by the first Laguerre mode.",
            "degenerate_faces": "sigma=0 gives X_t=theta+(x-theta)e^-kappa t for kappa>0; theta=0 gives deterministic decay. kappa=theta=0,sigma>0 is squared Bessel dimension zero with an absorbing atom at 0. kappa=sigma=0 is the constant process. These faces have no nontrivial Gamma/Laguerre stationary theorem.",
            "zeta_boundary": "The stochastic semigroup and its Laguerre kernel are not a primitive-orbit zeta, Fredholm determinant matched to an analytic target, or Hilbert--Polya operator.",
        },
        "regression": {
            "boundary_rows": [boundary_row(*row) for row in BOUNDARY_CASES], "boundary_row_count": len(BOUNDARY_CASES),
            "transform_rows": [transform_row(row) for row in TRANSFORM_CASES], "transform_row_count": len(TRANSFORM_CASES),
            "stationary_rows": [stationary_row(*row) for row in STATIONARY_CASES], "stationary_row_count": len(STATIONARY_CASES),
            "laguerre_rows": laguerre_rows(), "gap_rows": gap_rows(), "atom_rows": atom_rows(),
            "working_decimal_digits": 90, "serialized_significant_digits": 64,
        },
        "exact_identities": [
            {"name": "riccati_affine", "formula": "psi'=-kappa psi-(sigma^2/2)psi^2 and phi'=kappa theta psi"},
            {"name": "interior_closed_form", "formula": "h=sigma^2(1-e^-kappa t)/(2kappa), psi=u e^-kappa t/(1+h u), phi=alpha log(1+h u)"},
            {"name": "noncentral_chisquare_laplace", "formula": "c=sigma^2(1-e^-kappa t)/(4kappa), d=2alpha, lambda=4kappa e^-kappa t x/[sigma^2(1-e^-kappa t)]"},
            {"name": "feller_index", "formula": "delta=4kappa theta/sigma^2 and 0 is inaccessible iff delta>=2"},
            {"name": "gamma_invariance", "formula": "pi(dx)=x^(alpha-1)e^-x/beta dx/[Gamma(alpha) beta^alpha], alpha beta=theta"},
            {"name": "laguerre_eigen_equation", "formula": "z L_n''+(alpha-z)L_n'+n L_n=0"},
            {"name": "laguerre_orthogonality", "formula": "int L_n L_m z^(alpha-1)e^-z dz=Gamma(n+alpha)/n! delta_nm"},
            {"name": "poincare_gap", "formula": "E_pi[(f-pi f)^2]<=kappa^-1 E_pi[(sigma^2/2)x(f')^2]"},
            {"name": "zero_dimension_atom", "formula": "P_x(X_t=0)=exp[-x e^-kappa t/h_t] for theta=0,kappa>0,sigma>0; h_t=sigma^2(1-e^-kappa t)/(2kappa)"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "an exact affine stochastic semigroup with a source-native Gamma/Laguerre spectral decomposition and a complete boundary atlas",
            "strongest_failure": "the semigroup spectrum has no intrinsic rational-prime primitive orbit carrier and is not an arithmetic dynamical determinant",
        },
        "scope_flags": {
            "uses_target_zero_table": False, "uses_prime_table": False, "claims_arithmetic_local_data": False,
            "claims_euler_factors": False, "claims_root_numbers": False, "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False, "claims_hilbert_polya_operator": False, "invokes_route_b": False,
        },
        "citations": [
            {"id": "CoxIngersollRoss1985", "doi": "10.2307/1911252", "role": "original affine term-structure/CIR model"},
            {"id": "Feller1951", "doi": "10.2307/1969318", "role": "one-dimensional boundary classification framework"},
            {"id": "Alfonsi2010", "doi": "10.1090/S0025-5718-09-02252-2", "role": "square-root diffusion schemes and boundary context"},
            {"id": "Lepage2016", "doi": "10.1080/03610918.2015.1057222", "role": "CIR transition and noncentral chi-square formulas"},
        ],
        "nonclaims": [
            "The Gamma/Laguerre spectral theorem is stochastic Markov-semigroup analysis, not a primitive-orbit zeta or arithmetic determinant.",
            "Finite numerical rows validate the displayed formulas but do not replace the boundary or semigroup proofs.",
            "The equality 2 kappa theta=sigma^2 is classified as inaccessible/entrance; no stronger smooth-boundary assertion is made there.",
            "Degenerate faces are not silently assigned the interior Gamma law or spectral gap.",
            "No target arithmetic, Euler product, target divisor, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    tmp = args.output.with_name(args.output.name + ".tmp")
    tmp.write_text(raw)
    os.replace(tmp, args.output)
    print(json.dumps({"status": "C229_PRODUCER_PASS", "payload_sha256": data["payload_sha256"], "evidence_sha256": sha256(raw.encode()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
