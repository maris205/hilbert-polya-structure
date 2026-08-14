"""Boundary controls that prevent over-interpretation of exact results."""

from __future__ import annotations

from typing import Any

import sympy as sp

from .algebra import polynomial_record
from .periods import L


def require_exact_parameter(value: sp.Expr) -> str:
    if value.has(sp.Float) or isinstance(value, sp.Float):
        return "REJECTED_FLOATING_PARAMETER_NO_INTEGRALITY_METADATA"
    return "EXACT_PARAMETER_ACCEPTED"


def classify_reported_modulus(*, exact: bool, rational: bool | None) -> str:
    if not exact:
        return "APPROXIMATE_MODULUS_NOT_EXACT"
    if rational is False:
        return "IRRATIONAL_MODULUS_OUTSIDE_SUPPORT_CLAIM"
    if rational is True:
        return "EXACT_RATIONAL_MODULUS_REQUIRES_SUPPORT_CERTIFICATE"
    raise ValueError("exact records require a rationality decision")


def scope_audit() -> dict[str, Any]:
    cat = sp.Matrix([[2, 1], [1, 1]])
    char = sp.Poly(L**2 - 3 * L + 1, L, domain=sp.QQ)
    roots = sp.solve(char.as_expr(), L)
    spectral_radius = (sp.Integer(3) + sp.sqrt(5)) / 2
    cat_record = {
        "matrix": [[str(item) for item in row] for row in cat.tolist()],
        "determinant": str(cat.det()),
        "characteristic_polynomial": polynomial_record(char, L),
        "eigenvalues": [sp.sstr(item) for item in roots],
        "spectral_radius": sp.sstr(spectral_radius),
        "spectral_radius_minimal_polynomial": polynomial_record(char, L),
        "spectral_radius_is_rational": bool(spectral_radius.is_rational),
        "classification": "ALGEBRAIC_UNIT_IRRATIONAL_MODULUS",
        "role": "scope control only; not a Henon novelty claim",
    }

    floating_rejection = require_exact_parameter(sp.Float("1.543689012"))
    exact_acceptance = require_exact_parameter(sp.Symbol("u"))
    irrational_guard = classify_reported_modulus(exact=True, rational=False)
    approximate_guard = classify_reported_modulus(exact=False, rational=None)

    return {
        "run_ids": ["R040", "R041", "R042", "R043"],
        "irrational_unit_scope_control": cat_record,
        "floating_parameter_guard": floating_rejection,
        "exact_parameter_guard": exact_acceptance,
        "irrational_modulus_guard": irrational_guard,
        "near_rational_display_guard": approximate_guard,
        "bad_set_provenance": {
            "candidate": [],
            "planted_control": [2],
            "derivation_time": "before multiplier computation",
            "post_hoc_enlargement_allowed": False,
        },
        "nonclaims": [
            "irrational algebraic multiplier moduli may exceed one",
            "approximate or near-rational moduli are not exact classifications",
            "singular values and Lyapunov exponents are outside scope",
            "finite periods do not prove the all-period theorem",
            "no prime-orbit correspondence or target-zero determinant is asserted",
        ],
        "pass": (
            cat.det() == 1
            and char.eval(spectral_radius) == 0
            and spectral_radius.is_rational is False
            and floating_rejection == "REJECTED_FLOATING_PARAMETER_NO_INTEGRALITY_METADATA"
            and exact_acceptance == "EXACT_PARAMETER_ACCEPTED"
            and irrational_guard == "IRRATIONAL_MODULUS_OUTSIDE_SUPPORT_CLAIM"
            and approximate_guard == "APPROXIMATE_MODULUS_NOT_EXACT"
        ),
    }

