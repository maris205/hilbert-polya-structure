"""Frozen-candidate preflight, low-period audit, and conjugacy control."""

from __future__ import annotations

from typing import Any

import sympy as sp

from .algebra import CandidateField, candidate_field
from .resultant import MultiplierCertificate, certificate_record, multiplier_certificate


FROZEN_PERIODS = (1, 2, 3, 4)
FROZEN_FORMAL_DEGREES = (2, 2, 6, 12)
FROZEN_GENERIC_CYCLE_COUNTS = (2, 1, 2, 3)


def candidate_maps(field: CandidateField | None = None) -> tuple[CandidateField, sp.Poly, sp.Poly]:
    """Return the monic and inherited maps over the same exact cubic field."""

    selected = field if field is not None else candidate_field()
    u = selected.generator
    z = sp.Symbol("z")
    x = sp.Symbol("x")
    g = sp.Poly(z**2 - u, z, domain=selected.domain)
    f = sp.Poly(1 - u * x**2, x, domain=selected.domain)
    return selected, g, f


def parameter_and_conjugacy_preflight(field: CandidateField | None = None) -> dict[str, Any]:
    """Run R020--R022 without constructing any multiplier polynomial."""

    selected, g, f = candidate_maps(field)
    u = selected.generator
    U = selected.minimal_polynomial.gens[0]
    left = sp.Rational(3859, 2500)
    right = sp.Rational(15437, 10000)
    left_value = selected.minimal_polynomial.eval(left)
    right_value = selected.minimal_polynomial.eval(right)
    derivative = selected.minimal_polynomial.diff()
    monotonic_certificate = sp.expand(
        derivative.as_expr() - (3 * (U - sp.Rational(2, 3)) ** 2 + sp.Rational(2, 3))
    ) == 0

    x = f.gens[0]
    z = g.gens[0]
    phi = -u * x
    left_conjugacy = sp.Poly(phi.subs(x, f.as_expr()), x, domain=selected.domain)
    right_conjugacy = sp.Poly(g.as_expr().subs(z, phi), x, domain=selected.domain)
    conjugacy_pass = left_conjugacy == right_conjugacy
    derivative_content_pass = g.diff() == sp.Poly(2 * z, z, domain=selected.domain)
    relation_pass = selected.domain.from_sympy(u**3 - 2 * u**2 + 2 * u - 2) == selected.domain.zero
    left_negative = bool(left_value < 0)
    right_positive = bool(right_value > 0)
    checks = {
        "minimal_polynomial_relation": bool(relation_pass),
        "root_interval_left_negative": left_negative,
        "root_interval_right_positive": right_positive,
        "global_strict_monotonicity": bool(monotonic_certificate),
        "unique_real_root_selected": bool(
            left_negative and right_positive and monotonic_certificate
        ),
        "u_nonzero": bool(selected.minimal_polynomial.eval(0) != 0),
        "exact_conjugacy_phi_f_equals_g_phi": bool(conjugacy_pass),
        "derivative_content_g_prime_equals_2z": bool(derivative_content_pass),
    }
    passed = all(checks.values())
    return {
        "run_ids": ["R020", "R021", "R022"],
        "coefficient_field": "Q[u]/(u^3-2*u^2+2*u-2)",
        "root_isolation_interval": [str(left), str(right)],
        "endpoint_values": [str(left_value), str(right_value)],
        "monotonicity_identity": "P'(U)=3*(U-2/3)^2+2/3",
        "conjugacy": "phi(x)=-u*x; phi(f_u(x))=g(phi(x))",
        "checks": checks,
        "candidate_multiplier_polynomials_computed": False,
        "status": "PASS" if passed else "FAIL",
    }


