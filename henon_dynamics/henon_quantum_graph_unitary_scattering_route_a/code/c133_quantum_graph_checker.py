#!/usr/bin/env python3
"""Independent exact reconstruction for the C133 evidence object."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results" / "c133_quantum_graph_evidence.json"


def canon_without_hash(data: dict) -> str:
    clone = dict(data)
    clone.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clone, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def mat_strings(mat: sp.Matrix) -> list[list[str]]:
    return [[str(sp.factor(mat[i, j])) for j in range(mat.cols)] for i in range(mat.rows)]


def poly_dict(expr: sp.Expr, var: sp.Symbol) -> dict[str, str]:
    return {
        str(int(power[0])): str(sp.factor(coeff))
        for power, coeff in sorted(sp.Poly(sp.expand(expr), var).terms(), key=lambda row: row[0][0])
    }


def validate(data: dict) -> None:
    assert data["payload_sha256"] == canon_without_hash(data)
    assert set(data) == {
        "bond_reversal",
        "candidate_id",
        "controls",
        "date_utc",
        "exact_certificate",
        "exact_operator",
        "global_bond_scattering",
        "graph",
        "kirchhoff_vertex_scattering",
        "nonclaims",
        "orbit_trace_certificate",
        "payload_sha256",
        "progress",
        "route_a",
        "schema",
        "scope",
        "scope_flags",
        "secular_determinant",
    }
    assert data["schema"] == "HCS-C133-quantum-graph-v1"
    assert data["candidate_id"] == "HCS-C133"
    assert data["date_utc"] == "2026-08-24"
    assert data["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    graph = data["graph"]
    assert set(graph) == {
        "clock",
        "directed_bond_order",
        "edge_lengths",
        "undirected_edges",
        "vertex_condition",
        "vertices",
    }
    assert graph["vertices"] == ["L", "R"]
    assert graph["undirected_edges"] == ["e1", "e2", "e3"]
    assert graph["edge_lengths"] == [1, 2, 3]
    assert graph["directed_bond_order"] == ["e1_LR", "e2_LR", "e3_LR", "e1_RL", "e2_RL", "e3_RL"]
    assert graph["vertex_condition"] == "degree-three Kirchhoff"
    assert graph["clock"] == "metric length accumulated once per traversed directed bond"

    C = sp.Matrix(3, 3, lambda i, j: sp.Rational(2, 3) - (1 if i == j else 0))
    O = sp.zeros(3)
    I = sp.eye(3)
    S = O.row_join(C).col_join(C.row_join(O))
    J = O.row_join(I).col_join(I.row_join(O))
    assert data["kirchhoff_vertex_scattering"] == mat_strings(C)
    assert data["global_bond_scattering"] == mat_strings(S)
    assert data["bond_reversal"] == mat_strings(J)

    op = data["exact_operator"]
    assert set(op) == {
        "antiunitary",
        "definition",
        "hilbert_space",
        "phase_split_preserves_secular_determinant",
        "time_reversal_entries_checked",
        "time_reversal_identity",
        "time_reversal_symbolic_defect_zero",
        "unitarity_entries_checked",
        "unitary_for_real_k",
    }
    assert op["hilbert_space"] == "C^6 on directed bonds"
    assert op["definition"] == "U(k)=P(k) S P(k), P_bb(k)=exp(i*k*ell_b/2)"
    assert op["unitary_for_real_k"] is True
    assert op["unitarity_entries_checked"] == 36
    assert op["antiunitary"] == "Theta=J K"
    assert op["time_reversal_identity"] == "Theta U(k) Theta^{-1}=U(k)^{-1}"
    assert op["time_reversal_entries_checked"] == 36
    assert op["time_reversal_symbolic_defect_zero"] is True
    assert op["phase_split_preserves_secular_determinant"] is True
    assert S.T * S == sp.eye(6) and J * J == sp.eye(6) and J * S == S * J

    x1, x2, x3, z, t = sp.symbols("x1 x2 x3 z t")
    D = sp.diag(x1, x2, x3, x1, x2, x3)
    M = S * D
    detz = sp.factor((sp.eye(6) - z * M).det())
    multi = sp.factor(detz.subs(z, 1))
    physical = sp.factor(multi.subs({x1: t, x2: t**2, x3: t**3}))
    sec = data["secular_determinant"]
    assert set(sec) == {
        "convention",
        "determinant_degree_in_z",
        "length_specialization_coefficients",
        "length_specialization_factorized",
        "multivariate_expanded",
        "physical_z1_factorized",
    }
    assert sec["convention"] == "D(z;x1,x2,x3)=det(I-z*S*diag(x1,x2,x3,x1,x2,x3))"
    assert sec["multivariate_expanded"] == str(sp.expand(detz))
    assert sec["physical_z1_factorized"] == str(multi)
    assert sec["physical_z1_factorized"] == str(multi)
    assert sec["length_specialization_factorized"] == str(physical)
    assert sec["length_specialization_coefficients"] == poly_dict(physical, t)
    assert sec["determinant_degree_in_z"] == 6

    traces = {}
    for n in range(1, 7):
        traces[str(n)] = poly_dict(sp.trace(M**n).subs({x1: t, x2: t**2, x3: t**3}), t)
    orbit = data["orbit_trace_certificate"]
    assert set(orbit) == {
        "all_period_identity",
        "period_two_amplitude_sum_by_metric_length",
        "primitive_directed_cycles_n1_to_n8",
        "primitive_product",
        "rooted_closed_walks_n1_to_n8",
        "trace_polynomials_n1_to_n6",
    }
    assert orbit["trace_polynomials_n1_to_n6"] == traces
    A = O.row_join(sp.ones(3)).col_join(sp.ones(3).row_join(O))
    rooted = {str(n): int(sp.trace(A**n)) for n in range(1, 9)}
    primitive = {
        str(n): int(sum(sp.mobius(d) * sp.trace(A ** (n // d)) for d in sp.divisors(n)) // n)
        for n in range(1, 9)
    }
    assert orbit["rooted_closed_walks_n1_to_n8"] == rooted
    assert orbit["primitive_directed_cycles_n1_to_n8"] == primitive
    amp = {}
    lengths = [1, 2, 3]
    for e in range(3):
        for f in range(3):
            key = str(lengths[e] + lengths[f])
            amp[key] = str(sp.factor(sp.Rational(amp.get(key, "0")) + C[f, e] * C[e, f]))
    assert orbit["period_two_amplitude_sum_by_metric_length"] == amp
    assert orbit["all_period_identity"] == "det(I-zM)=exp(-sum_{n>=1} Tr(M^n) z^n/n)"
    assert orbit["primitive_product"] == "det(I-zM)=prod_[p](1-z^{n_p} A_p exp(i*k*L_p))"

    controls = data["controls"]
    assert set(controls) == {"direction_asymmetric_length", "wrong_vertex_normalization"}
    assert set(controls["wrong_vertex_normalization"]) == {
        "matrix",
        "nonzero_defect_entries",
        "unitarity_defect",
        "unitary",
    }
    Cbad = sp.Rational(1, 2) * sp.ones(3) - sp.eye(3)
    defect = Cbad.T * Cbad - sp.eye(3)
    assert controls["wrong_vertex_normalization"]["matrix"] == mat_strings(Cbad)
    assert controls["wrong_vertex_normalization"]["unitarity_defect"] == mat_strings(defect)
    assert controls["wrong_vertex_normalization"]["nonzero_defect_entries"] == sum(x != 0 for x in defect)
    assert controls["wrong_vertex_normalization"]["unitary"] is False
    asym = controls["direction_asymmetric_length"]
    assert set(asym) == {
        "directed_lengths",
        "scope",
        "theta_JK_reversal_defect_nonzero_entries",
        "time_reversal_preserved",
    }
    assert asym["directed_lengths"] == [1, 2, 3, 1, 2, 4]
    assert asym["theta_JK_reversal_defect_nonzero_entries"] == 8
    assert asym["time_reversal_preserved"] is False
    assert asym["scope"] == (
        "control changes the reverse length of e3 and therefore is not a metric graph "
        "with one length per undirected edge"
    )

    exact = data["exact_certificate"]
    assert exact == {
        "all_exact_checks_pass": True,
        "bond_reversal_commutes_with_scattering": True,
        "bond_reversal_involution": True,
        "global_scattering_orthogonal": True,
        "vertex_scattering_orthogonal": True,
    }
    progress = data["progress"]
    assert progress == {
        "closed_gate": "source-derived finite-dimensional unitary bond propagation with exact scattering and time reversal",
        "new_route_a_coordinate": "A4_UNITARY_OR_SCATTERING_CANDIDATE",
        "over_prior_round": "advances from a finite metaplectic quantization to an explicit metric-scattering candidate with a primitive bond-orbit secular determinant",
    }
    route_a = data["route_a"]
    assert route_a == {
        "overall": "ROUTE_A_EXPLORATORY",
        "route_b_invocation_allowed": False,
        "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"],
    }
    assert data["scope_flags"] == {
        "claims_automorphy_euler_or_root_number": False,
        "claims_hilbert_polya": False,
        "claims_target_divisor_match": False,
        "uses_prime_or_zero_table": False,
    }
    assert data["nonclaims"] == [
        "no prime-like orbit correspondence",
        "no target divisor or zero census",
        "no target functional equation or counting law",
        "no Hilbert--Polya operator and no Route-B readiness",
        "no claim that the secular zeros match an external arithmetic target",
    ]


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    validate(json.loads(path.read_text()))
    print("C133 independent checker: PASS")


if __name__ == "__main__":
    main()
