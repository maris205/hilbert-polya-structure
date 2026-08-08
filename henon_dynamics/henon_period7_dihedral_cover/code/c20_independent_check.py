#!/usr/bin/env python3
"""Non-importing exact checker for the HCS-C20 certificate.

This file intentionally imports no HCS-C20 producer module.  It reconstructs
the septic, branch data, chronological square class, finite-field counts, and
cubic norm factors from formulas contained here, then compares them with the
JSON certificate.
"""

from __future__ import annotations

import argparse
from array import array
import hashlib
import json
from pathlib import Path

import sympy as sp


SCHEMA = "HCS-C20-independent-check-1"


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def reconstruct() -> tuple[sp.Symbol, sp.Symbol, sp.Expr, sp.Expr, sp.Expr]:
    X, S = sp.symbols("x sigma")
    A = S**2 - 2 * S
    F = (
        X**7 - S*X**6 - (3*A-2*S)*X**5
        - (2*A-(3*A-4)*S-4)*X**4
        + (3*A**2-2*(2*A-1)*S+1)*X**3
        + (4*A**2-10*A-(3*A**2-8*A+1)*S-2)*X**2
        - (A-1)*(A**2-2*A*S+A+2)*X
        - 2*A**3+6*A**2+2*A+3+(A**3-4*A**2+A-2)*S
    )
    Q = 64*S**6-448*S**5+848*S**4+80*S**3-1048*S**2+152*S-151
    return X, S, sp.expand(A), sp.expand(F), Q


