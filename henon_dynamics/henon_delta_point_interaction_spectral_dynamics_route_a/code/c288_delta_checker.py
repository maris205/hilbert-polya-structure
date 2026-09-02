#!/usr/bin/env python3
"""Strict, producer-independent checker for HCS-C288.

The heat cells are reconstructed by numerical inverse Laplace transformation
of the independently derived resolvent.  In particular, this file contains
no copy of the producer's closed erfc heat formula.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c288_delta_evidence.json"
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]

TOP_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "model",
    "theorem_contract", "proof_contract", "route_a", "scope_flags",
    "enumeration", "resolvent_cells", "pole_cells", "scattering_cells",
    "bound_state_cells", "heat_cells", "references", "nonclaims",
    "payload_sha256",
}
MODEL = {
    "units": "hbar=2m=1",
    "form": "q_alpha[psi]=integral |psi'|^2+alpha|psi(0)|^2 on H^1(R)",
    "operator": "H_alpha=-d^2/dx^2 on R\\{0}",
    "interface": "psi continuous; psi'(0+)-psi'(0-)=alpha psi(0)",
    "clock": "unitary time exp(-it H_alpha) and heat time exp(-t H_alpha)",
}
THEOREM = {
    "realization": "closed lower-bounded H^1 form and the continuous derivative-jump domain define one self-adjoint operator",
    "resolvent": "the full negative-energy Green kernel is one explicit rank-one correction with the bound-state pole removed",
    "spectrum": "[0,infinity) is purely absolutely continuous with no singular-continuous part; exactly one eigenvalue -alpha^2/4 occurs iff alpha<0",
    "scattering": "left-right amplitudes, odd free channel, even unitary phase, and all energy limits are exact",
    "heat": "the erfc heat kernel and integrated diagonal relative trace hold for every real alpha and t>0",
    "boundary": "attractive, free, repulsive, pole, zero-energy, high-energy, small-time, and large-time faces are separated",
}
PROOF = {
    "form": "the one-dimensional trace inequality makes point evaluation infinitesimally form bounded",
    "krein": "solve the free Green equation and one scalar jump equation",
    "completeness": "odd/even half-line transforms give absolutely continuous spectral densities on [0,infinity), no singular-continuous part, and only the displayed attractive pole",
    "heat_inversion": "the explicit Laplace identity for the resolvent correction gives the erfc heat term",
    "trace_integral": "one integration by parts evaluates the diagonal defect",
    "finite_role": "finite cells audit constants and branches but do not prove the all-parameter theorem",
}
ROUTE = {
    "tuple": TUPLE,
    "overall": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
}
SCOPE_FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_input": False,
}
ENUMERATION = {
    "alpha_values": ["-4", "-2", "-1", "0", "1", "2", "4"],
    "regular_resolvent_cells": 32,
    "pole_cells": 3,
    "scattering_cells": 28,
    "bound_state_cells": 3,
    "heat_cells": 8,
}
REFERENCE = {
    "id": "Albeverio1988",
    "authors": "Sergio Albeverio, Friedrich Gesztesy, Raphael Hoegh-Krohn, and Helge Holden",
    "title": "Solvable Models in Quantum Mechanics",
    "venue": "Theoretical and Mathematical Physics, Springer, 1988",
    "identifier": "10.1007/978-3-642-88201-2",
    "url": "https://doi.org/10.1007/978-3-642-88201-2",
    "ownership": "direct owner; one-center delta-interaction in one dimension, pages 75-90",
}
NONCLAIMS = [
    "classical point-interaction formulas are not claimed as literature originality",
    "finite evidence does not prove the arbitrary-parameter analytic theorem",
    "a source Hamiltonian and relative heat trace are not a target determinant or Hilbert-Polya operator",
]
DECIMAL_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?$")


class Checks:
    def __init__(self) -> None:
        self.n = 0

    def ok(self, condition: bool, label: str) -> None:
        self.n += 1
        if not condition:
            raise AssertionError(label)


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite_json(token: str) -> None:
    raise ValueError(f"non-finite JSON number: {token}")


def strict_load(path: Path) -> dict[str, Any]:
    value = json.loads(
        path.read_text(),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_nonfinite_json,
    )
    if type(value) is not dict:
        raise TypeError("top-level JSON value must be an object")
    return value


def phash(data: dict[str, Any]) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def exact_keys(c: Checks, value: Any, keys: set[str], label: str) -> None:
    c.ok(type(value) is dict, f"{label} object type")
    c.ok(set(value) == keys, f"{label} exact keys")


def exact_type(c: Checks, value: Any, cls: type, label: str) -> None:
    c.ok(type(value) is cls, f"{label} type")


def require_exact_type(value: Any, cls: type, label: str) -> None:
    """Schema type gate kept separate from the numerical assertion count."""
    if type(value) is not cls:
        raise TypeError(f"{label} must have exact type {cls.__name__}")


def rational(c: Checks, value: Any, label: str) -> Fraction:
    exact_type(c, value, str, label)
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise AssertionError(f"{label} rational syntax") from error
    c.ok(str(result) == value, f"{label} canonical rational")
    return result


def decimal(c: Checks, value: Any, label: str) -> mp.mpf:
    exact_type(c, value, str, label)
    c.ok(DECIMAL_RE.fullmatch(value) is not None, f"{label} decimal syntax")
    result = mp.mpf(value)
    c.ok(mp.isfinite(result), f"{label} finite")
    return result


def inverse_laplace_kernel(alpha: mp.mpf, t: mp.mpf, x: mp.mpf, y: mp.mpf) -> mp.mpf:
    """Invert the independently reconstructed Green kernel in the s-plane."""
    def transformed(s: mp.mpc) -> mp.mpc:
        kappa = mp.sqrt(s)
        free = mp.exp(-kappa * abs(x - y)) / (2 * kappa)
        correction = -alpha * mp.exp(-kappa * (abs(x) + abs(y)))
        correction /= 2 * kappa * (2 * kappa + alpha)
        return free + correction

    return mp.invertlaplace(transformed, t, method="dehoog", degree=100)


def inverse_laplace_relative_trace(alpha: mp.mpf, t: mp.mpf) -> mp.mpf:
    """Integrate the diagonal resolvent defect, then invert its transform.

    On the diagonal the rank-one term is
    -alpha exp(-2*kappa*|x|)/(2*kappa*(2*kappa+alpha)).  Its spatial
    integral uses int_R exp(-2*kappa*|x|) dx=1/kappa.  This reconstructs
    the relative trace without inserting the producer's closed formula.
    """
    if alpha == 0:
        return mp.mpf("0")

    def transformed(s: mp.mpc) -> mp.mpc:
        kappa = mp.sqrt(s)
        return -alpha / (2 * kappa * kappa * (2 * kappa + alpha))

    return mp.invertlaplace(transformed, t, method="dehoog", degree=100)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = strict_load(args.input)
    c = Checks()

    exact_keys(c, data, TOP_KEYS, "top level")
    exact_type(c, data["payload_sha256"], str, "payload hash")
    c.ok(re.fullmatch(r"[0-9a-f]{64}", data["payload_sha256"]) is not None, "payload hash syntax")
    c.ok(data["payload_sha256"] == phash(data), "payload hash")
    c.ok(data["schema"] == "hcs-c288-delta-point-interaction-v1", "schema")
    c.ok(data["candidate_id"] == "HCS-C288", "candidate")
    c.ok(data["evaluation_date"] == "2026-09-02", "date")
    c.ok(data["source_commit"] == SOURCE, "source")
    exact_type(c, data["fixed_epoch"], int, "epoch")
    c.ok(data["fixed_epoch"] == 1788307200, "epoch value")
    c.ok(data["scope_literal"] == SCOPE, "scope")

    exact_keys(c, data["evaluator"], {"version", "sha256"}, "evaluator")
    for key in ("version", "sha256"):
        require_exact_type(data["evaluator"][key], str, f"evaluator {key}")
    c.ok(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}, "evaluator value")
    exact_keys(c, data["model"], set(MODEL), "model")
    for key in MODEL:
        require_exact_type(data["model"][key], str, f"model {key}")
    c.ok(data["model"] == MODEL, "model value")
    exact_keys(c, data["theorem_contract"], set(THEOREM), "theorem contract")
    for key in THEOREM:
        require_exact_type(data["theorem_contract"][key], str, f"theorem {key}")
    c.ok(data["theorem_contract"] == THEOREM, "theorem contract value")
    exact_keys(c, data["proof_contract"], set(PROOF), "proof contract")
    for key in PROOF:
        require_exact_type(data["proof_contract"][key], str, f"proof {key}")
    c.ok(data["proof_contract"] == PROOF, "proof contract value")
    exact_keys(c, data["route_a"], set(ROUTE), "route")
    require_exact_type(data["route_a"]["tuple"], list, "route tuple")
    for index, value in enumerate(data["route_a"]["tuple"]):
        require_exact_type(value, str, f"route tuple {index}")
    require_exact_type(data["route_a"]["overall"], str, "route overall")
    require_exact_type(data["route_a"]["route_b_invocation_allowed"], bool, "route B flag")
    c.ok(data["route_a"] == ROUTE, "route value")
    exact_keys(c, data["scope_flags"], set(SCOPE_FLAGS), "scope flags")
    for key in SCOPE_FLAGS:
        require_exact_type(data["scope_flags"][key], bool, f"scope flag {key}")
    c.ok(data["scope_flags"] == SCOPE_FLAGS, "scope flag values")
    exact_keys(c, data["enumeration"], set(ENUMERATION), "enumeration")
    require_exact_type(data["enumeration"]["alpha_values"], list, "alpha values")
    for index, value in enumerate(data["enumeration"]["alpha_values"]):
        require_exact_type(value, str, f"alpha value {index}")
    for key in set(ENUMERATION) - {"alpha_values"}:
        require_exact_type(data["enumeration"][key], int, f"enumeration {key}")
    c.ok(data["enumeration"] == ENUMERATION, "enumeration value")

    exact_type(c, data["references"], list, "references")
    c.ok(len(data["references"]) == 1, "reference count")
    exact_keys(c, data["references"][0], set(REFERENCE), "reference")
    for key in REFERENCE:
        require_exact_type(data["references"][0][key], str, f"reference {key}")
    c.ok(data["references"][0] == REFERENCE, "reference value")
    exact_type(c, data["nonclaims"], list, "nonclaims")
    for index, value in enumerate(data["nonclaims"]):
        require_exact_type(value, str, f"nonclaim {index}")
    c.ok(data["nonclaims"] == NONCLAIMS, "nonclaim values")

    alphas = tuple(Fraction(x) for x in ENUMERATION["alpha_values"])
    kappas = (Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3))
    expected_regular = {(a, k) for a in alphas for k in kappas if 2 * k + a != 0}
    expected_poles = {(a, k) for a in alphas for k in kappas if 2 * k + a == 0}

    regular = data["resolvent_cells"]
    exact_type(c, regular, list, "resolvent cells")
    c.ok(len(regular) == ENUMERATION["regular_resolvent_cells"], "regular count")
    seen_regular: set[tuple[Fraction, Fraction]] = set()
    regular_keys = {
        "alpha", "kappa", "free_coefficient", "image_coefficient",
        "interface_value_coefficient", "derivative_jump_ratio",
        "source_derivative_jump",
    }
    for index, row in enumerate(regular):
        exact_keys(c, row, regular_keys, f"resolvent row {index}")
        a = rational(c, row["alpha"], f"resolvent {index} alpha")
        k = rational(c, row["kappa"], f"resolvent {index} kappa")
        key = (a, k)
        c.ok(key not in seen_regular, f"resolvent {index} unique")
        seen_regular.add(key)
        c.ok(key in expected_regular, f"resolvent {index} expected key")
        free = rational(c, row["free_coefficient"], f"resolvent {index} free")
        image = rational(c, row["image_coefficient"], f"resolvent {index} image")
        value = rational(c, row["interface_value_coefficient"], f"resolvent {index} value")
        ratio = rational(c, row["derivative_jump_ratio"], f"resolvent {index} ratio")
        source_jump = rational(c, row["source_derivative_jump"], f"resolvent {index} source jump")
        c.ok(free == 1 / (2 * k), f"resolvent {index} free value")
        c.ok(image == -a / (2 * k * (2 * k + a)), f"resolvent {index} image value")
        c.ok(value == free + image == 1 / (2 * k + a), f"resolvent {index} interface value")
        jump = a / (2 * (2 * k + a)) - (-a / (2 * (2 * k + a)))
        c.ok(jump == a * value, f"resolvent {index} interface equation")
        c.ok(ratio == a, f"resolvent {index} jump ratio")
        c.ok(source_jump == -1, f"resolvent {index} source jump value")
    c.ok(seen_regular == expected_regular, "complete regular grid")

    poles = data["pole_cells"]
    exact_type(c, poles, list, "pole cells")
    c.ok(len(poles) == ENUMERATION["pole_cells"], "pole count")
    seen_poles: set[tuple[Fraction, Fraction]] = set()
    for index, row in enumerate(poles):
        exact_keys(c, row, {"alpha", "kappa", "pole"}, f"pole row {index}")
        a = rational(c, row["alpha"], f"pole {index} alpha")
        k = rational(c, row["kappa"], f"pole {index} kappa")
        exact_type(c, row["pole"], bool, f"pole {index} flag")
        key = (a, k)
        c.ok(key not in seen_poles, f"pole {index} unique")
        seen_poles.add(key)
        c.ok(key in expected_poles, f"pole {index} expected key")
        c.ok(row["pole"] is True, f"pole {index} true")
        c.ok(2 * k + a == 0, f"pole {index} equation")
    c.ok(seen_poles == expected_poles, "complete pole grid")

    scattering = data["scattering_cells"]
    exact_type(c, scattering, list, "scattering cells")
    c.ok(len(scattering) == ENUMERATION["scattering_cells"], "scattering count")
    momenta = (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(4))
    expected_scattering = {(a, k) for a in alphas for k in momenta}
    seen_scattering: set[tuple[Fraction, Fraction]] = set()
    scatter_keys = {
        "alpha", "k", "reflection_probability", "transmission_probability",
        "probability_sum", "odd_channel", "even_channel_modulus_squared",
    }
    for index, row in enumerate(scattering):
        exact_keys(c, row, scatter_keys, f"scattering row {index}")
        a = rational(c, row["alpha"], f"scattering {index} alpha")
        k = rational(c, row["k"], f"scattering {index} k")
        key = (a, k)
        c.ok(key not in seen_scattering, f"scattering {index} unique")
        seen_scattering.add(key)
        c.ok(key in expected_scattering, f"scattering {index} expected key")
        reflect = rational(c, row["reflection_probability"], f"scattering {index} reflection")
        transmit = rational(c, row["transmission_probability"], f"scattering {index} transmission")
        probability_sum = rational(c, row["probability_sum"], f"scattering {index} sum")
        odd = rational(c, row["odd_channel"], f"scattering {index} odd")
        even_modulus = rational(c, row["even_channel_modulus_squared"], f"scattering {index} even")
        denominator = 4 * k * k + a * a
        c.ok(reflect == a * a / denominator, f"scattering {index} reflection value")
        c.ok(transmit == 4 * k * k / denominator, f"scattering {index} transmission value")
        c.ok(reflect + transmit == probability_sum == 1, f"scattering {index} flux")
        c.ok(odd == even_modulus == 1, f"scattering {index} channels")
    c.ok(seen_scattering == expected_scattering, "complete scattering grid")

    bound = data["bound_state_cells"]
    exact_type(c, bound, list, "bound-state cells")
    c.ok(len(bound) == ENUMERATION["bound_state_cells"], "bound-state count")
    expected_bound = {Fraction(-4), Fraction(-2), Fraction(-1)}
    seen_bound: set[Fraction] = set()
    bound_keys = {
        "alpha", "energy", "decay_kappa", "normalization_squared",
        "normalization_integral",
    }
    for index, row in enumerate(bound):
        exact_keys(c, row, bound_keys, f"bound row {index}")
        a = rational(c, row["alpha"], f"bound {index} alpha")
        c.ok(a not in seen_bound, f"bound {index} unique")
        seen_bound.add(a)
        c.ok(a in expected_bound, f"bound {index} expected alpha")
        energy = rational(c, row["energy"], f"bound {index} energy")
        decay = rational(c, row["decay_kappa"], f"bound {index} decay")
        norm = rational(c, row["normalization_squared"], f"bound {index} norm")
        integral = rational(c, row["normalization_integral"], f"bound {index} integral")
        c.ok(energy == -a * a / 4, f"bound {index} energy value")
        c.ok(decay == -a / 2, f"bound {index} decay value")
        c.ok(norm == -a / 2, f"bound {index} normalization value")
        c.ok(norm * (-2 / a) == integral == 1, f"bound {index} normalization integral")
    c.ok(seen_bound == expected_bound, "complete bound-state grid")

    heat_rows = data["heat_cells"]
    exact_type(c, heat_rows, list, "heat cells")
    c.ok(len(heat_rows) == ENUMERATION["heat_cells"], "heat count")
    expected_heat = {
        (Fraction(-2), Fraction(1, 4), Fraction(0), Fraction(1)),
        (Fraction(-2), Fraction(2), Fraction(1, 2), Fraction(-1)),
        (Fraction(-1), Fraction(3, 4), Fraction(1), Fraction(2)),
        (Fraction(0), Fraction(1, 2), Fraction(-1), Fraction(1)),
        (Fraction(1), Fraction(1, 4), Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(3), Fraction(2), Fraction(-1, 2)),
        (Fraction(2), Fraction(1), Fraction(1, 2), Fraction(1, 2)),
        (Fraction(4), Fraction(1, 8), Fraction(-2), Fraction(1)),
    }
    seen_heat: set[tuple[Fraction, Fraction, Fraction, Fraction]] = set()
    heat_keys = {"alpha", "t", "x", "y", "kernel", "relative_trace"}
    mp.mp.dps = 80
    tolerance = mp.mpf("2e-40")
    for index, row in enumerate(heat_rows):
        exact_keys(c, row, heat_keys, f"heat row {index}")
        a_q = rational(c, row["alpha"], f"heat {index} alpha")
        t = decimal(c, row["t"], f"heat {index} t")
        x = decimal(c, row["x"], f"heat {index} x")
        y = decimal(c, row["y"], f"heat {index} y")
        kernel = decimal(c, row["kernel"], f"heat {index} kernel")
        relative_trace = decimal(c, row["relative_trace"], f"heat {index} trace")
        key = (a_q, Fraction(row["t"]), Fraction(row["x"]), Fraction(row["y"]))
        c.ok(key not in seen_heat, f"heat {index} unique")
        seen_heat.add(key)
        c.ok(key in expected_heat, f"heat {index} expected key")
        c.ok(t > 0, f"heat {index} positive time")
        a = mp.mpf(a_q.numerator) / a_q.denominator

        # Interface audit in Laplace space at a point to the right of every
        # possible attractive pole.  All retained y values are nonzero, so
        # the only jump at x=0 is the interaction jump.
        sigma = mp.mpf("4") + a * a
        kappa = mp.sqrt(sigma)
        interface_value = mp.exp(-kappa * abs(y)) / (2 * kappa + a)
        right_derivative = a * mp.exp(-kappa * abs(y)) / (2 * (2 * kappa + a))
        left_derivative = -right_derivative
        c.ok(mp.almosteq(right_derivative - left_derivative, a * interface_value), f"heat {index} transform interface")

        reconstructed = inverse_laplace_kernel(a, t, x, y)
        reconstructed_trace = inverse_laplace_relative_trace(a, t)
        c.ok(abs(kernel - reconstructed) < tolerance, f"heat {index} inverse Laplace kernel")
        c.ok(abs(relative_trace - reconstructed_trace) < tolerance, f"heat {index} integrated diagonal trace")
    c.ok(seen_heat == expected_heat, "complete heat grid")

    print(
        f"C288 independent Laplace/interface checker: PASS ({c.n} assertions; "
        "strict duplicate-rejecting schema)"
    )


if __name__ == "__main__":
    main()
