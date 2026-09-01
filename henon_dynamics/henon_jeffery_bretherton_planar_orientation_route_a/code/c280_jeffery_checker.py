#!/usr/bin/env python3
"""Producer-independent checker for HCS-C280."""
from __future__ import annotations

import hashlib
import itertools
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path(os.environ.get("C280_EVIDENCE", ROOT / "results/c280_jeffery_evidence.json"))
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
mp.mp.dps = 90
checks = 0


def claim(value: bool) -> None:
    global checks
    assert value
    checks += 1


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def fq(text: str) -> Q:
    return Q(text)


def close(text: str, value: mp.mpf, tol: str = "1e-65") -> bool:
    return abs(mp.mpf(text) - value) <= mp.mpf(tol) * max(1, abs(value))


def matrix_data(a: Q, b: Q, c: Q, lam: Q):
    vort, shear = (b - c) / 2, (b + c) / 2
    B = ((lam * a, vort + lam * shear), (-vort + lam * shear, -lam * a))
    delta = B[0][0] ** 2 + B[0][1] * B[1][0]
    return B, delta


def exponential(Bq, delta: Q, t: mp.mpf) -> mp.matrix:
    B = mp.matrix([[mp.mpf(x.numerator) / x.denominator for x in row] for row in Bq])
    if delta > 0:
        d = mp.sqrt(mp.mpf(delta.numerator) / delta.denominator)
        return mp.cosh(d*t)*mp.eye(2) + mp.sinh(d*t)/d*B
    if delta < 0:
        d = mp.sqrt(mp.mpf(-delta.numerator) / delta.denominator)
        return mp.cos(d*t)*mp.eye(2) + mp.sin(d*t)/d*B
    return mp.eye(2) + t*B


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    claim(data["payload_sha256"] == payload_hash(data))
    claim(data["schema"] == "hcs-c280-jeffery-bretherton-planar-orientation-v1")
    claim(data["candidate_id"] == "HCS-C280" and data["source_commit"] == SOURCE)
    claim(data["evaluation_date"] == "2026-09-01" and data["fixed_epoch"] == 1788220800)
    claim(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    claim(data["evaluator"] == {"version": "0.2.0", "sha256": EVAL})
    claim(data["proof_contract"]["status"] == "PROVABLE AS STATED")
    claim(data["route_a"] == {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                               "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False})
    claim(all(v is False for v in data["scope_flags"].values()))
    claim(data["model_contract"]["sphere_convention"] ==
          "at r=1 an unmarked sphere has no intrinsic shape director; RP2 is retained only for a marked material director")
    claim(data["classification_contract"]["hyperbolic"] ==
          "delta>0: exactly three eigen-directors; Ws([e0]) is P(span(e0,v_-)) without [v_-], Wu([e0]) is P(span(e0,v_+)) without [v_+], and their closures are RP1 projective lines")
    claim(data["simple_shear_contract"]["domain"] ==
          "gamma!=0 for period formulas; gamma=0 is the identity flow")
    claim(data["simple_shear_contract"]["oriented_period"] ==
          "2*pi*(r+r^(-1))/abs(gamma) for every nonvertical oriented vector; also the mixed-director RP2 period")

    rows = data["regression"]["parameter_rows"]
    claim(len(rows) == 625)
    grid = tuple(Q(i) for i in range(-2, 3))
    expected_keys = set(itertools.product(grid, grid, grid,
                                          (Q(-4, 5), Q(-3, 5), Q(0), Q(3, 5), Q(4, 5))))
    seen = set()
    for row in rows:
        a, b, c, lam = (fq(row[x]) for x in ("a", "b", "c", "lambda"))
        seen.add((a, b, c, lam))
        B, delta = matrix_data(a, b, c, lam)
        claim([fq(x) for x in row["B2"]] == [x for pair in B for x in pair])
        claim(fq(row["delta"]) == delta)
        claim(fq(row["strain_shear"]) == (b+c)/2 and fq(row["vorticity"]) == (b-c)/2)
        rank = 0 if not any(x for pair in B for x in pair) else (2 if delta else 1)
        claim(row["rank_B2"] == rank)
        expected_regime = "elliptic" if delta < 0 else "hyperbolic" if delta > 0 else "parabolic_nilpotent" if rank else "identity"
        claim(row["regime"] == expected_regime)
        fixed = "one_vertical_line" if delta < 0 else "three_eigenlines" if delta > 0 else "projective_kernel_line" if rank else "all_RP2"
        claim(row["projective_fixed_set"] == fixed)
    claim(seen == expected_keys)

    case_values = {
        "shear_prolate": (Q(0), Q(5), Q(0), Q(3, 5)), "shear_oblate": (Q(0), Q(5), Q(0), Q(-3, 5)),
        "rigid_rotation": (Q(0), Q(-3), Q(3), Q(4, 5)), "pure_extension": (Q(2), Q(0), Q(0), Q(3, 5)),
        "mixed_hyperbolic": (Q(1), Q(4), Q(2), Q(4, 5)), "parabolic": (Q(0), Q(8), Q(2), Q(3, 5)),
        "sphere_strain": (Q(2), Q(1), Q(1), Q(0)), "zero_flow": (Q(0), Q(0), Q(0), Q(3, 5)),
    }
    orbit_rows = data["regression"]["orbit_rows"]
    claim(len(orbit_rows) == 320)
    vector_values = (
        (Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(1)),
        (Q(1), Q(1), Q(0)), (Q(1), Q(-1), Q(0)), (Q(1), Q(0), Q(1)),
        (Q(0), Q(1), Q(1)), (Q(1), Q(2), Q(3)), (Q(-2), Q(1), Q(1)),
        (Q(3), Q(-1), Q(2)),
    )
    time_values = (Q(1, 7), Q(2, 5), Q(1), Q(3, 2))
    expected_orbit_keys = set(itertools.product(case_values, vector_values, time_values))
    seen_orbits = set()
    for row in orbit_rows:
        a, b, c, lam = case_values[row["case"]]
        Bq, delta = matrix_data(a, b, c, lam)
        tq = fq(row["t"])
        t = mp.mpf(tq.numerator) / tq.denominator
        q = [fq(x) for x in row["q"]]
        seen_orbits.add((row["case"], tuple(q), tq))
        qv = mp.matrix([mp.mpf(x.numerator) / x.denominator for x in q])
        M2 = exponential(Bq, delta, t)
        M3 = mp.eye(3)
        B3 = mp.zeros(3)
        for i in range(2):
            for j in range(2):
                M3[i, j] = M2[i, j]
                B3[i, j] = mp.mpf(Bq[i][j].numerator) / Bq[i][j].denominator
        v = M3*qv
        p = v/mp.sqrt(mp.fdot(v, v))
        rhs = B3*p-mp.fdot(p, B3*p)*p
        for got, want in zip(row["linear_numerator"], v): claim(close(got, want))
        for got, want in zip(row["director"], p): claim(close(got, want))
        for got, want in zip(row["vector_field"], rhs): claim(close(got, want))
        claim(close(row["director_norm"], mp.mpf(1)))
        claim(close(row["det_exp_B2"], mp.mpf(1)))
        claim(abs(mp.mpf(row["semigroup_defect"])) < mp.mpf("1e-65"))
        claim(fq(row["delta"]) == delta)
        rank = 0 if not any(x for pair in Bq for x in pair) else (2 if delta else 1)
        expected_regime = "elliptic" if delta < 0 else "hyperbolic" if delta > 0 else "parabolic_nilpotent" if rank else "identity"
        claim(row["regime"] == expected_regime)
    claim(seen_orbits == expected_orbit_keys)

    shear = data["regression"]["shear_rows"]
    claim(len(shear) == 10)
    expected_shear_keys = set(itertools.product((Q(1, 3), Q(1, 2), Q(1), Q(2), Q(3)), (Q(1), Q(5))))
    seen_shear = set()
    for row in shear:
        r, gamma, lam = fq(row["aspect_ratio"]), fq(row["shear_rate"]), fq(row["lambda"])
        seen_shear.add((r, gamma))
        claim(gamma != 0)
        claim(lam == (r*r-1)/(r*r+1))
        rm = mp.mpf(r.numerator)/r.denominator
        gm = abs(mp.mpf(gamma.numerator)/gamma.denominator)
        omega = gm*rm/(rm*rm+1)
        claim(close(row["omega"], omega))
        claim(close(row["director_equator_period"], mp.pi/omega))
        claim(close(row["oriented_or_off_equator_period"], 2*mp.pi/omega))
        claim(row["period_factor"] ==
              "for gamma!=0, the equatorial head-tail period is half every nonvertical oriented-vector period; the vertical vector is fixed")
    claim(seen_shear == expected_shear_keys)

    strobes = data["regression"]["strobe_rows"]
    claim(len(strobes) == 5)
    expected_strobes = {
        ("shear_prolate", "pi/8"): (mp.pi/8, "vertical_only"),
        ("shear_prolate", "pi/4"): (mp.pi/4, "vertical_only"),
        ("shear_prolate", "pi/2"): (mp.pi/2, "equator_RP1_union_vertical"),
        ("shear_prolate", "pi"): (mp.pi, "all_RP2"),
        ("shear_prolate", "3pi/2"): (3*mp.pi/2, "equator_RP1_union_vertical"),
    }
    seen_strobes = set()
    for row in strobes:
        key = (row["case"], row["time_label"])
        claim(key in expected_strobes)
        seen_strobes.add(key)
        want_time, want_fixed = expected_strobes[key]
        claim(close(row["time"], want_time))
        claim(row["fixed_set"] == want_fixed)
    claim(seen_strobes == set(expected_strobes))

    expected_boundaries = [
        {"face": "finite_aspect", "condition": "-1<lambda<1", "status": "physical nonspherical spheroid; r=1 uses the marked-material-director convention"},
        {"face": "sphere", "condition": "r=1,lambda=0", "status": "an unmarked sphere has no intrinsic director; a marked material director follows only vorticity"},
        {"face": "rod", "condition": "lambda=1", "status": "singular aspect-ratio limit; simple shear is parabolic"},
        {"face": "disk", "condition": "lambda=-1", "status": "singular aspect-ratio limit; simple shear is parabolic"},
        {"face": "zero_generator", "condition": "B=0", "status": "every director fixed"},
        {"face": "nilpotent", "condition": "delta=0 and B!=0", "status": "P(ker B) fixed; every other orbit converges algebraically to P(im B)"},
    ]
    claim(data["regression"]["boundary_rows"] == expected_boundaries)
    claim(data["regression"]["counts"] == {"parameter_rows": 625, "orbit_rows": 320, "shear_rows": 10, "strobe_rows": 5, "boundary_rows": 6})
    print(f"C280 independent checker: PASS ({checks} assertions; producer-independent reconstruction)")


if __name__ == "__main__":
    main()