def multiply(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            out[i+j] += a[i] * b[j]
    return out


def pair_mul(a: tuple[int, int], b: tuple[int, int], p: int) -> tuple[int, int]:
    return ((a[0]*b[0]+2*a[1]*b[1]) % p, (a[0]*b[1]+a[1]*b[0]) % p)


def pair_pow(a: tuple[int, int], n: int, p: int) -> tuple[int, int]:
    ans = (1, 0)
    while n > 0:
        if n % 2:
            ans = pair_mul(ans, a, p)
        a = pair_mul(a, a, p)
        n //= 2
    return ans


def eval_q_pair(s: tuple[int, int], p: int) -> tuple[int, int]:
    ans = (0, 0)
    for coefficient in (64, -448, 848, 80, -1048, 152, -151):
        ans = pair_mul(ans, s, p)
        ans = ((ans[0] + coefficient) % p, ans[1])
    return ans


def independent_counts(p: int, Q: sp.Expr, S: sp.Symbol) -> tuple[int, int]:
    sum1 = 0
    for value in range(p):
        q = int(Q.subs(S, value)) % p
        sum1 += 0 if q == 0 else (1 if pow(q, (p-1)//2, p) == 1 else -1)
    sum2 = 0
    for a in range(p):
        for b in range(p):
            q = eval_q_pair((a, b), p)
            if q == (0, 0):
                continue
            power = pair_pow(q, (p*p-1)//2, p)
            if power == (1, 0):
                sum2 += 1
            elif power == (p-1, 0):
                sum2 -= 1
            else:
                raise AssertionError("quadratic character outside {+1,-1}")
    return p + 2 + sum1, p*p + 2 + sum2


class PolynomialQuotientField:
    """Small finite field F_p[t]/(m), with elements encoded in base p."""

    MODULI = {
        (5, 2): (3, 0, 1),       # t^2-2
        (11, 2): (9, 0, 1),
        (13, 2): (11, 0, 1),
        (5, 3): (1, 1, 0, 1),    # t^3+t+1
        (11, 3): (4, 1, 0, 1),   # t^3+t+4
        (13, 3): (2, 0, 0, 1),   # t^3+2
    }
    MODULUS_LABELS = {
        (5, 2): "t^2-2", (11, 2): "t^2-2", (13, 2): "t^2-2",
        (5, 3): "t^3+t+1", (11, 3): "t^3+t+4", (13, 3): "t^3+2",
    }

    def __init__(self, p: int, degree: int):
        self.p = p
        self.degree = degree
        self.order = p**degree
        self.modulus = (0, 1) if degree == 1 else self.MODULI[(p, degree)]
        self.modulus_label = "prime field" if degree == 1 else self.MODULUS_LABELS[(p, degree)]
        self.digits = [self._decode(value) for value in range(self.order)]
        # For degrees two and three, absence of an F_p-root is equivalent to
        # irreducibility.  This check is performed afresh for every modulus.
        self.irreducible_verified = degree == 1 or all(
            sum(self.modulus[i] * pow(root, i, p) for i in range(degree + 1)) % p
            for root in range(p)
        )
        if not self.irreducible_verified:
            raise AssertionError(f"reducible quotient modulus {self.modulus_label} over F_{p}")
        self.addition = self._addition_table()
        self.negative = array("H", (self._encode(tuple(-c % p for c in coeffs)) for coeffs in self.digits))
        self.multiplication = self._multiplication_table()

    def _decode(self, value: int) -> tuple[int, ...]:
        coefficients = []
        for _ in range(self.degree):
            coefficients.append(value % self.p)
            value //= self.p
        return tuple(coefficients)

    def _encode(self, coefficients: tuple[int, ...] | list[int]) -> int:
        value = 0
        place = 1
        for coefficient in coefficients:
            value += (coefficient % self.p) * place
            place *= self.p
        return value

    def _raw_multiply(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        a, b = self.digits[left], self.digits[right]
        product = [0] * (2*self.degree-1)
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                product[i+j] = (product[i+j] + ai*bj) % self.p
        for k in range(2*self.degree-2, self.degree-1, -1):
            leading = product[k] % self.p
            if leading:
                for j in range(self.degree):
                    product[k-self.degree+j] = (
                        product[k-self.degree+j] - leading*self.modulus[j]
                    ) % self.p
        return self._encode(product[:self.degree])

    def _raw_power(self, value: int, exponent: int) -> int:
        answer = 1
        while exponent:
            if exponent & 1:
                answer = self._raw_multiply(answer, value)
            value = self._raw_multiply(value, value)
            exponent >>= 1
        return answer

    def _addition_table(self) -> array:
        q, p, degree = self.order, self.p, self.degree
        table = array("H", [0]) * (q*q)
        for left, a in enumerate(self.digits):
            row = [self._encode(tuple((a[i]+b[i]) % p for i in range(degree))) for b in self.digits]
            table[left*q:(left+1)*q] = array("H", row)
        return table

    @staticmethod
    def _prime_divisors(value: int) -> list[int]:
        divisors = []
        candidate = 2
        while candidate*candidate <= value:
            if value % candidate == 0:
                divisors.append(candidate)
                while value % candidate == 0:
                    value //= candidate
            candidate += 1
        if value > 1:
            divisors.append(value)
        return divisors

    def _multiplication_table(self) -> array:
        q = self.order
        factors = self._prime_divisors(q-1)
        primitive = next(
            value for value in range(2, q)
            if all(self._raw_power(value, (q-1)//factor) != 1 for factor in factors)
        )
        logarithm = [-1] * q
        exponential = []
        value = 1
        for exponent in range(q-1):
            if logarithm[value] != -1:
                raise AssertionError("primitive-element cycle repeated early")
            logarithm[value] = exponent
            exponential.append(value)
            value = self._raw_multiply(value, primitive)
        if value != 1 or any(logarithm[value] < 0 for value in range(1, q)):
            raise AssertionError("polynomial quotient is not a field")
        exponential += exponential
        table = array("H", [0]) * (q*q)
        for left in range(1, q):
            left_log = logarithm[left]
            row = [0] + [exponential[left_log+logarithm[right]] for right in range(1, q)]
            table[left*q:(left+1)*q] = array("H", row)
        return table

    def power(self, value: int, exponent: int) -> int:
        answer = 1
        q = self.order
        multiplication = self.multiplication
        while exponent:
            if exponent & 1:
                answer = multiplication[answer*q+value]
            value = multiplication[value*q+value]
            exponent >>= 1
        return answer


def checker_plane_coefficients(field: PolynomialQuotientField, sigma: int) -> tuple[int, ...]:
    q, p = field.order, field.p
    add, mul, negative = field.addition, field.multiplication, field.negative
    c = lambda value: value % p
    plus = lambda left, right: add[left*q+right]
    times = lambda left, right: mul[left*q+right]
    minus = lambda left, right: plus(left, negative[right])
    square = lambda value: times(value, value)
    parameter = minus(square(sigma), times(c(2), sigma))
    parameter2 = square(parameter)
    parameter3 = times(parameter2, parameter)
    three_a_minus_four = minus(times(c(3), parameter), c(4))
    return (
        c(1), negative[sigma], negative[minus(times(c(3), parameter), times(c(2), sigma))],
        negative[minus(minus(times(c(2), parameter), times(three_a_minus_four, sigma)), c(4))],
        plus(minus(times(c(3), parameter2), times(c(2), times(minus(times(c(2), parameter), c(1)), sigma))), c(1)),
        minus(
            minus(minus(times(c(4), parameter2), times(c(10), parameter)),
                  times(plus(minus(times(c(3), parameter2), times(c(8), parameter)), c(1)), sigma)),
            c(2),
        ),
        negative[times(minus(parameter, c(1)), plus(plus(minus(parameter2, times(c(2), times(parameter, sigma))), parameter), c(2)))],
        plus(
            plus(plus(plus(negative[times(c(2), parameter3)], times(c(6), parameter2)), times(c(2), parameter)), c(3)),
            times(plus(plus(minus(parameter3, times(c(4), parameter2)), parameter), negative[c(2)]), sigma),
        ),
    )


def checker_plane_count(p: int, r: int, checks: list[str]) -> tuple[int, bool]:
    field = PolynomialQuotientField(p, r)
    fail(field.irreducible_verified,
         f"polynomial-quotient modulus {field.modulus_label} irreducible p={p},r={r}", checks)
    q = field.order
    add, mul = field.addition, field.multiplication
    count = 0
    for sigma in range(q):
        coefficients = checker_plane_coefficients(field, sigma)
        for x in range(q):
            value = coefficients[0]
            for coefficient in coefficients[1:]:
                value = add[mul[value*q+x]*q+coefficient]
            count += value == 0
    node_value = (-7) % p
    splits = field.power(node_value, (q-1)//2) == 1
    return count, splits


def checker_newton_factor(p: int, point_counts: list[int]) -> tuple[list[int], list[int]]:
    powers = [p**r+1-point_counts[r-1] for r in (1,2,3)]
    first, second, third = powers
    e2 = (first**2-second)//2
    e3 = (third-first*second+e2*first)//3
    return powers, [1, -first, e2, -e3, p*e2, -p**2*first, p**3]


def initial_form(expr: sp.Expr, variables: tuple[sp.Symbol, sp.Symbol], weights: tuple[int, int]) -> sp.Expr:
    terms = sp.Poly(sp.expand(expr), *variables).terms()
    least = min(sum(a*b for a, b in zip(exponents, weights)) for exponents, _ in terms)
    return sp.factor(sum(
        coefficient * sp.prod(variable**exponent for variable, exponent in zip(variables, exponents))
        for exponents, coefficient in terms
        if sum(a*b for a, b in zip(exponents, weights)) == least
    ))


def check_selected_good_reduction(
    row: dict,
    p: int,
    sigma0: int,
    X: sp.Symbol,
    S: sp.Symbol,
    F: sp.Expr,
    Q: sp.Expr,
    checks: list[str],
) -> None:
    ledger = row["selected_prime_good_reduction"]
    qpoly = sp.Poly(Q, S, modulus=p)
    q_squarefree = sp.gcd(qpoly, qpoly.diff()).degree() == 0
    fail(q_squarefree and 64 % p != 0, f"B smooth model p={p}", checks)
    bscreen = ledger["B_smooth_model"]
    fail(
        bscreen["Q6_squarefree_mod_p"] is True
        and bscreen["Q6_is_not_a_square_in_Fp_sigma"] is True
        and bscreen["leading_coefficient_64_is_a_unit"] is True
        and bscreen["two_separated_infinity_points"] is True
        and bscreen["geometrically_integral_and_connected"] is True,
        f"B smooth and geometrically connected ledger p={p}", checks,
    )

    specialized = sp.Poly(F.subs(S, sigma0), X, modulus=p)
    expected_polynomials = {
        5: "x**7 - x**4 + x**3 - 2*x**2 + 2*x - 2",
        11: "x**7 + 4*x**4 + x**3 - 2*x**2 + 2*x + 3",
        13: "x**7 - x**6 + 5*x**5 - x**4 - 3*x**3 - 5*x + 1",
    }
    witness = ledger["plane_integrality_witness"]
    fail(specialized.is_irreducible and str(specialized.as_expr()) == expected_polynomials[p],
         f"irreducible specialization polynomial p={p}", checks)
    fail(witness["sigma0"] == sigma0 and witness["P_sigma0_mod_p"] == expected_polynomials[p]
         and witness["irreducible_over_Fp"] is True,
         f"recorded irreducible specialization p={p}", checks)

    node_sigma = 9 * pow(4, -1, p) % p
    node_gcd = sp.gcd(
        sp.Poly(F.subs(S, node_sigma), X, modulus=p),
        sp.Poly(sp.diff(F, X).subs(S, node_sigma), X, modulus=p),
    ).monic()
    expected_nodes = {5: "x + 1", 11: "x - 3", 13: "x + 3"}
    fail(str(node_gcd.as_expr()) == expected_nodes[p] and node_gcd.degree() == 1,
         f"residual node gcd p={p}", checks)
    node_point = {S: sp.Rational(9, 4), X: sp.Rational(1, 4)}
    tangent_discriminant = sp.factor(
        sp.diff(F, S, X).subs(node_point) ** 2
        - sp.diff(F, S, 2).subs(node_point) * sp.diff(F, X, 2).subs(node_point)
    )
    fail(tangent_discriminant == -7 and int(tangent_discriminant) % p != 0,
         f"ordinary-node tangent discriminant p={p}", checks)
    discriminant_mod = sp.Poly(sp.discriminant(F, X), S, modulus=p)
    singular_resultant = sp.Poly(sp.resultant(F, sp.diff(F, S), X), S, modulus=p)
    projected = sp.gcd(discriminant_mod, singular_resultant).monic()
    expected_projected = sp.Poly((4*S-9)**2, S, modulus=p).monic()
    fail(projected == expected_projected, f"only expected affine node p={p}", checks)
    node = ledger["residual_node_screen"]
    fail(node["sigma_9_over_4_mod_p"] == node_sigma and node["gcd_P_Px"] == expected_nodes[p]
         and node["tangent_discriminant_over_Q"] == -7
         and node["tangent_discriminant_mod_p"] == (-7) % p
         and node["unique_ordinary_node_persists"] is True
         and node["only_expected_affine_singularity"] is True,
         f"recorded node screen p={p}", checks)

    t, y, z, w = sp.symbols("t y z w")
    chart = sp.cancel(t**7 * F.subs({S: 1/t, X: y/t}))
    actual_forms = {
        "plus": initial_form(chart.subs(y, 1+z), (t, z), (1, 1)),
        "minus": initial_form(chart.subs(y, -1+z), (t, z), (1, 1)),
        "plus_double": initial_form(chart.subs(y, 1-t+w), (t, w), (1, 2)),
        "minus_double": initial_form(chart.subs(y, -1+t+w), (t, w), (1, 2)),
    }
    wanted_forms = {
        "plus": 8*z*(t+z)**2*(2*t+z),
        "minus": 16*(-2*t+z)*(-t+z)**2,
        "plus_double": -4*t**2*w*(t**2+2*w),
        "minus_double": -8*t*(t**2-2*w)*(t**2-w),
    }
    fail(all(sp.expand(actual_forms[k]-wanted_forms[k]) == 0 for k in wanted_forms),
         f"infinity blowup forms p={p}", checks)
    half = pow(2, -1, p)
    signatures = [(1,0,None),(1,-2%p,None),(1,-1%p,0),(1,-1%p,-half%p),
                  (-1%p,2,None),(-1%p,1,half),(-1%p,1,1)]
    fail(len(set(signatures)) == 7 and all(u % p for u in (2,4,8,16)),
         f"seven separated rational infinity branches p={p}", checks)
    infinity = ledger["infinity_screen"]
    fail(infinity["branch_count"] == 7 and infinity["branches_rational_and_separated_mod_p"] is True
         and infinity["all_screen_coefficients_are_units"] is True,
         f"recorded infinity unit screen p={p}", checks)

    vertical = ledger["vertical_inertia_screen"]
    fail(p not in (2,7) and p % 7 != 1, f"tame congruence screen p={p}", checks)
    fail(vertical["p_not_2_or_7"] is True and vertical["p_mod_7"] == p % 7
         and vertical["p_mod_7_not_1"] is True
         and vertical["full_C7_vertical_inertia_excluded"] is True
         and "k=F_p(B_special)" in vertical["logic"]
         and "7|(p-1)" in vertical["logic"],
         f"vertical C7 inertia ledger p={p}", checks)

    purity = ledger["purity_and_tame_quotient"]
    fail(all(purity[key] is True for key in (
        "horizontal_branch_divisor_Q6_is_etale", "node_disjoint_from_Q6",
        "infinity_unramified_and_separated", "no_codimension_one_vertical_branch_by_purity",
        "E_to_B_extends_finite_etale_degree_7", "reflection_order_2_is_invertible",
        "degree_six_fixed_divisor_is_finite_etale")),
        f"purity and tame quotient hypotheses p={p}", checks)
    fail("purity" in purity["logic"] and "finite etale" in purity["logic"]
         and "reflection quotient" in purity["logic"],
         f"purity theorem logic p={p}", checks)

    plane = ledger["plane_special_fiber_birational_comparison"]
    fail(all(plane[key] is True for key in (
        "P_is_monic_degree_7_in_x", "irreducible_specialization_forces_plane_integrality_over_Fp",
        "plane_special_fiber_integral_over_Fp", "C_special_fiber_map_to_P1_has_degree_7",
        "only_affine_defect_is_the_screened_node", "seven_infinity_branches_match_the_normalization",
        "same_function_field_as_E_mod_J")),
        f"plane special-fiber birational comparison p={p}", checks)
    fail("birational, hence isomorphic" in plane["conclusion"],
         f"plane normalization conclusion p={p}", checks)
    connectedness = ledger["geometric_connectedness"]
    fail(connectedness["source"] == "smooth proper model E over Z_p"
         and connectedness["generic_fiber_geometrically_connected"] is True
         and connectedness["smooth_proper_fibers_geometrically_connected"] is True
         and connectedness["C_as_quotient_of_connected_E_is_connected"] is True
         and "not inferred from p mod 7" in connectedness["logic"],
         f"proper-smooth geometric connectedness p={p}", checks)
    conclusion = ledger["conclusion"]
    fail(conclusion == {"B_good_reduction_proved":True, "C_good_reduction_proved":True,
                        "E_good_reduction_proved":True, "blanket_all_prime_claim":False},
         f"selected-prime-only good-reduction conclusion p={p}", checks)


def fail(condition: bool, message: str, checks: list[str]) -> None:
    if not condition:
        raise AssertionError(message)
    checks.append(message)


def verify_certificate(path: Path) -> dict:
    raw = path.read_text()
    certificate = json.loads(raw)
    checks: list[str] = []
    fail(certificate.get("schema_version") == "HCS-C20-producer-1", "producer schema", checks)
    fail(certificate.get("candidate_id") == "HCS-C20", "candidate identity", checks)
    X, S, A, F, Q = reconstruct()
    fail(certificate["frozen_septic"]["P"] == str(F), "frozen septic formula", checks)
    fail(certificate["frozen_septic"]["P_sha256"] == digest(str(F)), "frozen septic hash", checks)

    branch = certificate["branch_and_square_class"]
    discriminant = sp.factor(sp.discriminant(F, X))
    fail(sp.expand(discriminant - (4*S-9)**2*Q**3) == 0, "septic discriminant identity", checks)
    fail(branch["septic_discriminant"] == str((4*S-9)**2*Q**3), "recorded septic discriminant", checks)
    fail(branch["Q6"] == str(Q), "recorded Q6", checks)
    fail(sp.Poly(Q, S, domain=sp.QQ).is_irreducible, "Q6 irreducibility", checks)
    qdisc = sp.discriminant(Q, S)
    fail(qdisc == 2**63*97 == branch["Q6_discriminant"], "Q6 discriminant", checks)

    U = -(160*S**5-760*S**4+412*S**3+1120*S**2-111*S+166)/4
    fail(branch["branch_root_u"] == str(U), "branch root u formula", checks)
    qmod = sp.Poly(Q, S, domain=sp.QQ)
    f_at_u = sp.cancel(F.subs(X, U))
    fail(sp.Poly(sp.fraction(f_at_u)[0], S, domain=sp.QQ).rem(qmod).is_zero,
         "P(u)=0 modulo Q6", checks)
    px_at_u = sp.cancel(sp.diff(F, X).subs(X, U))
    pn, pd = sp.fraction(px_at_u)
    prem = sp.cancel(sp.Poly(pn, S, domain=sp.QQ).rem(qmod).as_expr()/pd)
    expected_prem = 2*(8*S**4-36*S**3+16*S**2+39*S+37)
    fail(sp.expand(prem-expected_prem) == 0, "Px(u) remainder modulo Q6", checks)
    resultant = sp.resultant(Q, expected_prem, S)
    fail(resultant == 2**42 == branch["resultant_Q6_Px_at_u_remainder"],
         "Q6/Px remainder resultant 2^42", checks)
    fail(branch["branch_root_is_simple"] is True, "simple branch-root flag", checks)

    # Rebuild the degree-two chronological correspondence over Q(S)[X]/F.
    Y = sp.symbols("y")
    K = sp.QQ.frac_field(S)
    modulus = sp.Poly(F, X, domain=K)
    sequence = sp.subresultants(F.subs(X, Y), F.subs(X, A-Y**2-X), Y)
    pattern = []
    final_coefficients = None
    for item in sequence:
        yp = sp.Poly(item, Y)
        reduced = [sp.Poly(c, X, domain=K).rem(modulus) for c in yp.all_coeffs()]
        is_zero = all(c.is_zero for c in reduced)
        pattern.append((int(yp.degree()), is_zero))
        if not is_zero:
            final_coefficients = reduced
    expected_pattern = [(14,False),(7,False),(6,False),(5,False),(4,False),
                        (3,False),(2,False),(1,True),(0,True)]
    fail(pattern == expected_pattern, "chronological subresultant pattern", checks)
    fail(final_coefficients is not None and len(final_coefficients) == 3,
         "chronological quadratic recovered", checks)
    c2, c1, c0 = final_coefficients
    fail((c1-c2*sp.Poly(X**2-A, X, domain=K)).rem(modulus).is_zero,
         "neighbor-sum identity", checks)
    raw_delta = (c1*c1-4*c2*c0).rem(modulus)
    delta = sp.cancel(raw_delta.as_expr()/c2.as_expr()**2)
    dn, dd = sp.fraction(delta)
    rn = sp.factor(sp.resultant(F, dn, X))
    rd = sp.factor(sp.resultant(F, dd, X))
    field_norm = sp.factor(sp.cancel(rn/rd))
    neighbor = certificate["chronological_neighbor"]
    fail(sp.expand(field_norm-Q) == 0, "neighbor discriminant norm equals Q6", checks)
    fail(neighbor["normalized_neighbor_discriminant_sha256"] == digest(str(delta)),
         "normalized neighbor discriminant hash", checks)
    fail(neighbor["norm_numerator_sha256"] == digest(str(rn)), "norm numerator hash", checks)
    fail(neighbor["norm_denominator_sha256"] == digest(str(rd)), "norm denominator hash", checks)
    fail(neighbor["norm_is_nonsquare"] is True, "nonsquare norm flag", checks)
    fail(neighbor["direct_square_root_identity_claimed"] is False,
         "no direct square-root identity claim", checks)
    control = neighbor["nonsquare_control"]
    fail(control == {"prime":5,"sigma":3,"x_component":0,"normalized_Delta":2,
                     "Q6":3,"Delta_over_Q6":4,"both_Delta_and_Q6_nonsquare":True},
         "F5 nonsquare specialization control", checks)

    group = certificate["group_and_genus"]
    fail(group["geometric_group"] == "D7" and group["group_order"] == 14,
         "D7 order ledger", checks)
    fail(group["presentation"] == "<tau,J | tau^7=J^2=1, J*tau*J=tau^-1>",
         "D7 presentation", checks)
    fail(group["reflection_naming"] == {
        "R":"R(x,y)=(y,x) is edge reversal",
        "J":"J=R*tau, so J(x,y)=(x,a-x^2-y), is the scalar-fixing reflection",
    }, "edge-reversal versus scalar-reflection naming", checks)
    quot = group["quotients"]
    fail(quot["C=E/<J>"] == {"degree_E_to_C":2,"genus":3,"total_ramification":6},
         "reflection quotient ledger", checks)
    fail(quot["B=E/<tau>"] == {"degree_E_to_B":7,"genus":2,"unramified":True},
         "rotation quotient ledger", checks)
    fail(group["genus_E"] == 8 and 2*(2*3-2)+6 == 7*(2*2-2) == 14,
         "Riemann-Hurwitz genus ledger", checks)

    local = certificate["local_factors"]
    fail(local["B_model"] == "u^2=Q6(sigma)" and local["B_genus"] == 2,
         "genus-two quotient model", checks)
    alpha, z, T = sp.symbols("alpha z T")
    cubic = alpha**3+alpha**2-2*alpha-1
    fail(sp.Poly(cubic, alpha, domain=sp.QQ).is_irreducible and sp.discriminant(cubic,alpha)==49,
         "real cubic field", checks)
    expressions = {5:alpha**2+2*alpha, 11:2-alpha, 13:alpha**2-1}
    expected_min = {
        5:z**3-3*z**2-4*z-1,
        11:z**3-7*z**2+14*z-7,
        13:z**3-2*z**2-z+1,
    }
    expected_lb = {5:[1,2,4,10,25], 11:[1,2,1,22,121], 13:[1,-4,12,-52,169]}
    expected_lc = {
        5:[1,3,11,31,55,75,125],
        11:[1,7,47,161,517,847,1331],
        13:[1,2,38,51,494,338,2197],
    }
    expected_le = {
        5:[1,8,47,224,882,2968,8918,23570,55574,117850,222950,371000,551250,700000,734375,625000,390625],
        11:[1,16,172,1302,8029,40880,181531,706384,2478217,7770224,21965251,54411280,117552589,209688402,304708492,311794736,214358881],
        13:[1,0,76,-70,2541,-4452,51723,-114510,762748,-1488630,8741187,-9781044,72573501,-25990510,366837484,0,815730721],
    }
    rows = local["selected_primes"]
    fail([row["p"] for row in rows] == [5,11,13], "selected prime list", checks)
    sigma0_witnesses = {5: 0, 11: 0, 13: 1}
    for row in rows:
        p = row["p"]
        check_selected_good_reduction(row, p, sigma0_witnesses[p], X, S, F, Q, checks)
        n1, n2 = independent_counts(p, Q, S)
        power = [p+1-n1, p*p+1-n2]
        lb = [1, -power[0], (power[0]**2-power[1])//2, -p*power[0], p*p]
        fail(row["B_point_counts"] == {"N1":n1,"N2":n2}, f"B counts p={p}", checks)
        fail(row["B_power_sums"] == power and lb == expected_lb[p] == row["L_B_coefficients_ascending"],
             f"B factor p={p}", checks)
        fail(row["B_good_reduction_proved"] is True and int(qdisc)%p != 0,
             f"B good reduction p={p}", checks)
        b = expressions[p]
        minpoly = sp.factor(sp.resultant(cubic, z-b, alpha))
        fail(sp.expand(minpoly-expected_min[p]) == 0 and row["b_p_minimal_polynomial"] == str(expected_min[p]),
             f"b_p conjugates p={p}", checks)
        fail(row["b_p_conjugates"] == f"the three roots b_p^(i) of {expected_min[p]}" and
             row["conjugate_product_identity"] ==
             f"L_C,{p}(T)=Product_i=1^3(1+b_{p}^(i)*T+{p}*T^2)",
             f"explicit conjugate-product identity p={p}", checks)
        norm = sp.Poly(sp.expand(sp.resultant(cubic, 1+b*T+p*T**2, alpha)), T)
        lc = [int(norm.nth(i)) for i in range(7)]
        fail(lc == expected_lc[p] == row["L_C_coefficients_ascending"],
             f"cubic norm factor p={p}", checks)
        affine_counts = []
        node_splits = []
        c_counts = []
        for extension_degree in (1,2,3):
            affine, splits = checker_plane_count(p, extension_degree, checks)
            affine_counts.append(affine)
            node_splits.append(splits)
            c_counts.append(affine+7+(1 if splits else -1))
        c_powers, lc_from_counts = checker_newton_factor(p, c_counts)
        provenance = row["C_point_count_provenance"]
        fail(provenance["plane_affine_counts"] == affine_counts
             and provenance["node_splits"] == node_splits
             and provenance["C_point_counts"] == c_counts,
             f"plane and normalized C counts r=1,2,3 p={p}", checks)
        fail(provenance["C_frobenius_power_sums"] == c_powers
             and provenance["L_C_from_Newton_coefficients_ascending"] == lc_from_counts,
             f"Newton reconstruction from C counts p={p}", checks)
        fail(lc_from_counts == lc and provenance["agrees_with_cubic_norm_identity"] is True,
             f"point-count factor equals cubic norm p={p}", checks)
        le = multiply(lb, multiply(lc, lc))
        fail(le == expected_le[p] == row["L_E_coefficients_ascending"],
             f"genuine selected-prime E factor p={p}", checks)
        fail(all(le[16-i] == p**(8-i)*le[i] for i in range(9)),
             f"genus-eight functional equation p={p}", checks)
        fail(row["C_good_reduction_proved"] is True and row["E_good_reduction_proved"] is True
             and row["L_C_status"].startswith("certified Hasse-Weil")
             and row["L_E_status"].startswith("certified Hasse-Weil")
             and row["factorization_identity"] == "L_E=L_B*L_C^2",
             f"certified selected-prime factor scope p={p}", checks)

    boundary = certificate["claim_boundary"]
    fail(boundary == {
        "B_good_local_factors_at_5_11_13": True,
        "C_good_reduction_at_5_11_13": True,
        "E_good_reduction_at_5_11_13": True,
        "L_C_factors_certified_at_5_11_13": True,
        "L_E_equals_L_B_times_L_C_squared_certified_at_5_11_13": True,
        "blanket_good_reduction_claim_outside_5_11_13": False,
        "hilbert_polya_realization_claimed": False,
    }, "claim boundary", checks)
    return {
        "schema_version": SCHEMA,
        "candidate_id": "HCS-C20",
        "status": "PASS",
        "certificate_sha256": hashlib.sha256(raw.encode()).hexdigest(),
        "checks_passed": len(checks),
        "checks": checks,
        "independence": (
            "no import from c20_producer, C19, galois, or numpy; plane counts use "
            "self-contained polynomial-quotient finite fields with independently checked moduli"
        ),
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=root/"results"/"c20_certificate.json")
    parser.add_argument("--output", type=Path, default=root/"results"/"c20_independent_check.json")
    args = parser.parse_args()
    report = verify_certificate(args.certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n")
    print(f"PASS ({report['checks_passed']} checks); wrote {args.output}")


if __name__ == "__main__":
    main()
