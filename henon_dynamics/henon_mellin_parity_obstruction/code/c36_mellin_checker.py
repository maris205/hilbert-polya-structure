#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C36 certificate.

The checker deliberately does not import the producer.  It reconstructs the
Mellin continuations with python-flint/Arb, verifies the elementary contour
majorant, and then applies a quantitative Rouche argument on the registered
disc.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable

import flint
from flint import acb, acb_series, arb, ctx


SCHEMA = "hcs-c36-mellin-parity-obstruction-v1"
CHECK_SCHEMA = "hcs-c36-independent-check-v1"
PROJECT = Path(__file__).resolve().parents[1]
REPOSITORY = PROJECT.parents[1]
SOURCE_PATHS = {
    "area_preserving_henon_model": (
        "henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf"
    ),
    "c35_theorem_package": "henon_dynamics/adelic_henon_theta_route/THEOREM_PACKAGE.md",
    "c35_derivation_package": "henon_dynamics/adelic_henon_theta_route/DERIVATION_PACKAGE.md",
    "route_a_evaluator": "henon_dynamics/skills/route-a-evaluator.md",
}
CENTER_RE = Fraction(7286922241147175, 10**16)
CENTER_IM = Fraction(16054479123346985, 10**16)
RADIUS = Fraction(1, 10**12)
THRESHOLDS = {
    "A_center_abs_upper": Fraction(1, 10**16),
    "A_prime_center_abs_lower": Fraction(2, 5),
    "A_second_disc_abs_upper": Fraction(1200),
    "A_mirror_abs_lower": Fraction(3, 10),
    "B_disc_abs_lower": Fraction(4, 5),
    "B_mirror_abs_lower": Fraction(13, 10),
    "linear_parent_abs_lower": Fraction(7, 10),
    "completed_xi_abs_lower": Fraction(9, 20),
}


class GateFailure(Exception):
    """A certificate failed a declared semantic gate."""


