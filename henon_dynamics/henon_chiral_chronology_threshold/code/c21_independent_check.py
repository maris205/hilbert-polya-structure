#!/usr/bin/env python3
"""Non-importing independent checker for the HCS-C21 certificate.

This checker does not import the producer or predecessor project code.  It
reconstructs the source polynomials, uses resultant determinants rather than
the producer's discriminant calls, checks the projective node and infinity
ledger, enumerates the chronological permutation action, and independently
rebuilds the half-orbit controls.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


SCHEMA = "HCS-C21-independent-check-1"
CANDIDATE = "HCS-C21"

CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
HENON = PROJECT.parent
PAPER5 = HENON / "docs" / "prior_work" / "papers" / "5-An Area-Preserving Henon-Map Model.pdf"
C12C_CERT = HENON / "henon_dihedral_chronology_obstruction" / "results" / "certificate.json"
C20_CERT = HENON / "henon_period7_dihedral_cover" / "results" / "c20_certificate.json"

EXPECTED_HASHES = {
    "paper5_pdf": "23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9",
    "hcs_c12c_certificate": "964b8c98abc850493529b8e939a9c8ff96c832300ad2b1629b1cff807f0e8020",
    "hcs_c20_certificate": "7ee43e3253aff15ec00d78b9633c3d3362e71cd5a880cd3e928e7f322abb2681",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(condition: bool, label: str, passed: list[str]) -> None:
    if not condition:
        raise AssertionError(label)
    passed.append(label)


def check_equal(actual, expected, label: str, passed: list[str]) -> None:
    check(actual == expected, f"{label}: expected {expected!r}, got {actual!r}", passed)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def squarefree_mobius(n: int) -> int:
    primes = 0
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            primes += 1
            if n % factor == 0:
                return 0
            while n % factor == 0:
                n //= factor
        factor += 1
    if n > 1:
        primes += 1
    return -1 if primes & 1 else 1


def resultant_discriminant(polynomial: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    degree = sp.degree(polynomial, variable)
    leading = sp.LC(sp.Poly(polynomial, variable))
    sign = -1 if (degree * (degree - 1) // 2) % 2 else 1
    return sp.factor(sign * sp.resultant(polynomial, sp.diff(polynomial, variable), variable) / leading)


def permutation_action_checks(passed: list[str]) -> None:
    states = tuple((eps, order) for eps in (1, -1) for order in itertools.permutations((0, 1, 2)))

    def tau(state):
        eps, order = state
        return -eps, (order[1], order[2], order[0])

    def rho(state):
        eps, order = state
        return -eps, (order[1], order[0], order[2])

    def power(function, state, exponent):
        for _ in range(exponent):
            state = function(state)
        return state

    check(len(states) == 12, "formal ordered state count", passed)
    check(all(power(tau, state, 6) == state for state in states), "tau sixth power", passed)
    for exponent in range(1, 6):
        check(not all(power(tau, state, exponent) == state for state in states), f"tau order excludes {exponent}", passed)
    check(all(rho(rho(state)) == state for state in states), "rho involution", passed)
    check(
        all(rho(tau(rho(state))) == power(tau, state, 5) for state in states),
        "dihedral conjugation relation",
        passed,
    )
    orbit = {states[0]}
    queue = [states[0]]
    while queue:
        state = queue.pop()
        for function in (tau, rho):
            image = function(state)
            if image not in orbit:
                orbit.add(image)
                queue.append(image)
    check(len(orbit) == 12, "dihedral transitivity", passed)


def reconstruct_half_orbit(n: int, A: sp.Symbol, z: sp.Symbol) -> sp.Expr:
    values = {-1: z, 0: z}
    for index in range(n // 2 + 1):
        values[index + 1] = sp.expand(A - values[index] ** 2 - values[index - 1])
    k = n // 2
    return sp.expand(values[k + 1] - values[k - 1]) if n & 1 else sp.expand(values[k] - values[k - 1])


def verify_certificate(path: Path) -> dict:
    certificate_bytes = path.read_bytes()
    certificate = json.loads(certificate_bytes)
    passed: list[str] = []

    check_equal(certificate.get("schema_version"), "HCS-C21-producer-1", "producer schema", passed)
    check_equal(certificate.get("candidate_id"), CANDIDATE, "candidate identity", passed)
    check("twelve-state" in certificate["object_scope"], "ordered-cover scope", passed)

    dependency_paths = {
        "paper5_pdf": PAPER5,
        "hcs_c12c_certificate": C12C_CERT,
        "hcs_c20_certificate": C20_CERT,
    }
    actual_hashes = {key: sha256_file(value) for key, value in dependency_paths.items()}
    check_equal(actual_hashes, EXPECTED_HASHES, "dependency byte hashes", passed)
    for key, expected in EXPECTED_HASHES.items():
        check_equal(certificate["source_lock"]["files"][key]["sha256"], expected, f"certificate source hash {key}", passed)
    clocks = certificate["source_lock"]["clock_separation"]
    check_equal(
        sorted(clocks),
        ["identified_or_averaged", "n", "r", "s"],
        "three-clock key set",
        passed,
    )
    check_equal(clocks["identified_or_averaged"], False, "three clocks are not averaged", passed)
    notation = certificate["source_lock"]["notation_separation"]
    check_equal(notation["radical_in_prose"], "eta with eta^2=A-3", "radical prose notation", passed)
    check_equal(notation["frobenius_degree_in_prose"], "r_F", "Frobenius prose notation", passed)

    # Recompute the all-period combinatorial boundary without SymPy's mobius.
    expected_rows = []
    for n in range(1, 8):
        nu = sum(squarefree_mobius(n // d) * 2**d for d in divisors(n))
        M = nu // n
        axial = sum(squarefree_mobius(n // d) * 2 ** ((d + 1) // 2) for d in divisors(n))
        parabolic = sum(squarefree_mobius(n // d) * 2 ** ((d + 2) // 2) for d in divisors(n))
        D = axial if n & 1 else axial // 2
        N = 0 if n & 1 else parabolic // 2
        C = M - D - N
        expected_rows.append((n, nu, M, D, N, C, C // 2))
    cert_rows = [
        (
            row["n"], row["exact_points"], row["cyclic_orbits"], row["diagonal_orbits"],
            row["nondiagonal_self_reversing_orbits"], row["chiral_cyclic_orbits"], row["chiral_doublets"],
        )
        for row in certificate["lower_period_chirality"]["rows"]
    ]
    check_equal(cert_rows, expected_rows, "Mobius-Burnside rows", passed)
    check_equal(certificate["lower_period_chirality"]["first_chiral_period"], 6, "first chiral count", passed)

    A, r, x = sp.symbols("A r x")
    f_r = x**3 - (1 + r) * x**2 - A * x + A * (1 + r) - 1
    f_m = x**3 - (1 - r) * x**2 - A * x + A * (1 - r) - 1
    P = sp.expand(
        x**6 - 2*x**5 + (4 - 3*A)*x**4 + (4*A - 2)*x**3
        + (3*A**2 - 8*A + 2)*x**2 + (-2*A**2 + 2*A)*x
        - A**3 + 4*A**2 - 2*A + 1
    )
    product_reduced = sp.rem(sp.expand(f_r * f_m), r**2 - A + 3, r)
    check(sp.expand(product_reduced - P) == 0, "published cubic product reconstruction", passed)
    src = certificate["period_six_source_polynomials"]
    check_equal(src["f_r"], str(f_r), "f_r exact string", passed)
    check_equal(src["f_minus_r"], str(f_m), "f_-r exact string", passed)
    check_equal(src["P6_coordinate_carrier"], str(P), "P6 exact string", passed)
    disc_P = resultant_discriminant(P, x)
    expected_disc_P = 64 * (A - 3)**3 * (16*A**2 - 8*A + 5)**2
    check(sp.expand(disc_P - expected_disc_P) == 0, "P6 Sylvester discriminant", passed)
    check_equal(src["Disc_x_P6"], str(expected_disc_P), "P6 discriminant certificate", passed)

    F = sp.expand(f_r.subs(A, r**2 + 3))
    expected_F = r**3-r**2*x+r**2-r*x**2+3*r+x**3-x**2-3*x+2
    check(sp.expand(F - expected_F) == 0, "base-changed cubic", passed)
    disc_F = resultant_discriminant(F, x)
    expected_disc_F = 16*r**4 + 88*r**2 + 125
    check(sp.expand(disc_F - expected_disc_F) == 0, "cubic Sylvester discriminant", passed)
    check(sp.gcd(sp.Poly(disc_F, r), sp.Poly(sp.diff(disc_F, r), r)).degree() == 0, "four simple cubic branch points", passed)

    # Independently check the projective node rather than trusting a genus field.
    z_h, X, Z = sp.symbols("z_h X Z")
    Fh = sp.Poly(F, r, x).homogenize(z_h).as_expr()
    local = sp.expand(Fh.subs({r: 1, x: 1 + X, z_h: Z}))
    terms2 = sum(
        term for term in local.as_ordered_terms()
        if sp.Poly(term, X, Z).total_degree() == 2
    )
    check(sp.expand(terms2 - 2*X*(X-Z)) == 0, "ordinary-node tangent cone", passed)
    affine_singular = sp.groebner([F, sp.diff(F, r), sp.diff(F, x)], r, x, order="lex")
    check(affine_singular.polys == [sp.Poly(1, r, x, domain=sp.ZZ)], "no affine singularities", passed)
    infinity_gradient = tuple(
        sp.expand(partial.subs({r: 1, x: -1, z_h: 0}))
        for partial in (sp.diff(Fh, r), sp.diff(Fh, x), sp.diff(Fh, z_h))
    )
    check(infinity_gradient != (0, 0, 0), "other infinity point smooth", passed)
    check_equal(src["scalar_coordinate_curve_normalization_genus"], 0, "scalar normalization genus", passed)
    check_equal(src["scalar_curve_infinity_node"]["affine_singular_ideal"], "(1)", "affine singularity certificate", passed)

    # Root matching and inverse by exact polynomial division.
    m_x = x**2 + 1 - (r**2 + 3) - r
    target = sp.expand(f_m.subs({A: r**2 + 3, x: m_x}))
    q_match, rem_match = sp.div(target, F, x)
    check(rem_match == 0, "forbidden matching divisibility", passed)
    inverse = sp.expand(m_x**2 + 1 - (r**2 + 3) + r)
    check(sp.rem(inverse - x, F, x) == 0, "matching inverse", passed)
    matching_cert = certificate["ordered_cover_geometry"]["matching_map"]
    check_equal(matching_cert["m_r(x)"], str(m_x), "matching formula", passed)
    check_equal(matching_cert["F_minus_r_at_m_r_div_F_r_quotient"], str(sp.factor(q_match)), "matching quotient", passed)
    check_equal(matching_cert["remainder"], "0", "matching remainder", passed)

    # Reconstruct the six-cycle using an independently specified root ideal.
    alpha, beta = sp.symbols("alpha beta")
    gamma = 1 + r - alpha - beta
    A_r = r**2 + 3
    e2_relation = sp.expand(alpha*beta + alpha*gamma + beta*gamma + A_r)
    e3_relation = sp.expand(alpha*beta*gamma - (1 - A_r*(1+r)))
    ideal = sp.groebner([e3_relation, e2_relation], beta, alpha, order="grlex", domain=sp.QQ.frac_field(r))
    m = lambda value: sp.expand(value**2 + 1 - A_r - r)
    sequence = [alpha, m(beta), gamma, m(alpha), beta, m(gamma)]
    for index in range(6):
        relation = sp.expand(sequence[(index+1) % 6] - (A_r - sequence[index]**2 - sequence[(index-1) % 6]))
        check(ideal.reduce(relation)[1] == 0, f"chronological recurrence edge {index}", passed)
    sequence_cert = certificate["ordered_cover_geometry"]["valid_ordered_edge_model"]
    check_equal(sequence_cert["six_cycle"], [str(value) for value in sequence], "six-cycle certificate", passed)
    check_equal(sequence_cert["generic_degree_over_A"], 12, "ordered cover degree", passed)
    check_equal(
        sequence_cert["edge_coordinate_convention"],
        "(x_i,x_(i+1)); forward edge shift is H_A^-1(x,y)=(y,A-y^2-x)",
        "forward-edge coordinate convention",
        passed,
    )
    check(
        "conjugate by reversal rho" in sequence_cert["comparison_to_c20_convention"],
        "C20 convention comparison",
        passed,
    )
    even_sum = sp.expand(sequence[0] + sequence[2] + sequence[4] - (1+r))
    odd_sum = sp.expand(sequence[1] + sequence[3] + sequence[5] - (1-r))
    check(ideal.reduce(even_sum)[1] == 0, "ordered orbit recovers even root sum", passed)
    check(ideal.reduce(odd_sum)[1] == 0, "ordered orbit recovers odd root sum", passed)
    check_equal(
        sequence_cert["recover_r_from_ordered_orbit"],
        "r=(x0-x1+x2-x3+x4-x5)/2",
        "ordered orbit recovers r",
        passed,
    )
    sheet_resultant = sp.factor(sp.resultant(F, f_m.subs(A, A_r), x))
    check_equal(sheet_resultant, 8*r**3, "sheet separation resultant", passed)
    check_equal(
        sequence_cert["sheet_separation_resultant"],
        str(sheet_resultant),
        "sheet separation certificate",
        passed,
    )
    check_equal(
        sequence_cert["twelve_states_distinct_on_generic_open"],
        True,
        "twelve generic states are distinct",
        passed,
    )

    permutation_action_checks(passed)
    geometry = certificate["ordered_cover_geometry"]
    c, d = sp.symbols("c d")
    coefficients = [sp.factor(value) for value in sp.Poly(sp.expand(F.subs(x, c*r+d)), r).all_coeffs()]
    check_equal(sp.factor(coefficients[0]), (c-1)**2*(c+1), "linear-root leading coefficient", passed)
    check_equal(sp.factor(coefficients[2].subs(c, 1)), 2*d*(d-1), "linear-root c=1 case", passed)
    check_equal(coefficients[3].subs(d, 0), 2, "linear-root c=1,d=0 exclusion", passed)
    check_equal(coefficients[3].subs(d, 1), -1, "linear-root c=1,d=1 exclusion", passed)
    check_equal(sp.factor(coefficients[1].subs(c, -1)), 4*d, "linear-root c=-1 case", passed)
    check_equal(coefficients[2].subs({c: -1, d: 0}), 6, "linear-root c=-1,d=0 exclusion", passed)
    check_equal(geometry["connectedness_and_group"]["f_r_absolutely_irreducible_over_Qbar(r)"], True, "absolute irreducibility certificate", passed)
    check_equal(geometry["connectedness_and_group"]["geometric_Galois_group_over_Qbar(r)"], "S3", "geometric cubic Galois group", passed)
    check_equal(geometry["connectedness_and_group"]["ordered_edge_recovers_r_and_all_three_roots"], True, "splitting-field inverse recovery", passed)
    check_equal(geometry["connectedness_and_group"]["Galois_group_over_Q(r)"], "S3", "cubic Galois group", passed)
    check_equal(geometry["connectedness_and_group"]["Galois_group_over_Q(A)"], "D6", "ordered Galois group", passed)
    check_equal(
        geometry["connectedness_and_group"]["group_convention"],
        "D6 has order 12 and is abstractly S3 x C2",
        "D6 group convention",
        passed,
    )
    check_equal(geometry["connectedness_and_group"]["group_order"], 12, "ordered group order", passed)

    # Infinity is unramified: the double leading slope splits with c=0,1.
    t, u, c = sp.symbols("t u c")
    scaled = sp.expand(t**3 * F.subs({r: 1/t, x: u/t}))
    expected_scaled = (u-1)**2*(u+1) + t*(1-u**2) + 3*t**2*(1-u) + 2*t**3
    check(sp.expand(scaled - expected_scaled) == 0, "infinity scaled cubic", passed)
    at_double = sp.expand(scaled.subs(u, 1+c*t))
    leading_t2 = sp.Poly(at_double, t).coeff_monomial(t**2)
    check(sp.expand(leading_t2 - 2*c*(c-1)) == 0, "infinity double-slope separation", passed)
    branch = geometry["branch_and_genus"]
    check_equal(branch["finite_simple_branch_points"], 4, "finite branch count", passed)
    check_equal(branch["infinity_unramified"], True, "infinity status", passed)
    rh_value = 6*(-2) + 4*3
    check_equal(rh_value, 0, "Riemann-Hurwitz arithmetic", passed)
    check_equal(branch["genus_E6"], 1, "ordered cover genus", passed)

    # The matching map reverses the Vandermonde sign because e1*e2-e3=-1.
    e1, e2, e3 = 1+r, -A_r, 1-A_r*(1+r)
    check(sp.expand(e1*e2-e3 + 1) == 0, "Vandermonde matching sign", passed)
    delta_A = 16*A**2 - 8*A + 5
    quotient_rhs = sp.expand((A-3)*delta_A)
    quotient_disc = resultant_discriminant(quotient_rhs, A)
    check_equal(int(quotient_disc), -4_000_000, "rotation quotient squarefreeness", passed)
    coh = certificate["weight_one_cohomology"]
    check_equal(coh["rotation_invariant"], "v=r*w", "rotation invariant", passed)
    check_equal(coh["rotation_quotient"], f"v^2={quotient_rhs}", "rotation quotient equation", passed)
    fixed = coh["fixed_field_ledger"]
    check_equal(fixed["tau_square_generates"], "A3", "tau-square subgroup", passed)
    check_equal(fixed["tau_cube"], "iota", "tau-cube involution", passed)
    check_equal(fixed["candidate_degree_over_Q(A)"], 2, "candidate fixed-field degree", passed)
    check_equal(
        fixed["subgroup_fixed_field_degree_over_Q(A)"],
        geometry["connectedness_and_group"]["group_order"] // geometry["label_action"]["tau_exact_order"],
        "subgroup fixed-field degree",
        passed,
    )
    check_equal(fixed["conclusion"], "Q(E6)^<tau>=Q(A,v)", "rotation fixed-field equality", passed)
    check_equal(coh["rotation_quotient_genus"], 1, "rotation quotient genus", passed)
    check_equal(coh["H1_dimension"], 2, "period-six H1 dimension", passed)
    check_equal(coh["rotation_invariant_H1_dimension"], 2, "period-six invariant H1 dimension", passed)
    check_equal(coh["tau_characteristic_polynomial_on_H1"], "(T-1)^2", "tau characteristic polynomial", passed)
    check_equal(coh["tau_minimal_polynomial_on_H1"], "T-1", "tau minimal polynomial", passed)
    check_equal(coh["nontrivial_tau_isotypic_dimension"], 0, "period-six nontrivial chronology", passed)

    # The apparent cross-period relation factors through period one.
    sigma6, sigma7 = sp.symbols("sigma6 sigma7")
    D1 = u**2 + 2*u - A
    D6 = sigma6**2 + 4*sigma6 - 4*A
    C7 = sigma7**2 - 2*sigma7 - A
    check(sp.expand(D6 - 4*D1.subs(u, sigma6/2)) == 0, "D6 through D1", passed)
    check(sp.expand(C7 - D1.subs(u, sigma7-2)) == 0, "C7 through D1", passed)
    fiber = sp.factor(sigma6**2 + 4*sigma6 - 4*(sigma7**2 - 2*sigma7))
    check_equal(fiber, (sigma6 + 2*sigma7)*(sigma6 - 2*sigma7 + 4), "two graph fiber product", passed)
    shadow = certificate["cross_period_shadow"]
    check_equal(shadow["fiber_product"]["factorization"], str(fiber), "fiber-product certificate", passed)
    check_equal(shadow["markers"]["D6_object"], "period-six reversible/diagonal orbit-sum marker; not the period-six chiral cover", "D6 marker object boundary", passed)
    check_equal(shadow["fiber_product"]["global_intersection"], "the two graphs meet at A=-1, sigma6=-2, sigma7=1", "fiber-product intersection", passed)
    check_equal(shadow["fiber_product"]["normalization"], "two disjoint graph components", "fiber-product normalization", passed)
    check("D6->D1<-C7" in shadow["interpretation"], "lower-period shadow interpretation", passed)
    morphism_obstruction = shadow["chronology_equivariant_morphism_obstruction"]
    check("dominant nonconstant rational" in morphism_obstruction["hypothesis"], "dominance hypothesis", passed)
    check("multivalued correspondences" in morphism_obstruction["not_excluded"], "correspondence boundary", passed)

    # Rebuild the half-orbit factorization and irreducibility controls.
    z = sp.symbols("z")
    D1z = z**2 + 2*z - A
    cert_half_rows = {row["n"]: row for row in shadow["half_orbit_control"]["rows"]}
    for n in (5, 6, 7):
        raw = reconstruct_half_orbit(n, A, z)
        quotient, remainder = sp.div(raw, D1z, z)
        check(remainder == 0, f"half-orbit fixed factor n={n}", passed)
        base = sp.expand(quotient.subs(A, u**2 + 2*u))
        check_equal(cert_half_rows[n]["raw_degree_z"], sp.degree(raw, z), f"half-orbit raw degree n={n}", passed)
        check_equal(cert_half_rows[n]["primitive_candidate_degree_z"], sp.degree(quotient, z), f"half-orbit quotient degree n={n}", passed)
        check_equal(cert_half_rows[n]["base_changed_factorization"], str(sp.factor(base)), f"half-orbit factorization n={n}", passed)
        if n in (5, 7):
            check(sp.Poly(base, z, domain=sp.QQ.frac_field(u)).is_irreducible, f"base irreducibility n={n}", passed)

    # Byte-bound period-seven comparison: genus 8 and quotient genus 2 imply
    # twelve nontrivial chronological H1 dimensions.
    c20 = json.loads(C20_CERT.read_text())
    c20_group = c20["group_and_genus"]
    check_equal(c20_group["geometric_group"], "D7", "C20 group dependency", passed)
    check_equal(c20_group["genus_E"], 8, "C20 genus dependency", passed)
    check_equal(c20_group["quotients"]["B=E/<tau>"]["genus"], 2, "C20 rotation quotient dependency", passed)
    nontrivial7 = 2*8 - 2*2
    check_equal(nontrivial7, 12, "period-seven nontrivial chronology arithmetic", passed)
    p7 = certificate["period_seven_comparison"]
    check_equal(p7["nontrivial_tau_isotypic_dimension"], 12, "period-seven certificate chronology", passed)
    threshold = certificate["chronology_threshold"]
    check_equal(
        threshold["first_witnessed_nontrivial_weight_one_chronology_period_within_declared_component_scope"],
        7,
        "scoped chronology threshold period",
        passed,
    )
    check_equal(
        threshold["scope"],
        (
            "source-identified and repository-certified chiral ordered components through n=7; "
            "the n=7 assertion is existential for the HCS-C20 adopted component"
        ),
        "threshold scope",
        passed,
    )

    boundary = certificate["claim_boundary"]
    expected_false = (
        "published_period6_scalar_formulas_claimed_new",
        "all_exact_period_components_classified",
        "period7_full_saturated_scheme_claimed",
        "primitive_cross_period_Hecke_bridge_claimed",
        "cross_period_Fredholm_determinant_claimed",
        "Riemann_divisor_claimed",
        "Hilbert_Polya_operator_claimed",
    )
    for key in expected_false:
        check_equal(boundary[key], False, f"claim boundary {key}", passed)
    for key in (
        "period6_ordered_cover_D6_genus1_proved",
        "period6_tau_H1_trivial_proved",
        "scoped_first_witnessed_threshold_through_n7_proved",
    ):
        check_equal(boundary[key], True, f"claim boundary {key}", passed)

    return {
        "schema_version": SCHEMA,
        "candidate_id": CANDIDATE,
        "status": "PASS",
        "checks_passed": len(passed),
        "named_checks": passed,
        "certificate_sha256": hashlib.sha256(certificate_bytes).hexdigest(),
        "dependency_hashes": actual_hashes,
        "independence": (
            "no import from c21_producer or predecessor code; resultant discriminants, "
            "projective-node and infinity calculations, alternate root-ideal order, "
            "fresh permutation enumeration, and fresh half-orbit reconstruction"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=PROJECT / "results" / "c21_certificate.json")
    parser.add_argument("--output", type=Path, default=PROJECT / "results" / "c21_independent_check.json")
    args = parser.parse_args()
    report = verify_certificate(args.certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.output}")
    print(f"status={report['status']} checks={report['checks_passed']}")


if __name__ == "__main__":
    main()
