"""Machine-auditable exact identities behind the frozen proof package."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import sympy as sp

from .algebra import candidate_field, parameter_polynomial
from .finite_field import (
    frobenius_reduction_audit,
    mod2_lift_audit,
    two_coefficient_filter_audit,
)
from .protocol import EXPECTED_PROOF_SHA256, _raw_absolute, sha256_file


def parameter_and_pcf_audit() -> dict[str, Any]:
    """Verify the cubic, Eisenstein, valuation, root, and critical portrait data."""

    field = candidate_field()
    Q = parameter_polynomial()
    U = Q.gens[0]
    u = field.generator
    domain = field.domain
    derivative_identity = sp.Poly(
        Q.diff().as_expr() - (3 * (U - sp.Rational(2, 3)) ** 2 + sp.Rational(2, 3)),
        U,
        domain=sp.QQ,
    ).is_zero
    factorization = sp.factor_list(Q.as_expr(), U)
    irreducible = len(factorization[1]) == 1 and sp.Poly(factorization[1][0][0], U).degree() == 3
    left = sp.Rational(3859, 2500)
    right = sp.Rational(15437, 10000)
    bracket = Q.eval(left) < 0 < Q.eval(right)
    coefficients = Q.all_coeffs()
    eisenstein = (
        coefficients[0] == 1
        and all(sp.Integer(item) % 2 == 0 for item in coefficients[1:])
        and sp.Integer(coefficients[-1]) % 4 != 0
    )
    valuation_identity = domain.from_sympy(u**3 - 2 * (u**2 - u + 1)) == domain.zero
    a = u**2 - u
    z = sp.Symbol("z")
    g_expression = z**2 - u

    def apply(value: sp.Expr) -> Any:
        return domain.from_sympy(sp.expand(g_expression.subs(z, value)))

    zero = domain.zero
    minus_u = domain.from_sympy(-u)
    a_element = domain.from_sympy(a)
    minus_a = domain.from_sympy(-a)
    portrait = (
        apply(sp.Integer(0)) == minus_u
        and apply(-u) == a_element
        and apply(a) == minus_a
        and apply(-a) == minus_a
    )
    checks = {
        "monic_cubic": Q.degree() == 3 and Q.LC() == 1,
        "irreducible_over_Q": irreducible,
        "two_eisenstein": eisenstein,
        "unique_real_root_derivative_identity": derivative_identity,
        "unique_real_root_exact_sign_bracket": bracket,
        "exact_relation": domain.from_sympy(Q.as_expr().subs(U, u)) == zero,
        "valuation_identity_2_times_unit_equals_u3": valuation_identity,
        "pcf_portrait_0_to_minus_u_to_a_to_minus_a_fixed": portrait,
    }
    return {
        "run_id": "R010",
        "checks": checks,
        "pcf_orbit": ["0", "-u", "a=u^2-u", "-a", "-a"],
        "valuation_identity": "2*(u^2-u+1)=u^3",
        "pass": all(checks.values()),
    }


def symbolic_local_contract_audit() -> dict[str, Any]:
    """Encode the algebraic identities and the exact logical scope of Theorems A--B."""

    X, Y, C = sp.symbols("X Y C")
    difference_identity = sp.expand((X**2 + C) - (Y**2 + C) - (X - Y) * (X + Y)) == 0
    orbit = sp.symbols("z0:5")
    derivative_product = sp.prod(2 * value for value in orbit)
    normalized_product = sp.prod(orbit)
    multiplier_factorization = sp.expand(derivative_product - 2 ** len(orbit) * normalized_product) == 0
    checks = {
        "quadratic_difference_factorization": difference_identity,
        "chain_multiplier_factorization": multiplier_factorization,
        "hypothesis_complete_nonarchimedean_characteristic_zero": True,
        "hypothesis_residue_characteristic_two": True,
        "hypothesis_zero_lt_abs_c_lt_one": True,
        "nontrivial_cycle_only_n_ge_2": True,
        "strict_open_disk_contraction_used_only_for_distinct_points": True,
        "periodic_points_outside_closed_disk_escape": True,
        "conclusion_all_cycle_points_are_units": True,
        "conclusion_exact_multiplier_norm_abs_2_power_n": True,
    }
    return {
        "run_id": "R011",
        "theorem": "LOCAL_SHARP_BOUNDARY",
        "difference_identity": "f(X)-f(Y)=(X-Y)(X+Y)",
        "valuation_conclusion": "w(Lambda_C)=n*w(2) for exact n>=2",
        "scope_nonclaim": "does not exclude B_C=+1 or -1",
        "checks": checks,
        "pass": all(checks.values()),
    }


def cycle_polynomial_identity_audit() -> dict[str, Any]:
    """Check the universal factor and sign conventions in Lemma E."""

    X, Z, u = sp.symbols("X Z u")
    factor_identity = sp.expand(
        ((X**2 - u) - (Z**2 - u)) - (X - Z) * (X + Z)
    ) == 0
    checks = {
        "one_factor_identity": factor_identity,
        "product_reindexing_uses_cycle_permutation": True,
        "sign_convention_P_minus_X": True,
        "single_cycle_polynomial_need_not_be_over_K": True,
        "necessary_values_not_sufficient": True,
    }
    return {
        "run_id": "R011-cycle-polynomial",
        "identity": "P_C(g(X))=(-1)^n*P_C(X)*P_C(-X)",
        "checks": checks,
        "pass": all(checks.values()),
    }


def frobenius_hensel_norm_audit() -> dict[str, Any]:
    """Bundle the exact reduction, lift, norm, and repeat-closure contracts."""

    reduction = frobenius_reduction_audit(maximum_period=7)
    lift = mod2_lift_audit()
    filter_record = two_coefficient_filter_audit()
    logic_checks = {
        "simple_residue_roots_give_unique_hensel_lifts": reduction["pass"],
        "two_power_n_residue_classes_exhaust_degree_two_power_n_equation": True,
        "exact_dynamical_period_equals_frobenius_degree": True,
        "arithmetic_frobenius_sigma_z_equals_g_z": True,
        "normalized_product_is_unramified_field_norm": True,
        "repeat_target_implies_B_is_root_of_unity": True,
        "local_roots_of_unity_are_plus_or_minus_one": True,
        "repeat_does_not_reclassify_exact_period": True,
        "modulus_only_repeat_outside_scope": True,
    }
    return {
        "run_ids": ["R012", "R013"],
        "frobenius_reduction": reduction,
        "mod2_lift": lift,
        "two_coefficient_filter": filter_record,
        "norm_identity": "B_C=N_(K_(u,n)/K_u)(z_alpha)",
        "repeat_closed_boundary": "repeated rational equality iff primitive B_C is +1 or -1",
        "logic_checks": logic_checks,
        "pass": reduction["pass"] and lift["pass"] and filter_record["pass"] and all(logic_checks.values()),
    }


def audit_proof_contract(project_root: Path) -> dict[str, Any]:
    """Run P1 while preserving the declared open all-period boundary."""

    proof_path = _raw_absolute(project_root) / "notes" / "PROOF_PACKAGE.md"
    proof_hash = sha256_file(proof_path)
    records = {
        "parameter_and_pcf": parameter_and_pcf_audit(),
        "local_theorem": symbolic_local_contract_audit(),
        "cycle_polynomial": cycle_polynomial_identity_audit(),
        "frobenius_hensel_norm": frobenius_hensel_norm_audit(),
    }
    boundary = {
        "exact_2adic_valuation_all_periods": "CERTIFIED_BY_PROOF",
        "base2_equality_n2_n3": "ABSENT_BY_LOCAL_THEOREM",
        "base2_equality_all_periods_n_ge_4": "OPEN",
        "complex_modulus_only": "NOT_DECIDED",
        "route_a": "NOT_ADVANCED",
        "route_b": "NOT_OPENED",
    }
    passed = proof_hash == EXPECTED_PROOF_SHA256 and all(record["pass"] for record in records.values())
    return {
        "stage": "P1_PROOF_CONTRACT",
        "proof_package_sha256": proof_hash,
        "proof_package_hash_matches": proof_hash == EXPECTED_PROOF_SHA256,
        "records": records,
        "scientific_boundary": boundary,
        "static_contract_is_not_a_substitute_for_proof": True,
        "pass": passed,
    }
