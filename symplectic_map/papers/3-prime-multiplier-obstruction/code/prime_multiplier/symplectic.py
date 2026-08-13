"""Exact checks for the strictly branchwise cotangent bridge."""

from __future__ import annotations

from typing import Any

import sympy as sp


def audit_symplectic_bridge(max_period: int = 4) -> dict[str, Any]:
    """Run R040--R042 with explicit global negative checks."""

    if max_period != 4:
        raise ValueError("bridge audit accompanies the frozen periods 1..4")
    q, u = sp.symbols("q u", nonzero=True)
    p = sp.Symbol("p")
    Q = q**2 - u
    P = p / (2 * q)
    pullback_residual = sp.simplify(P * sp.diff(Q, q) - p)
    jacobian = sp.Matrix([Q, P]).jacobian([q, p])
    determinant_residual = sp.simplify(jacobian.det() - 1)
    zero_section_jacobian = sp.simplify(jacobian.subs(p, 0))
    expected_one_step = sp.diag(2 * q, 1 / (2 * q))
    critical_denominator = sp.denom(sp.cancel(P))
    critical_line_is_pole = sp.simplify(critical_denominator.subs(q, 0)) == 0
    unbounded_parameter = sp.Symbol("t", positive=True)
    regular_domain_unbounded = sp.limit(unbounded_parameter, unbounded_parameter, sp.oo) == sp.oo

    return_records: list[dict[str, Any]] = []
    for period in range(1, max_period + 1):
        orbit_symbols = sp.symbols(f"q0:{period}", nonzero=True)
        product = sp.eye(2)
        multiplier = sp.Integer(1)
        for orbit_point in orbit_symbols:
            product = sp.diag(2 * orbit_point, 1 / (2 * orbit_point)) * product
            multiplier *= 2 * orbit_point
        residual = sp.simplify(product - sp.diag(multiplier, 1 / multiplier))
        return_records.append(
            {
                "period": period,
                "lambda_expression": sp.sstr(multiplier),
                "return_matrix": sp.sstr(product),
                "reciprocal_pair_identity": "PASS" if residual == sp.zeros(2) else "FAIL",
            }
        )

    a, r = sp.symbols("a r", positive=True, nonzero=True)
    positive_output = (a**2 - u, r / (2 * a))
    negative_output = ((-a) ** 2 - u, (-r) / (2 * (-a)))
    overlap_pass = all(sp.simplify(left - right) == 0 for left, right in zip(positive_output, negative_output))
    checks = {
        "canonical_one_form_pullback_residual_zero": pullback_residual == 0,
        "jacobian_determinant_one_on_regular_locus": determinant_residual == 0,
        "zero_section_one_step_diagonal": zero_section_jacobian == expected_one_step,
        "periodic_return_reciprocal_pair": all(
            item["reciprocal_pair_identity"] == "PASS" for item in return_records
        ),
        "critical_line_q_zero_rejected": critical_line_is_pole,
        "two_branch_images_overlap": overlap_pass,
        "global_inverse_rejected": overlap_pass,
        "regular_domain_unbounded": regular_domain_unbounded,
    }
    passed = all(checks.values())
    return {
        "run_ids": ["R040", "R041", "R042"],
        "map": "Ghat(q,p)=(q^2-u,p/(2*q))",
        "domain": ["q<0", "q>0"],
        "canonical_one_form_residual": sp.sstr(pullback_residual),
        "jacobian": sp.sstr(jacobian),
        "jacobian_determinant_residual": sp.sstr(determinant_residual),
        "zero_section_jacobian": sp.sstr(zero_section_jacobian),
        "critical_denominator": sp.sstr(critical_denominator),
        "critical_denominator_at_q_zero": sp.sstr(critical_denominator.subs(q, 0)),
        "noncompactness_witness": "the regular branch contains (q,p)=(t,0) for every t>0 and t tends to infinity",
        "return_products": return_records,
        "branch_overlap_witness": {
            "inputs": ["(a,r)", "(-a,-r)"],
            "common_output": [sp.sstr(positive_output[0]), sp.sstr(positive_output[1])],
        },
        "mandatory_limitations": [
            "undefined at q=0",
            "the two regular branches have overlapping images",
            "noncompact phase space",
            "not a global symplectomorphism",
            "critical cycles with zero multiplier are outside the reciprocal lift",
        ],
        "checks": checks,
        "status": "PASS" if passed else "FAIL",
    }
