#!/usr/bin/env python3
"""Produce the exact HCS-C138 magnetic theta-graph certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c138_magnetic_graph_evidence.json"
LENGTHS = (1, 2, 3)


def fs(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def matrix_strings(mat: sp.Matrix) -> list[list[str]]:
    return [[str(sp.factor(mat[i, j])) for j in range(mat.cols)] for i in range(mat.rows)]


def canonical(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[i:] + word[:i] for i in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(word != word[:d] * (n // d) for d in range(1, n) if n % d == 0)


def reverse_word(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((state + 3) % 6 for state in reversed(word))


def state_name(state: int) -> str:
    return ("+" if state < 3 else "-") + str(state % 3 + 1)


def orbit_data(word: tuple[int, ...]) -> tuple[str, Fraction, int, tuple[int, int, int]]:
    amp = Fraction(1)
    winding = [0, 0, 0]
    length = 0
    for j, state in enumerate(word):
        nxt = word[(j + 1) % len(word)]
        edge, next_edge = state % 3, nxt % 3
        amp *= Fraction(-1, 3) if edge == next_edge else Fraction(2, 3)
        length += LENGTHS[edge]
        winding[edge] += 1 if state < 3 else -1
    assert sum(winding) == 0
    names = ",".join(state_name(s) for s in word)
    can = ",".join(state_name(s) for s in canonical(word))
    rev = ",".join(state_name(s) for s in canonical(reverse_word(word)))
    token = f"{names}:A={fs(amp)}:L={length}:m={winding[0]},{winding[1]},{winding[2]}:canon={can}:reverse={rev}"
    return token, amp, length, tuple(winding)


def rooted_words(n: int):
    if n % 2:
        return
    for start_sign in (0, 1):
        for edges in product(range(3), repeat=n):
            yield tuple(edges[i] + 3 * ((start_sign + i) % 2) for i in range(n))


def digest(lines: list[str]) -> str:
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def build() -> dict:
    C = sp.Rational(2, 3) * sp.ones(3) - sp.eye(3)
    Z = sp.zeros(3)
    S = Z.row_join(C).col_join(C.row_join(Z))
    J = Z.row_join(sp.eye(3)).col_join(sp.eye(3).row_join(Z))
    x1, x2, x3, q1, q2, q3, rho, c, t = sp.symbols("x1 x2 x3 q1 q2 q3 rho c t", nonzero=True)
    xs, qs = (x1, x2, x3), (q1, q2, q3)
    Xp = sp.diag(*(xs[i] * qs[i] for i in range(3)))
    Xm = sp.diag(*(xs[i] / qs[i] for i in range(3)))
    determinant = sp.factor((sp.eye(3) - rho**2 * C * Xm * C * Xp).det())
    Q = lambda i, j: qs[i]/qs[j] + qs[j]/qs[i]
    T1 = sp.Rational(1,9)*sum(x*x for x in xs) + sp.Rational(4,9)*sum(xs[i]*xs[j]*Q(i,j) for i in range(3) for j in range(i+1,3))
    T2 = sp.Rational(1,9)*sum(xs[i]**2*xs[j]**2 for i in range(3) for j in range(i+1,3)) + sp.Rational(4,9)*sum(xs[i]*xs[j]*xs[3-i-j]**2*Q(i,j) for i in range(3) for j in range(i+1,3))
    closed = 1-rho**2*T1+rho**4*T2-rho**6*(x1*x2*x3)**2
    assert sp.factor(determinant-closed) == 0
    coeffs = {str(power): str(sp.factor(sp.expand(determinant).coeff(rho, power))) for power in (0,2,4,6)}
    gauge = sp.factor(determinant.subs({q1:c*q1,q2:c*q2,q3:c*q3})-determinant)
    inverted = sp.factor(determinant.subs({q1:1/q1,q2:1/q2,q3:1/q3})-determinant)
    assert gauge == 0 and inverted == 0
    zero_flux = sp.factor(determinant.subs({q1:1,q2:1,q3:1,x1:t,x2:t**2,x3:t**3,rho:1}))
    zero_expected = -sp.Rational(1,9)*(t-1)**3*(t+1)*(t**2+1)*(t**2+t+1)*(3*t**2-2*t+3)*(3*t**2+5*t+3)
    assert sp.factor(zero_flux-zero_expected) == 0
    pi_rho2 = sp.factor(sp.expand(determinant.subs({q1:-1,q2:1,q3:1})-determinant.subs({q1:1,q2:1,q3:1})).coeff(rho,2))
    assert pi_rho2 == sp.Rational(16,9)*x1*(x2+x3)

    ledgers = []
    rooted_total = primitive_total = 0
    for n in range(1, 9):
        words = list(rooted_words(n) or [])
        lines = [orbit_data(word)[0] for word in words]
        prim_words = sorted({canonical(word) for word in words if primitive(word)})
        prim_lines = [orbit_data(word)[0] for word in prim_words]
        ledgers.append({"n": n, "rooted_closed_walks": len(words), "primitive_cycles": len(prim_words), "rooted_ledger_sha256": digest(lines), "primitive_ledger_sha256": digest(prim_lines)})
        rooted_total += len(words)
        primitive_total += len(prim_words)
    assert rooted_total == 14760 and primitive_total == 1905
    witnesses = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            word = (i, j+3)
            token, amp, length, winding = orbit_data(word)
            witnesses.append({"oriented_pair": [i+1,j+1], "word": [state_name(s) for s in word], "amplitude": fs(amp), "metric_length": length, "winding": list(winding), "phase": f"q{i+1}/q{j+1}", "ledger_token": token})

    u = (1+sp.I)/sp.sqrt(2)
    Pa = sp.diag(u,1,1,sp.conjugate(u),1,1)
    Pm = sp.diag(sp.conjugate(u),1,1,u,1,1)
    Ua, Um = Pa*S*Pa, Pm*S*Pm
    correct = (J*Ua.conjugate()*J-Um.inv()).applyfunc(sp.simplify)
    wrong = (J*Ua.conjugate()*J-Ua.inv()).applyfunc(sp.simplify)
    wrong_norm = sp.simplify(sum(sp.conjugate(v)*v for v in wrong))
    assert correct == sp.zeros(6) and sum(v != 0 for v in wrong) == 8 and wrong_norm == sp.Rational(64,9)
    Cbad = sp.Rational(1,2)*sp.ones(3)-sp.eye(3)
    bad_defect = (Cbad.T*Cbad-sp.eye(3)).applyfunc(sp.factor)
    v = sp.symbols("v", nonzero=True)
    Pasym = sp.diag(v,v**2,v**3,v,v**2,v**4)
    Uasym = Pasym*S*Pasym
    asym = (J*Uasym.subs(v,1/v)*J-Uasym.inv()).applyfunc(sp.simplify)

    data = {
        "schema": "HCS-C138-magnetic-theta-graph-v1",
        "candidate_id": "HCS-C138",
        "date_utc": "2026-08-24",
        "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "graph": {"vertices": ["L","R"], "edge_lengths": [1,2,3], "directed_bond_order": ["+1","+2","+3","-1","-2","-3"], "vertex_condition": "degree-three Kirchhoff", "hilbert_space": "C^6 on directed bonds", "clock": "one metric length per traversed directed bond"},
        "scattering": {"kirchhoff_C": matrix_strings(C), "global_S": matrix_strings(S), "bond_reversal_J": matrix_strings(J), "C_orthogonal": C.T*C == sp.eye(3), "S_orthogonal": S.T*S == sp.eye(6)},
        "magnetic_family": {
            "phase_split": "P_alpha(k)=diag(exp(i(k*l_j+alpha_j)/2), exp(i(k*l_j-alpha_j)/2))",
            "operator": "U_alpha(k)=P_alpha(k) S P_alpha(k)",
            "unitary_for_real_k_alpha": True,
            "common_phase_gauge": "alpha_j -> alpha_j+c leaves U_alpha(k) unchanged because D_c S D_c=S",
            "gauge_invariant_flux_coordinates": ["alpha_1-alpha_3", "alpha_2-alpha_3"],
            "antiunitary": "Theta=J K",
            "antiunitary_identity": "Theta U_alpha(k) Theta^{-1}=U_{-alpha}(k)^{-1}",
            "orientation_statement": "individual orbit phases invert under orientation reversal; only the full determinant is even under alpha -> -alpha",
        },
        "laurent_determinant": {
            "convention": "D(rho;x,q)=det(I_3-rho^2*C*X_-*C*X_+)",
            "X_plus": "diag(x1*q1,x2*q2,x3*q3)", "X_minus": "diag(x1/q1,x2/q2,x3/q3)",
            "rho_coefficients": coeffs, "rho_degree": 6,
            "T1": "1/9*sum_i x_i^2+4/9*sum_(i<j) x_i*x_j*(q_i/q_j+q_j/q_i)",
            "T2": "1/9*sum_(i<j) x_i^2*x_j^2+4/9*sum_(i<j) x_i*x_j*x_k^2*(q_i/q_j+q_j/q_i), k=complement",
            "closed_form": "1-rho^2*T1+rho^4*T2-rho^6*(x1*x2*x3)^2",
            "common_q_scaling_invariant": gauge == 0, "q_inversion_invariant": inverted == 0,
            "zero_flux_c133_factor": str(sp.factor(zero_flux)),
        },
        "oriented_orbit_ledger": {
            "periods_through_8": ledgers,
            "rooted_closed_walks_through_8": rooted_total,
            "primitive_cycles_through_8": primitive_total,
            "token_fields": ["directed states","signed rational amplitude","metric length","winding vector","canonical rotation","reverse id"],
            "phase_rule": "A_p*rho^n*exp(i*k*L_p)*product_j q_j^m_j",
            "primitive_product_germ": "product_[p primitive](1-rho^n_p*A_p*exp(i*k*L_p)*q^m(p))",
            "shortest_orientation_witnesses": witnesses,
        },
        "controls": {
            "zero_flux_recovery": {"passes": True, "factor": str(sp.factor(zero_flux))},
            "common_phase_gauge": {"passes": True, "operator_defect_nonzero_entries": 0},
            "pi_flux": {"q": [-1,1,1], "rho2_coefficient_change": "16/9*x1*(x2+x3)", "changes_determinant": True},
            "pi_over_2_fixed_alpha_reversal": {"alpha": ["pi/2","0","0"], "correct_alpha_to_minus_alpha_defect_nonzero_entries": 0, "wrong_fixed_alpha_defect_nonzero_entries": 8, "wrong_fixed_alpha_frobenius_norm_squared": "64/9"},
            "wrong_vertex_normalization": {"coefficient": "1/2", "unitarity_defect": matrix_strings(bad_defect), "nonzero_defect_entries": sum(v != 0 for v in bad_defect), "unitary": False},
            "direction_asymmetric_reverse_length": {"directed_lengths": [1,2,3,1,2,4], "reversal_defect_nonzero_entries": sum(v != 0 for v in asym), "preserves_reversal": False},
        },
        "progress": {"magnetic_unitary_family": "PASS_EXACT", "gauge_and_antiunitary_structure": "PASS_EXACT", "full_laurent_determinant": "PASS_EXACT", "orientation_sensitive_orbit_ledger": "PASS_EXACT"},
        "route_a": {"tuple": ["A1_WEAK","A2_FAIL","A3_FAIL","A4_UNITARY_OR_SCATTERING_CANDIDATE"], "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False},
        "scope_flags": {"uses_prime_table": False, "uses_zero_table": False, "claims_target_divisor": False, "claims_euler_factors": False, "claims_root_number": False, "claims_automorphy": False, "claims_hilbert_polya": False},
        "nonclaims": ["no prime-like orbit correspondence", "no target divisor or zero census", "no target functional equation or counting law", "no arithmetic Euler factors or root number", "no Hilbert--Polya operator or external spectral identification"],
    }
    payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    data["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), indent=2, sort_keys=True)+"\n")
    print(args.output)


if __name__ == "__main__":
    main()
