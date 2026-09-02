#!/usr/bin/env python3
"""Produce the canonical exact/regression certificate for HCS-C303."""
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c303_thermal_qubit_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C303/2026-09-02.yaml"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]


def f(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def char_coefficients(gd: Fraction, gu: Fraction, gp: Fraction, w: Fraction) -> list[str]:
    g1 = gd + gu
    g2 = g1 / 2 + gp
    c = g2 * g2 + w * w
    return [f(Fraction(1)), f(2 * g2 + g1), f(c + 2 * g1 * g2), f(g1 * c), f(Fraction(0))]


def threshold(p_num: int, p_den: int, q: int) -> dict:
    getcontext().prec = 100
    p = Decimal(p_num) / Decimal(p_den)
    r = p * (Decimal(1) - p)
    lo, hi = Decimal(0), Decimal(1)
    for _ in range(240):
        mid = (lo + hi) / 2
        value = r * (1 - mid) ** 2 - mid ** q
        if value > 0:
            lo = mid
        else:
            hi = mid
    eta = (lo + hi) / 2
    residual = r * (1 - eta) ** 2 - eta ** q
    return {
        "p": f(Fraction(p_num, p_den)),
        "q": q,
        "eta_lower": format(lo, ".80e"),
        "eta_upper": format(hi, ".80e"),
        "eta_mid": format(eta, ".80e"),
        "dimensionless_Gamma1_t": format(-eta.ln(), ".80e"),
        "residual_abs_bound": format(abs(residual), ".12e"),
    }


def main() -> None:
    choi_rows = []
    for p in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]:
        for eta in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]:
            for q in [1, 2, 3]:
                a = 1 - p * (1 - eta)
                b = p * (1 - eta)
                d = (1 - p) * (1 - eta)
                e = eta + p * (1 - eta)
                k = eta ** q
                cp_delta = a * e - k
                ppt_delta = b * d - k
                choi_rows.append({
                    "p": f(p), "eta": f(eta), "q": q,
                    "a": f(a), "b": f(b), "d": f(d), "e": f(e),
                    "coherence_abs_squared": f(k),
                    "choi_corner_minor": f(cp_delta),
                    "ppt_middle_minor": f(ppt_delta),
                    "choi_positive": cp_delta >= 0,
                    "entanglement_breaking": ppt_delta >= 0,
                })

    rate_cases = [
        (0, 0, 0, 0), (0, 0, 1, 0), (0, 0, 1, 2),
        (1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0),
        (3, 1, 2, 1), (2, 1, 3, -2), (1, 3, 0, 4),
        (5, 2, 1, 0), (2, 5, 7, 3), (4, 4, 2, -5),
    ]
    liouvillian_rows = []
    for gd_i, gu_i, gp_i, w_i in rate_cases:
        gd, gu, gp, w = map(Fraction, (gd_i, gu_i, gp_i, w_i))
        g1, g2 = gd + gu, (gd + gu) / 2 + gp
        liouvillian_rows.append({
            "gamma_down": f(gd), "gamma_up": f(gu), "gamma_phi": f(gp), "omega": f(w),
            "Gamma1": f(g1), "Gamma2": f(g2),
            "characteristic_coefficients_descending": char_coefficients(gd, gu, gp, w),
            "diagonalizable": True,
            "stationary_dimension": (4 if g1 == 0 and gp == 0 and w == 0 else (2 if g1 == 0 else 1)),
        })

    trace_rows = []
    for gd_i, gu_i, gp_i in [(1, 0, 0), (0, 1, 0), (1, 1, 0), (3, 1, 0), (3, 1, 1),
                              (3, 1, 2), (3, 1, 4), (2, 5, 0), (2, 5, 2), (2, 5, 7)]:
        gd, gu, gp = map(Fraction, (gd_i, gu_i, gp_i))
        g1, g2 = gd + gu, (gd + gu) / 2 + gp
        trace_rows.append({
            "gamma_down": f(gd), "gamma_up": f(gu), "gamma_phi": f(gp),
            "Gamma1": f(g1), "Gamma2": f(g2),
            "winning_axis": "transverse" if g2 < g1 else ("longitudinal" if g1 < g2 else "tie"),
            "coefficient_formula": "max(exp(-Gamma1*t),exp(-Gamma2*t))",
            "strict_for_positive_t": True,
        })

    semigroup_rows = []
    for p in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1)]:
        for eta1, eta2 in [(Fraction(1, 2), Fraction(1, 3)), (Fraction(3, 4), Fraction(2, 5)), (Fraction(1), Fraction(1, 7))]:
            semigroup_rows.append({
                "p": f(p), "eta1": f(eta1), "eta2": f(eta2),
                "eta_composed": f(eta1 * eta2),
                "translation_composed": f(p * (1 - eta1 * eta2)),
                "translation_two_step": f(p * (1 - eta2) + eta2 * p * (1 - eta1)),
            })

    thresholds = [threshold(*args) for args in [
        (1, 2, 1), (1, 4, 1), (1, 3, 1), (1, 2, 2),
        (1, 4, 2), (1, 3, 3), (2, 5, 4), (1, 2, 5),
    ]]

    scope_flags = {
        "claims_target_arithmetic_local_data": False,
        "claims_target_euler_factors": False,
        "claims_root_number": False,
        "claims_automorphy": False,
        "claims_target_divisor_or_counting_law": False,
        "claims_target_functional_equation": False,
        "claims_target_zero_match": False,
        "claims_hilbert_polya_operator": False,
        "invokes_route_b": False,
    }
    nonclaims = [
        "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
        "Liouvillian eigenvalues and Choi determinants are finite-dimensional source data, not prime norms or target spectral zeros.",
        "The dissipative GKSL generator is not asserted to be a Hilbert--Polya operator.",
        "No priority claim is made for GKSL, Choi, PPT, or entanglement-breaking channel theory.",
    ]
    boundaries = [
        {"face": "Gamma1>0 and 0<p<1", "stationary": "unique faithful thermal state", "finite_EB": True, "recurrence": "fixed point only"},
        {"face": "Gamma1>0 and p=0", "stationary": "unique pure ground state", "finite_EB": False, "recurrence": "fixed point only"},
        {"face": "Gamma1>0 and p=1", "stationary": "unique pure excited state", "finite_EB": False, "recurrence": "fixed point only"},
        {"face": "Gamma1=0 and gamma_phi>0", "stationary": "all diagonal states", "finite_EB": False, "recurrence": "fixed states only"},
        {"face": "Gamma1=0, gamma_phi=0, omega!=0", "stationary": "all diagonal states", "finite_EB": False, "recurrence": "periodic off-diagonal states"},
        {"face": "Gamma1=0, gamma_phi=0, omega=0", "stationary": "every state", "finite_EB": False, "recurrence": "identity dynamics"},
        {"face": "t=infinity on p endpoints or pure dephasing", "stationary": "limiting channel depends on face", "finite_EB": False, "recurrence": "limiting channel is EB"},
    ]
    references = [
        {"identifier": "10.1063/1.522979", "owner": "Gorini--Kossakowski--Sudarshan (1976)", "role": "finite-dimensional quantum dynamical semigroup generators"},
        {"identifier": "10.1007/BF01608499", "owner": "Lindblad (1976)", "role": "completely positive semigroup generators"},
        {"identifier": "10.1016/0024-3795(75)90075-0", "owner": "Choi (1975)", "role": "complete positivity matrix criterion"},
        {"identifier": "10.1142/S0129055X03001709", "owner": "Horodecki--Shor--Ruskai (2003)", "role": "entanglement-breaking channels"},
        {"identifier": "10.1016/S0375-9601(96)00706-2", "owner": "Horodecki--Horodecki--Horodecki (1996)", "role": "PPT separability in two-by-two systems"},
    ]
    collision = {
        "C223": "closed unitary Jaynes--Cummings excitation blocks, not a dissipative qubit channel semigroup",
        "C224": "nonautonomous unitary Landau--Zener scattering, not a time-homogeneous GKSL flow",
        "C237": "classical Kramers Ornstein--Uhlenbeck dynamics, not a CPTP density-matrix channel",
        "C243": "nonlinear Hamiltonian Bose--Josephson Bloch-sphere motion, not affine Bloch-ball contraction",
        "C297": "non-CPTP PT-symmetric gain/loss ray dynamics, not trace-preserving positive density evolution",
        "C298": "Grassmann projection gradient flow, not an open-quantum semigroup",
        "proves_too_much_guard": "finite Choi or characteristic polynomials do not imply an arithmetic determinant or target zero set",
    }
    data = {
        "schema": "hcs-c303-thermal-qubit-lindblad-v1",
        "candidate_id": "HCS-C303",
        "obstruction_id": "HEN-O287",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_file_sha256": hashlib.sha256(EVALUATION.read_bytes()).hexdigest(),
        "model": {
            "basis": "|0> ground, |1> excited",
            "sigma_z": "|1><1|-|0><0|",
            "generator": "-i[(omega/2)sigma_z,rho]+gamma_down D[sigma_-]+gamma_up D[sigma_+]+(gamma_phi/2)(sigma_z rho sigma_z-rho)",
            "dephasing_convention": "the isolated coherence decay rate is gamma_phi",
            "Gamma1": "gamma_down+gamma_up",
            "Gamma2": "Gamma1/2+gamma_phi",
        },
        "theorem_contract": {
            "population": "rho_11(t)=p+exp(-Gamma1*t)(rho_11(0)-p)",
            "coherence": "rho_01(t)=exp((-Gamma2+i*omega)*t)rho_01(0)",
            "liouvillian_spectrum": "0,-Gamma1,-Gamma2+i*omega,-Gamma2-i*omega",
            "trace_contraction": "max(exp(-Gamma1*t),exp(-Gamma2*t))",
            "choi_ppt": "p(1-p)(1-eta)^2>=eta^q",
            "threshold": "unique eta_* in (0,1) when 0<p<1; t_EB=-log(eta_*)/Gamma1",
        },
        "proof_contract": {
            "complete_positivity": "ae-|c|^2=p(1-p)(1-eta)^2+eta-eta^q>=0",
            "ppt_equivalence": "two-qubit Choi separability is equivalent to positivity of its partial transpose",
            "threshold_uniqueness": "r(1-eta)^2-eta^q is strictly decreasing from r to -1",
            "no_recurrence": "strict trace-norm contraction for Gamma1>0 leaves only the stationary state recurrent",
            "diagonalizability": "population and two coherence invariant subspaces supply an eigenbasis on every parameter face",
        },
        "route_a": {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": scope_flags,
        "nonclaims": nonclaims,
        "collision_boundary": collision,
        "references": references,
        "boundary_rows": boundaries,
        "choi_exact_rows": choi_rows,
        "liouvillian_rows": liouvillian_rows,
        "trace_contraction_rows": trace_rows,
        "semigroup_rows": semigroup_rows,
        "threshold_rows": thresholds,
        "summary": {
            "choi_exact_cells": len(choi_rows),
            "liouvillian_cases": len(liouvillian_rows),
            "trace_cases": len(trace_rows),
            "semigroup_cases": len(semigroup_rows),
            "threshold_cases": len(thresholds),
            "boundary_faces": len(boundaries),
            "audited_rows": len(choi_rows) + len(liouvillian_rows) + len(trace_rows) + len(semigroup_rows) + len(thresholds) + len(boundaries),
        },
    }
    data["payload_sha256"] = canonical_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C303_PRODUCER_PASS", "audited_rows": data["summary"]["audited_rows"],
        "payload_sha256": data["payload_sha256"],
        "evidence_sha256": hashlib.sha256(OUT.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
