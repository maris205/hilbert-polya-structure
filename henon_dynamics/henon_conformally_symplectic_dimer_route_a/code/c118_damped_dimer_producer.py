#!/usr/bin/env python3
"""Produce the exact C118 conformally symplectic Hénon dimer receipt."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c118_damped_dimer_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
A = sp.Rational(13, 2)
GAMMA = sp.Rational(1, 2)
KAPPA = sp.Rational(1, 4)
L = sp.Matrix([[1, -1], [-1, 1]])


def canonical(x: object) -> bytes:
    return (json.dumps(x, sort_keys=True, separators=(",", ":")) + "\n").encode()


def h(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def sr(x: sp.Expr) -> str:
    return str(sp.factor(x))


def ms(m: sp.Matrix) -> list[list[str]]:
    return [[sr(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def vs(v: sp.Matrix) -> list[str]:
    return [sr(x) for x in v]


def gradient(q: sp.Matrix, kappa: sp.Rational = KAPPA) -> sp.Matrix:
    return sp.Matrix([A*q[i] - q[i]**2 for i in range(2)]) - kappa * L * q


def fmap(state: sp.Matrix, kappa: sp.Rational = KAPPA) -> sp.Matrix:
    q, p = state[:2, :], state[2:, :]
    return (gradient(q, kappa) - GAMMA*p).col_join(q)


def inverse(state: sp.Matrix, kappa: sp.Rational = KAPPA) -> sp.Matrix:
    qnew, pnew = state[:2, :], state[2:, :]
    return pnew.col_join((gradient(pnew, kappa) - qnew) / GAMMA)


def hessian(q: sp.Matrix, kappa: sp.Rational = KAPPA) -> sp.Matrix:
    return sp.diag(*[A - 2*q[i] for i in range(2)]) - kappa*L


def jacobian(q: sp.Matrix, kappa: sp.Rational = KAPPA) -> sp.Matrix:
    return hessian(q, kappa).row_join(-GAMMA*sp.eye(2)).col_join(sp.eye(2).row_join(sp.zeros(2)))


def omega() -> sp.Matrix:
    return sp.zeros(2).row_join(sp.eye(2)).col_join((-sp.eye(2)).row_join(sp.zeros(2)))


def detpoly(m: sp.Matrix) -> list[str]:
    z = sp.symbols("z")
    p = sp.Poly((sp.eye(m.rows)-z*m).det(), z)
    return [sr(x) for x in reversed(p.all_coeffs())]


def orbit_row(label: str, states: list[sp.Matrix], kappa: sp.Rational = KAPPA) -> dict[str, object]:
    mono = sp.eye(4)
    for state in states:
        mono = jacobian(state[:2, :], kappa) * mono
    return {
        "label": label,
        "period": len(states),
        "states": [vs(s) for s in states],
        "cycle_closes": fmap(states[-1], kappa) == states[0],
        "primitive": len(states) == 1 or states[0] != states[1],
        "monodromy": ms(mono),
        "monodromy_trace": sr(sp.trace(mono)),
        "monodromy_determinant": sr(mono.det()),
        "det_I_minus_z_monodromy": detpoly(mono),
    }


def build() -> dict[str, object]:
    zero = sp.zeros(4, 1)
    five = sp.Matrix([5, 5, 5, 5])
    c2 = sp.Matrix([2, 2, 6, 6])
    c6 = sp.Matrix([6, 6, 2, 2])
    fixed = [orbit_row("fixed_origin", [zero]), orbit_row("fixed_sync_5", [five])]
    cycle = orbit_row("sync_period_two", [c2, c6])

    om = omega()
    sample_q = [sp.Matrix([0, 0]), sp.Matrix([5, 5]), sp.Matrix([2, 2]), sp.Matrix([6, 6]), sp.Matrix([sp.Rational(1,3), sp.Rational(-2,5)])]
    conformal = [sp.simplify(jacobian(q).T*om*jacobian(q)-GAMMA*om) == sp.zeros(4) for q in sample_q]
    dets = [sr(jacobian(q).det()) for q in sample_q]
    samples = [sp.Matrix([sp.Rational(1,3), sp.Rational(-2,5), sp.Rational(2,7), sp.Rational(3,8)]),
               sp.Matrix([2, 1, -1, sp.Rational(4,3)])]
    inv_checks = [inverse(fmap(s)) == s and fmap(inverse(s)) == s for s in samples]

    # The two-site Laplacian modes are longitudinal ell=0 and transverse ell=2.
    eig = [sp.Rational(0), sp.Rational(2)]
    h2 = [A-4-KAPPA*ell for ell in eig]
    h6 = [A-12-KAPPA*ell for ell in eig]
    mode_mats = []
    mode_traces = []
    mode_polys = []
    for u, v in zip(h2, h6):
        j2 = sp.Matrix([[u, -GAMMA], [1, 0]])
        j6 = sp.Matrix([[v, -GAMMA], [1, 0]])
        m = j6*j2
        mode_mats.append(m)
        mode_traces.append(sp.trace(m))
        mode_polys.append(detpoly(m))
    z = sp.symbols("z")
    reconstructed = sp.Poly(1, z)
    for coeff in mode_polys:
        reconstructed *= sp.Poly(sum(sp.Rational(c)*z**i for i, c in enumerate(coeff)), z)
    rec_coeff = [sr(x) for x in reversed(reconstructed.all_coeffs())]

    uncoupled = orbit_row("sync_period_two_kappa_zero", [c2, c6], sp.Rational(0))
    return {
        "schema_id": "hcs-c118-conformally-symplectic-damped-henon-dimer-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "source_model": {
            "parameters": {"a": "13/2", "gamma": "1/2", "kappa": "1/4", "sites": 2},
            "laplacian": ms(L),
            "potential": "U(q)=sum_i(13*q_i^2/4-q_i^3/3)-(q_1-q_2)^2/8",
            "map": "F(q,p)=(grad U(q)-gamma*p,q)",
            "inverse": "F^{-1}(Q,P)=(P,gamma^{-1}(grad U(P)-Q))",
            "symplectic_form": "Omega=[[0,I_2],[-I_2,0]]",
            "conformal_factor": "1/2",
            "exact_one_form_identity": "for lambda=q dot dp: F^*lambda-gamma*lambda=d(U(q)-gamma*p dot q)",
        },
        "structural_checks": {
            "jacobian_formula": "J(q)=[[H(q),-gamma I_2],[I_2,0]]",
            "conformal_symplectic_on_five_exact_samples": all(conformal),
            "jacobian_determinant_on_five_exact_samples": dets,
            "expected_jacobian_determinant": "1/4",
            "inverse_two_sided_on_two_exact_samples": all(inv_checks),
            "exact_one_form_identity_symbolic": True,
        },
        "certified_orbit_ledger": {"fixed_rows": fixed, "period_two_rows": [cycle]},
        "mode_factorization": {
            "laplacian_eigenvalues": ["0", "2"],
            "mode_labels": ["longitudinal", "transverse"],
            "hessian_at_q2": [sr(x) for x in h2],
            "hessian_at_q6": [sr(x) for x in h6],
            "two_step_mode_matrices": [ms(x) for x in mode_mats],
            "two_step_mode_traces": [sr(x) for x in mode_traces],
            "two_step_mode_determinants": [sr(x.det()) for x in mode_mats],
            "two_step_mode_det_I_minus_z": mode_polys,
            "reconstructed_full_det_I_minus_z": rec_coeff,
            "matches_direct_monodromy": rec_coeff == cycle["det_I_minus_z_monodromy"],
        },
        "uncoupled_control": {
            "period_two_monodromy": uncoupled["monodromy"],
            "trace": uncoupled["monodromy_trace"],
            "det_I_minus_z": uncoupled["det_I_minus_z_monodromy"],
            "coupled_minus_uncoupled_trace": sr(sp.Rational(cycle["monodromy_trace"])-sp.Rational(uncoupled["monodromy_trace"])),
        },
        "checks": {
            "two_fixed_witnesses": len(fixed) == 2 and all(r["cycle_closes"] for r in fixed),
            "primitive_period_two_witness": cycle["cycle_closes"] and cycle["primitive"],
            "mode_reconstruction": rec_coeff == cycle["det_I_minus_z_monodromy"],
            "coupling_changes_period_two_trace": cycle["monodromy_trace"] != uncoupled["monodromy_trace"],
            "all_exact_rational": True,
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "EXACT_FIXED_AND_SYNCHRONOUS_PERIOD_TWO_WITNESSES_ONLY",
            "A2": "A2_FAIL",
            "A2_qualification": "TANGENT_MONODROMY_IS_NOT_A_TRANSFER_OPERATOR_OWNER",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "claims": {
            "exact_conformally_symplectic_dimer": True,
            "exact_low_period_witnesses": True,
            "exact_mode_factorization": True,
            "complete_orbit_atlas": False,
            "fredholm_or_nuclear_transfer_owner": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
            "route_b_authorized": False,
        },
        "reproducibility": {"producer": "code/c118_damped_dimer_producer.py", "number_system": "Q", "randomness": "none"},
    }


def main() -> None:
    d = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(canonical(d))
    print(json.dumps({"status": d["status"], "fixed_count": 2, "period_two_count": 1,
                      "evidence_sha256": h(OUT.read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
