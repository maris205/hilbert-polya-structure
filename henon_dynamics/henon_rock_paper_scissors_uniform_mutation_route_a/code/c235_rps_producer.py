#!/usr/bin/env python3
"""Deterministic certificate producer for the three-strategy RPS flow.

The ledger is deliberately source-local.  It records the conservative first
integral, endpoint-cancelled period quadratures, and the uniform-mutation
Lyapunov/contraction checks.  No arithmetic target data are read.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c235_rps_evidence.json"
WORKING_DIGITS = 90
SERIALIZED_DIGITS = 64
mp.mp.dps = WORKING_DIGITS


def ftext(v: F) -> str:
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"


def mpq(v: F | int | str) -> mp.mpf:
    q = v if isinstance(v, F) else F(v)
    return mp.mpf(q.numerator) / q.denominator


def dec(v: mp.mpf, digits: int = SERIALIZED_DIGITS) -> str:
    if abs(v) < mp.mpf("1e-82"):
        v = mp.mpf("0")
    return mp.nstr(v, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def field(a: mp.mpf, mu: mp.mpf, p: tuple[mp.mpf, mp.mpf, mp.mpf]) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    x, y, z = p
    return (
        a * x * (y - z) + mu * (mp.mpf(1) / 3 - x),
        a * y * (z - x) + mu * (mp.mpf(1) / 3 - y),
        a * z * (x - y) + mu * (mp.mpf(1) / 3 - z),
    )


def rk4(a: mp.mpf, mu: mp.mpf, p: tuple[mp.mpf, mp.mpf, mp.mpf], t: F, steps: int = 800) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Fixed-step RK4 is only a reproducible diagnostic, not the theorem."""
    h = mpq(t) / steps
    q = p
    for _ in range(steps):
        k1 = field(a, mu, q)
        q2 = tuple(q[i] + h * k1[i] / 2 for i in range(3))
        k2 = field(a, mu, q2)
        q3 = tuple(q[i] + h * k2[i] / 2 for i in range(3))
        k3 = field(a, mu, q3)
        q4 = tuple(q[i] + h * k3[i] for i in range(3))
        k4 = field(a, mu, q4)
        q = tuple(q[i] + h * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6 for i in range(3))
    return q


def hvalue(p: tuple[mp.mpf, mp.mpf, mp.mpf]) -> mp.mpf:
    return p[0] * p[1] * p[2]


def distance_bary(p: tuple[mp.mpf, mp.mpf, mp.mpf]) -> mp.mpf:
    return mp.sqrt(mp.fsum((q - mp.mpf(1) / 3) ** 2 for q in p))


def dlog_fraction(mu: F, p: tuple[F, F, F]) -> F | None:
    if any(q == 0 for q in p):
        return None
    x, y, z = p
    return mu * (1 / x + 1 / y + 1 / z - 9) / 3


def cubic(x: mp.mpf, h: mp.mpf) -> mp.mpf:
    return x * (1 - x) ** 2 - 4 * h


