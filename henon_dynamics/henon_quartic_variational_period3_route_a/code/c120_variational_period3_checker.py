#!/usr/bin/env python3
"""Independent semantic checker for C120; never imports the producer."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c120_variational_period3_evidence.json"
ALPHA = sp.Integer(2)


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def scalar(value: sp.Expr) -> str:
    return str(sp.factor(value))


def vector(value: sp.Matrix) -> list[str]:
    return [scalar(entry) for entry in value]


def matrix(value: sp.Matrix) -> list[list[str]]:
    return [[scalar(value[i, j]) for j in range(value.cols)] for i in range(value.rows)]


def f(state: sp.Matrix, alpha: sp.Rational = ALPHA, cubic: bool = True) -> sp.Matrix:
    q, p = state
    return sp.Matrix([(q**3 if cubic else 0)-alpha*q-p, q])


def inv(state: sp.Matrix) -> sp.Matrix:
    q, p = state
    return sp.Matrix([p, p**3-2*p-q])


def r(state: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([state[1], state[0]])


def b(q: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[3*q**2-2, -1], [1, 0]])


def v(q: sp.Expr) -> sp.Expr:
    return q**4/sp.Integer(4)-q**2


def detpoly(value: sp.Matrix) -> list[str]:
    z = sp.symbols("z")
    poly = sp.Poly((sp.eye(value.rows)-z*value).det(), z)
    return [scalar(item) for item in reversed(poly.all_coeffs())]


def validate(path: Path = EVIDENCE) -> dict[str, object]:
    raw = path.read_bytes()
    data = json.loads(raw)
    assert raw == canonical(data)
    assert data["schema_id"] == "hcs-c120-quartic-variational-period3-prefreeze-v1"
    assert data["status"] == "PREFREEZE_G3_PASS"
    assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert data["source_model"]["parameter_alpha"] == "2"
    assert data["source_model"]["map"] == "F(q,p)=(q^3-2*q-p,q)"
    assert data["source_model"]["generating_convention"] == "p=-partial_q S and P=partial_Q S"

    q, p, Q = sp.symbols("q p Q")
    state = sp.Matrix([q, p])
    structural = data["structural_checks"]
    assert structural["jacobian_determinant_symbolic"] == "1"
    assert structural["inverse_two_sided_symbolic"] is True
    assert structural["reversibility_symbolic_RFR_equals_inverse"] is True
    assert f(inv(state)) == state and inv(f(state)) == state
    assert r(f(r(state))) == inv(state)
    generating = q*Q-(q**4/sp.Integer(4)-q**2)
    assert scalar(-sp.diff(generating, q)) == structural["generating_relations_symbolic"]["minus_partial_q_S"]
    assert scalar(sp.diff(generating, Q)) == structural["generating_relations_symbolic"]["partial_Q_S"]
    assert structural["generating_relations_symbolic"]["recovers_map_relations"] is True

    fixed = data["fixed_point_ledger"]
    assert fixed["fixed_equation_factorization"] == "q*(q-2)*(q+2)"
    assert fixed["count"] == 3 and len(fixed["rows"]) == 3
    for row, q0 in zip(fixed["rows"], (0, 2, -2)):
        point = sp.Matrix([q0, q0])
        assert row["state"] == vector(point)
        assert row["closes"] is True and f(point) == point
        assert row["jacobian"] == matrix(b(q0))
        assert row["jacobian_trace"] == scalar(sp.trace(b(q0)))
        assert row["jacobian_determinant"] == "1"

    cycle = data["primitive_period_three"]
    states = [sp.Matrix([0, -1]), sp.Matrix([1, 0]), sp.Matrix([-1, 1])]
    images = [f(item) for item in states]
    assert cycle["states"] == [vector(item) for item in states]
    assert cycle["images"] == [vector(item) for item in images]
    assert images == [states[1], states[2], states[0]]
    assert cycle["cycle_closes"] is True and cycle["pairwise_distinct_states"] is True
    assert cycle["primitive_period"] == 3
    jacobians = [b(item[0]) for item in states]
    monodromy = jacobians[2]*jacobians[1]*jacobians[0]
    assert cycle["chronological_jacobians"] == [matrix(item) for item in jacobians]
    assert cycle["chronological_monodromy_order"] == "B(-1)*B(1)*B(0)"
    assert monodromy == sp.Matrix([[-1, 0], [-3, -1]])
    assert cycle["monodromy"] == matrix(monodromy)
    assert cycle["monodromy_trace"] == "-2"
    assert cycle["monodromy_determinant"] == "1"
    assert cycle["det_I_minus_z_monodromy"] == ["1", "2", "1"] == detpoly(monodromy)

    action = data["discrete_action_certificate"]
    qword = [sp.Integer(0), sp.Integer(1), sp.Integer(-1)]
    terms = [qword[i]*qword[(i+1) % 3]-v(qword[i]) for i in range(3)]
    assert action["coordinate_word"] == ["0", "1", "-1"]
    assert action["action_terms"] == [scalar(item) for item in terms] == ["0", "-1/4", "3/4"]
    assert action["action"] == "1/2"
    hessian = sp.Matrix([[2, 1, 1], [1, -1, 1], [1, 1, -1]])
    lam = sp.symbols("lambda")
    assert action["stationary_gradient"] == ["0", "0", "0"]
    assert action["hessian"] == matrix(hessian)
    assert action["hessian_determinant"] == "4"
    assert action["hessian_characteristic_polynomial"] == scalar(hessian.charpoly(lam).as_expr()) == "(lambda + 2)*(lambda**2 - 2*lambda - 2)"
    assert action["hessian_eigenvalues"] == ["-2", "1 - sqrt(3)", "1 + sqrt(3)"]
    assert action["morse_index"] == 2 and action["nondegenerate"] is True

    controls = data["controls"]
    target = states[2]
    nearby = f(states[1], sp.Rational(5, 2))
    assert controls["nearby_parameter"]["alpha"] == "5/2"
    assert controls["nearby_parameter"]["actual_image"] == vector(nearby)
    assert controls["nearby_parameter"]["residual_actual_minus_target"] == vector(nearby-target) == ["-1/2", "0"]
    assert controls["nearby_parameter"]["frozen_cycle_survives"] is False
    deleted = f(states[1], ALPHA, cubic=False)
    assert controls["deleted_cubic_term"]["actual_image"] == vector(deleted)
    assert controls["deleted_cubic_term"]["residual_actual_minus_target"] == ["-1", "0"]
    assert controls["deleted_cubic_term"]["frozen_cycle_survives"] is False
    nonstates = [sp.Matrix([0, -1]), sp.Matrix([1, 0]), sp.Matrix([0, 1])]
    nonimages = [f(item) for item in nonstates]
    assert controls["noncyclic_word"]["actual_images"] == [vector(item) for item in nonimages]
    assert controls["noncyclic_word"]["all_transitions_close"] is False
    assert controls["noncyclic_word"]["first_failed_residual"] == ["-1", "0"]

    assert all(data["checks"].values())
    verdict = data["route_a_verdict"]
    assert verdict == {
        "A1": "A1_WEAK",
        "A1_qualification": "ONE_EXACT_PRIMITIVE_CYCLE_WITH_MONODROMY_BUT_NO_TARGET_PRIME_CORRESPONDENCE_OR_COMPLETENESS",
        "A2": "A2_FAIL",
        "A2_qualification": "NO_SOURCE_OWNED_DYNAMICAL_ZETA_OR_FREDHOLM_OBJECT_AND_NO_TARGET_DIVISOR",
        "A3": "A3_FAIL",
        "A3_qualification": "NO_GLOBAL_DETERMINANT_ANALYTIC_STRUCTURE_OR_TARGET_DIVISOR",
        "A4": "A4_FORMAL_HINT",
        "A4_qualification": "EXACT_SYMPLECTIC_GENERATING_AND_REVERSING_STRUCTURE_BUT_NO_QUANTUM_OBJECT_HILBERT_SPACE_OR_DOMAIN",
        "overall": "ROUTE_A_EXPLORATORY",
    }
    assert data["route_a_evaluator_audit"] == {
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
    }
    for key in (
        "complete_orbit_atlas", "target_prime_correspondence", "target_log_prime_clock",
        "transfer_fredholm_or_nuclear_owner", "source_owned_dynamical_zeta_or_fredholm_object",
        "target_divisor_match", "global_analytic_structure_match",
        "global_variational_classification", "arithmetic_local_data", "euler_factors",
        "root_numbers", "automorphy", "hilbert_polya_operator", "route_b_authorized",
    ):
        assert data["claims"][key] is False
    return data


if __name__ == "__main__":
    validate()
    print(json.dumps({"status": "C120_INDEPENDENT_CHECK_PASS", "fixed_count": 3, "period_three_count": 1}, sort_keys=True))
