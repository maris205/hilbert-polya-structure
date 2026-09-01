#!/usr/bin/env python3
"""Produce the deterministic HCS-C280 Jeffery--Bretherton certificate."""
from __future__ import annotations

import hashlib
import itertools
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C280_EVIDENCE_OUT", ROOT / "results/c280_jeffery_evidence.json"))
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
mp.mp.dps = 90

LAMBDAS = (Q(-4, 5), Q(-3, 5), Q(0), Q(3, 5), Q(4, 5))
GRID = (-2, -1, 0, 1, 2)
TIMES = (Q(1, 7), Q(2, 5), Q(1), Q(3, 2))
VECTORS = (
    (Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(1)),
    (Q(1), Q(1), Q(0)), (Q(1), Q(-1), Q(0)), (Q(1), Q(0), Q(1)),
    (Q(0), Q(1), Q(1)), (Q(1), Q(2), Q(3)), (Q(-2), Q(1), Q(1)),
    (Q(3), Q(-1), Q(2)),
)
CASES = {
    "shear_prolate": (Q(0), Q(5), Q(0), Q(3, 5)),
    "shear_oblate": (Q(0), Q(5), Q(0), Q(-3, 5)),
    "rigid_rotation": (Q(0), Q(-3), Q(3), Q(4, 5)),
    "pure_extension": (Q(2), Q(0), Q(0), Q(3, 5)),
    "mixed_hyperbolic": (Q(1), Q(4), Q(2), Q(4, 5)),
    "parabolic": (Q(0), Q(8), Q(2), Q(3, 5)),
    "sphere_strain": (Q(2), Q(1), Q(1), Q(0)),
    "zero_flow": (Q(0), Q(0), Q(0), Q(3, 5)),
}


