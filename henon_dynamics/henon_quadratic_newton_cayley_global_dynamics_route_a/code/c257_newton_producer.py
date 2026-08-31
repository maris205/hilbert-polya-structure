#!/usr/bin/env python3
"""Deterministic exact certificate for the quadratic Newton--Cayley family."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd
from pathlib import Path

SOURCE_COMMIT = "b89544f1f7b1043f4158dfdf9db77787b332f146"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c257_newton_cayley_evidence.json"


def qtext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    p = 2
    sign = 1
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -sign if n > 1 else sign


def exact_points(n: int) -> int:
    return sum(mobius(n // d) * (2**d + 1) for d in divisors(n))


def v2(n: int) -> int:
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def ord2(q: int) -> int:
    if q == 1:
        return 1
    assert q % 2 == 1 and gcd(2, q) == 1
    value = 2 % q
    k = 1
    while value != 1:
        value = (2 * value) % q
        k += 1
    return k


def period_rows() -> list[dict]:
    rows = []
    for n in range(1, 17):
        fixed = 2**n + 1
        exact = exact_points(n)
        rows.append({
            "n": n,
            "fixed_points_on_sphere": fixed,
            "exact_period_points": exact,
            "primitive_orbits": exact // n,
            "julia_exact_period_points": exact - (2 if n == 1 else 0),
            "julia_cycle_multiplier": str(2**n),
        })
    return rows


def root_order_rows() -> list[dict]:
    rows = []
    for m in range(1, 129):
        e = v2(m)
        q = m >> e
        period = ord2(q)
        rows.append({
            "root_of_unity_order": m,
            "two_adic_tail": e,
            "odd_part": q,
            "eventual_exact_period": period,
            "landing_order": q,
            "classification": "periodic" if e == 0 else "strictly_preperiodic",
            "rule": "tail=v2(m); period=ord_q(2), with ord_1(2)=1",
        })
    return rows


def real_sample_rows() -> list[dict]:
    rows = []
    for u in (F(-9), F(-3), F(-1), F(-1, 2), F(0), F(1, 3), F(1), F(2), F(5), F(13)):
        if u == -1:
            rows.append({"u=z/a": "-1", "w=(u-1)/(u+1)": "infinity", "w_after_1": "infinity", "w_after_2": "infinity", "basin": "root -a", "root_error_coordinate_after_n": "infinity is fixed"})
            continue
        w = (u - 1) / (u + 1)
        if abs(w) < 1:
            basin = "root +a"
            error = "w_n=w_0^(2^n)"
        elif abs(w) > 1:
            basin = "root -a"
            error = "v_n=(1/w_0)^(2^n)"
        else:
            basin = "Julia boundary"
            error = "no basin contraction"
        rows.append({
            "u=z/a": qtext(u),
            "w=(u-1)/(u+1)": qtext(w),
            "w_after_1": qtext(w**2),
            "w_after_2": qtext(w**4),
            "basin": basin,
            "root_error_coordinate_after_n": error,
        })
    return rows


def cauchy_rows() -> list[dict]:
    rows = []
    for s in (F(-7), F(-3, 2), F(-1), F(-1, 3), F(1, 4), F(1), F(5, 2), F(9)):
        image = (s * s - 1) / (2 * s)
        rows.append({
            "s": qtext(s),
            "T(s)=(s^2-1)/(2s)": qtext(image),
            "line_point": "z=i*a*s",
            "density": "ds/(pi*(1+s^2))",
            "angle_owner": "s=cot(theta/2); theta maps to 2*theta mod 2*pi",
        })
    return rows


def identities() -> list[dict]:
    items = [
        ("newton_map", "N_a(z)=(z^2+a^2)/(2z) for p_a(z)=z^2-a^2 and a!=0"),
        ("cayley", "C_a(z)=(z-a)/(z+a); C_a^{-1}(w)=a*(1+w)/(1-w)"),
        ("conjugacy", "C_a(N_a(z))=C_a(z)^2 on the Riemann sphere"),
        ("iterate", "C_a(N_a^n(z))=C_a(z)^(2^n)"),
        ("plus_basin", "B(+a)={z: abs(C_a(z))<1}={z: Re(z/a)>0}"),
        ("minus_basin", "B(-a)={z: abs(C_a(z))>1}={z: Re(z/a)<0}"),
        ("julia", "J(N_a)={z: abs(C_a(z))=1}={z: Re(z/a)=0} union {infinity}"),
        ("plus_error", "z_n-a=2*a*w_0^(2^n)/(1-w_0^(2^n))"),
        ("minus_error", "z_n+a=-2*a*v_0^(2^n)/(1-v_0^(2^n)), v_0=1/w_0"),
        ("fixed_count", "#Fix(N_a^n)=2^n+1 on the Riemann sphere"),
        ("exact_count", "P_n=sum_{d|n} mobius(n/d)*(2^d+1); primitive cycles=P_n/n"),
        ("am_zeta", "zeta_AM(t)=exp(sum_{n>=1}(2^n+1)t^n/n)=1/((1-t)*(1-2t))"),
        ("periodic", "nonzero finite w is periodic iff its root-of-unity order q is odd; period=ord_q(2)"),
        ("preperiodic", "if ord(w)=2^e*q with q odd, exact tail=e and eventual period=ord_q(2), ord_1(2)=1"),
        ("multipliers", "the root cycles have multiplier 0; every Julia cycle of exact period n has multiplier 2^n"),
        ("critical_points", "the only critical points are w=0 and w=infinity, corresponding to roots +a and -a"),
        ("cauchy_measure", "Haar measure on abs(w)=1 pushes to ds/(pi*(1+s^2)) on z=i*a*s"),
        ("boundary_map", "on z=i*a*s, N_a gives s maps to (s^2-1)/(2s)"),
        ("lyapunov", "the boundary invariant measure is mixing and has Lyapunov exponent log(2) in Cayley angle"),
        ("scale", "N_a(a*u)=a*N_1(u); replacing a by -a swaps the two root basins"),
        ("collision_c141", "C141 owns a Hardy inverse-branch Ruelle operator for z^2-6, not Newton root basins"),
        ("collision_c177", "C177 owns degree-b circle Wold theory; C257 owns the global Newton sphere and root-order tails"),
        ("degenerate_a0", "at a=0 the rational degree drops and N_0(z)=z/2 for finite z"),
    ]
    return [{"identity_id": k, "formula": v} for k, v in items]


def build() -> dict:
    periods = period_rows()
    orders = root_order_rows()
    real_rows = real_sample_rows()
    boundary_rows = cauchy_rows()
    data = {
        "schema": "hcs-c257-quadratic-newton-cayley-global-v1",
        "candidate_id": "HCS-C257",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE_COMMIT,
        "fixed_epoch": FIXED_EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "Cayley conjugacy closes the global quadratic Newton dynamics: both root basins, the Julia line, double-exponential errors, every periodic and preperiodic point, multipliers, zeta, and boundary Cauchy dynamics.",
        "frozen_object": {
            "phase_space": "Riemann sphere P^1(C)",
            "polynomial": "p_a(z)=z^2-a^2 with a in C*",
            "dynamics": "N_a(z)=z-p_a(z)/p_a'(z)=(z^2+a^2)/(2z)",
            "cayley_coordinate": "w=C_a(z)=(z-a)/(z+a)",
            "clock": "Newton iteration n in Z_{≥0}",
            "parameter": "a in C*; a=0 is a separately recorded degree-drop face",
            "arithmetic_origin": "none; deterministic complex root-finding dynamics",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target determinants, Hilbert--Polya operators",
        },
        "theorem": {
            "global_conjugacy": "For every a!=0, C_a is a Mobius conjugacy from N_a on P^1(C) to D(w)=w^2; hence C_a(N_a^n(z))=C_a(z)^(2^n) for every n.",
            "basin_julia_atlas": "The basins of +a and -a are Re(z/a)>0 and Re(z/a)<0; their common boundary Re(z/a)=0 union infinity is the Julia set.",
            "double_exponential": "In either open basin the exact Cayley error is raised to 2^n, yielding the displayed root-error identities and global quadratic convergence away from the Julia line.",
            "periodic_preperiodic": "Besides w=0 and infinity, preperiodic points are exactly roots of unity. If ord(w)=2^e*q with q odd, the exact tail is e and the eventual exact period is ord_q(2), with ord_1(2)=1; periodicity is exactly e=0.",
            "counts_multipliers_zeta": "#Fix(N_a^n)=2^n+1; Mobius inversion gives exact-period points and primitive cycles; both root cycles are superattracting and every Julia n-cycle has multiplier 2^n; zeta_AM=1/((1-t)(1-2t)).",
            "boundary_measure": "Haar measure under w=e^{i theta} pushes through z=i*a*cot(theta/2) to the normalized Cauchy law; it is invariant and mixing, and the Cayley-angle Lyapunov exponent is log 2.",
            "parameter_boundaries": "Scale covariance removes nonzero a, changing a to -a exchanges roots, and a=0 is a degree-one degeneration N_0(z)=z/2 rather than part of the degree-two theorem.",
            "ownership": "Unlike C141, no Hardy inverse-branch Ruelle operator is built; unlike C177, the object is the Newton map on the full sphere with two root basins and an exact even-order preperiodic tail.",
            "scope": "This is a source-local complex-dynamics and root-finding theorem, not an arithmetic determinant, target spectrum, or Hilbert--Polya construction.",
        },
        "exact_receipt": {
            "period_rows": periods,
            "period_row_count": len(periods),
            "root_order_rows": orders,
            "root_order_row_count": len(orders),
            "real_sample_rows": real_rows,
            "real_sample_row_count": len(real_rows),
            "cauchy_rows": boundary_rows,
            "cauchy_row_count": len(boundary_rows),
            "receipt_status": "finite exact regression prefix supporting an all-period analytic theorem",
        },
        "exact_identities": identities(),
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "A global Mobius conjugacy closes the basins, Julia set, all periodic/preperiodic points, multipliers, Artin--Mazur zeta, and invariant boundary law.",
            "strongest_failure": "The orbit law is the universal degree-two squaring law and supplies no intrinsic rational-prime carrier, logarithmic prime clock, target divisor, or arithmetic determinant owner.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "Cayley1879", "claim": "historical quadratic Newton basin problem", "source": "A. Cayley, Desiderata and Suggestions: No. 3. The Newton-Fourier Imaginary Problem, American Journal of Mathematics 2 (1879), 97", "url": "https://doi.org/10.2307/2369201"},
            {"key": "ArtinMazur1965", "claim": "periodic-point zeta definition", "source": "M. Artin and B. Mazur, On Periodic Points, Annals of Mathematics 81 (1965), 82--99", "url": "https://www.jstor.org/stable/1970384"},
        ],
        "nonclaims": [
            "a workspace or literature novelty/priority theorem",
            "a corresponding classification for cubic or higher-degree Newton maps",
            "arithmetic local data, Euler factors, root numbers, automorphy, or a target functional equation",
            "a target zeta/Fredholm determinant, target zero match, or Hilbert--Polya operator",
            "Route B eligibility or external peer review",
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
    print(json.dumps({"status": "C257_PRODUCER_PASS", "period_rows": data["exact_receipt"]["period_row_count"], "root_order_rows": data["exact_receipt"]["root_order_row_count"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
