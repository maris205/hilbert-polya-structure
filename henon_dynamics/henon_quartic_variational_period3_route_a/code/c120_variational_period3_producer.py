#!/usr/bin/env python3
"""Produce the exact C120 quartic variational period-three receipt."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c120_variational_period3_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
ALPHA = sp.Integer(2)


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def scalar(value: sp.Expr) -> str:
    return str(sp.factor(value))


def vector(value: sp.Matrix) -> list[str]:
    return [scalar(entry) for entry in value]


def matrix(value: sp.Matrix) -> list[list[str]]:
    return [vector(value.row(index).T) for index in range(value.rows)]


def fmap(state: sp.Matrix, alpha: sp.Rational = ALPHA, cubic: bool = True) -> sp.Matrix:
    q, p = state
    lead = q**3 if cubic else sp.Integer(0)
    return sp.Matrix([lead - alpha*q - p, q])


def finverse(state: sp.Matrix, alpha: sp.Rational = ALPHA) -> sp.Matrix:
    q, p = state
    return sp.Matrix([p, p**3 - alpha*p - q])


def reversor(state: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([state[1], state[0]])


def jacobian(q: sp.Expr, alpha: sp.Rational = ALPHA) -> sp.Matrix:
    return sp.Matrix([[3*q**2-alpha, -1], [1, 0]])


def potential(q: sp.Expr, alpha: sp.Rational = ALPHA) -> sp.Expr:
    return q**4/sp.Integer(4) - alpha*q**2/sp.Integer(2)


def det_polynomial(value: sp.Matrix) -> list[str]:
    z = sp.symbols("z")
    poly = sp.Poly((sp.eye(value.rows)-z*value).det(), z)
    return [scalar(item) for item in reversed(poly.all_coeffs())]


def fixed_row(q: sp.Expr) -> dict[str, object]:
    state = sp.Matrix([q, q])
    b = jacobian(q)
    return {
        "state": vector(state),
        "closes": fmap(state) == state,
        "jacobian": matrix(b),
        "jacobian_trace": scalar(sp.trace(b)),
        "jacobian_determinant": scalar(b.det()),
    }


def build() -> dict[str, object]:
    states = [sp.Matrix([0, -1]), sp.Matrix([1, 0]), sp.Matrix([-1, 1])]
    images = [fmap(state) for state in states]
    one_step = [jacobian(state[0]) for state in states]
    monodromy = one_step[2]*one_step[1]*one_step[0]

    qword = [state[0] for state in states]
    action_terms = [
        sp.expand(qword[index]*qword[(index+1) % 3]-potential(qword[index]))
        for index in range(3)
    ]
    action = sp.expand(sum(action_terms))
    qvars = sp.symbols("q0:3")
    symbolic_action = sum(
        qvars[index]*qvars[(index+1) % 3]-potential(qvars[index])
        for index in range(3)
    )
    cycle_substitution = dict(zip(qvars, qword))
    action_gradient = sp.Matrix([
        sp.diff(symbolic_action, value) for value in qvars
    ]).subs(cycle_substitution)
    action_hessian = sp.hessian(symbolic_action, qvars).subs(cycle_substitution)
    lam = sp.symbols("lambda")
    action_charpoly = sp.factor(action_hessian.charpoly(lam).as_expr())
    action_eigenvalues = [-2, 1-sp.sqrt(3), 1+sp.sqrt(3)]

    nearby_alpha = sp.Rational(5, 2)
    nearby_actual = fmap(states[1], nearby_alpha)
    deleted_actual = fmap(states[1], ALPHA, cubic=False)
    noncycle_states = [sp.Matrix([0, -1]), sp.Matrix([1, 0]), sp.Matrix([0, 1])]
    noncycle_images = [fmap(state) for state in noncycle_states]

    q, p, Q = sp.symbols("q p Q")
    symbolic_b = jacobian(q)
    symbolic_state = sp.Matrix([q, p])
    generating = q*Q-potential(q)
    return {
        "schema_id": "hcs-c120-quartic-variational-period3-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "source_model": {
            "phase_space": "Q^2 for certified states; polynomial identities over Q",
            "parameter_alpha": "2",
            "potential": "V(q)=q^4/4-q^2",
            "map": "F(q,p)=(q^3-2*q-p,q)",
            "inverse": "F^{-1}(Q,P)=(P,P^3-2*P-Q)",
            "reversor": "R(q,p)=(p,q)",
            "type_one_generating_function": "S(q,Q)=q*Q-V(q)",
            "generating_convention": "p=-partial_q S and P=partial_Q S",
        },
        "structural_checks": {
            "jacobian_formula": "B(q)=[[3*q^2-2,-1],[1,0]]",
            "jacobian_determinant_symbolic": scalar(symbolic_b.det()),
            "inverse_two_sided_symbolic": (
                sp.simplify(finverse(fmap(symbolic_state))-symbolic_state) == sp.zeros(2, 1)
                and sp.simplify(fmap(finverse(symbolic_state))-symbolic_state) == sp.zeros(2, 1)
            ),
            "reversibility_symbolic_RFR_equals_inverse": (
                sp.simplify(reversor(fmap(reversor(symbolic_state)))-finverse(symbolic_state))
                == sp.zeros(2, 1)
            ),
            "generating_relations_symbolic": {
                "minus_partial_q_S": scalar(-sp.diff(generating, q)),
                "partial_Q_S": scalar(sp.diff(generating, Q)),
                "recovers_map_relations": (
                    sp.expand(-sp.diff(generating, q)-(q**3-2*q-Q)) == 0
                    and sp.expand(sp.diff(generating, Q)-q) == 0
                ),
            },
        },
        "fixed_point_ledger": {
            "fixed_equation_factorization": "q*(q-2)*(q+2)",
            "rows": [fixed_row(value) for value in (0, 2, -2)],
            "count": 3,
        },
        "primitive_period_three": {
            "states": [vector(state) for state in states],
            "images": [vector(image) for image in images],
            "cycle_closes": images == [states[1], states[2], states[0]],
            "pairwise_distinct_states": len({tuple(state) for state in states}) == 3,
            "primitive_period": 3,
            "chronological_jacobians": [matrix(item) for item in one_step],
            "chronological_monodromy_order": "B(-1)*B(1)*B(0)",
            "monodromy": matrix(monodromy),
            "monodromy_trace": scalar(sp.trace(monodromy)),
            "monodromy_determinant": scalar(monodromy.det()),
            "det_I_minus_z_monodromy": det_polynomial(monodromy),
        },
        "discrete_action_certificate": {
            "coordinate_word": [scalar(value) for value in qword],
            "action_definition": "A=sum_i(q_i*q_{i+1}-V(q_i)), cyclic indices",
            "action_terms": [scalar(value) for value in action_terms],
            "action": scalar(action),
            "stationary_gradient": vector(action_gradient),
            "hessian": matrix(action_hessian),
            "hessian_determinant": scalar(action_hessian.det()),
            "hessian_characteristic_polynomial": scalar(action_charpoly),
            "hessian_eigenvalues": [scalar(value) for value in action_eigenvalues],
            "morse_index": 2,
            "nondegenerate": action_hessian.det() != 0,
        },
        "controls": {
            "nearby_parameter": {
                "alpha": scalar(nearby_alpha),
                "tested_transition": [vector(states[1]), vector(states[2])],
                "actual_image": vector(nearby_actual),
                "residual_actual_minus_target": vector(nearby_actual-states[2]),
                "frozen_cycle_survives": nearby_actual == states[2],
            },
            "deleted_cubic_term": {
                "map": "G(q,p)=(-2*q-p,q)",
                "tested_transition": [vector(states[1]), vector(states[2])],
                "actual_image": vector(deleted_actual),
                "residual_actual_minus_target": vector(deleted_actual-states[2]),
                "frozen_cycle_survives": deleted_actual == states[2],
            },
            "noncyclic_word": {
                "candidate_states": [vector(state) for state in noncycle_states],
                "actual_images": [vector(image) for image in noncycle_images],
                "all_transitions_close": noncycle_images == [noncycle_states[1], noncycle_states[2], noncycle_states[0]],
                "first_failed_residual": vector(noncycle_images[1]-noncycle_states[2]),
            },
        },
        "checks": {
            "three_fixed_points": all(row["closes"] for row in [fixed_row(value) for value in (0, 2, -2)]),
            "primitive_period_three_witness": images == [states[1], states[2], states[0]] and len({tuple(state) for state in states}) == 3,
            "parabolic_period_monodromy": monodromy == sp.Matrix([[-1, 0], [-3, -1]]),
            "action_stationary_nondegenerate_index_two": action == sp.Rational(1, 2) and action_hessian.det() == 4,
            "all_three_controls_reject_target": nearby_actual != states[2] and deleted_actual != states[2] and not (noncycle_images == [noncycle_states[1], noncycle_states[2], noncycle_states[0]]),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "ONE_EXACT_PRIMITIVE_CYCLE_WITH_MONODROMY_BUT_NO_TARGET_PRIME_CORRESPONDENCE_OR_COMPLETENESS",
            "A2": "A2_FAIL",
            "A2_qualification": "NO_SOURCE_OWNED_DYNAMICAL_ZETA_OR_FREDHOLM_OBJECT_AND_NO_TARGET_DIVISOR",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_GLOBAL_DETERMINANT_ANALYTIC_STRUCTURE_OR_TARGET_DIVISOR",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "EXACT_SYMPLECTIC_GENERATING_AND_REVERSING_STRUCTURE_BUT_NO_QUANTUM_OBJECT_HILBERT_SPACE_OR_DOMAIN",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "route_a_evaluator_audit": {
            "skill": "route-a-evaluator",
            "skill_version": "0.1.0",
            "canonical_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "a1": {
                "structural_evidence_status": "PROVED",
                "exact_primitive_cycle_and_monodromy": True,
                "target_prime_correspondence": False,
                "target_log_prime_clock_test": False,
                "complete_orbit_enumeration": False,
            },
            "a2": {
                "source_owned_dynamical_zeta_or_fredholm_object": False,
                "target_divisor_match": False,
                "target_root_count_test": False,
            },
            "a3": {
                "global_analytic_structure_match": False,
                "functional_equation_or_gamma_factor_treatment": False,
                "analytic_continuation_or_controlled_domain": False,
            },
            "a4": {
                "exact_symplectic_variational_structure": True,
                "quantum_or_scattering_object_defined": False,
                "hilbert_space_and_operator_domain_named": False,
            },
            "route_b_invocation_allowed": False,
        },
        "claims": {
            "exact_low_period_variational_witness": True,
            "exact_reversibility_and_area_preservation": True,
            "exact_action_morse_certificate": True,
            "complete_orbit_atlas": False,
            "target_prime_correspondence": False,
            "target_log_prime_clock": False,
            "transfer_fredholm_or_nuclear_owner": False,
            "source_owned_dynamical_zeta_or_fredholm_object": False,
            "target_divisor_match": False,
            "global_analytic_structure_match": False,
            "global_variational_classification": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
            "route_b_authorized": False,
        },
        "reproducibility": {
            "producer": "code/c120_variational_period3_producer.py",
            "number_system": "Q with exact Q(sqrt(3)) Hessian eigenvalues",
            "randomness": "none",
        },
    }


def main() -> None:
    data = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(canonical(data))
    print(json.dumps({
        "status": data["status"],
        "fixed_count": data["fixed_point_ledger"]["count"],
        "period_three_count": 1,
        "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
