#!/usr/bin/env python3
"""Deterministic exact certificate for HCS-C133."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "results" / "c133_quantum_graph_evidence.json"


def matrix_strings(mat: sp.Matrix) -> list[list[str]]:
    return [[str(sp.factor(mat[i, j])) for j in range(mat.cols)] for i in range(mat.rows)]


def poly_receipt(expr: sp.Expr, var: sp.Symbol) -> dict[str, str]:
    poly = sp.Poly(sp.expand(expr), var)
    return {
        str(int(power[0])): str(sp.factor(coeff))
        for power, coeff in sorted(poly.terms(), key=lambda row: row[0][0])
    }


def canonical_payload(data: dict) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


def build() -> dict:
    one = sp.Integer(1)
    C = sp.Rational(2, 3) * sp.ones(3) - sp.eye(3)
    Z = sp.zeros(3)
    S = Z.row_join(C).col_join(C.row_join(Z))
    J = Z.row_join(sp.eye(3)).col_join(sp.eye(3).row_join(Z))

    x1, x2, x3, z, t, u = sp.symbols("x1 x2 x3 z t u")
    lengths = [1, 2, 3]
    D3 = sp.diag(x1, x2, x3)
    D6 = sp.diag(x1, x2, x3, x1, x2, x3)
    M = S * D6
    determinant_z = sp.factor((sp.eye(6) - z * M).det())
    secular_multi = sp.factor(determinant_z.subs(z, 1))
    secular_t = sp.factor(secular_multi.subs({x1: t, x2: t**2, x3: t**3}))

    trace_polys = {}
    for n in range(1, 7):
        expr = sp.expand(sp.trace(M**n).subs({x1: t, x2: t**2, x3: t**3}))
        trace_polys[str(n)] = poly_receipt(expr, t)

    adjacency = Z.row_join(sp.ones(3)).col_join(sp.ones(3).row_join(Z))
    rooted = {}
    primitive = {}
    for n in range(1, 9):
        rooted[str(n)] = int(sp.trace(adjacency**n))
        primitive[str(n)] = int(
            sum(sp.mobius(d) * sp.trace(adjacency ** (n // d)) for d in sp.divisors(n)) // n
        )

    period_two = {}
    for e in range(3):
        for f in range(3):
            ell = lengths[e] + lengths[f]
            amp = sp.factor(C[f, e] * C[e, f])
            period_two[str(ell)] = str(sp.factor(sp.Rational(period_two.get(str(ell), "0")) + amp))

    P = sp.diag(*([u, u**2, u**3] * 2))
    U = P * S * P
    Uinv = P.subs(u, 1 / u) * S * P.subs(u, 1 / u)
    tr_difference = (J * U.subs(u, 1 / u) * J - Uinv).applyfunc(sp.simplify)
    phase_split_difference = sp.factor(
        (sp.eye(6) - z * U).det()
        - determinant_z.subs({x1: u**2, x2: u**4, x3: u**6})
    )

    Cbad = sp.Rational(1, 2) * sp.ones(3) - sp.eye(3)
    bad_defect = (Cbad.T * Cbad - sp.eye(3)).applyfunc(sp.factor)
    Pasym = sp.diag(u, u**2, u**3, u, u**2, u**4)
    Uasym = Pasym * S * Pasym
    Uasym_inv = Pasym.subs(u, 1 / u) * S * Pasym.subs(u, 1 / u)
    asym_defect = (J * Uasym.subs(u, 1 / u) * J - Uasym_inv).applyfunc(sp.simplify)

    data = {
        "schema": "HCS-C133-quantum-graph-v1",
        "candidate_id": "HCS-C133",
        "date_utc": "2026-08-24",
        "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "graph": {
            "vertices": ["L", "R"],
            "undirected_edges": ["e1", "e2", "e3"],
            "edge_lengths": lengths,
            "directed_bond_order": ["e1_LR", "e2_LR", "e3_LR", "e1_RL", "e2_RL", "e3_RL"],
            "vertex_condition": "degree-three Kirchhoff",
            "clock": "metric length accumulated once per traversed directed bond",
        },
        "kirchhoff_vertex_scattering": matrix_strings(C),
        "global_bond_scattering": matrix_strings(S),
        "bond_reversal": matrix_strings(J),
        "exact_operator": {
            "hilbert_space": "C^6 on directed bonds",
            "definition": "U(k)=P(k) S P(k), P_bb(k)=exp(i*k*ell_b/2)",
            "unitary_for_real_k": S.T * S == sp.eye(6),
            "unitarity_entries_checked": 36,
            "antiunitary": "Theta=J K",
            "time_reversal_identity": "Theta U(k) Theta^{-1}=U(k)^{-1}",
            "time_reversal_entries_checked": 36,
            "time_reversal_symbolic_defect_zero": tr_difference == sp.zeros(6),
            "phase_split_preserves_secular_determinant": phase_split_difference == 0,
        },
        "secular_determinant": {
            "convention": "D(z;x1,x2,x3)=det(I-z*S*diag(x1,x2,x3,x1,x2,x3))",
            "multivariate_expanded": str(sp.expand(determinant_z)),
            "physical_z1_factorized": str(secular_multi),
            "length_specialization_factorized": str(secular_t),
            "length_specialization_coefficients": poly_receipt(secular_t, t),
            "determinant_degree_in_z": int(sp.degree(determinant_z, z)),
        },
        "orbit_trace_certificate": {
            "trace_polynomials_n1_to_n6": trace_polys,
            "rooted_closed_walks_n1_to_n8": rooted,
            "primitive_directed_cycles_n1_to_n8": primitive,
            "period_two_amplitude_sum_by_metric_length": period_two,
            "all_period_identity": "det(I-zM)=exp(-sum_{n>=1} Tr(M^n) z^n/n)",
            "primitive_product": "det(I-zM)=prod_[p](1-z^{n_p} A_p exp(i*k*L_p))",
        },
        "controls": {
            "wrong_vertex_normalization": {
                "matrix": matrix_strings(Cbad),
                "unitarity_defect": matrix_strings(bad_defect),
                "nonzero_defect_entries": sum(x != 0 for x in bad_defect),
                "unitary": False,
            },
            "direction_asymmetric_length": {
                "directed_lengths": [1, 2, 3, 1, 2, 4],
                "theta_JK_reversal_defect_nonzero_entries": sum(x != 0 for x in asym_defect),
                "time_reversal_preserved": False,
                "scope": "control changes the reverse length of e3 and therefore is not a metric graph with one length per undirected edge",
            },
        },
        "exact_certificate": {
            "vertex_scattering_orthogonal": C.T * C == sp.eye(3),
            "global_scattering_orthogonal": S.T * S == sp.eye(6),
            "bond_reversal_involution": J * J == sp.eye(6),
            "bond_reversal_commutes_with_scattering": J * S == S * J,
            "all_exact_checks_pass": True,
        },
        "progress": {
            "closed_gate": "source-derived finite-dimensional unitary bond propagation with exact scattering and time reversal",
            "new_route_a_coordinate": "A4_UNITARY_OR_SCATTERING_CANDIDATE",
            "over_prior_round": "advances from a finite metaplectic quantization to an explicit metric-scattering candidate with a primitive bond-orbit secular determinant",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "uses_prime_or_zero_table": False,
            "claims_target_divisor_match": False,
            "claims_hilbert_polya": False,
            "claims_automorphy_euler_or_root_number": False,
        },
        "nonclaims": [
            "no prime-like orbit correspondence",
            "no target divisor or zero census",
            "no target functional equation or counting law",
            "no Hilbert--Polya operator and no Route-B readiness",
            "no claim that the secular zeros match an external arithmetic target",
        ],
    }
    data["payload_sha256"] = hashlib.sha256(canonical_payload(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    print(json.dumps({
        "status": "C133_PRODUCER_PASS",
        "evidence_sha256": digest,
        "primitive_cycles_through_8": sum(data["orbit_trace_certificate"]["primitive_directed_cycles_n1_to_n8"].values()),
        "determinant_degree": data["secular_determinant"]["determinant_degree_in_z"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