def roots_for(h: F) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Return x_-<1/3<x_+ and the third root x_3=2-x_--x_+."""
    hm = mpq(h)
    if not (0 < hm < mp.mpf(1) / 27):
        raise ValueError("quadrature rows require 0<h<1/27")
    lo, hi = mp.mpf(0), mp.mpf(1) / 3
    for _ in range(360):
        mid = (lo + hi) / 2
        if cubic(mid, hm) > 0:
            hi = mid
        else:
            lo = mid
    xm = (lo + hi) / 2
    lo, hi = mp.mpf(1) / 3, mp.mpf(1)
    for _ in range(360):
        mid = (lo + hi) / 2
        if cubic(mid, hm) > 0:
            lo = mid
        else:
            hi = mid
    xp = (lo + hi) / 2
    return xm, xp, 2 - xm - xp


def period(a: F, h: F) -> mp.mpf:
    """Endpoint-cancelled form of the stated x-quadrature."""
    xm, xp, x3 = roots_for(h)
    mid, half = (xm + xp) / 2, (xp - xm) / 2

    def integrand(theta: mp.mpf) -> mp.mpf:
        x = mid + half * mp.sin(theta)
        # Since x(1-x)^2-4h=(x-x_-)(x-x_+)(x-x_3),
        # the cosine endpoint factor cancels exactly.
        return 1 / mp.sqrt(x * (x3 - x))

    return (2 / mpq(a)) * mp.quad(integrand, [-mp.pi / 2, 0, mp.pi / 2])


CONSERVATIVE_CASES = [
    ("conservative_a1", F(1)),
    ("conservative_a2", F(2)),
    ("conservative_a3", F(3)),
]
H_VALUES = [F(1, 1000), F(1, 100), F(1, 50), F(1, 30), F(1, 28)]

MUTATION_CASES = [
    ("mu_small_interior", F(1), F(1, 10), (F(1, 2), F(1, 3), F(1, 6)), F(2)),
    ("mu_small_skew", F(2), F(1, 10), (F(3, 5), F(1, 5), F(1, 5)), F(2)),
    ("mu_large_interior", F(3), F(1, 2), (F(1, 10), F(2, 5), F(1, 2)), F(3, 2)),
    ("mu_boundary_x", F(1), F(1, 4), (F(0), F(1, 2), F(1, 2)), F(1)),
    ("mu_boundary_y", F(2), F(1, 3), (F(2, 3), F(0), F(1, 3)), F(1)),
    ("mu_boundary_z", F(3), F(1, 2), (F(1, 3), F(2, 3), F(0)), F(1)),
]

CONTRACTION_CASES = [
    ("a_zero_mu_quarter", F(1, 4), (F(4, 5), F(1, 10), F(1, 10)), F(1, 2)),
    ("a_zero_mu_two", F(2), (F(1, 6), F(1, 3), F(1, 2)), F(3, 4)),
    ("a_zero_mu_one", F(1), (F(1, 20), F(7, 20), F(3, 5)), F(1)),
]


def conservative_row(case_id: str, a: F, h: F) -> dict:
    xm, xp, x3 = roots_for(h)
    T = period(a, h)
    return {
        "case_id": case_id,
        "a": ftext(a),
        "h": ftext(h),
        "x_minus": dec(xm),
        "x_plus": dec(xp),
        "x_third": dec(x3),
        "period": dec(T),
        "a_period": dec(mpq(a) * T),
        "left_residual": dec(cubic(xm, mpq(h))),
        "right_residual": dec(cubic(xp, mpq(h))),
        "simple_level": True,
    }


def center_limit_row(a: F) -> dict:
    lim = 2 * mp.pi * mp.sqrt(3) / mpq(a)
    return {"case_id": f"center_limit_a{ftext(a)}", "a": ftext(a), "h": ftext(F(1, 27)), "period_limit": dec(lim), "scaled_limit": dec(mpq(a) * lim), "barycenter": ["1/3", "1/3", "1/3"]}


def mutation_row(case_id: str, a: F, mu: F, p: tuple[F, F, F], t: F) -> dict:
    pm = tuple(mpq(q) for q in p)
    am, mum = mpq(a), mpq(mu)
    end = rk4(am, mum, pm, t)
    f0 = field(am, mum, pm)
    dlog = dlog_fraction(mu, p)
    return {
        "case_id": case_id,
        "a": ftext(a), "mu": ftext(mu), "initial": [ftext(q) for q in p], "time": ftext(t), "steps": 800,
        "initial_field": [dec(v) for v in f0], "field_sum": dec(mp.fsum(f0)),
        "dlog_h_exact": None if dlog is None else ftext(dlog),
        "initial_h": dec(hvalue(pm)), "final_state": [dec(v) for v in end],
        "final_sum": dec(mp.fsum(end)), "final_h": dec(hvalue(end)),
        "initial_distance": dec(distance_bary(pm)), "final_distance": dec(distance_bary(end)),
        "strictly_positive_after": all(v > 0 for v in end),
    }


def contraction_row(case_id: str, mu: F, p: tuple[F, F, F], t: F) -> dict:
    mum, tm = mpq(mu), mpq(t)
    q = tuple(mp.mpf(1) / 3 + (mpq(p[i]) - mp.mpf(1) / 3) * mp.exp(-mum * tm) for i in range(3))
    return {
        "case_id": case_id, "a": "0", "mu": ftext(mu), "initial": [ftext(v) for v in p], "time": ftext(t),
        "exact_state": [dec(v) for v in q], "sum": dec(mp.fsum(q)), "distance_factor": dec(mp.exp(-mum * tm)),
        "positive": all(v > 0 for v in q),
    }


def linearization_row(case_id: str, a: F, mu: F) -> dict:
    return {"case_id": case_id, "a": ftext(a), "mu": ftext(mu), "real_part": dec(-mpq(mu)), "imag_abs": dec(mpq(a) / mp.sqrt(3)), "tangent_trace": dec(-2 * mpq(mu)), "tangent_determinant": dec(mpq(mu) ** 2 + mpq(a) ** 2 / 3)}


def build() -> dict:
    conservative = [conservative_row(cid, a, h) for cid, a in CONSERVATIVE_CASES for h in H_VALUES]
    limits = [center_limit_row(a) for _, a in CONSERVATIVE_CASES]
    mutations = [mutation_row(*spec) for spec in MUTATION_CASES]
    contractions = [contraction_row(*spec) for spec in CONTRACTION_CASES]
    linear = [linearization_row("linear_a1_mu1_10", F(1), F(1, 10)), linearization_row("linear_a3_mu1_2", F(3), F(1, 2)), linearization_row("linear_a0_mu1_4", F(0), F(1, 4)), linearization_row("linear_identity", F(0), F(0))]
    data = {
        "schema": "hcs-c235-rps-uniform-mutation-v1", "candidate_id": "HCS-C235", "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT, "fixed_epoch": FIXED_EPOCH, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The three-strategy rock--paper--scissors flow has an exact product invariant in the conservative face and a uniform-mutation Lyapunov atlas with global barycentric convergence.",
        "frozen_object": {
            "state_space": "Delta={x,y,z>=0:x+y+z=1}",
            "equations": "x_dot=a*x*(y-z)+mu*(1/3-x), cyclically in (x,y,z)",
            "parameters": "a>=0, mu>=0; only additive uniform mutation is included",
            "clock": "physical continuous ODE time t>=0",
            "normalization": "simplex mass x+y+z=1 and H=xyz on mu=0",
            "determinant_convention": "none; no orbit/Fredholm determinant",
            "arithmetic_origin": "none; a and mu are source-defined dynamical parameters",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert--Polya operators",
        },
        "theorem": {
            "simplex_invariance": "The closed simplex is forward invariant; for mu>0 each zero coordinate has inward derivative mu/3 and every nonzero-time state is interior.",
            "conservative_integral": "When mu=0, H=xyz is constant. If in addition a>0, every level 0<h<1/27 is one regular periodic orbit and the boundary consists of the three heteroclinic edges and their cyclic network; at a=0 the flow is the identity.",
            "period_quadrature": "If x_-<x_+ are the two roots in (0,1) of x(1-x)^2=4h, then T(h)=2/a integral_{x_-}^{x_+} dx/[x sqrt((1-x)^2-4h/x)]. The endpoint-cancelled implementation uses x(theta) and x_3=2-x_--x_+.",
            "center_limit": "For a>0, as h increases to 1/27, T(h) tends to 2*pi*sqrt(3)/a; as h decreases to zero the period diverges toward the boundary heteroclinic network.",
            "mutation_lyapunov": "For mu>0 and interior states, d log(xyz)/dt=mu/3*(1/x+1/y+1/z-9)>=0, with equality only at (1/3,1/3,1/3).",
            "global_convergence": "LaSalle's invariance principle gives global convergence to the barycenter and excludes nonconstant recurrent trajectories for mu>0, including boundary starts after the instantaneous entrance.",
            "linearization": "On the tangent plane at the barycenter the eigenvalues are -mu +/- i*a/sqrt(3).",
            "faces": "For a=0, x_i(t)=1/3+(x_i(0)-1/3)e^{-mu t}; for a=mu=0 the vector field is zero and every simplex point is fixed. No general nonuniform mutation matrix is claimed.",
            "route_boundary": "The ODE has no intrinsic arithmetic labels, primitive periodic repetition law, target determinant, or Hilbert--Polya operator.",
        },
        "regression": {
            "conservative_rows": conservative, "center_limit_rows": limits, "mutation_rows": mutations,
            "contraction_rows": contractions, "linearization_rows": linear,
            "conservative_row_count": len(conservative), "center_limit_row_count": len(limits), "mutation_row_count": len(mutations),
            "contraction_row_count": len(contractions), "linearization_row_count": len(linear),
            "working_digits": WORKING_DIGITS, "serialized_digits": SERIALIZED_DIGITS,
        },
        "exact_identities": [
            {"identity_id": "mass", "formula": "x_dot+y_dot+z_dot=0"},
            {"identity_id": "conservative_product", "formula": "d(log(xyz))/dt=a[(y-z)+(z-x)+(x-y)]=0 when mu=0"},
            {"identity_id": "mutation_product", "formula": "d(log(xyz))/dt=mu/3*(1/x+1/y+1/z-9)"},
            {"identity_id": "AM_HM", "formula": "1/x+1/y+1/z >= 9/(x+y+z)=9"},
            {"identity_id": "cubic_turning", "formula": "x(1-x)^2-4h=0 at y=z"},
            {"identity_id": "period_limit", "formula": "for a>0, lim_{h->1/27} T(h)=2*pi*sqrt(3)/a"},
            {"identity_id": "center_spectrum", "formula": "lambda_tangent=-mu +/- i*a/sqrt(3)"},
            {"identity_id": "zero_a_flow", "formula": "x_i(t)-1/3=exp(-mu*t)*(x_i(0)-1/3)"},
            {"identity_id": "identity_face", "formula": "a=mu=0 implies X_t=X_0"},
        ],
        "route_a": {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "strongest_positive": "A complete source-native conservative period atlas and uniform-mutation convergence theorem are proved.", "strongest_failure": "There is no intrinsic rational-prime carrier, primitive-orbit repetition weight, target determinant, or natural Hilbert--Polya lift."},
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "MayLeonard1975", "claim": "cyclic three-species competition context only; not the frozen mutation model", "source": "R. M. May and W. J. Leonard, Nonlinear aspects of competition between three species, SIAM Journal on Applied Mathematics 29, 243--253 (1975)"},
            {"key": "HofbauerSigmund1998", "claim": "invariance and persistence vocabulary for population flows", "source": "Hofbauer and Sigmund, Evolutionary Games and Population Dynamics (1998)"},
            {"key": "LaSalle1960", "claim": "invariance-principle framework", "source": "LaSalle, Contributions to the Stability Problem (1960)"},
        ],
        "nonclaims": [
            "literature priority or exhaustive novelty certification",
            "general nonuniform mutation motifs or arbitrary mutation matrices",
            "a target arithmetic interpretation, Euler factors, root numbers, automorphy, target divisor or functional equation",
            "a primitive-orbit zeta, Fredholm determinant, or Hilbert--Polya operator",
            "external peer review, acceptance, or numerical evidence promoted to a theorem",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C235_PRODUCER_PASS", "conservative_rows": len(data["regression"]["conservative_rows"]), "mutation_rows": len(data["regression"]["mutation_rows"]), "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
