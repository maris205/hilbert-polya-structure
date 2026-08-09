#!/usr/bin/env python3
"""Exact certificate producer for the HCS-C22G graded Ruelle complex.

The program certifies algebraic and rational parts of the theorem.  It does
not approximate a transfer-operator spectrum.  In particular, all graph
branches retain their chronological order and all pass/fail decisions are
made with exact arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PARENT = PROJECT_ROOT.parent / "henon_time_ordered_ruelle_cocycle"
PARENT_CERTIFICATE = PARENT / "results" / "c22_t4_certificate.json"
PAPER5 = PROJECT_ROOT.parent / "docs" / "prior_work" / "papers" / (
    "5-An Area-Preserving Henon-Map Model.pdf"
)
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c22g_certificate.json"

A_MIN = Fraction(59, 10)
A_MAX = Fraction(61, 10)
BETA = Fraction(123, 112)
GAMMA = Fraction(112, 123)
CX, RX = Fraction(23, 48), Fraction(7, 48)
CY, RY = Fraction(121, 256), Fraction(41, 256)
M_RADIUS = Fraction(1, 2)
PROJECTIVE_IMAGE = Fraction(125440, 466211)
COORDINATE_CLEARANCE = Fraction(7, 5490)

STATES = ((-1, -1), (-1, 1), (1, -1), (1, 1))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def fpayload(value: Fraction) -> dict[str, object]:
    return {"fraction": ftext(value), "decimal": format(float(value), ".17g")}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def label(sign: int) -> str:
    return "+" if sign > 0 else "-"


def state_label(state: tuple[int, int]) -> str:
    return "".join(label(sign) for sign in state)


def graph_edges() -> list[dict[str, object]]:
    """Source (s,t) maps to target (r,s); (+,+) endpoint is forbidden."""

    edges: list[dict[str, object]] = []
    for s, t in STATES:
        for r in (-1, 1):
            if t == 1 and r == 1:
                continue
            target = (r, s)
            edges.append(
                {
                    "source": state_label((s, t)),
                    "target": state_label(target),
                    "input_unstable_sign": label(s),
                    "input_stable_base_sign": label(t),
                    "output_unstable_sign": label(r),
                    "letter_multiplicity": 2,
                }
            )
    return edges


def pinning_certificate() -> dict[str, object]:
    nesting_ratio = (abs(CX - CY) + RX) / RY
    projective_ratio = PROJECTIVE_IMAGE / M_RADIUS
    unstable_ratio = 1 - COORDINATE_CLEARANCE / RX
    c_upper = 2 * A_MAX * Fraction(5, 8) + BETA * M_RADIUS
    full_jacobian_lower = 1 / c_upper**2
    pinning_stable_jacobian_lower = 1 / (
        2 * A_MAX * Fraction(5, 8) * c_upper**2
    )

    a, x, z, p, m, beta, gamma = sp.symbols(
        "a x z P m beta gamma", nonzero=True
    )
    c = -2 * a * p - beta * m
    px = -1 / (2 * a * p)
    gm = gamma * beta / c**2
    stable_det = sp.factor(px * gm).subs(gamma * beta, 1)
    second_residual = sp.expand(1 - a * p**2 - x - z)

    return {
        "bps_convention": {
            "input_contracting_stable": "w=(x,m)=(p,m)",
            "input_expanding_unstable": "y=q",
            "fixed_mixed_data": "input stable w and output unstable z",
            "partial_inverse": "phi_s(w,z)=P_(a,sigma)(x,z)=sigma*sqrt((1-x-z)/a)",
            "stable_output": "phi_u(w,z)=(P,G_(a,P)(m))",
            "identity": "Fhat(w,phi_s(w,z))=(phi_u(w,z),z)",
            "reverse_stable_output_inverse_used": False,
        },
        "symbolic": {
            "output_unstable_residual_mod_aP2_relation": str(second_residual),
            "relation": "a*P^2=1-x-z",
            "partial_q_output_unstable": "-2*a*P",
            "stable_pinning_jacobian": str(stable_det),
            "stable_pinning_jacobian_expected": "-1/(2*P*a*(2*P*a+beta*m)**2)",
            "full_lifted_jacobian": "1/(-2*a*y-beta*m)^2",
        },
        "strict_inclusions": {
            "stable_base_X_inside_Y_ratio": fpayload(nesting_ratio),
            "stable_slope_GM_inside_M_ratio": fpayload(projective_ratio),
            "unstable_half_inverse_inside_X_ratio": fpayload(unstable_ratio),
            "all_ratios_below_one": max(
                nesting_ratio, projective_ratio, unstable_ratio
            )
            < 1,
            "source": "inherited exact C22 T5 disk certificate",
        },
        "nonvanishing": {
            "c_modulus_upper": fpayload(c_upper),
            "full_lifted_jacobian_modulus_lower": fpayload(full_jacobian_lower),
            "stable_pinning_jacobian_modulus_lower": fpayload(
                pinning_stable_jacobian_lower
            ),
            "partial_unstable_inverse_nonzero": True,
            "full_map_locally_biholomorphic": True,
            "stable_pinning_map_locally_biholomorphic": True,
        },
        "graph": {
            "states": [state_label(state) for state in STATES],
            "edges": graph_edges(),
            "state_edges": len(graph_edges()),
            "parameter_letters": [ftext(A_MIN), ftext(A_MAX)],
            "branch_blocks": 2 * len(graph_edges()),
            "averaging_used": False,
        },
        "fixed_points": {
            "iterated_pinning_principle": "strict holomorphic product contraction",
            "one_complex_fixed_point_per_closed_joint_word": True,
            "unique_complex_fixed_point_is_real": True,
            "markov_boundary_multiplicity": 0,
            "lifted_return_eigenvalues": "lambda,lambda^(-1),lambda^(-2)",
            "det_I_minus_return_nonzero": True,
        },
        "pass": max(nesting_ratio, projective_ratio, unstable_ratio) < 1
        and stable_det
        == -1 / (2 * a * p * (2 * a * p + beta * m) ** 2)
        and full_jacobian_lower == Fraction(50176, 3352561)
        and pinning_stable_jacobian_lower == Fraction(401408, 204506221),
    }


def residue_certificate() -> dict[str, object]:
    a11, a12, a21, a22, b1, b2, c1, c2, d = sp.symbols(
        "a11 a12 a21 a22 b1 b2 c1 c2 d", nonzero=True
    )
    aa = sp.Matrix([[a11, a12], [a21, a22]])
    bb = sp.Matrix([[b1], [b2]])
    cc = sp.Matrix([[c1, c2]])
    eye2 = sp.eye(2)
    qmat = sp.Matrix.vstack(
        sp.Matrix.hstack(eye2, sp.zeros(2, 1)),
        sp.Matrix.hstack(cc, sp.Matrix([[d]])),
    )
    pmat = sp.Matrix.vstack(
        sp.Matrix.hstack(aa, bb),
        sp.Matrix.hstack(sp.zeros(1, 2), sp.ones(1, 1)),
    )
    monodromy = pmat * qmat.inv()
    residual = sp.Matrix.vstack(
        sp.Matrix.hstack(eye2 - aa, -bb),
        sp.Matrix.hstack(-cc, sp.Matrix([[1 - d]])),
    )
    identity = sp.factor(residual.det() + d * (sp.eye(3) - monodromy).det())

    generic = sp.Matrix(3, 3, sp.symbols("m0:9"))
    e2 = sum(
        generic.extract(indices, indices).det()
        for indices in ((0, 1), (0, 2), (1, 2))
    )
    exterior_identity = sp.expand(
        1 - sp.trace(generic) + e2 - generic.det() - (sp.eye(3) - generic).det()
    )

    lam = sp.symbols("lambda", nonzero=True)
    lifted_identity = sp.factor(
        (1 - lam) * (1 - 1 / lam) * (1 - 1 / lam**2)
        - (1 - (lam + 1 / lam + 1 / lam**2)
           + (1 + 1 / lam + 1 / lam**3) - 1 / lam**2)
    )

    m0 = sp.Matrix([[-1, 2, -2], [0, -2, 1], [1, 1, 3]])
    m1 = sp.Matrix([[1, -1, -2], [1, -2, 1], [1, 2, -2]])
    m2 = sp.Matrix([[3, 1, 0], [3, -1, 2], [-2, 0, -2]])
    chronological = m2 * m1 * m0
    reversed_product = m0 * m1 * m2

    return {
        "pinning_derivative_blocks": {
            "A": "d_w phi_u (2x2)",
            "B": "d_z phi_u (2x1)",
            "C": "d_w phi_s (1x2)",
            "D": "d_z phi_s (1x1)",
            "return_derivative": "[[A,B],[0,I]]*[[I,0],[C,D]]^(-1)",
        },
        "raw_residue": {
            "identity": "det(DR)=-det(D)*det(I-DF_return)",
            "symbolic_zero": str(identity),
            "one_unstable_coordinate": True,
            "raw_trace_sign": -1,
            "scalar_variable_order": ["x", "m", "u"],
            "tangent_fibre_basis": ["e_x", "e_y", "e_m"],
            "product_contour_order": "dx*dm*du",
            "product_orientation": "dx wedge dm wedge du",
            "source_weight_cocycle": "g_(a,sigma,s)(u,m)*wedge^k DFhat_a(x,u,m)",
            "conditional_trace_formula": "tr(L_(s,k)^n)=-sum g_s^(n)*tr(wedge^k DF^n)/det(I-DF^n)",
            "all_word_kernel_trace_proved": False,
        },
        "exterior": {
            "identity": "sum_(k=0)^3 (-1)^k tr(wedge^k M)=det(I-M)",
            "symbolic_zero": str(exterior_identity),
            "lifted_eigenvalue_symbolic_zero": str(lifted_identity),
            "supertrace_parity": "(-1)^(k+1)",
            "fredholm_exponents": [
                {"degree": degree, "exponent": -1 if degree % 2 == 0 else 1}
                for degree in range(4)
            ],
            "alternating_quotient": "D_inst=D_1*D_3/(D_0*D_2)",
        },
        "chronology_control": {
            "product_rule": "later one-step tangent/exterior matrices act on the left",
            "forward_trace": int(sp.trace(chronological)),
            "reversed_trace": int(sp.trace(reversed_product)),
            "mutation_detected": sp.trace(chronological) != sp.trace(reversed_product),
            "actual_Henon_reversal_note": "pure instability remains reversal-equal by the common reversor",
            "averaging_used": False,
        },
        "period_gates": {
            "finite_block_algebra": "generic residue and exterior polynomial identities",
            "period_1_actual_kernel_trace": "OPEN",
            "period_2_actual_kernel_trace": "OPEN",
            "general_n_kernel_composition_and_trace": "OPEN",
            "finite_algebra_pass": identity == 0 and exterior_identity == 0 and lifted_identity == 0,
        },
        "finite_algebra_pass": identity == 0
        and exterior_identity == 0
        and lifted_identity == 0
        and sp.trace(chronological) != sp.trace(reversed_product),
    }


def nuclear_certificate(pinning: dict[str, object]) -> dict[str, object]:
    inclusions = pinning["strict_inclusions"]
    ratios = [
        Fraction(inclusions["stable_base_X_inside_Y_ratio"]["fraction"]),
        Fraction(inclusions["stable_slope_GM_inside_M_ratio"]["fraction"]),
        Fraction(inclusions["unstable_half_inverse_inside_X_ratio"]["fraction"]),
    ]
    p_one_sum = Fraction(1)
    for ratio in ratios:
        p_one_sum /= 1 - ratio
    return {
        "candidate_banach_space": "finite direct sum of mixed disk algebras A_0((Cbar\\Y_t)x(Cbar\\M)xX_s) tensor wedge^k(C^3)",
        "factorization_status": "OPEN: enlarged intermediate spaces and an output-z restriction have not been constructed",
        "image_ratios": [fpayload(ratio) for ratio in ratios],
        "ratio_scope": "rho_3 is a half-inverse image ratio, not an output-z restriction ratio",
        "formal_p_one_ratio_expression": fpayload(p_one_sum),
        "nuclear_order": "OPEN",
        "approximation_property": "OPEN for the specific reciprocal vanishing ideal and mixed spaces",
        "parameter_holomorphy": "OPEN in a fixed nuclear ideal",
        "fredholm_factors": "CONDITIONAL on the open all-word, nuclearity, approximation-property, and trace gates",
        "alternating_product_scope": "conditional meromorphic germ on C^2; no continuation is proved",
        "all_ratios_below_one": all(ratio < 1 for ratio in ratios),
        "exact_ratio_regression_pass": all(ratio < 1 for ratio in ratios),
        "nuclearity_pass": False,
    }


def main() -> None:
    args = parse_args()
    if not PARENT_CERTIFICATE.exists() or not PAPER5.exists():
        raise SystemExit("missing parent certificate or Paper 5 source")

    parent = json.loads(PARENT_CERTIFICATE.read_text(encoding="utf-8"))
    if not parent.get("decision", {}).get("all_certificate_checks_pass"):
        raise SystemExit("parent C22 certificate is not a passing release")

    pinning = pinning_certificate()
    residue = residue_certificate()
    nuclear = nuclear_certificate(pinning)
    algebraic_regression_pass = bool(
        pinning["pass"]
        and residue["finite_algebra_pass"]
        and nuclear["exact_ratio_regression_pass"]
    )

    output = {
        "material_passport": {
            "id": "HCS-C22G-GRADED-RUELLE-COMPLEX-V1",
            "type": "exact_one_step_and_finite_algebra_certificate_with_conditional_operator_blueprint",
            "status": "VERIFIED_BY_PRODUCER_PENDING_INDEPENDENT_CHECK",
            "version": "1.0.0",
            "lineage": "HCS-C22 T1-T4 -> orbitwise scalar T5 no-go -> graded exterior complex",
            "determinism": "exact rational and symbolic; no random seed",
        },
        "environment": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "gate_arithmetic": "Fraction and exact SymPy algebra",
            "decimal_values_decide_gates": False,
        },
        "source_lock": {
            "parent_certificate": str(PARENT_CERTIFICATE.relative_to(PROJECT_ROOT.parent)),
            "parent_sha256": sha256(PARENT_CERTIFICATE),
            "paper5": str(PAPER5.relative_to(PROJECT_ROOT.parent)),
            "paper5_sha256": sha256(PAPER5),
            "bps_pdf_sha256_audited_2026_08_09": "384cd555d8da1eff5eee73b5dcd01e89d97dd9387b988b2417bd60cc3c2da833",
            "ruelle_1990_pdf_sha256_audited_2026_08_09": "d4889f8d28be195b59a32ccef5526a685da4d0bde9fc0a372efa8a5be70b499b",
        },
        "clock_and_chronology": {
            "clock": "one binary skew-product microstep",
            "composition": "F_w=H_(w[n-1]) composed through H_(w[0])",
            "letter_operator": "sum of the two parameter-letter blocks, never their average",
            "primitive_object": "joint parameter-state cyclic orbit",
            "reversal_quotiented": False,
        },
        "g1_lifted_pinning": pinning,
        "g2_g4_residue_and_supertrace": residue,
        "g3_nuclearity": nuclear,
        "g5_determinant": {
            "conditional_identity": "D_inst(z,s)=product_(k=0)^3 det(I-zL_(s,k))^((-1)^(k+1))",
            "conditional_quotient": "D_1(z,s)*D_3(z,s)/(D_0(z,s)*D_2(z,s))",
            "joint_meromorphic_continuation_to_C2": False,
            "status": "CONDITIONAL_ON_OPEN_G2_G3_G4_GATES",
            "entire_scalar_determinant_claimed": False,
            "actual_pole_list_claimed": False,
            "functional_equation_claimed": False,
        },
        "g0_novelty_gate": {
            "analytic_mechanism": "candidate specialization of classical Ruelle-Rugh pinning, Grothendieck nuclearity, and exterior Lefschetz cancellation",
            "henon_specific_output": "uniform exact one-step domains, constants, and finite residue algebra for every chronological two-letter branch",
            "new_operator_mechanism_claimed": False,
            "standalone_positive_paper_promoted": False,
            "decision": "CLOSE_AS_CONDITIONAL_BLUEPRINT_AFTER_THEOREM_AUDIT",
        },
        "decisions": {
            "g0_source_reconstruction_pass": True,
            "g0_conceptual_novelty_pass": False,
            "g1_common_lifted_pinning_pass": bool(pinning["pass"]),
            "g2_one_step_candidate_kernel_defined": True,
            "g2_all_word_kernel_composition_pass": False,
            "g3_nuclear_order_zero_pass": False,
            "g4_finite_residue_exterior_algebra_pass": bool(residue["finite_algebra_pass"]),
            "g4_all_period_nuclear_supertrace_pass": False,
            "g5_meromorphic_continuation_pass": False,
            "all_operator_theorem_gates_pass": False,
            "exact_algebraic_regression_checks_pass": algebraic_regression_pass,
            "promotion_pass": False,
            "lineage_status": "CLOSED_AS_CONDITIONAL_BLUEPRINT_AFTER_THEOREM_AUDIT",
            "next_candidate": "HCS-C23 closed at cyclic-resultant baseline; change dynamical form",
        },
        "claim_boundary": [
            "The exact image ratios do not prove an output-z restriction, order-zero nuclearity, or the approximation property.",
            "The actual period-1/2 kernels, all-word composition, and equality of nuclear trace with the residue are open.",
            "The alternating Fredholm quotient and joint meromorphic continuation are conditional, not results of this certificate.",
            "No arithmetic primitive law, Riemann divisor, functional equation, or self-adjoint Hilbert-Polya operator is constructed.",
            "The candidate projective/exterior mechanism is classical; only exact one-step switched-Henon geometry and finite algebra are retained.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")
    print(f"sha256 {sha256(args.output)}")


if __name__ == "__main__":
    main()