def qstr(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def mq(x: Q) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def ds(x: mp.mpf) -> str:
    x = mp.mpf(x)
    if abs(x) < mp.mpf("1e-82"):
        x = mp.mpf(0)
    return mp.nstr(x, 76, strip_zeros=False)


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def b2_exact(a: Q, b: Q, c: Q, lam: Q) -> tuple[tuple[Q, Q], tuple[Q, Q]]:
    k, s = (b - c) / 2, (b + c) / 2
    return ((lam * a, k + lam * s), (-k + lam * s, -lam * a))


def delta_exact(a: Q, b: Q, c: Q, lam: Q) -> Q:
    B = b2_exact(a, b, c, lam)
    return B[0][0] * B[0][0] + B[0][1] * B[1][0]


def regime(delta: Q, B: tuple[tuple[Q, Q], tuple[Q, Q]]) -> str:
    if delta < 0:
        return "elliptic"
    if delta > 0:
        return "hyperbolic"
    if any(x for row in B for x in row):
        return "parabolic_nilpotent"
    return "identity"


def exp2(Bq: tuple[tuple[Q, Q], tuple[Q, Q]], delta: Q, t: mp.mpf) -> mp.matrix:
    B = mp.matrix([[mq(Bq[i][j]) for j in range(2)] for i in range(2)])
    I = mp.eye(2)
    if delta > 0:
        rho = mp.sqrt(mq(delta))
        return mp.cosh(rho * t) * I + mp.sinh(rho * t) / rho * B
    if delta < 0:
        omega = mp.sqrt(-mq(delta))
        return mp.cos(omega * t) * I + mp.sin(omega * t) / omega * B
    return I + t * B


def parameter_rows() -> list[dict]:
    rows: list[dict] = []
    for a0, b0, c0, lam in itertools.product(GRID, GRID, GRID, LAMBDAS):
        a, b, c = Q(a0), Q(b0), Q(c0)
        B = b2_exact(a, b, c, lam)
        delta = delta_exact(a, b, c, lam)
        rank = 0 if not any(x for row in B for x in row) else (2 if delta else 1)
        rows.append({
            "a": qstr(a), "b": qstr(b), "c": qstr(c), "lambda": qstr(lam),
            "strain_shear": qstr((b + c) / 2), "vorticity": qstr((b - c) / 2),
            "B2": [qstr(x) for row in B for x in row], "delta": qstr(delta),
            "regime": regime(delta, B), "rank_B2": rank,
            "projective_fixed_set": (
                "one_vertical_line" if delta < 0 else
                "three_eigenlines" if delta > 0 else
                "projective_kernel_line" if rank == 1 else "all_RP2"
            ),
        })
    return rows


def orbit_rows() -> list[dict]:
    rows: list[dict] = []
    for name, (a, b, c, lam) in CASES.items():
        Bq = b2_exact(a, b, c, lam)
        delta = delta_exact(a, b, c, lam)
        B3 = mp.zeros(3)
        for i in range(2):
            for j in range(2):
                B3[i, j] = mq(Bq[i][j])
        for q in VECTORS:
            qv = mp.matrix([mq(x) for x in q])
            for tq in TIMES:
                t = mq(tq)
                M2 = exp2(Bq, delta, t)
                M3 = mp.eye(3)
                for i in range(2):
                    for j in range(2):
                        M3[i, j] = M2[i, j]
                v = M3 * qv
                nv = mp.sqrt(mp.fdot(v, v))
                p = v / nv
                Bp = B3 * p
                rhs = Bp - mp.fdot(p, Bp) * p
                half = exp2(Bq, delta, t / 2)
                rows.append({
                    "case": name, "q": [qstr(x) for x in q], "t": qstr(tq),
                    "regime": regime(delta, Bq), "delta": qstr(delta),
                    "linear_numerator": [ds(x) for x in v],
                    "director": [ds(x) for x in p], "director_norm": ds(mp.fdot(p, p)),
                    "vector_field": [ds(x) for x in rhs],
                    "det_exp_B2": ds(mp.det(M2)),
                    "semigroup_defect": ds(max(abs((half * half - M2)[i, j]) for i in range(2) for j in range(2))),
                })
    return rows


def shear_rows() -> list[dict]:
    rows = []
    for r in (Q(1, 3), Q(1, 2), Q(1), Q(2), Q(3)):
        for gamma in (Q(1), Q(5)):
            lam = (r * r - 1) / (r * r + 1)
            omega = abs(mq(gamma)) * mq(r) / mq(r * r + 1)
            rows.append({
                "aspect_ratio": qstr(r), "shear_rate": qstr(gamma), "lambda": qstr(lam),
                "omega": ds(omega), "director_equator_period": ds(mp.pi / omega),
                "oriented_or_off_equator_period": ds(2 * mp.pi / omega),
                "period_factor": "for gamma!=0, the equatorial head-tail period is half every nonvertical oriented-vector period; the vertical vector is fixed",
            })
    return rows


def strobe_rows() -> list[dict]:
    # shear_prolate has delta=-4 and omega=2.
    specs = (
        ("pi/8", mp.pi / 8, "vertical_only"),
        ("pi/4", mp.pi / 4, "vertical_only"),
        ("pi/2", mp.pi / 2, "equator_RP1_union_vertical"),
        ("pi", mp.pi, "all_RP2"),
        ("3pi/2", 3 * mp.pi / 2, "equator_RP1_union_vertical"),
    )
    return [{"case": "shear_prolate", "time_label": lab, "time": ds(t), "fixed_set": fixed}
            for lab, t, fixed in specs]


def boundary_rows() -> list[dict]:
    return [
        {"face": "finite_aspect", "condition": "-1<lambda<1", "status": "physical nonspherical spheroid; r=1 uses the marked-material-director convention"},
        {"face": "sphere", "condition": "r=1,lambda=0", "status": "an unmarked sphere has no intrinsic director; a marked material director follows only vorticity"},
        {"face": "rod", "condition": "lambda=1", "status": "singular aspect-ratio limit; simple shear is parabolic"},
        {"face": "disk", "condition": "lambda=-1", "status": "singular aspect-ratio limit; simple shear is parabolic"},
        {"face": "zero_generator", "condition": "B=0", "status": "every director fixed"},
        {"face": "nilpotent", "condition": "delta=0 and B!=0", "status": "P(ker B) fixed; every other orbit converges algebraically to P(im B)"},
    ]


def main() -> None:
    regression = {
        "parameter_rows": parameter_rows(), "orbit_rows": orbit_rows(),
        "shear_rows": shear_rows(), "strobe_rows": strobe_rows(),
        "boundary_rows": boundary_rows(),
    }
    regression["counts"] = {name: len(rows) for name, rows in regression.items()}
    data = {
        "schema": "hcs-c280-jeffery-bretherton-planar-orientation-v1",
        "candidate_id": "HCS-C280", "evaluation_date": "2026-09-01",
        "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Every spheroidal Jeffery director in an incompressible planar linear flow is the projectivization of one traceless matrix exponential, yielding a complete elliptic, hyperbolic, nilpotent, strobe, and aspect-ratio atlas.",
        "evaluator": {"version": "0.2.0", "sha256": EVAL},
        "model_contract": {
            "state": "head-tail director [p] in RP2; unit representatives are gauge only",
            "flow_gradient": "L=diag([[a,b],[c,-a]],0)",
            "shape": "lambda=(r^2-1)/(r^2+1), r>0, hence -1<lambda<1",
            "sphere_convention": "at r=1 an unmarked sphere has no intrinsic shape director; RP2 is retained only for a marked material director",
            "equation": "p_dot=W p+lambda(E p-(p^T E p)p)",
            "linear_owner": "B=W+lambda E and [p(t)]=[exp(tB)q0]",
            "clock": "physical time",
        },
        "classification_contract": {
            "invariant": "delta=lambda^2*(a^2+((b+c)/2)^2)-((b-c)/2)^2=-det(B2)",
            "elliptic": "delta<0: vertical fixed; equator director period pi/sqrt(-delta); every mixed director period 2*pi/sqrt(-delta)",
            "hyperbolic": "delta>0: exactly three eigen-directors; Ws([e0]) is P(span(e0,v_-)) without [v_-], Wu([e0]) is P(span(e0,v_+)) without [v_+], and their closures are RP1 projective lines",
            "parabolic": "delta=0,B2!=0: P(ker B) is a fixed RP1 and every other orbit converges algebraically to the horizontal kernel/image line",
            "identity": "B2=0: every point of RP2 is fixed",
            "strobe": "elliptic non-half strobes fix only vertical; odd half-period fixes equator union vertical; full period fixes all RP2",
        },
        "simple_shear_contract": {
            "L2": "[[0,gamma],[0,0]]", "omega": "abs(gamma)*r/(r^2+1)",
            "domain": "gamma!=0 for period formulas; gamma=0 is the identity flow",
            "director_period": "pi*(r+r^(-1))/abs(gamma) on the equator for gamma!=0",
            "oriented_period": "2*pi*(r+r^(-1))/abs(gamma) for every nonvertical oriented vector; also the mixed-director RP2 period",
            "vertical_boundary": "the vertical oriented vector is fixed",
        },
        "proof_contract": {
            "status": "PROVABLE AS STATED",
            "dependencies": ["projective linearization", "traceless two-by-two Cayley-Hamilton identity", "real projective eigenspace geometry"],
            "scope": "axisymmetric spheroidal passive director in a prescribed steady incompressible planar linear flow; no Brownian rotation, inertia, particle interaction, or spatial transport",
            "novelty_boundary": "the package proves a frozen all-parameter synthesis and does not claim invention of Jeffery's equation or literature priority",
        },
        "analytic_proof_obligations": [
            "derive the normalized projective solution from the linear equation", "prove B2^2=delta I and classify every sign",
            "prove true RP2 minimal periods and all strobe fixed sets", "classify the hyperbolic RP1 stable and unstable manifolds with endpoint exclusions",
            "prove the nilpotent fixed line and algebraic limit", "recover the gamma!=0 director and nonvertical oriented-vector shear periods",
            "separate finite aspect ratios from rod and disk limits and mark the r=1 material-director convention",
        ],
        "regression": regression,
        "route_a": {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {
            "arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
            "automorphy": False, "target_divisor_or_counting_law": False,
            "target_functional_equation": False, "target_zero_match": False,
            "hilbert_polya_operator": False, "route_b_authorization": False,
        },
        "nonclaims": [
            "No rational-prime carrier, logarithmic prime clock, target determinant, or target zero match is obtained.",
            "Elliptic periodic points form clean continua rather than isolated primitive orbits.",
            "The prescribed-flow orientation model does not solve fluid-particle coupling or noisy suspension dynamics.",
            "Finite regression rows are not a proof of the all-real-parameter theorem.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C280_PRODUCER_PASS", "counts": regression["counts"],
                      "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