def audit_candidate(
    *,
    field: CandidateField | None = None,
    max_period: int = 4,
) -> tuple[dict[str, Any], dict[int, MultiplierCertificate]]:
    """Execute the frozen exact candidate audit for periods one through four."""

    if max_period != 4:
        raise ValueError("candidate audit is source-locked to periods 1..4")
    selected, g, _ = candidate_maps(field)
    certificates = {
        period: multiplier_certificate(g, period, field=selected) for period in FROZEN_PERIODS
    }
    records = [
        certificate_record(certificates[period], field=selected, derivative_content=2)
        for period in FROZEN_PERIODS
    ]
    checks: dict[str, bool] = {
        "formal_degrees_match_freeze": tuple(item["formal_degree"] for item in records)
        == FROZEN_FORMAL_DEGREES,
        "exact_degrees_equal_formal_degrees": all(
            item["formal_degree"] == item["exact_period_degree"] for item in records
        ),
        "cycle_counts_match_freeze": tuple(item["exact_cycle_count"] for item in records)
        == FROZEN_GENERIC_CYCLE_COUNTS,
        "all_chain_rule_checks_pass": all(item["chain_rule_identity"] == "PASS" for item in records),
        "all_cycle_power_checks_pass": all(item["perfect_cycle_power"] == "PASS" for item in records),
        "all_quotient_checks_pass": all(item["quotient_annihilation"] == "PASS" for item in records),
        "all_rational_candidates_divisible_by_2_power_n": all(
            candidate["content_divisibility_pass"]
            for item in records
            for candidate in item["rational_candidate_records"]
        ),
        "no_low_period_raw_rational_prime": not any(
            candidate["raw_rational_prime"]
            for item in records
            for candidate in item["rational_candidate_records"]
        ),
        "no_low_period_odd_exponent_prime": not any(
            candidate["exponent_prime_kind"] == "EXPONENT_PRIME_ODD"
            for item in records
            for candidate in item["rational_candidate_records"]
        ),
    }
    passed = all(checks.values())
    result = {
        "run_ids": ["R031", "R032", "R033", "R034"],
        "candidate_id": "pcf_quadratic_prime_multiplier_obstruction_v1",
        "map": "g(z)=z^2-u",
        "period_cutoff": [1, 2, 3, 4],
        "coefficient_field": "Q[u]/(u^3-2*u^2+2*u-2)",
        "periods": records,
        "checks": checks,
        "raw_rational_prime_all_periods": "ABSENT_BY_THEOREM",
        "odd_exponent_prime_all_periods": "ABSENT_BY_THEOREM",
        "p2_exponent_prime_period_1": "ABSENT_BY_FIXED_POINT_CALCULATION",
        "p2_exponent_prime_period_ge_2": "OPEN",
        "external_prime_or_zero_data_accessed": False,
        "status": "PASS" if passed else "FAIL",
    }
    return result, certificates


def audit_conjugacy(
    g_certificates: dict[int, MultiplierCertificate],
    *,
    field: CandidateField | None = None,
    max_period: int = 4,
) -> dict[str, Any]:
    """Independently run ``f_u`` and compare exact normalized invariants."""

    if max_period != 4:
        raise ValueError("conjugacy audit is source-locked to periods 1..4")
    selected, g, f = candidate_maps(field)
    u = selected.generator
    z = g.gens[0]
    x = f.gens[0]
    records: list[dict[str, Any]] = []
    for period in FROZEN_PERIODS:
        g_certificate = g_certificates[period]
        f_certificate = multiplier_certificate(f, period, field=selected)
        transformed_formal = sp.Poly(
            g_certificate.dynatomic.formal.as_expr().subs(z, -u * x),
            x,
            domain=selected.domain,
        ).monic()
        transformed_exact = sp.Poly(
            g_certificate.dynatomic.exact.as_expr().subs(z, -u * x),
            x,
            domain=selected.domain,
        ).monic()
        checks = {
            "formal_dynatomic_under_phi": transformed_formal == f_certificate.dynatomic.formal,
            "exact_period_component_under_phi": transformed_exact == f_certificate.dynatomic.exact,
            "point_multiplier_resultant_equal": (
                g_certificate.point_resultant == f_certificate.point_resultant
            ),
            "cycle_multiplier_polynomial_equal": (
                g_certificate.cycle_polynomial == f_certificate.cycle_polynomial
            ),
            "rational_candidate_list_equal": (
                g_certificate.rational_candidates == f_certificate.rational_candidates
            ),
            "f_chain_rule_identity": f_certificate.chain_rule_pass,
            "f_cycle_power": f_certificate.perfect_cycle_power_pass,
            "f_quotient_annihilation": f_certificate.quotient_annihilation_pass,
        }
        records.append(
            {
                "period": period,
                "checks": checks,
                "status": "PASS" if all(checks.values()) else "FAIL",
                "f_u_certificate": certificate_record(
                    f_certificate,
                    field=selected,
                    derivative_content=2,
                ),
            }
        )
    passed = all(item["status"] == "PASS" for item in records)
    return {
        "run_id": "R021-periodic-invariant-control",
        "conjugacy": "z=-u*x",
        "normalization": "monic in the orbit variable and monic in L",
        "periods": records,
        "status": "PASS" if passed else "FAIL",
    }
