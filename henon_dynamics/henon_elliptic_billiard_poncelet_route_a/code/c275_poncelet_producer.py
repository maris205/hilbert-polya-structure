#!/usr/bin/env python3
"""Deterministic high-precision certificate for HCS-C275."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from math import gcd
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C275_OUTPUT_PATH", ROOT / "results/c275_poncelet_evidence.json"))
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90


def mq(value: Q) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def qs(value: Q) -> str:
    return f"{value.numerator}/{value.denominator}"


def ds(value: mp.mpf) -> str:
    if abs(value) < mp.mpf("1e-80"):
        value = mp.mpf(0)
    return mp.nstr(value, 72, strip_zeros=False)


def payload_hash(data: dict) -> str:
    copy = dict(data)
    copy.pop("payload_sha256", None)
    raw = json.dumps(copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def rotation(e: mp.mpf, f: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    modulus_parameter = e * e
    complete = mp.ellipk(modulus_parameter)
    omega = mp.asin(mp.sqrt((e * e - f * f) / (e * e * (1 - f * f))))
    incomplete = mp.ellipf(omega, modulus_parameter)
    return incomplete / (2 * complete), omega, incomplete, complete


def point(e: mp.mpf, f: mp.mpf, theta: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    complete = mp.ellipk(e * e)
    u = 4 * complete * theta
    sn = mp.ellipfun("sn", u, e * e)
    cn = mp.ellipfun("cn", u, e * e)
    return -sn / f, mp.sqrt(1 - f * f) * cn / f


def outer_residual(f: mp.mpf, z: tuple[mp.mpf, mp.mpf]) -> mp.mpf:
    x, y = z
    return f * f * x * x + f * f * y * y / (1 - f * f) - 1


def tangent_residual(
    e: mp.mpf, z0: tuple[mp.mpf, mp.mpf], z1: tuple[mp.mpf, mp.mpf]
) -> mp.mpf:
    x0, y0 = z0
    x1, y1 = z1
    aa = y0 - y1
    bb = x1 - x0
    cc = x0 * y1 - x1 * y0
    raw = cc * cc - aa * aa / (e * e) - bb * bb * (1 - e * e) / (e * e)
    scale = max(
        mp.mpf(1), abs(cc * cc), abs(aa * aa / (e * e)),
        abs(bb * bb * (1 - e * e) / (e * e)),
    )
    return raw / scale


def cd(u: mp.mpf, e: mp.mpf) -> mp.mpf:
    return mp.ellipfun("cn", u, e * e) / mp.ellipfun("dn", u, e * e)


def main() -> None:
    eccentricities = (
        Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3),
        Q(3, 4), Q(4, 5), Q(9, 10), Q(19, 20),
    )
    ratios = (Q(1, 5), Q(2, 5), Q(3, 5), Q(4, 5))
    theta_grid = (Q(0), Q(1, 13), Q(2, 13), Q(5, 13), Q(8, 13), Q(12, 13))

    formula_cells = []
    covering_cells = []
    for e_q in eccentricities:
        e = mq(e_q)
        for ratio_q in ratios:
            f_q = e_q * ratio_q
            f = mq(f_q)
            rho, omega, incomplete, complete = rotation(e, f)
            assert 0 < omega < mp.pi / 2 and 0 < rho < mp.mpf(1) / 2
            formula_cells.append({
                "e": qs(e_q), "f": qs(f_q), "f_over_e": qs(ratio_q),
                "omega": ds(omega), "F_omega_e": ds(incomplete),
                "K_e": ds(complete), "rho": ds(rho),
            })
            for theta_q in theta_grid:
                theta = mq(theta_q)
                z0 = point(e, f, theta)
                z1 = point(e, f, theta + rho)
                deck = point(e, f, theta + 1)
                r0 = outer_residual(f, z0)
                r1 = outer_residual(f, z1)
                tangency = tangent_residual(e, z0, z1)
                deck_error = max(abs(deck[0] - z0[0]), abs(deck[1] - z0[1]))
                assert max(abs(r0), abs(r1), abs(tangency), deck_error) < mp.mpf("1e-75")
                covering_cells.append({
                    "e": qs(e_q), "f": qs(f_q), "theta": qs(theta_q),
                    "next_theta": ds(theta + rho),
                    "point": [ds(z0[0]), ds(z0[1])],
                    "next_point": [ds(z1[0]), ds(z1[1])],
                    "outer_residual": ds(r0),
                    "next_outer_residual": ds(r1),
                    "caustic_tangency_relative_residual": ds(tangency),
                    "deck_period_error": ds(deck_error),
                })

    monotonic_f = []
    for e_q in eccentricities:
        e = mq(e_q)
        values = []
        for j in range(1, 10):
            f_q = e_q * Q(j, 10)
            rho = rotation(e, mq(f_q))[0]
            values.append({"f": qs(f_q), "rho": ds(rho)})
        assert all(mp.mpf(values[j]["rho"]) > mp.mpf(values[j + 1]["rho"])
                   for j in range(len(values) - 1))
        monotonic_f.append({"fixed_e": qs(e_q), "direction": "strictly_decreasing_in_f",
                            "values": values})

    monotonic_e = []
    fixed_f_values = (Q(1, 10), Q(1, 5), Q(1, 3), Q(1, 2), Q(3, 4))
    for f_q in fixed_f_values:
        f = mq(f_q)
        values = []
        for j in range(1, 10):
            e_q = f_q + (1 - f_q) * Q(j, 10)
            rho = rotation(mq(e_q), f)[0]
            values.append({"e": qs(e_q), "rho": ds(rho)})
        assert all(mp.mpf(values[j]["rho"]) < mp.mpf(values[j + 1]["rho"])
                   for j in range(len(values) - 1))
        monotonic_e.append({"fixed_f": qs(f_q), "direction": "strictly_increasing_in_e",
                            "values": values})

    endpoint_paths = []

    def add_endpoint_path(path: str, fixed_name: str, fixed_q: Q, items: list[dict]) -> None:
        errors = [mp.mpf(item["error_to_limit"]) for item in items]
        assert all(errors[j + 1] < errors[j] for j in range(len(errors) - 1))
        endpoint_paths.append({
            "path": path, fixed_name: qs(fixed_q), "limit": items[0]["limit"], "values": items,
        })

    for e_q in (Q(1, 3), Q(2, 3), Q(9, 10)):
        e = mq(e_q)
        coalescing = []
        vanishing_outer_eccentricity = []
        for k in range(2, 10):
            f_near_q = e_q * (1 - Q(1, 2**k))
            r_near = rotation(e, mq(f_near_q))[0]
            coalescing.append({"k": k, "e": qs(e_q), "f": qs(f_near_q),
                               "rho": ds(r_near), "limit": "0",
                               "error_to_limit": ds(r_near)})
            f_zero_q = e_q * Q(1, 2**k)
            r_half = rotation(e, mq(f_zero_q))[0]
            vanishing_outer_eccentricity.append({
                "k": k, "e": qs(e_q), "f": qs(f_zero_q), "rho": ds(r_half),
                "limit": "1/2", "error_to_limit": ds(mp.mpf(1) / 2 - r_half),
            })
        add_endpoint_path("f_to_e_minus", "fixed_e", e_q, coalescing)
        add_endpoint_path("f_to_zero_plus", "fixed_e", e_q, vanishing_outer_eccentricity)

    for f_q in (Q(1, 10), Q(1, 3), Q(2, 3)):
        f = mq(f_q)
        coalescing = []
        segment_caustic = []
        for k in range(2, 10):
            e_near_q = f_q + (1 - f_q) * Q(1, 2**k)
            r_near = rotation(mq(e_near_q), f)[0]
            coalescing.append({"k": k, "e": qs(e_near_q), "f": qs(f_q),
                               "rho": ds(r_near), "limit": "0",
                               "error_to_limit": ds(r_near)})
            e_one_q = 1 - (1 - f_q) * Q(1, 2**k)
            r_half = rotation(mq(e_one_q), f)[0]
            segment_caustic.append({
                "k": k, "e": qs(e_one_q), "f": qs(f_q), "rho": ds(r_half),
                "limit": "1/2", "error_to_limit": ds(mp.mpf(1) / 2 - r_half),
            })
        add_endpoint_path("e_to_f_plus", "fixed_f", f_q, coalescing)
        add_endpoint_path("e_to_one_minus", "fixed_f", f_q, segment_caustic)

    porism_cases = []
    rational_rotations = ((1, 5), (1, 4), (1, 3), (2, 5), (2, 7), (3, 8))
    porism_e_values = (Q(1, 4), Q(1, 2), Q(3, 4), Q(9, 10))
    porism_vertex_cells = 0
    for p, q in rational_rotations:
        assert gcd(p, q) == 1 and 0 < 2 * p < q
        ell = mp.mpf(p) / q
        for e_q in porism_e_values:
            e = mq(e_q)
            complete = mp.ellipk(e * e)
            f = e * cd(2 * complete * ell, e)
            recovered = rotation(e, f)[0]
            assert 0 < f < e and abs(recovered - ell) < mp.mpf("1e-75")
            theta0 = mp.mpf(1) / 37
            vertices = []
            max_outer = mp.mpf(0)
            max_tangent = mp.mpf(0)
            for j in range(q):
                theta = theta0 + j * ell
                z0 = point(e, f, theta)
                z1 = point(e, f, theta + ell)
                out = abs(outer_residual(f, z0))
                tangent = abs(tangent_residual(e, z0, z1))
                max_outer = max(max_outer, out)
                max_tangent = max(max_tangent, tangent)
                vertices.append({"j": j, "theta": ds(theta), "x": ds(z0[0]), "y": ds(z0[1])})
            closure = point(e, f, theta0 + q * ell)
            start = point(e, f, theta0)
            closure_error = max(abs(closure[0] - start[0]), abs(closure[1] - start[1]))
            assert max(max_outer, max_tangent, closure_error) < mp.mpf("1e-74")
            assert all((k * p) % q != 0 for k in range(1, q))
            porism_vertex_cells += q
            porism_cases.append({
                "p": p, "q": q, "e": qs(e_q), "f": ds(f),
                "rho_recovered": ds(recovered), "q_rho": ds(q * recovered),
                "minimal_period": q, "tangent_q_return_derivative": "1",
                "restricted_q_return": "identity_on_the_entire_elliptic_caustic_curve",
                "periodic_orbit_family": "one_parameter_circle_quotient",
                "isolated_orbit_product_applicable": False,
                "ambient_unipotent_conclusion": False,
                "max_outer_residual": ds(max_outer),
                "max_caustic_tangency_relative_residual": ds(max_tangent),
                "closure_error": ds(closure_error), "vertices": vertices,
            })

    counts = {
        "formula_cells": len(formula_cells),
        "covering_cells": len(covering_cells),
        "monotonicity_values": sum(len(row["values"]) for row in monotonic_f + monotonic_e),
        "endpoint_values": sum(len(row["values"]) for row in endpoint_paths),
        "porism_cases": len(porism_cases),
        "porism_vertex_cells": porism_vertex_cells,
        "return_derivative_cells": len(porism_cases),
    }
    assert counts == {
        "formula_cells": 32, "covering_cells": 192, "monotonicity_values": 117,
        "endpoint_values": 96, "porism_cases": 24, "porism_vertex_cells": 128,
        "return_derivative_cells": 24,
    }

    data = {
        "schema": "hcs-c275-elliptic-billiard-poncelet-v1",
        "candidate_id": "HCS-C275",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0", "sha256": EVALUATOR,
        },
        "owner": {
            "phase_space": "positive-orientation elliptic-caustic invariant curves of the billiard in E(f)",
            "outer_boundary": "E(f): f^2 x^2 + f^2 y^2/(1-f^2)=1",
            "caustic": "confocal inner ellipse E(e)",
            "parameter_domain": "0<f<e<1",
            "clock": "one billiard reflection",
            "normalization": "Jacobi modulus e and circle coordinate theta mod 1",
            "excluded_sector": "hyperbolic caustics and their non-Birkhoff atlas",
        },
        "theorem_contract": {
            "covering": "pi_e^f(theta)=f^{-1}(-sn(4K(e)theta,e),sqrt(1-f^2)cn(4K(e)theta,e))",
            "rigid_rotation": "B_e^f composed with pi_e^f equals pi_e^f composed with (theta maps to theta+rho)",
            "rotation_number": "rho=F(omega,e)/(2K(e)), omega=asin sqrt((e^2-f^2)/(e^2(1-f^2)))",
            "strict_monotonicity": "partial_e rho>0 and partial_f rho<0 on 0<f<e<1",
            "endpoints": "rho tends to 0 on e=f and to 1/2 on either f=0 or e=1",
            "porism": "rho=p/q reduced implies every point has minimal period q",
            "clean_family": "the q-th restricted return is the identity with unit tangent derivative on a one-parameter family",
            "sector_firewall": "no conclusion is asserted for hyperbolic caustics or ambient Jordan type",
        },
        "proof_obligations": [
            "Jacobi covering and exact rigid-rotation conjugacy",
            "rotation formula with the modulus convention fixed",
            "strict monotonicity in both eccentricities and all four boundary paths",
            "reduced rational rotation implies common minimal period",
            "restricted unit derivative and periodic-family obstruction without ambient unipotence",
            "elliptic-caustic sector and Route-A claim firewalls",
            "A4 clock and orbit-phase gates for the ambient Dirichlet quantum billiard",
        ],
        "regression": {
            "counts": counts,
            "formula_cells": formula_cells,
            "covering_cells": covering_cells,
            "monotonicity_in_f": monotonic_f,
            "monotonicity_in_e": monotonic_e,
            "endpoint_paths": endpoint_paths,
            "porism_cases": porism_cases,
        },
        "sources": [
            {
                "author": "H. E. Lomeli and J. D. Meiss",
                "title": "Symmetry Reduction and Rotation Numbers for Poncelet maps",
                "identifier": "arXiv:2309.08013v1",
                "doi": "10.48550/arXiv.2309.08013",
                "role": "covering, rotation formula, monotonicity, endpoints, porisms",
                "verified_at": "official arXiv record and PDF on 2026-09-01",
            },
            {
                "author": "Shau-Jin Chang and Richard Friedberg",
                "title": "Elliptical billiards and Poncelet's theorem",
                "journal": "Journal of Mathematical Physics 29 (1988), 1537-1550",
                "doi": "10.1063/1.527900",
                "role": "classical elliptic-billiard Poncelet closure theorem",
            },
            {
                "author": "Rafal Kolodziej",
                "title": "The rotation number of some transformation related to billiards in an ellipse",
                "journal": "Studia Mathematica 81 (1985), 293-302",
                "doi": "10.4064/sm-81-3-293-302",
                "role": "primary rotation-number antecedent",
            },
        ],
        "a4_liftability": {
            "classification": "A4_FORMAL_HINT",
            "ambient_quantum_owner": {
                "domain_geometry": "Omega_f is the smooth bounded interior of E(f)",
                "hilbert_space": "L^2(Omega_f)",
                "operator": "-Delta_D",
                "operator_domain": "H^2(Omega_f) cap H_0^1(Omega_f)",
                "self_adjoint": True,
                "compact_resolvent": True,
                "unitary_group": "U(t)=exp(-it(-Delta_D))",
                "time_parameter": "continuous physical flight time",
                "antiunitary_time_reversal": (
                    "C is complex conjugation; C U(t) C=U(-t)"
                ),
            },
            "classical_owner_clock": "one billiard reflection",
            "coherent_ambient_quantization": True,
            "same_clock_quantum_return_constructed": False,
            "fixed_caustic_orbit_phases_weights_preserved": False,
            "target_identification": False,
            "gate_reason": (
                "the ambient Dirichlet unitary uses continuous physical flight time, "
                "whereas the frozen owner is the one-reflection Poincare map; no "
                "same-clock quantum return or fixed-caustic phase/weight bridge is proved"
            ),
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data": False, "automorphy": False,
            "euler_factors": False, "functional_equation": False,
            "hilbert_polya_operator": False, "root_numbers": False,
            "target_divisor": False,
        },
        "nonclaims": [
            "Workspace ownership is not a literature-priority claim.",
            "The theorem covers only positive-orientation elliptic caustics, not hyperbolic caustics.",
            "Unit tangent derivative of the restricted q-th return is not an ambient unipotent or Jordan-form claim.",
            "The ambient Dirichlet quantum billiard is only an A4 formal hint: no same-clock quantum return, fixed-caustic phase/weight bridge, or target Hilbert-Polya identification is proved.",
            "The one-parameter Poncelet family is not promoted to an isolated-orbit Euler product.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        "C275_PRODUCER_PASS "
        f"covering={counts['covering_cells']} porism_vertices={porism_vertex_cells} "
        f"payload={data['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