class DuplicateKeyError(ValueError):
    """JSON duplicate keys are forbidden by the release parser."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def require_keys(value: Any, keys: set[str], label: str) -> None:
    require(type(value) is dict, f"{label} must be an object")
    require(value.keys() == keys, f"{label} key set mismatch")


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(
            strict_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            strict_equal(a, b) for a, b in zip(left, right)
        )
    return left == right


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def parse_fraction(value: Any, label: str) -> Fraction:
    require(type(value) is str, f"{label} must be a string")
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise GateFailure(f"{label} is not a fraction") from error
    require(fraction_text(result) == value, f"{label} is not canonically serialized")
    return result


def as_arb(value: Fraction) -> arb:
    return arb(value.numerator) / value.denominator


def _series(value: Any, order: int = 3) -> acb_series:
    return acb_series([acb(value)], order)


def independent_kappa(z: acb, sign: int, with_jet: bool = False) -> acb_series:
    """Reconstruct the rotated-contour hypergeometric continuation."""

    require(sign in {-1, 1}, "Mellin sign must be +/-1")
    order = 3
    variable = acb_series([z, 1], order) if with_jet else acb_series([z], order)
    pi = arb.pi()
    four_pi = 4 * pi
    two_pi_scaled = _series(2 * pi * four_pi ** (-arb(1) / 3), order)
    signed_i = _series(acb(0, sign), order)
    pi_series = _series(pi, order)
    argument = _series(-2 * pi**2 / 27, order)

    term_zero = (
        (variable / 3).gamma()
        * acb_series.hypgeom(
            [variable / 3],
            [_series(arb(1) / 3), _series(arb(2) / 3)],
            argument,
        )
    )
    term_one = (
        two_pi_scaled
        * (-signed_i * pi_series / 3).exp()
        * ((variable + 1) / 3).gamma()
        * acb_series.hypgeom(
            [(variable + 1) / 3],
            [_series(arb(2) / 3), _series(arb(4) / 3)],
            argument,
        )
    )
    term_two = (
        two_pi_scaled**2
        * (-2 * signed_i * pi_series / 3).exp()
        * ((variable + 2) / 3).gamma()
        * acb_series.hypgeom(
            [(variable + 2) / 3],
            [_series(arb(4) / 3), _series(arb(5) / 3)],
            argument,
        )
        / 2
    )
    prefactor = (
        _series(four_pi, order) ** (-variable / 3)
        * (signed_i * pi_series * variable / 6).exp()
        / 3
    )
    return prefactor * (term_zero + term_one + term_two)


def independent_parity(z: acb, with_jet: bool = False) -> tuple[acb_series, acb_series]:
    positive = independent_kappa(z, 1, with_jet)
    negative = independent_kappa(z, -1, with_jet)
    return positive + negative, (positive - negative) / _series(acb(0, 1))


def duplicate_rejecting_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_certificate(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=duplicate_rejecting_object)
    if type(value) is not dict:
        raise GateFailure("certificate root must be an object")
    return value


def audit(certificate: dict[str, Any]) -> list[dict[str, str]]:
    """Run every gate, returning PASS/FAIL/ERROR records without short-circuiting."""

    records: list[dict[str, str]] = []

    def gate(name: str, action: Callable[[], None]) -> None:
        try:
            action()
        except GateFailure as error:
            records.append({"gate": name, "status": "FAIL", "detail": str(error)})
        except Exception as error:  # checker exceptions reject, never promote
            records.append(
                {
                    "gate": name,
                    "status": "ERROR",
                    "detail": f"{type(error).__name__}: {error}",
                }
            )
        else:
            records.append(
                {"gate": name, "status": "PASS", "detail": "independent replay passed"}
            )

    def g0_schema() -> None:
        require_keys(certificate, {"schema", "payload_sha256", "payload"}, "certificate")
        require(certificate["schema"] == SCHEMA, "certificate schema mismatch")
        require(type(certificate["payload_sha256"]) is str, "payload hash must be a string")
        require(len(certificate["payload_sha256"]) == 64, "payload hash length mismatch")
        require(
            certificate["payload_sha256"]
            == hashlib.sha256(canonical_json(certificate["payload"])).hexdigest(),
            "payload hash mismatch",
        )
        payload = certificate["payload"]
        require_keys(
            payload,
            {
                "schema",
                "runtime",
                "source_lock",
                "object",
                "analytic_gate",
                "certified_zero_disc",
                "second_derivative_majorant",
                "no_cancellation_gate",
                "route_a",
                "decisions",
                "scope",
            },
            "payload",
        )
        require(payload["schema"] == SCHEMA, "payload schema mismatch")
        require_keys(payload["runtime"], {"python_flint", "arb_decimal_digits"}, "runtime")
        require_keys(
            payload["source_lock"], set(SOURCE_PATHS), "source_lock"
        )
        for name in SOURCE_PATHS:
            require_keys(payload["source_lock"][name], {"path", "sha256"}, f"source_lock.{name}")
        require_keys(
            payload["object"],
            {
                "phase",
                "mellin_symbols",
                "matrix_symbol",
                "even_symbol",
                "odd_symbol",
                "formal_scattering",
            },
            "object",
        )
        require_keys(
            payload["analytic_gate"],
            {
                "rotated_contour",
                "hypergeometric_argument",
                "recurrence",
                "conjugation",
                "parity_reciprocity",
                "critical_line_unitarity",
                "status",
            },
            "analytic_gate",
        )
        zero = payload["certified_zero_disc"]
        require_keys(
            zero,
            {
                "center_re",
                "center_im",
                "radius",
                "contained_in_open_critical_strip",
                "disjoint_from_critical_line",
                "thresholds",
                "arb_enclosures",
                "rouche_lhs_upper",
                "rouche_rhs_lower",
                "zero_count_with_multiplicity",
                "simple_zero",
                "evidence_status",
            },
            "certified_zero_disc",
        )
        require_keys(zero["thresholds"], set(THRESHOLDS), "thresholds")
        require_keys(
            zero["arb_enclosures"],
            {
                "A_center",
                "A_prime_center",
                "A_mirror_disc",
                "B_disc",
                "B_mirror_disc",
                "linear_parent_disc",
                "completed_xi_disc",
            },
            "arb_enclosures",
        )
        require_keys(
            payload["second_derivative_majorant"],
            {"disc_bounds", "elementary_bounds", "conclusion", "status"},
            "second_derivative_majorant",
        )
        require_keys(
            payload["no_cancellation_gate"],
            {
                "A_of_1_minus_disc_nonzero",
                "B_on_disc_nonzero",
                "B_of_1_minus_disc_nonzero",
                "linear_parent_on_disc_nonzero",
                "completed_xi_on_disc_nonzero",
                "conclusion",
                "status",
            },
            "no_cancellation_gate",
        )
        require_keys(payload["route_a"], {"tuple", "overall", "route_b_invocation_allowed"}, "route_a")
        require_keys(
            payload["decisions"],
            {
                "scalar_kappa_ratio",
                "ordinary_Fredholm_multiplier",
                "unrenormalized_parity_scattering",
                "posthoc_zero_removal",
                "independently_derived_reference_cancellation",
                "homogeneous_cubic_pivot",
            },
            "decisions",
        )
        require_keys(
            payload["scope"],
            {
                "no_RH_proof",
                "no_Riemann_zero_table_used",
                "one_local_certified_extra_divisor_is_sufficient",
                "no_global_strip_zero_census_claimed",
                "formal_symbol_not_yet_operator_scattering",
            },
            "scope",
        )

    gate("G0_STRICT_SCHEMA_AND_HASH", g0_schema)
    payload = certificate.get("payload", {})

    def g1_sources_object() -> None:
        require(flint.__version__ == "0.9.0", "checker python-flint version mismatch")
        require(
            strict_equal(
                payload["runtime"],
                {"python_flint": "0.9.0", "arb_decimal_digits": 80},
            ),
            "runtime lock mismatch",
        )
        expected_sources = {
            name: {"path": relative, "sha256": sha256(REPOSITORY / relative)}
            for name, relative in SOURCE_PATHS.items()
        }
        require(strict_equal(payload["source_lock"], expected_sources), "source lock mismatch")
        expected_object = {
            "phase": "P6(u)=2*u^3-u",
            "mellin_symbols": (
                "kappa_sigma(z)=integral_0^infinity exp(sigma*2*pi*i*P6(u))*u^(z-1) du"
            ),
            "matrix_symbol": "K(z)=[[kappa_+(z),kappa_-(z)],[kappa_-(z),kappa_+(z)]]",
            "even_symbol": "A(z)=kappa_+(z)+kappa_-(z)",
            "odd_symbol": "B(z)=(kappa_+(z)-kappa_-(z))/i",
            "formal_scattering": "S_H(z)=K(1-z)*K(z)^(-1)",
        }
        require(strict_equal(payload["object"], expected_object), "Mellin object mismatch")

    gate("G1_SOURCE_RUNTIME_OBJECT_LOCK", g1_sources_object)

    def g2_symbolic() -> None:
        expected = {
            "rotated_contour": "u=exp(sigma*i*pi/6)*r",
            "hypergeometric_argument": "-2*pi^2/27",
            "recurrence": (
                "12*pi*kappa_sigma(z+3)-2*pi*kappa_sigma(z+1)=sigma*i*z*kappa_sigma(z)"
            ),
            "conjugation": "kappa_-(z)=conjugate(kappa_+(conjugate(z)))",
            "parity_reciprocity": "S_j(z)*S_j(1-z)=1",
            "critical_line_unitarity": "|S_j(1/2+i*t)|=1 away from divisor",
            "status": "PROVED_SYMBOLICALLY",
        }
        require(strict_equal(payload["analytic_gate"], expected), "analytic identity block mismatch")

    gate("G2_SYMBOLIC_MELLIN_IDENTITIES", g2_symbolic)

    def g3_disc_protocol() -> None:
        zero = payload["certified_zero_disc"]
        real = parse_fraction(zero["center_re"], "center_re")
        imaginary = parse_fraction(zero["center_im"], "center_im")
        radius = parse_fraction(zero["radius"], "radius")
        require(real == CENTER_RE, "registered real center changed")
        require(imaginary == CENTER_IM, "registered imaginary center changed")
        require(radius == RADIUS, "registered radius changed")
        require(radius > 0, "disc radius must be positive")
        require(real - radius > 0 and real + radius < 1, "disc not inside critical strip")
        require(real - radius > Fraction(1, 2), "disc intersects critical line")
        require(zero["contained_in_open_critical_strip"] is True, "strip verdict mismatch")
        require(zero["disjoint_from_critical_line"] is True, "critical-line verdict mismatch")
        expected_thresholds = {key: fraction_text(value) for key, value in THRESHOLDS.items()}
        require(strict_equal(zero["thresholds"], expected_thresholds), "threshold registry mismatch")
        require(zero["evidence_status"] == "NUMERICALLY_CERTIFIED", "evidence status mismatch")

    gate("G3_REGISTERED_DISC_PROTOCOL", g3_disc_protocol)

    def reconstruct() -> dict[str, Any]:
        ctx.dps = 80
        ctx.cap = 4
        center = acb(as_arb(CENTER_RE), as_arb(CENTER_IM))
        radius = as_arb(RADIUS)
        disc = acb(arb(center.real, radius), arb(center.imag, radius))
        even_jet, _ = independent_parity(center, with_jet=True)
        even_mirror = independent_parity(acb(1) - disc)[0][0]
        odd_disc = independent_parity(disc)[1][0]
        odd_mirror = independent_parity(acb(1) - disc)[1][0]
        pi = arb.pi()
        linear_parent = 2 * (2 * pi) ** (-disc) * disc.gamma() * (pi * disc / 2).cos()
        completed_xi = (
            arb(1) / 2
            * disc
            * (disc - 1)
            * pi ** (-disc / 2)
            * (disc / 2).gamma()
            * disc.zeta()
        )
        return {
            "A_center": even_jet[0],
            "A_prime_center": even_jet[1],
            "A_mirror_disc": even_mirror,
            "B_disc": odd_disc,
            "B_mirror_disc": odd_mirror,
            "linear_parent_disc": linear_parent,
            "completed_xi_disc": completed_xi,
        }

    cache: dict[str, Any] = {}

    def numerical_values() -> dict[str, Any]:
        if not cache:
            cache.update(reconstruct())
        return cache

    def g4_arb_reconstruction() -> None:
        values = numerical_values()
        disclosed = payload["certified_zero_disc"]["arb_enclosures"]
        require(
            strict_equal(disclosed, {key: str(value) for key, value in values.items()}),
            "disclosed Arb enclosure does not equal independent reconstruction",
        )
        require(abs(values["A_center"]) < as_arb(THRESHOLDS["A_center_abs_upper"]), "A(center) bound failed")
        require(abs(values["A_prime_center"]) > as_arb(THRESHOLDS["A_prime_center_abs_lower"]), "A'(center) bound failed")
        require(abs(values["A_mirror_disc"]) > as_arb(THRESHOLDS["A_mirror_abs_lower"]), "A(1-D) bound failed")
        require(abs(values["B_disc"]) > as_arb(THRESHOLDS["B_disc_abs_lower"]), "B(D) bound failed")
        require(abs(values["B_mirror_disc"]) > as_arb(THRESHOLDS["B_mirror_abs_lower"]), "B(1-D) bound failed")
        require(abs(values["linear_parent_disc"]) > as_arb(THRESHOLDS["linear_parent_abs_lower"]), "linear parent bound failed")
        require(abs(values["completed_xi_disc"]) > as_arb(THRESHOLDS["completed_xi_abs_lower"]), "completed xi bound failed")

    gate("G4_INDEPENDENT_ARB_RECONSTRUCTION", g4_arb_reconstruction)

    def g5_majorant() -> None:
        expected = {
            "disc_bounds": ["18/25<Re(z)<1", "abs(Im(z))<161/100"],
            "elementary_bounds": [
                "pi<22/7",
                "exp(pi)<24",
                "exp(pi*(161/100)/6)<3",
                "integral_(0,1) t^(18/25-1)*(abs(log(t))+pi/6)^2 dt<8",
                "integral_(1,infinity) exp(-9*t)*(t+1)^2 dt<1",
            ],
            "conclusion": "sup_D abs(A_second(z))<1200",
            "status": "PROVED_BY_ROTATED_CONTOUR_MAJORANT",
        }
        require(strict_equal(payload["second_derivative_majorant"], expected), "majorant ledger mismatch")
        require(CENTER_RE - RADIUS > Fraction(18, 25), "real lower disc bound failed")
        require(CENTER_RE + RADIUS < 1, "real upper disc bound failed")
        require(CENTER_IM + RADIUS < Fraction(161, 100), "imaginary disc bound failed")
        pi = arb.pi()
        require(pi < arb(22) / 7, "pi<22/7 replay failed")
        require(pi > 3, "pi>3 replay failed")
        require(pi.exp() < 24, "exp(pi)<24 replay failed")
        require((pi * arb(161) / 600).exp() < 3, "phase-prefactor bound failed")
        exponent = arb(18) / 25
        constant = pi / 6
        inner = 2 / exponent**3 + 2 * constant / exponent**2 + constant**2 / exponent
        require(inner < 8, "small-radius logarithmic integral bound failed")
        tail = (-arb(9)).exp() * (arb(4) / 9 + arb(4) / 81 + arb(2) / 729)
        require(tail < 1, "large-radius tail integral bound failed")
        # Each sign is < 3*(24*8+1)=579; summing signs gives 1158.
        one_sign = Fraction(3) * (Fraction(24 * 8) + 1)
        require(one_sign == 579, "one-sign contour majorant arithmetic failed")
        require(2 * one_sign == 1158, "two-sign contour majorant arithmetic failed")
        require(2 * one_sign < THRESHOLDS["A_second_disc_abs_upper"], "declared A'' bound not implied")

    gate("G5_ROTATED_CONTOUR_SECOND_DERIVATIVE_MAJORANT", g5_majorant)

    def g6_rouche() -> None:
        zero = payload["certified_zero_disc"]
        lhs = THRESHOLDS["A_center_abs_upper"] + THRESHOLDS["A_second_disc_abs_upper"] * RADIUS**2 / 2
        rhs = THRESHOLDS["A_prime_center_abs_lower"] * RADIUS
        require(parse_fraction(zero["rouche_lhs_upper"], "rouche_lhs_upper") == lhs, "Rouche lhs mismatch")
        require(parse_fraction(zero["rouche_rhs_lower"], "rouche_rhs_lower") == rhs, "Rouche rhs mismatch")
        require(lhs < rhs, "strict Rouche inequality failed")
        require(zero["zero_count_with_multiplicity"] == 1, "zero-count conclusion mismatch")
        require(type(zero["zero_count_with_multiplicity"]) is int, "zero count must be integer")
        require(zero["simple_zero"] is True, "simplicity conclusion mismatch")

    gate("G6_ROUCHE_UNIQUE_SIMPLE_ZERO", g6_rouche)

    def g7_companions() -> None:
        values = numerical_values()
        block = payload["no_cancellation_gate"]
        expected = {
            "A_of_1_minus_disc_nonzero": True,
            "B_on_disc_nonzero": True,
            "B_of_1_minus_disc_nonzero": True,
            "linear_parent_on_disc_nonzero": True,
            "completed_xi_on_disc_nonzero": True,
            "conclusion": "det(S_H) has one extra pole on D and one zero on 1-D, plus conjugates, while completed xi is nonzero on D",
            "status": "NUMERICALLY_CERTIFIED",
        }
        require(strict_equal(block, expected), "no-cancellation verdict block mismatch")
        require(abs(values["A_mirror_disc"]) > as_arb(THRESHOLDS["A_mirror_abs_lower"]), "A mirror may cancel")
        require(abs(values["B_disc"]) > as_arb(THRESHOLDS["B_disc_abs_lower"]), "B may cancel on D")
        require(abs(values["B_mirror_disc"]) > as_arb(THRESHOLDS["B_mirror_abs_lower"]), "B may cancel on 1-D")
        require(abs(values["linear_parent_disc"]) > as_arb(THRESHOLDS["linear_parent_abs_lower"]), "linear parent may match")
        require(abs(values["completed_xi_disc"]) > as_arb(THRESHOLDS["completed_xi_abs_lower"]), "completed xi may vanish on D")

    gate("G7_NO_PARITY_OR_PARENT_CANCELLATION", g7_companions)

    def g8_route_scope() -> None:
        expected_route = {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED_FOR_UNRENORMALIZED_MELLIN_PARITY_CANDIDATE",
            "route_b_invocation_allowed": False,
        }
        expected_decisions = {
            "scalar_kappa_ratio": "STOP",
            "ordinary_Fredholm_multiplier": "STOP_NONCOMPACT_MULTIPLICATION_OPERATOR",
            "unrenormalized_parity_scattering": "STOP_CERTIFIED_EXTRA_DIVISOR",
            "posthoc_zero_removal": "FORBIDDEN",
            "independently_derived_reference_cancellation": "OPEN_FINAL_ESCAPE_GATE",
            "homogeneous_cubic_pivot": "GO_NEXT_BIG_DOOR",
        }
        expected_scope = {
            "no_RH_proof": True,
            "no_Riemann_zero_table_used": True,
            "one_local_certified_extra_divisor_is_sufficient": True,
            "no_global_strip_zero_census_claimed": True,
            "formal_symbol_not_yet_operator_scattering": True,
        }
        require(strict_equal(payload["route_a"], expected_route), "Route-A verdict mismatch")
        require(strict_equal(payload["decisions"], expected_decisions), "decision ledger mismatch")
        require(strict_equal(payload["scope"], expected_scope), "claim-scope firewall mismatch")

    gate("G8_ROUTE_A_AND_SCOPE_FIREWALL", g8_route_scope)
    return records


def build_report(certificate: dict[str, Any], source_path: Path) -> dict[str, Any]:
    gates = audit(certificate)
    passed = sum(row["status"] == "PASS" for row in gates)
    return {
        "schema": CHECK_SCHEMA,
        "certificate_file": source_path.name,
        "certificate_sha256": sha256(source_path),
        "certificate_payload_sha256": certificate.get("payload_sha256"),
        "gate_count": len(gates),
        "pass_count": passed,
        "overall": "PASS" if passed == len(gates) else "REJECT",
        "gates": gates,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    options = parser.parse_args()
    try:
        certificate = load_certificate(options.certificate)
        report = build_report(certificate, options.certificate)
    except Exception as error:
        report = {
            "schema": CHECK_SCHEMA,
            "certificate_file": options.certificate.name,
            "gate_count": 0,
            "pass_count": 0,
            "overall": "REJECT",
            "parser_error": f"{type(error).__name__}: {error}",
        }
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if options.output:
        options.output.parent.mkdir(parents=True, exist_ok=True)
        options.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    if report["overall"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
