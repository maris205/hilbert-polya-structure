#!/usr/bin/env python3
"""Fail-closed independent checker for the HCS-C33 exact certificate.

The checker does not import the producer.  It reconstructs the chronological
map, action, resultants, quotient-field node, Hill determinant, field norm,
and finite controls from the certificate's mathematical definitions.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import traceback
import warnings
from pathlib import Path
from typing import Any, Callable

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning

warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)


SCHEMA = "HCS-C33-PHASE3-KUMMER-1"
CANDIDATE = "HCS-C33_HENON_ACTION_COLLISION_KUMMER"
A, Q, P, C = sp.symbols("A q p c")
QQ = sp.QQ
PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parent.parent
SOURCE_PATHS = (
    "henon_dynamics/phase1_hcs_c33_henon_action_collision_kummer/RESEARCH_QUESTION_BRIEF.md",
    "henon_dynamics/phase1_hcs_c33_henon_action_collision_kummer/METHODOLOGY_BLUEPRINT.md",
    "henon_dynamics/phase1_hcs_c33_henon_action_collision_kummer/PILOT_LEDGER.md",
    "henon_dynamics/phase1_hcs_c33_henon_action_collision_kummer/DEVILS_ADVOCATE_CHECKPOINT1.md",
    "henon_dynamics/phase2_hcs_c33_henon_action_collision_kummer/SEARCH_STRATEGY.md",
    "henon_dynamics/phase2_hcs_c33_henon_action_collision_kummer/SOURCE_CORPUS_AND_ANNOTATED_BIBLIOGRAPHY.md",
    "henon_dynamics/phase2_hcs_c33_henon_action_collision_kummer/SOURCE_VERIFICATION_REPORT.md",
    "henon_dynamics/henon_frobenius_scheme_obstruction/code/c12a_producer.py",
    "henon_dynamics/phase3_hcs_c32_artin_schreier_quantum_trace/results/c32_morse_gate_certificate.json",
    "henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf",
)


class GateFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def exact_keys(value: Any, keys: set[str], where: str) -> dict[str, Any]:
    require(type(value) is dict, f"{where}: expected object")
    require(set(value) == keys, f"{where}: key mismatch {set(value) ^ keys}")
    return value


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(strict_equal(left[key], right[key]) for key in left)
    if type(left) in (list, tuple):
        return len(left) == len(right) and all(strict_equal(a, b) for a, b in zip(left, right))
    return left == right


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def decode_rational(value: Any, where: str) -> sp.Rational:
    item = exact_keys(value, {"numerator", "denominator"}, where)
    require(type(item["numerator"]) is int, f"{where}.numerator: non-integer")
    require(type(item["denominator"]) is int and item["denominator"] > 0, f"{where}.denominator invalid")
    require(math.gcd(abs(item["numerator"]), item["denominator"]) == 1, f"{where}: noncanonical rational")
    return sp.Rational(item["numerator"], item["denominator"])


def decode_poly(value: Any, variables: tuple[sp.Symbol, ...], where: str) -> sp.Expr:
    item = exact_keys(value, {"variables", "terms"}, where)
    require(strict_equal(item["variables"], [str(variable) for variable in variables]), f"{where}: variables changed")
    require(type(item["terms"]) is list, f"{where}.terms: expected list")
    seen: set[tuple[int, ...]] = set()
    previous: tuple[int, ...] | None = None
    expression = sp.Integer(0)
    for index, term_value in enumerate(item["terms"]):
        term = exact_keys(term_value, {"exponents", "numerator", "denominator"}, f"{where}.terms[{index}]")
        require(type(term["exponents"]) is list and len(term["exponents"]) == len(variables), f"{where}: exponent arity")
        require(all(type(exponent) is int and exponent >= 0 for exponent in term["exponents"]), f"{where}: bad exponent")
        monomial = tuple(term["exponents"])
        require(monomial not in seen, f"{where}: duplicate monomial")
        require(previous is None or previous > monomial, f"{where}: noncanonical term order")
        seen.add(monomial)
        previous = monomial
        coefficient = decode_rational(
            {"numerator": term["numerator"], "denominator": term["denominator"]},
            f"{where}.terms[{index}]",
        )
        require(coefficient != 0, f"{where}: zero term serialized")
        product = coefficient
        for variable, exponent in zip(variables, monomial):
            product *= variable**exponent
        expression += product
    return sp.Poly(expression, *variables, domain=QQ).as_expr()


class KRing:
    def __init__(self, modulus: sp.Expr):
        self.modulus = sp.Poly(modulus, A, domain=QQ)
        self.degree = self.modulus.degree()

    def red(self, value: sp.Expr | sp.Poly) -> sp.Poly:
        expression = value.as_expr() if isinstance(value, sp.Poly) else value
        return sp.Poly(sp.cancel(expression), A, domain=QQ).rem(self.modulus)

    def add(self, left: sp.Poly, right: sp.Poly) -> sp.Poly:
        return self.red(left.as_expr() + right.as_expr())

    def neg(self, value: sp.Poly) -> sp.Poly:
        return self.red(-value.as_expr())

    def mul(self, left: sp.Poly, right: sp.Poly) -> sp.Poly:
        return self.red(left.as_expr() * right.as_expr())

    def inv(self, value: sp.Poly) -> sp.Poly:
        value = self.red(value)
        require(not value.is_zero, "attempted quotient-field division by zero")
        return sp.invert(value, self.modulus)

    def div(self, left: sp.Poly, right: sp.Poly) -> sp.Poly:
        return self.mul(left, self.inv(right))

    def decode(self, value: Any, where: str) -> sp.Poly:
        item = exact_keys(value, {"basis", "numerators_low_to_high", "denominator"}, where)
        require(strict_equal(item["basis"], [f"A^{index}" for index in range(self.degree)]), f"{where}: basis mismatch")
        nums = item["numerators_low_to_high"]
        den = item["denominator"]
        require(type(nums) is list and len(nums) == self.degree, f"{where}: coefficient length")
        require(all(type(number) is int for number in nums), f"{where}: noninteger numerator")
        require(type(den) is int and den > 0, f"{where}: invalid denominator")
        divisor = den
        for number in nums:
            divisor = math.gcd(divisor, abs(number))
        require(divisor == 1, f"{where}: noncanonical common divisor")
        return self.red(sum(sp.Rational(number, den) * A**index for index, number in enumerate(nums)))

    def eval_c(self, expression: sp.Expr, value: sp.Poly) -> sp.Poly:
        poly = sp.Poly(expression, C, domain=QQ[A])
        result = self.red(0)
        for index in range(poly.degree(), -1, -1):
            result = self.add(self.mul(result, value), self.red(poly.nth(index)))
        return result


def trim(poly: list[sp.Poly]) -> list[sp.Poly]:
    poly = list(poly)
    while poly and poly[-1].is_zero:
        poly.pop()
    return poly


def divmod_k(left: list[sp.Poly], right: list[sp.Poly], ring: KRing) -> tuple[list[sp.Poly], list[sp.Poly]]:
    left = trim([ring.red(value) for value in left])
    right = trim([ring.red(value) for value in right])
    require(bool(right), "zero divisor polynomial")
    quotient = [ring.red(0) for _ in range(max(0, len(left) - len(right) + 1))]
    inverse_lead = ring.inv(right[-1])
    while len(left) >= len(right):
        shift = len(left) - len(right)
        factor = ring.mul(left[-1], inverse_lead)
        quotient[shift] = factor
        for index, coefficient in enumerate(right):
            position = shift + index
            left[position] = ring.add(left[position], ring.neg(ring.mul(factor, coefficient)))
        left = trim(left)
    return trim(quotient), left


def gcd_k(left: list[sp.Poly], right: list[sp.Poly], ring: KRing) -> list[sp.Poly]:
    left, right = trim(left), trim(right)
    while right:
        _, remainder = divmod_k(left, right, ring)
        left, right = right, remainder
    if not left:
        return []
    inverse = ring.inv(left[-1])
    return [ring.mul(value, inverse) for value in left]


def q_coefficients(expression: sp.Expr, ring: KRing) -> list[sp.Poly]:
    poly = sp.Poly(expression, Q, domain=QQ[A])
    return [ring.red(poly.nth(index)) for index in range(poly.degree() + 1)]


def reduce_mod_quadratic(expression: sp.Expr, g2: list[sp.Poly], ring: KRing) -> tuple[sp.Poly, sp.Poly]:
    coefficients = q_coefficients(expression, ring)
    constant, linear = ring.red(0), ring.red(0)
    power_constant, power_linear = ring.red(1), ring.red(0)
    for coefficient in coefficients:
        constant = ring.add(constant, ring.mul(coefficient, power_constant))
        linear = ring.add(linear, ring.mul(coefficient, power_linear))
        power_constant, power_linear = (
            ring.neg(ring.mul(power_linear, g2[0])),
            ring.add(power_constant, ring.neg(ring.mul(power_linear, g2[1]))),
        )
    return constant, linear


def multiply_pair(
    left: tuple[sp.Poly, sp.Poly], right: tuple[sp.Poly, sp.Poly], g2: list[sp.Poly], ring: KRing
) -> tuple[sp.Poly, sp.Poly]:
    a, b = left
    c, d = right
    bd = ring.mul(b, d)
    return (
        ring.add(ring.mul(a, c), ring.neg(ring.mul(bd, g2[0]))),
        ring.add(ring.add(ring.mul(a, d), ring.mul(b, c)), ring.neg(ring.mul(bd, g2[1]))),
    )


def inverse_pair(value: tuple[sp.Poly, sp.Poly], g2: list[sp.Poly], ring: KRing) -> tuple[tuple[sp.Poly, sp.Poly], sp.Poly]:
    a, b = value
    norm = ring.add(
        ring.add(ring.mul(a, a), ring.neg(ring.mul(g2[1], ring.mul(a, b)))),
        ring.mul(g2[0], ring.mul(b, b)),
    )
    inv_norm = ring.inv(norm)
    return (
        ring.mul(ring.add(a, ring.neg(ring.mul(b, g2[1]))), inv_norm),
        ring.mul(ring.neg(b), inv_norm),
    ), norm


def recurrence_data() -> tuple[sp.Expr, list[sp.Expr], sp.Expr, sp.Expr]:
    previous = current = Q
    coordinates: list[sp.Expr] = []
    for _ in range(5):
        coordinates.append(current)
        previous, current = current, sp.expand(1 - A * current**2 - previous)
    equation_5 = current - Q
    equation_4 = previous - Q
    domain = QQ.frac_field(A)
    common = sp.monic(
        sp.gcd(sp.Poly(equation_5, Q, domain=domain), sp.Poly(equation_4, Q, domain=domain))
    ).as_expr()
    fixed = A * Q**2 + 2 * Q - 1
    marker_rational = sp.cancel(common / fixed)
    numerator, denominator = sp.fraction(marker_rational)
    require(denominator == A**7, "unexpected marker normalization denominator")
    marker = sp.Poly(numerator, Q, A, domain=sp.ZZ).primitive()[1].as_expr()
    if sp.Poly(marker, Q, A).LC() < 0:
        marker = -marker
    return marker, coordinates, equation_4, equation_5


def action_data(marker: sp.Expr, coordinates: list[sp.Expr]) -> tuple[sp.Expr, sp.Expr]:
    action = sum(
        coordinates[index] * coordinates[(index + 1) % 5]
        - coordinates[index]
        + A * coordinates[index] ** 3 / 3
        for index in range(5)
    )
    domain = QQ.frac_field(A)
    remainder = sp.rem(sp.Poly(3 * A**2 * action, Q, domain=domain), sp.Poly(marker, Q, domain=domain)).as_expr()
    resultant = sp.resultant(marker, 3 * A**2 * C - remainder, Q)
    content, primitive = sp.Poly(resultant, C, domain=QQ[A]).primitive()
    require(sp.factor(content) == A**30, "action resultant normalization changed")
    action_curve = sp.Poly(primitive.as_expr(), C, A, domain=sp.ZZ).primitive()[1].as_expr()
    return sp.expand(remainder), sp.expand(action_curve)


def hill_data(marker: sp.Expr, coordinates: list[sp.Expr]) -> tuple[sp.Expr, sp.Expr]:
    monodromy = sp.eye(2)
    for coordinate in coordinates:
        monodromy = sp.Matrix([[-2 * A * coordinate, -1], [1, 0]]) * monodromy
    domain = QQ.frac_field(A)
    hill = sp.rem(
        sp.Poly(sp.expand((sp.eye(2) - monodromy).det()), Q, domain=domain),
        sp.Poly(marker, Q, domain=domain),
    ).as_expr()
    hessian = sp.zeros(5)
    for index, coordinate in enumerate(coordinates):
        hessian[index, index] = 2 * A * coordinate
        hessian[index, (index + 1) % 5] += 1
        hessian[(index + 1) % 5, index] += 1
    hessian_det = sp.rem(
        sp.Poly(sp.expand(hessian.det()), Q, domain=domain), sp.Poly(marker, Q, domain=domain)
    ).as_expr()
    require(sp.expand(hill - hessian_det) == 0, "cyclic Hessian/Hill identity failed")
    trace = sp.rem(
        sp.Poly(sp.expand(monodromy.trace()), Q, domain=domain),
        sp.Poly(marker, Q, domain=domain),
    ).as_expr()
    return sp.expand(hill), sp.expand(trace)


@functools.lru_cache(maxsize=1)
def base_replay() -> dict[str, Any]:
    marker, coordinates, equation_4, equation_5 = recurrence_data()
    remainder, action_curve = action_data(marker, coordinates)
    marker_disc = sp.factor(sp.discriminant(marker, Q))
    action_disc = sp.factor(sp.discriminant(action_curve, C))
    marker_factors = sp.factor_list(marker_disc)
    action_factors = sp.factor_list(action_disc)
    p2 = [factor for factor, power in action_factors[1] if sp.degree(factor, A) == 2 and power == 5][0]
    p5 = [factor for factor, power in action_factors[1] if sp.degree(factor, A) == 5 and power == 3][0]
    p9 = [factor for factor, power in action_factors[1] if sp.degree(factor, A) == 9 and power == 2][0]
    hill, trace = hill_data(marker, coordinates)
    return {
        "marker": marker,
        "coordinates": coordinates,
        "equation_4": equation_4,
        "equation_5": equation_5,
        "remainder": remainder,
        "action_curve": action_curve,
        "marker_disc": marker_disc,
        "action_disc": action_disc,
        "marker_factors": marker_factors,
        "action_factors": action_factors,
        "p2": p2,
        "p5": p5,
        "p9": p9,
        "hill": hill,
        "trace": trace,
        "fixed_resultant": sp.factor(sp.resultant(marker, A * Q**2 + 2 * Q - 1, Q)),
        "plus_resultant": sp.factor(sp.resultant(marker, hill, Q)),
        "minus_resultant": sp.factor(sp.resultant(marker, 4 - hill, Q)),
    }


def evaluate_mod(expression: sp.Expr, q_value: int, prime: int) -> int:
    return int(expression.subs({A: 6, Q: q_value})) % prime


def legendre(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        return 0
    return 1 if pow(value, (prime - 1) // 2, prime) == 1 else -1


def finite_state_step(
    state: tuple[int, int], parameter: int, prime: int
) -> tuple[int, int]:
    q_value, previous = state
    return ((1 - parameter * q_value * q_value - previous) % prime, q_value)


def finite_least_period(
    state: tuple[int, int], parameter: int, prime: int, limit: int = 5
) -> int | None:
    current = state
    for period in range(1, limit + 1):
        current = finite_state_step(current, parameter, prime)
        if current == state:
            return period
    return None


@functools.lru_cache(maxsize=1)
def finite_replay() -> dict[int, dict[str, Any]]:
    base = base_replay()
    marker, remainder, hill = base["marker"], base["remainder"], base["hill"]
    result: dict[int, dict[str, Any]] = {}
    for prime in (61, 157, 3203, 21943):
        roots = [value for value in range(prime) if evaluate_mod(marker, value, prime) == 0]
        groups: dict[int, list[tuple[int, int]]] = {}
        for root in roots:
            action = evaluate_mod(remainder, root, prime) * pow(108, -1, prime) % prime
            groups.setdefault(action, []).append((root, evaluate_mod(hill, root, prime)))
        collisions = [(action, values) for action, values in groups.items() if len(values) == 2]
        require(len(collisions) == 1, f"independent collision count p={prime}")
        action, values = collisions[0]
        result[prime] = {"roots": roots, "action": action, "values": values}
    return result


class Audit:
    def __init__(self) -> None:
        self.gates: list[dict[str, str]] = []

    def gate(self, gate_id: str, description: str, function: Callable[[], None]) -> None:
        try:
            function()
        except GateFailure as error:
            self.gates.append({"id": gate_id, "description": description, "status": "FAIL", "detail": str(error)})
        else:
            self.gates.append({"id": gate_id, "description": description, "status": "PASS", "detail": ""})


def audit_certificate(certificate: Any) -> dict[str, Any]:
    top = exact_keys(certificate, {"schema", "payload", "payload_sha256"}, "certificate")
    require(type(top["schema"]) is str and top["schema"] == SCHEMA, "schema mismatch")
    require(type(top["payload_sha256"]) is str and len(top["payload_sha256"]) == 64, "payload digest malformed")
    payload = top["payload"]
    require(type(payload) is dict, "payload must be object")
    expected_payload_keys = {
        "material_passport", "source_lock", "conventions", "derived_polynomials", "node_gate",
        "exact_period_and_nonparabolic_gate", "collision_parameter_galois_gate", "hill_kummer_gate",
        "finite_prime_controls", "route_a_evaluation", "decisions", "scope",
    }
    exact_keys(payload, expected_payload_keys, "payload")
    audit = Audit()

    def g0() -> None:
        actual = sha256_bytes(canonical_json(payload).encode("utf-8"))
        require(actual == top["payload_sha256"], "canonical payload digest mismatch")
        passport = payload["material_passport"]
        exact_keys(passport, {"candidate_id", "phase", "date_utc", "ai_assistance_disclosed", "evidence_mode"}, "passport")
        require(strict_equal(passport, {
            "candidate_id": CANDIDATE,
            "phase": 3,
            "date_utc": "2026-08-12",
            "ai_assistance_disclosed": True,
            "evidence_mode": "exact symbolic computation plus theorem audit",
        }), "material passport changed")
        require(strict_equal(payload["conventions"], {
            "map": "H_A(q,p)=(1-A*q^2-p,q)",
            "reversor_line": "p=q",
            "chronological_recurrence": "x_(i+1)=1-A*x_i^2-x_(i-1)",
            "cyclic_action": "Phi_5A=sum_i(x_i*x_(i+1)-x_i+(A/3)*x_i^3)",
            "action_coordinate": "c=Phi_5A; elimination uses 3*A^2*c-R_A(q)",
            "hill_value": "h_A(q)=det(I-DH_A^5), chronological later factors on the left",
        }), "mathematical conventions changed")
    audit.gate("G0", "schema, type-strict passport, and canonical payload digest", g0)

    def g1() -> None:
        lock = payload["source_lock"]
        require(type(lock) is dict and set(lock) == set(SOURCE_PATHS), "source-lock inventory mismatch")
        for relative in SOURCE_PATHS:
            require(type(lock[relative]) is str, f"source digest type changed: {relative}")
            require(lock[relative] == sha256_file(REPO / relative), f"source drift: {relative}")
    audit.gate("G1", "exact source provenance", g1)

    base = base_replay()
    marker = base["marker"]
    coordinates = base["coordinates"]
    equation_4 = base["equation_4"]
    equation_5 = base["equation_5"]
    remainder = base["remainder"]
    action_curve = base["action_curve"]
    derived = payload["derived_polynomials"]

    def g2() -> None:
        exact_keys(derived, {
            "exact_period_five_marker_G", "reduced_action_numerator_R", "action_curve_W",
            "raw_resultant_content_removed", "marker_discriminant", "action_curve_discriminant",
            "P2", "P5", "P9", "marker_discriminant_factor_degrees_and_powers",
            "action_discriminant_factor_degrees_and_powers", "P9_coprime_to_P2P5",
            "normalization_birational_inverse", "generic_irreducibility_certificate",
        }, "derived_polynomials")
        require(sp.expand(decode_poly(derived["exact_period_five_marker_G"], (Q, A), "G") - marker) == 0, "marker mismatch")
        domain = QQ.frac_field(A)
        require(sp.rem(sp.Poly(equation_4, Q, domain=domain), sp.Poly(marker, Q, domain=domain)).is_zero, "x4 recurrence residual")
        require(sp.rem(sp.Poly(equation_5, Q, domain=domain), sp.Poly(marker, Q, domain=domain)).is_zero, "x5 recurrence residual")
        require(sp.expand(decode_poly(derived["reduced_action_numerator_R"], (Q, A), "R") - remainder) == 0, "action remainder mismatch")
        require(sp.expand(decode_poly(derived["action_curve_W"], (C, A), "W") - action_curve) == 0, "action curve mismatch")
        require(decode_poly(derived["raw_resultant_content_removed"], (A,), "content") == A**30, "resultant content mismatch")
        for index in range(5):
            residual = coordinates[(index - 1) % 5] + coordinates[(index + 1) % 5] - 1 + A * coordinates[index] ** 2
            require(sp.rem(sp.Poly(residual, Q, domain=domain), sp.Poly(marker, Q, domain=domain)).is_zero, "Euler-Lagrange chronology mismatch")
    audit.gate("G2", "chronological marker, action, and plane-image reconstruction", g2)

    marker_disc = base["marker_disc"]
    action_disc = base["action_disc"]
    marker_factors = base["marker_factors"]
    action_factors = base["action_factors"]
    p2, p5, p9 = base["p2"], base["p5"], base["p9"]

    def g3() -> None:
        require(sp.expand(decode_poly(derived["marker_discriminant"], (A,), "discG") - marker_disc) == 0, "marker discriminant mismatch")
        require(sp.expand(decode_poly(derived["action_curve_discriminant"], (A,), "discW") - action_disc) == 0, "action discriminant mismatch")
        for key, expected in (("P2", p2), ("P5", p5), ("P9", p9)):
            require(sp.expand(decode_poly(derived[key], (A,), key) - expected) == 0, f"{key} mismatch")
        require(strict_equal(derived["marker_discriminant_factor_degrees_and_powers"], [[1, 30], [2, 1], [5, 1]]), "marker factor profile")
        require(strict_equal(derived["action_discriminant_factor_degrees_and_powers"], [[1, 60], [2, 5], [5, 3], [9, 2]]), "action factor profile")
        require(derived["P9_coprime_to_P2P5"] is True, "P9 coprimality verdict")
        require(sp.gcd(sp.Poly(p9, A), sp.Poly(p2 * p5, A)).degree() == 0, "P9 not coprime")
    audit.gate("G3", "discriminant split and new Maxwell-type factor", g3)

    def g4() -> None:
        record = derived["normalization_birational_inverse"]
        exact_keys(record, {"linear_subresultant_coefficient_q", "linear_subresultant_constant", "coefficient_q_coprime_to_W_over_QQ_A", "inverse_formula", "conclusion"}, "birational")
        linears = [item for item in sp.subresultants(marker, 3 * A**2 * C - remainder, Q) if sp.degree(item, Q) == 1]
        require(len(linears) == 1, "linear inverse subresultant absent")
        polynomial = sp.Poly(linears[0], Q, domain=QQ[A, C])
        u, v = polynomial.nth(1), polynomial.nth(0)
        require(sp.expand(decode_poly(record["linear_subresultant_coefficient_q"], (C, A), "U") - u) == 0, "inverse U mismatch")
        require(sp.expand(decode_poly(record["linear_subresultant_constant"], (C, A), "V") - v) == 0, "inverse V mismatch")
        require(sp.gcd(sp.Poly(u, C, domain=QQ.frac_field(A)), sp.Poly(action_curve, C, domain=QQ.frac_field(A))).degree() == 0, "U not generically invertible")
        require(
            record["coefficient_q_coprime_to_W_over_QQ_A"] is True
            and record["inverse_formula"] == "q=-V(A,c)/U(A,c)"
            and record["conclusion"] == "QQ(A,q)=QQ(A,c)",
            "birational conclusion changed",
        )
        irreducibility = exact_keys(
            derived["generic_irreducibility_certificate"],
            {"parameter_value", "prime", "rows", "degree_preserved", "conclusion"},
            "generic irreducibility",
        )
        require(
            type(irreducibility["parameter_value"]) is int
            and irreducibility["parameter_value"] == 6
            and type(irreducibility["prime"]) is int
            and irreducibility["prime"] == 37
            and irreducibility["degree_preserved"] is True,
            "irreducibility specialization changed",
        )
        require(
            type(irreducibility["rows"]) is list and len(irreducibility["rows"]) == 2,
            "irreducibility row count",
        )
        expected_specializations = {
            "G_at_A6": (marker.subs(A, 6), Q),
            "W_at_A6": (action_curve.subs(A, 6), C),
        }
        for row in irreducibility["rows"]:
            exact_keys(
                row,
                {
                    "polynomial", "variable", "degree",
                    "coefficients_high_to_low_mod_p", "factor_degrees",
                    "irreducible",
                },
                "irreducibility row",
            )
            require(row["polynomial"] in expected_specializations, "unknown irreducibility row")
            expression, variable = expected_specializations[row["polynomial"]]
            polynomial_mod = sp.Poly(expression, variable, modulus=37)
            factors = sp.factor_list(polynomial_mod)[1]
            profile = sorted(
                [factor.degree() for factor, exponent in factors for _ in range(exponent)],
                reverse=True,
            )
            require(
                row["variable"] == str(variable)
                and type(row["degree"]) is int
                and row["degree"] == polynomial_mod.degree() == 6,
                "specialization degree changed",
            )
            require(
                strict_equal(
                    row["coefficients_high_to_low_mod_p"],
                    [int(coefficient) % 37 for coefficient in polynomial_mod.all_coeffs()],
                ),
                "specialization coefficients changed",
            )
            require(
                strict_equal(row["factor_degrees"], profile)
                and strict_equal(profile, [6]),
                "specialization reducible",
            )
            require(row["irreducible"] is True, "irreducibility verdict false")
        require(
            {row["polynomial"] for row in irreducibility["rows"]}
            == set(expected_specializations),
            "duplicate irreducibility row",
        )
        require(
            irreducibility["conclusion"] == "G_and_W_irreducible_over_QQ(A)",
            "generic irreducibility conclusion changed",
        )
    audit.gate("G4", "old normalization/function-field firewall", g4)

    galois = payload["collision_parameter_galois_gate"]
    def g5() -> None:
        exact_keys(galois, {"P9_primitive", "P9_discriminant", "P9_discriminant_factorization", "modular_factorizations", "argument", "conclusion"}, "galois")
        p9_poly = sp.Poly(p9, A, domain=sp.ZZ)
        discriminant = int(sp.discriminant(p9, A))
        require(galois["P9_primitive"] is True and int(sp.gcd_list(p9_poly.all_coeffs())) == 1, "P9 nonprimitive")
        require(type(galois["P9_discriminant"]) is int and galois["P9_discriminant"] == discriminant, "P9 discriminant mismatch")
        require(strict_equal(galois["P9_discriminant_factorization"], {str(k): int(v) for k, v in sp.factorint(discriminant).items()}), "P9 discriminant factors")
        require(type(galois["modular_factorizations"]) is list and len(galois["modular_factorizations"]) == 3, "modular ledger size")
        expected_profiles = {7: [9], 17: [5, 2, 1, 1], 23: [8, 1]}
        seen_primes: list[int] = []
        for row in galois["modular_factorizations"]:
            exact_keys(row, {"prime", "unramified", "factor_degrees", "monic_factors"}, "galois row")
            prime = row["prime"]
            require(type(prime) is int and prime in expected_profiles, "unexpected Galois prime")
            seen_primes.append(prime)
            factors = sp.factor_list(sp.Poly(p9, A, modulus=prime))[1]
            profile = sorted([factor.degree() for factor, exponent in factors for _ in range(exponent)], reverse=True)
            require(row["unramified"] is True and discriminant % prime != 0, "ramified cycle-type prime")
            require(
                strict_equal(row["factor_degrees"], profile)
                and strict_equal(profile, expected_profiles[prime]),
                "cycle profile mismatch",
            )
            actual = sorted(
                [{"coefficients_high_to_low": [int(x) % prime for x in factor.monic().all_coeffs()], "exponent": int(exponent)} for factor, exponent in factors],
                key=lambda item: (len(item["coefficients_high_to_low"]), item["coefficients_high_to_low"]),
            )
            require(strict_equal(row["monic_factors"], actual), "modular factor coefficients mismatch")
        require(
            set(seen_primes) == set(expected_profiles) and len(set(seen_primes)) == 3,
            "Galois prime ledger must contain 7, 17, and 23 exactly once",
        )
        require(strict_equal(galois["argument"], [
            "degree-9 factor modulo 7 proves irreducibility and a 9-cycle",
            "type (8,1) modulo 23 plus transitivity gives 2-transitivity and primitivity",
            "squaring type (5,2,1,1) modulo 17 gives a pure 5-cycle",
            "Jordan gives A9; the 8-cycle is odd; hence S9",
        ]), "S9 deduction ledger changed")
        require(galois["conclusion"] == "Gal(P9/QQ)=S9", "S9 conclusion changed")
    audit.gate("G5", "unramified modular cycle types and S9 deduction", g5)

    ring = KRing(p9)
    node = payload["node_gate"]
    c0 = ring.decode(node["double_action_value_c0"], "node.c0")
    branch = exact_keys(node["branch_pair_polynomial"], {"variable", "coefficients_low_to_high"}, "branch pair")
    require(branch["variable"] == "q" and type(branch["coefficients_low_to_high"]) is list and len(branch["coefficients_low_to_high"]) == 3, "branch polynomial schema")
    g2 = [ring.decode(value, f"g2[{index}]") for index, value in enumerate(branch["coefficients_low_to_high"])]

    def g6() -> None:
        exact_keys(node, {"collision_field", "double_action_value_c0", "branch_pair_polynomial", "branch_pair_discriminant", "branch_pair_divides_marker", "branch_pair_coprime_to_marker_quotient", "action_image_derivatives", "tangent_cone_discriminant_WAc_squared_minus_WAA_Wcc", "normalization_branch_slope", "zero_gates", "nonzero_gates", "conclusion"}, "node")
        require(g2[2] == ring.red(1), "g2 not monic")
        linears = [item for item in sp.subresultants(action_curve, sp.diff(action_curve, C), C) if sp.degree(item, C) == 1]
        require(len(linears) == 1, "collision action gcd not linear")
        linear = sp.Poly(linears[0], C, domain=QQ[A])
        expected_c0 = ring.div(ring.neg(ring.red(linear.nth(0))), ring.red(linear.nth(1)))
        require(c0 == expected_c0, "c0 not reconstructed from subresultant")
        branch_equation = 3 * A**2 * c0.as_expr() - remainder
        marker_coeffs = q_coefficients(marker, ring)
        branch_coeffs = q_coefficients(branch_equation, ring)
        quotient, rem_marker = divmod_k(marker_coeffs, g2, ring)
        _, rem_branch = divmod_k(branch_coeffs, g2, ring)
        require(not rem_marker and not rem_branch, "g2 does not divide both fiber equations")
        require(len(gcd_k(g2, quotient, ring)) == 1, "two-point fiber is nonreduced")
        require(node["collision_field"] == "K9=QQ[A]/(P9)", "collision field changed")
        require(
            node["branch_pair_divides_marker"] is (not bool(rem_marker))
            and node["branch_pair_coprime_to_marker_quotient"] is (len(gcd_k(g2, quotient, ring)) == 1),
            "branch-pair verdict changed",
        )
        discriminant = ring.add(ring.mul(g2[1], g2[1]), ring.neg(ring.mul(ring.red(4), g2[0])))
        require(not discriminant.is_zero, "branch pair repeated")
        require(ring.decode(node["branch_pair_discriminant"], "branch disc") == discriminant, "branch discriminant mismatch")
        derivatives = exact_keys(node["action_image_derivatives"], {"W", "W_A", "W_c", "W_AA", "W_Ac", "W_cc"}, "node derivatives")
        expressions = {"W": action_curve, "W_A": sp.diff(action_curve, A), "W_c": sp.diff(action_curve, C), "W_AA": sp.diff(action_curve, A, 2), "W_Ac": sp.diff(action_curve, A, C), "W_cc": sp.diff(action_curve, C, 2)}
        values = {key: ring.eval_c(expression, c0) for key, expression in expressions.items()}
        for key, value in values.items():
            require(ring.decode(derivatives[key], f"node.{key}") == value, f"node derivative mismatch {key}")
        require(all(values[key].is_zero for key in ("W", "W_A", "W_c")), "singular-point equations fail")
        tangent = ring.add(ring.mul(values["W_Ac"], values["W_Ac"]), ring.neg(ring.mul(values["W_AA"], values["W_cc"])))
        require(not values["W_cc"].is_zero and not tangent.is_zero, "ordinary transverse node fails")
        require(ring.decode(node["tangent_cone_discriminant_WAc_squared_minus_WAA_Wcc"], "tangent") == tangent, "tangent discriminant mismatch")
        require(strict_equal(node["zero_gates"], {"W": True, "W_A": True, "W_c": True}), "node zero gates changed")
        require(strict_equal(node["nonzero_gates"], {
            "W_cc": True,
            "tangent_cone_discriminant": True,
            "branch_pair_discriminant": True,
            "normalization_slope_linear_coefficient": True,
            "normalization_slope_difference_square": True,
        }), "node nonzero gate contract changed")
        require(node["conclusion"] == "TWO_DISTINCT_NORMALIZATION_POINTS_WITH_TRANSVERSE_ORDINARY_ACTION_IMAGE_NODE", "node conclusion changed")
    audit.gate("G6", "two-point normalization fiber and ordinary action-image node", g6)

    hill, trace = base["hill"], base["trace"]
    period_gate = payload["exact_period_and_nonparabolic_gate"]
    def g7() -> None:
        exact_keys(period_gate, {"chronology", "hill_polynomial_det_I_minus_DH5", "cyclic_action_hessian_equals_hill", "fixed_point_collision_resultant", "multiplier_plus_one_resultant", "multiplier_minus_one_resultant_det_I_plus_DH5", "identity_det_I_plus_M_equals_4_minus_det_I_minus_M", "P9_coprime_to_fixed_collision_resultant", "P9_coprime_to_multiplier_plus_one_resultant", "P9_coprime_to_multiplier_minus_one_resultant", "conclusion"}, "period gate")
        require(
            period_gate["chronology"]
            == "DH_A^5=D_4*D_3*D_2*D_1*D_0, later factors on the left",
            "derivative chronology changed",
        )
        require(sp.expand(decode_poly(period_gate["hill_polynomial_det_I_minus_DH5"], (Q, A), "hill") - hill) == 0, "Hill polynomial mismatch")
        require(period_gate["cyclic_action_hessian_equals_hill"] is True, "Hill identity verdict false")
        require(sp.expand(4 - hill - (2 + trace)) == 0, "det(I+M)=4-h identity failed")
        fixed_resultant = base["fixed_resultant"]
        plus_resultant = base["plus_resultant"]
        minus_resultant = base["minus_resultant"]
        for key, expected in (("fixed_point_collision_resultant", fixed_resultant), ("multiplier_plus_one_resultant", plus_resultant), ("multiplier_minus_one_resultant_det_I_plus_DH5", minus_resultant)):
            require(sp.expand(decode_poly(period_gate[key], (A,), key) - expected) == 0, f"{key} mismatch")
            require(sp.gcd(sp.Poly(p9, A), sp.Poly(expected, A)).degree() == 0, f"P9 collision with {key}")
        require(period_gate["identity_det_I_plus_M_equals_4_minus_det_I_minus_M"] is True, "minus-one identity verdict")
        require(period_gate["P9_coprime_to_fixed_collision_resultant"] is True, "exact-period gate false")
        require(period_gate["P9_coprime_to_multiplier_plus_one_resultant"] is True, "+1 gate false")
        require(period_gate["P9_coprime_to_multiplier_minus_one_resultant"] is True, "-1 gate false")
        require(period_gate["conclusion"] == "GENERIC_P9_BRANCHES_HAVE_EXACT_PERIOD_FIVE_AND_NO_MULTIPLIER_PLUS_OR_MINUS_ONE", "period conclusion changed")
    audit.gate("G7", "exact period, Hill identity, and both plus/minus-one multiplier gates", g7)

    def g8() -> None:
        slope = exact_keys(node["normalization_branch_slope"], {"formula", "constant", "linear_q", "denominator_norm", "slope_difference_square"}, "slope")
        require(
            slope["formula"]
            == "((A*R_A-2*R)*G_q-A*R_q*G_Aparam)/(3*A^3*G_q)",
            "normalization-slope formula changed",
        )
        ga = reduce_mod_quadratic(sp.diff(marker, A), g2, ring)
        gq = reduce_mod_quadratic(sp.diff(marker, Q), g2, ring)
        ra = reduce_mod_quadratic(sp.diff(remainder, A), g2, ring)
        rq = reduce_mod_quadratic(sp.diff(remainder, Q), g2, ring)
        rv = reduce_mod_quadratic(remainder, g2, ring)
        alpha = ring.red(A)
        a3 = ring.mul(ring.mul(alpha, alpha), alpha)
        left = (ring.add(ring.mul(alpha, ra[0]), ring.neg(ring.mul(ring.red(2), rv[0]))), ring.add(ring.mul(alpha, ra[1]), ring.neg(ring.mul(ring.red(2), rv[1]))))
        numerator = multiply_pair(left, gq, g2, ring)
        correction = multiply_pair((ring.mul(alpha, rq[0]), ring.mul(alpha, rq[1])), ga, g2, ring)
        numerator = (ring.add(numerator[0], ring.neg(correction[0])), ring.add(numerator[1], ring.neg(correction[1])))
        denominator = (ring.mul(ring.mul(ring.red(3), a3), gq[0]), ring.mul(ring.mul(ring.red(3), a3), gq[1]))
        inverse_denominator, denominator_norm = inverse_pair(denominator, g2, ring)
        actual_slope = multiply_pair(numerator, inverse_denominator, g2, ring)
        branch_disc = ring.add(ring.mul(g2[1], g2[1]), ring.neg(ring.mul(ring.red(4), g2[0])))
        difference_square = ring.mul(ring.mul(actual_slope[1], actual_slope[1]), branch_disc)
        require(not denominator_norm.is_zero and not actual_slope[1].is_zero and not difference_square.is_zero, "branch tangents not separated")
        require(ring.decode(slope["constant"], "slope constant") == actual_slope[0], "slope constant mismatch")
        require(ring.decode(slope["linear_q"], "slope linear") == actual_slope[1], "slope linear mismatch")
        require(ring.decode(slope["denominator_norm"], "slope denominator") == denominator_norm, "slope denominator mismatch")
        require(ring.decode(slope["slope_difference_square"], "slope difference") == difference_square, "slope difference mismatch")
    audit.gate("G8", "normalization branches have distinct action-image tangents", g8)

    kummer = payload["hill_kummer_gate"]
    def g9() -> None:
        exact_keys(kummer, {"hill_remainder_mod_branch_pair", "symmetric_branch_norm_NH", "field_norm", "field_norm_factorization", "branch_exchange_invariant", "square_class_identity", "common_hill_normalization", "action_gauge", "conclusion"}, "kummer")
        hrem = exact_keys(kummer["hill_remainder_mod_branch_pair"], {"constant", "linear_q"}, "hill remainder")
        constant, linear = reduce_mod_quadratic(hill, g2, ring)
        require(ring.decode(hrem["constant"], "hill remainder constant") == constant, "Hill remainder constant mismatch")
        require(ring.decode(hrem["linear_q"], "hill remainder linear") == linear, "Hill remainder linear mismatch")
        nh = ring.add(ring.add(ring.mul(constant, constant), ring.neg(ring.mul(g2[1], ring.mul(linear, constant)))), ring.mul(g2[0], ring.mul(linear, linear)))
        require(ring.decode(kummer["symmetric_branch_norm_NH"], "NH") == nh, "quadratic norm mismatch")
        encoded = kummer["symmetric_branch_norm_NH"]
        nums = encoded["numerators_low_to_high"]
        den = encoded["denominator"]
        numerator_poly = sp.Poly(sum(sp.Integer(number) * A**index for index, number in enumerate(nums)), A, domain=sp.ZZ)
        p9_poly = sp.Poly(p9, A, domain=sp.ZZ)
        field_norm = sp.factor(sp.Rational(1, den) ** 9 * sp.Rational(sp.resultant(p9, numerator_poly.as_expr(), A), p9_poly.LC() ** numerator_poly.degree()))
        require(decode_rational(kummer["field_norm"], "field norm") == field_norm, "field norm mismatch")
        factors = exact_keys(kummer["field_norm_factorization"], {"numerator", "denominator", "odd_valuations"}, "norm factors")
        expected_num = {str(key): value for key, value in sp.factorint(abs(sp.numer(field_norm))).items()}
        expected_den = {str(key): value for key, value in sp.factorint(sp.denom(field_norm)).items()}
        require(strict_equal(factors["numerator"], expected_num) and strict_equal(factors["denominator"], expected_den), "field norm factorization mismatch")
        expected_odd = {**expected_num, **{key: -value for key, value in expected_den.items()}}
        expected_odd = {key: value for key, value in expected_odd.items() if value % 2}
        require(strict_equal(factors["odd_valuations"], expected_odd) and bool(expected_odd), "nonsquare norm certificate failed")
        require(
            kummer["branch_exchange_invariant"] is True
            and kummer["square_class_identity"]
            == "[h/sigma(h)]=[h*sigma(h)] in E^x/E^(x2) because (h/sigma(h))/(h*sigma(h))=sigma(h)^(-2)"
            and kummer["common_hill_normalization"]
            == "h_i -> mu(A)*h_i multiplies N_H by mu(A)^2"
            and kummer["conclusion"]
            == "NONTRIVIAL_QUADRATIC_KUMMER_CLASS_OVER_K9",
            "Kummer descent or conclusion changed",
        )
        gauge = exact_keys(
            kummer["action_gauge"],
            {
                "parameter_constant", "cyclic_coboundary",
                "common_nonzero_rescaling", "hill_intrinsic",
            },
            "action gauge",
        )
        require(
            strict_equal(gauge, {
                "parameter_constant":
                    "c -> c+5*kappa(A); equal-action locus unchanged",
                "cyclic_coboundary":
                    "sum_i(F(x_(i+1))-F(x_i))=0 on every closed orbit",
                "common_nonzero_rescaling":
                    "c -> lambda(A)*c is a local coordinate change where lambda!=0",
                "hill_intrinsic":
                    "det(I-DH_A^5) is unchanged by action-coordinate gauges",
            }),
            "action-gauge contract changed",
        )
    audit.gate("G9", "descended symmetric Hill norm and nonsquare field norm", g9)

    controls = payload["finite_prime_controls"]
    def g10() -> None:
        exact_keys(controls, {"selection_rule", "P9_at_6", "factorization", "rows"}, "finite controls")
        p9_at_6 = int(sp.Poly(p9, A).eval(6))
        factors = sp.factorint(p9_at_6)
        require(
            controls["selection_rule"]
            == "all prime divisors of P9(6), frozen before Phase 3",
            "finite-control selection rule changed",
        )
        require(type(controls["P9_at_6"]) is int and controls["P9_at_6"] == p9_at_6 and strict_equal(controls["factorization"], {str(k): v for k, v in factors.items()}), "prime selection factorization")
        require(strict_equal([row["prime"] for row in controls["rows"]], [61, 157, 3203, 21943]), "finite-prime order")
        replayed = finite_replay()
        for row in controls["rows"]:
            exact_keys(row, {"prime", "selection_status", "all_marker_roots", "common_action", "branches", "hill_product", "hill_ratio", "hill_product_character", "hill_ratio_character", "multiplier_plus_one_excluded", "multiplier_minus_one_excluded"}, "finite row")
            prime = row["prime"]
            roots = replayed[prime]["roots"]
            require(strict_equal(row["all_marker_roots"], roots), f"root ledger mismatch p={prime}")
            action, values = replayed[prime]["action"], replayed[prime]["values"]
            require(type(row["common_action"]) is int and row["common_action"] == action, f"action mismatch p={prime}")
            for branch in row["branches"]:
                exact_keys(branch, {"q", "hill", "least_state_period"}, "finite branch")
            require(strict_equal([(branch["q"], branch["hill"]) for branch in row["branches"]], values), f"branch mismatch p={prime}")
            expected_periods = [
                finite_least_period((q_value, q_value), 6, prime)
                for q_value, _ in values
            ]
            require(
                strict_equal([branch["least_state_period"] for branch in row["branches"]], expected_periods)
                and strict_equal(expected_periods, [5, 5]),
                f"lower-period branch p={prime}",
            )
            h1, h2 = values[0][1], values[1][1]
            product = h1 * h2 % prime
            ratio = h1 * pow(h2, -1, prime) % prime
            require(type(row["hill_product"]) is int and row["hill_product"] == product and type(row["hill_ratio"]) is int and row["hill_ratio"] == ratio, f"Hill arithmetic p={prime}")
            require(type(row["hill_product_character"]) is int and row["hill_product_character"] == legendre(product, prime) and type(row["hill_ratio_character"]) is int and row["hill_ratio_character"] == legendre(ratio, prime), f"quadratic character p={prime}")
            require(
                row["multiplier_plus_one_excluded"] is all(
                    hill_value != 0 for hill_value in (h1, h2)
                ),
                f"+1 multiplier control p={prime}",
            )
            require(
                row["multiplier_minus_one_excluded"] is all(
                    (4 - hill_value) % prime != 0 for hill_value in (h1, h2)
                ),
                f"-1 multiplier control p={prime}",
            )
        require(
            strict_equal([row["selection_status"] for row in controls["rows"]], [
                "POST_HOC_C32_REGRESSION",
                "STRUCTURAL_SQUARE_CONTROL",
                "ADVERSARIAL_NONSQUARE_CONTROL",
                "STRUCTURAL_SQUARE_CONTROL",
            ]),
            "finite-control status ledger changed",
        )
        require(controls["rows"][2]["hill_product_character"] == -1, "p=3203 adversarial control lost")
    audit.gate("G10", "complete structurally selected finite-prime replay", g10)

    def g11() -> None:
        require(strict_equal(payload["route_a_evaluation"], {
            "testability": "NOT_TESTABLE_AS_ROUTE_A_DETERMINANT",
            "tuple_ceiling": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "reason": "one fixed-period arithmetic cover supplies neither an all-length clock nor a dynamical determinant",
            "route_b_invocation_allowed": False,
        }), "Route-A boundary changed")
        require(strict_equal(payload["decisions"], {
            "phase3_exact_gate": "GO",
            "main_conclusion": "NONTRIVIAL_HENON_ACTION_IMAGE_NODE_HILL_KUMMER_CLASS",
            "normalization_cover_novelty": "REJECTED_PRIOR_WORK",
            "generic_maxwell_mechanism_novelty": "REJECTED_PRIOR_WORK",
            "full_wreath_group": "OPEN_NOT_CLAIMED",
            "picard_lefschetz": "OPEN_NOT_CLAIMED",
            "dynamical_zeta_or_HP": "NOT_CONSTRUCTED",
        }), "decision boundary changed")
        scope = exact_keys(payload["scope"], {"periods", "family", "characteristic_zero_primary", "finite_primes_are_controls_not_primary_proof", "prime_61_is_post_hoc", "no_period_extension", "no_prime_or_zero_fitting", "no_full_wreath_claim", "no_picard_lefschetz_claim", "no_zeta_claim", "no_hilbert_polya_claim"}, "scope")
        require(strict_equal(scope["periods"], [5]) and scope["family"] == "area-preserving Hénon H_A", "scope object changed")
        require(all(value is True for key, value in scope.items() if key not in ("periods", "family")), "scope firewall disabled")
    audit.gate("G11", "Route-A rejection and theorem-scope firewalls", g11)

    passed = all(gate["status"] == "PASS" for gate in audit.gates)
    return {
        "schema": "HCS-C33-PHASE3-INDEPENDENT-CHECK-1",
        "certificate_payload_sha256": top["payload_sha256"],
        "gate_count": len(audit.gates),
        "passed_gate_count": sum(gate["status"] == "PASS" for gate in audit.gates),
        "gates": audit.gates,
        "all_pass": passed,
        "status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
        report = audit_certificate(certificate)
        exit_code = 0 if report["all_pass"] else 1
    except GateFailure as error:
        report = {"schema": "HCS-C33-PHASE3-INDEPENDENT-CHECK-1", "status": "FAIL", "all_pass": False, "fatal_gate_failure": str(error)}
        exit_code = 1
    except Exception as error:  # unexpected checker bugs are not semantic rejections
        report = {
            "schema": "HCS-C33-PHASE3-INDEPENDENT-CHECK-1",
            "status": "ERROR",
            "all_pass": False,
            "unexpected_error_type": type(error).__name__,
            "unexpected_error": str(error),
            "traceback": traceback.format_exc(),
        }
        exit_code = 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"status={report['status']}")
    if "gate_count" in report:
        print(f"gates={report['passed_gate_count']}/{report['gate_count']}")
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
