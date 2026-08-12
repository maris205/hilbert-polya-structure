#!/usr/bin/env python3
"""Certified producer for the HCS-C36 Mellin--parity obstruction."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import flint
from flint import acb, acb_series, arb, ctx


SCHEMA = "hcs-c36-mellin-parity-obstruction-v1"
PROJECT = Path(__file__).resolve().parents[1]
REPOSITORY = PROJECT.parents[1]
SOURCE_FILES = {
    "area_preserving_henon_model": REPOSITORY
    / "henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf",
    "c35_theorem_package": REPOSITORY
    / "henon_dynamics/adelic_henon_theta_route/THEOREM_PACKAGE.md",
    "c35_derivation_package": REPOSITORY
    / "henon_dynamics/adelic_henon_theta_route/DERIVATION_PACKAGE.md",
    "route_a_evaluator": REPOSITORY / "henon_dynamics/skills/route-a-evaluator.md",
}
CENTER_RE = Fraction(7286922241147175, 10**16)
CENTER_IM = Fraction(16054479123346985, 10**16)
RADIUS = Fraction(1, 10**12)


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frac_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _cseries(value: Any, order: int = 3) -> acb_series:
    return acb_series([acb(value)], order)


def kappa_hyper(z: acb, sign: int, derivatives: bool = False) -> acb_series:
    """Rigorous hypergeometric continuation of kappa_sign at an acb ball."""

    order = 3
    zz = acb_series([z, 1], order) if derivatives else acb_series([z], order)
    pi = arb.pi()
    scale = 4 * pi
    lam = _cseries(2 * pi * scale ** (-arb(1) / 3), order)
    imaginary = _cseries(acb(0, sign), order)
    piseries = _cseries(pi, order)
    xarg = _cseries(-2 * pi * pi / 27, order)

    h0 = acb_series.hypgeom(
        [zz / 3], [_cseries(arb(1) / 3), _cseries(arb(2) / 3)], xarg
    )
    h1 = acb_series.hypgeom(
        [(zz + 1) / 3], [_cseries(arb(2) / 3), _cseries(arb(4) / 3)], xarg
    )
    h2 = acb_series.hypgeom(
        [(zz + 2) / 3], [_cseries(arb(4) / 3), _cseries(arb(5) / 3)], xarg
    )
    bracket = (
        (zz / 3).gamma() * h0
        + lam * (-imaginary * piseries / 3).exp() * ((zz + 1) / 3).gamma() * h1
        + lam**2
        * (-2 * imaginary * piseries / 3).exp()
        / 2
        * ((zz + 2) / 3).gamma()
        * h2
    )
    return (
        _cseries(scale, order) ** (-zz / 3)
        * (imaginary * piseries * zz / 6).exp()
        / 3
        * bracket
    )


def parity_symbols(z: acb, derivatives: bool = False) -> tuple[acb_series, acb_series]:
    plus = kappa_hyper(z, 1, derivatives)
    minus = kappa_hyper(z, -1, derivatives)
    return plus + minus, (plus - minus) / _cseries(acb(0, 1))


def build_payload() -> dict[str, Any]:
    if flint.__version__ != "0.9.0":
        raise RuntimeError("release certificate requires python-flint 0.9.0")
    ctx.dps = 80
    ctx.cap = 4
    center = acb(
        arb(CENTER_RE.numerator) / CENTER_RE.denominator,
        arb(CENTER_IM.numerator) / CENTER_IM.denominator,
    )
    radius = arb(RADIUS.numerator) / RADIUS.denominator
    disc = acb(arb(center.real, radius), arb(center.imag, radius))
    one = acb(1)

    even_jet, odd_jet = parity_symbols(center, derivatives=True)
    even_mirror = parity_symbols(one - disc)[0][0]
    odd_disc = parity_symbols(disc)[1][0]
    odd_mirror = parity_symbols(one - disc)[1][0]
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

    thresholds = {
        "A_center_abs_upper": Fraction(1, 10**16),
        "A_prime_center_abs_lower": Fraction(2, 5),
        "A_second_disc_abs_upper": Fraction(1200),
        "A_mirror_abs_lower": Fraction(3, 10),
        "B_disc_abs_lower": Fraction(4, 5),
        "B_mirror_abs_lower": Fraction(13, 10),
        "linear_parent_abs_lower": Fraction(7, 10),
        "completed_xi_abs_lower": Fraction(9, 20),
    }
    assert abs(even_jet[0]) < arb(thresholds["A_center_abs_upper"].numerator) / thresholds["A_center_abs_upper"].denominator
    assert abs(even_jet[1]) > arb(2) / 5
    assert abs(even_mirror) > arb(3) / 10
    assert abs(odd_disc) > arb(4) / 5
    assert abs(odd_mirror) > arb(13) / 10
    assert abs(linear_parent) > arb(7) / 10
    assert abs(completed_xi) > arb(9) / 20

    # Exact Rouché inequality using the independently proved M=1200 bound.
    lhs = thresholds["A_center_abs_upper"] + thresholds["A_second_disc_abs_upper"] * RADIUS**2 / 2
    rhs = thresholds["A_prime_center_abs_lower"] * RADIUS
    assert lhs < rhs

    return {
        "schema": SCHEMA,
        "runtime": {"python_flint": flint.__version__, "arb_decimal_digits": 80},
        "source_lock": {
            name: {"path": path.relative_to(REPOSITORY).as_posix(), "sha256": sha256(path)}
            for name, path in SOURCE_FILES.items()
        },
        "object": {
            "phase": "P6(u)=2*u^3-u",
            "mellin_symbols": "kappa_sigma(z)=integral_0^infinity exp(sigma*2*pi*i*P6(u))*u^(z-1) du",
            "matrix_symbol": "K(z)=[[kappa_+(z),kappa_-(z)],[kappa_-(z),kappa_+(z)]]",
            "even_symbol": "A(z)=kappa_+(z)+kappa_-(z)",
            "odd_symbol": "B(z)=(kappa_+(z)-kappa_-(z))/i",
            "formal_scattering": "S_H(z)=K(1-z)*K(z)^(-1)",
        },
        "analytic_gate": {
            "rotated_contour": "u=exp(sigma*i*pi/6)*r",
            "hypergeometric_argument": "-2*pi^2/27",
            "recurrence": "12*pi*kappa_sigma(z+3)-2*pi*kappa_sigma(z+1)=sigma*i*z*kappa_sigma(z)",
            "conjugation": "kappa_-(z)=conjugate(kappa_+(conjugate(z)))",
            "parity_reciprocity": "S_j(z)*S_j(1-z)=1",
            "critical_line_unitarity": "|S_j(1/2+i*t)|=1 away from divisor",
            "status": "PROVED_SYMBOLICALLY",
        },
        "certified_zero_disc": {
            "center_re": frac_text(CENTER_RE),
            "center_im": frac_text(CENTER_IM),
            "radius": frac_text(RADIUS),
            "contained_in_open_critical_strip": True,
            "disjoint_from_critical_line": True,
            "thresholds": {key: frac_text(value) for key, value in thresholds.items()},
            "arb_enclosures": {
                "A_center": str(even_jet[0]),
                "A_prime_center": str(even_jet[1]),
                "A_mirror_disc": str(even_mirror),
                "B_disc": str(odd_disc),
                "B_mirror_disc": str(odd_mirror),
                "linear_parent_disc": str(linear_parent),
                "completed_xi_disc": str(completed_xi),
            },
            "rouche_lhs_upper": frac_text(lhs),
            "rouche_rhs_lower": frac_text(rhs),
            "zero_count_with_multiplicity": 1,
            "simple_zero": True,
            "evidence_status": "NUMERICALLY_CERTIFIED",
        },
        "second_derivative_majorant": {
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
        },
        "no_cancellation_gate": {
            "A_of_1_minus_disc_nonzero": True,
            "B_on_disc_nonzero": True,
            "B_of_1_minus_disc_nonzero": True,
            "linear_parent_on_disc_nonzero": True,
            "completed_xi_on_disc_nonzero": True,
            "conclusion": "det(S_H) has one extra pole on D and one zero on 1-D, plus conjugates, while completed xi is nonzero on D",
            "status": "NUMERICALLY_CERTIFIED",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED_FOR_UNRENORMALIZED_MELLIN_PARITY_CANDIDATE",
            "route_b_invocation_allowed": False,
        },
        "decisions": {
            "scalar_kappa_ratio": "STOP",
            "ordinary_Fredholm_multiplier": "STOP_NONCOMPACT_MULTIPLICATION_OPERATOR",
            "unrenormalized_parity_scattering": "STOP_CERTIFIED_EXTRA_DIVISOR",
            "posthoc_zero_removal": "FORBIDDEN",
            "independently_derived_reference_cancellation": "OPEN_FINAL_ESCAPE_GATE",
            "homogeneous_cubic_pivot": "GO_NEXT_BIG_DOOR",
        },
        "scope": {
            "no_RH_proof": True,
            "no_Riemann_zero_table_used": True,
            "one_local_certified_extra_divisor_is_sufficient": True,
            "no_global_strip_zero_census_claimed": True,
            "formal_symbol_not_yet_operator_scattering": True,
        },
    }


def build_certificate() -> dict[str, Any]:
    payload = build_payload()
    return {
        "schema": SCHEMA,
        "payload_sha256": hashlib.sha256(canonical_json(payload)).hexdigest(),
        "payload": payload,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    encoded = json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
