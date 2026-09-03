#!/usr/bin/env python3
"""Deterministic high-precision receipts for the HCS-C327 delta comb."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c327_kronig_penney_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C327/2026-09-03.yaml"
SOURCE = "1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
mp.mp.dps = 100

FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
Q_VALUES = [Fraction(-8), Fraction(-6), Fraction(-4), Fraction(-3), Fraction(-1),
            Fraction(1), Fraction(3), Fraction(4), Fraction(8)]


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mpf(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def dec(value: mp.mpf) -> str:
    if abs(value) < mp.mpf("1e-86"):
        return "0.0"
    return mp.nstr(value, 72, strip_zeros=False)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def semantic_yaml_hash(raw: str) -> str:
    value = yaml.safe_load(raw)
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha(canonical)


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def bisect_increasing(function, target: mp.mpf, left: mp.mpf, right: mp.mpf) -> mp.mpf:
    """Fixed-iteration monotone bisection; endpoints must bracket target."""
    while function(right) <= target:
        right *= 2
    for _ in range(360):
        middle = (left + right) / 2
        if function(middle) < target:
            left = middle
        else:
            right = middle
    return (left + right) / 2


def y_plus(q_value: Fraction) -> mp.mpf:
    h = -mpf(q_value)
    return bisect_increasing(lambda y: 2 * y * mp.tanh(y / 2), h, mp.mpf("0"), max(2, h + 2))


def y_minus(q_value: Fraction) -> mp.mpf:
    h = -mpf(q_value)
    return bisect_increasing(lambda y: 2 * y / mp.tanh(y / 2), h, mp.mpf("1e-80"), h + 2)


def shifted_edge(q_value: Fraction, n: int) -> mp.mpf | None:
    """Non-fixed edge adjacent to n*pi; n=0 is allowed only for q>0."""
    coupling = mpf(q_value)
    if coupling > 0:
        left, right = n * mp.pi, (n + 1) * mp.pi
    else:
        if n == 1 and coupling < -4:
            return None
        if n == 1 and coupling == -4:
            return mp.mpf("0")
        left, right = (n - 1) * mp.pi, n * mp.pi
    epsilon = mp.mpf("1e-80")
    lo, hi = left + epsilon, right - epsilon
    function = lambda x: 2 * x * mp.tan((x - n * mp.pi) / 2)
    # The function is strictly increasing on the selected cell.
    for _ in range(360):
        middle = (lo + hi) / 2
        if function(middle) < coupling:
            lo = middle
        else:
            hi = middle
    return (lo + hi) / 2


def discriminant_z(z: mp.mpf, coupling: mp.mpf) -> mp.mpf:
    if z > 0:
        x = mp.sqrt(z)
        return mp.cos(x) + coupling * mp.sin(x) / (2 * x)
    if z < 0:
        y = mp.sqrt(-z)
        return mp.cosh(y) + coupling * mp.sinh(y) / (2 * y)
    return 1 + coupling / 2


def derivative_z(z: mp.mpf, coupling: mp.mpf) -> mp.mpf:
    if z > 0:
        x = mp.sqrt(z)
        return -mp.sin(x) / (2 * x) + coupling * (x * mp.cos(x) - mp.sin(x)) / (4 * x**3)
    if z < 0:
        y = mp.sqrt(-z)
        return -(mp.sinh(y) + coupling * (y * mp.cosh(y) - mp.sinh(y)) / (2 * y**2)) / (2 * y)
    return -mp.mpf("0.5") - coupling / 12


def band_edges(q_value: Fraction, index: int) -> tuple[mp.mpf, mp.mpf]:
    coupling = mpf(q_value)
    if coupling > 0:
        lower_x = shifted_edge(q_value, index)
        if lower_x is None:
            raise RuntimeError("missing repulsive band edge")
        return lower_x**2, ((index + 1) * mp.pi) ** 2
    if coupling == 0:
        return (index * mp.pi) ** 2, ((index + 1) * mp.pi) ** 2
    if index == 0:
        lower = -y_plus(q_value) ** 2
        if coupling > -4:
            upper_x = shifted_edge(q_value, 1)
            if upper_x is None:
                raise RuntimeError("missing weak-attraction edge")
            return lower, upper_x**2
        if coupling == -4:
            return lower, mp.mpf("0")
        return lower, -y_minus(q_value) ** 2
    upper_x = shifted_edge(q_value, index + 1)
    if upper_x is None:
        raise RuntimeError("missing positive band edge")
    return (index * mp.pi) ** 2, upper_x**2


def negative_rows() -> list[dict]:
    rows = []
    for coupling in [value for value in Q_VALUES if value < 0]:
        h = -coupling
        plus = y_plus(coupling)
        minus = y_minus(coupling) if h > 4 else None
        location = "BAND_INTERIOR" if h < 4 else ("BAND_EDGE_MINUS" if h == 4 else "GAP")
        rows.append({
            "q_equals_ga": qstr(coupling),
            "h_equals_minus_ga": qstr(h),
            "delta_at_zero": qstr(1 + coupling / 2),
            "zero_location": location,
            "y_plus": dec(plus),
            "plus_edge_residual": dec(2 * plus * mp.tanh(plus / 2) - mpf(h)),
            "y_minus": None if minus is None else dec(minus),
            "minus_edge_residual": None if minus is None else dec(2 * minus / mp.tanh(minus / 2) - mpf(h)),
            "negative_band_lower_scaled_energy": dec(-plus**2),
            "negative_band_upper_scaled_energy": dec(mp.mpf("0") if minus is None else -minus**2),
            "negative_gap_to_zero": h > 4,
        })
    return rows


def low_edge_rows() -> list[dict]:
    rows = []
    for coupling in Q_VALUES:
        if coupling > 0:
            edge = shifted_edge(coupling, 0)
            kind = "REPULSIVE_POSITIVE_BOTTOM"
        elif coupling > -4:
            edge = shifted_edge(coupling, 1)
            kind = "ATTRACTIVE_ZERO_CONNECTED_UPPER"
        elif coupling == -4:
            edge = mp.mpf("0")
            kind = "ZERO_ANTIPERIODIC_THRESHOLD"
        else:
            edge = None
            kind = "STRONG_ATTRACTION_NO_FIRST_POSITIVE_SHIFTED_EDGE"
        rows.append({
            "q_equals_ga": qstr(coupling),
            "kind": kind,
            "positive_edge_x": None if edge is None else dec(edge),
            "scaled_energy": None if edge is None else dec(edge**2),
            "equation_residual": None if edge is None else ("0.0" if coupling == -4 else dec(
                (2 * edge * mp.tan(edge / 2) - mpf(coupling)) if coupling > 0
                else (2 * edge * mp.tan((edge - mp.pi) / 2) - mpf(coupling))
            )),
        })
    return rows


def bragg_rows() -> list[dict]:
    rows = []
    for coupling in Q_VALUES:
        for n in range(1, 25):
            edge = shifted_edge(coupling, n)
            fixed = n * mp.pi
            if edge is None:
                side = "NONPOSITIVE_THRESHOLD"
                width = None
                positive_axis_portion = fixed**2
                residual = None
            else:
                side = "RIGHT" if coupling > 0 else ("ZERO_THRESHOLD" if edge == 0 else "LEFT")
                width = abs(edge**2 - fixed**2)
                positive_axis_portion = None
                residual = (mp.mpf("0") if coupling == -4 and n == 1 else
                            2 * edge * mp.tan((edge - fixed) / 2) - mpf(coupling))
            asymptotic_error = None
            if width is not None and n >= 2:
                asymptotic_error = n**2 * (width - 2 * abs(mpf(coupling)))
            rows.append({
                "q_equals_ga": qstr(coupling),
                "n": n,
                "fixed_edge_x": dec(fixed),
                "fixed_discriminant": -1 if n % 2 else 1,
                "shifted_edge_exists": edge is not None,
                "shifted_edge_x": None if edge is None else dec(edge),
                "side": side,
                "edge_equation_residual": None if residual is None else dec(residual),
                "scaled_gap_width": None if width is None else dec(width),
                "positive_axis_gap_portion": None if positive_axis_portion is None else dec(positive_axis_portion),
                "n_squared_width_error": None if asymptotic_error is None else dec(asymptotic_error),
                "gap_open": True,
            })
    return rows


def transfer_rows() -> list[dict]:
    rows = []
    scaled_energies = [("-4", -mp.mpf(4)), ("0", mp.mpf(0)), ("1", mp.mpf(1)),
                       ("pi_squared", mp.pi**2), ("9pi_squared/4", 9 * mp.pi**2 / 4)]
    for spacing in (Fraction(1, 2), Fraction(1), Fraction(2)):
        av = mpf(spacing)
        for coupling in Q_VALUES + [Fraction(0)]:
            gv = mpf(coupling) / av
            for token, z in scaled_energies:
                energy = z / av**2
                if z > 0:
                    k = mp.sqrt(energy)
                    c, s = mp.cos(k * av), mp.sin(k * av)
                    p00, p01, p10, p11 = c, s / k, -k * s, c
                elif z < 0:
                    kappa = mp.sqrt(-energy)
                    c, s = mp.cosh(kappa * av), mp.sinh(kappa * av)
                    p00, p01, p10, p11 = c, s / kappa, kappa * s, c
                else:
                    p00, p01, p10, p11 = mp.mpf(1), av, mp.mpf(0), mp.mpf(1)
                m00, m01 = p00, p01
                m10, m11 = gv * p00 + p10, gv * p01 + p11
                delta = (m00 + m11) / 2
                rows.append({
                    "a": qstr(spacing), "q_equals_ga": qstr(coupling), "scaled_energy": token,
                    "g": qstr(coupling / spacing), "energy": dec(energy),
                    "m00": dec(m00), "m01": dec(m01), "m10": dec(m10), "m11": dec(m11),
                    "determinant": dec(m00 * m11 - m01 * m10),
                    "half_trace": dec(delta),
                    "closed_formula": dec(discriminant_z(z, mpf(coupling))),
                    "in_spectrum": abs(delta) <= 1 + mp.mpf("1e-80"),
                })
    return rows


def ids_rows() -> list[dict]:
    rows = []
    for coupling in Q_VALUES + [Fraction(0)]:
        cv = mpf(coupling)
        for index in range(7):
            lower, upper = band_edges(coupling, index)
            middle = (lower + upper) / 2
            delta = discriminant_z(middle, cv)
            derivative = derivative_z(middle, cv)
            phase = mp.acos(((-1) ** index) * delta)
            ids = index + phase / mp.pi
            dos = abs(derivative) / (mp.pi * mp.sqrt(1 - delta**2))
            rows.append({
                "q_equals_ga": qstr(coupling), "band_index": index,
                "lower_scaled_energy": dec(lower), "upper_scaled_energy": dec(upper),
                "mid_scaled_energy": dec(middle), "delta_mid": dec(delta),
                "delta_prime_scaled_energy": dec(derivative),
                "unwrapped_phase": dec(index * mp.pi + phase),
                "ids_per_unit_length_at_a_one": dec(ids),
                "dos_per_unit_length_at_a_one": dec(dos),
            })
    return rows


def make_data() -> dict:
    evaluation_raw = EVALUATION.read_bytes()
    negative = negative_rows()
    low = low_edge_rows()
    bragg = bragg_rows()
    transfer = transfer_rows()
    ids = ids_rows()
    data = {
        "schema": "hcs-c327-kronig-penney-v1",
        "candidate_id": "HCS-C327",
        "obstruction_id": "HEN-O311",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR,
        },
        "evaluation": {
            "path": "evaluations/route_a/HCS-C327/2026-09-03.yaml",
            "raw_sha256": sha(evaluation_raw),
            "semantic_sha256": semantic_yaml_hash(evaluation_raw.decode()),
        },
        "model": {
            "operator": "H=-d^2/dx^2+g sum_{n in Z} delta(x-na)",
            "domain": "a>0 and g real",
            "jump": "psi continuous and psi'(na+)-psi'(na-)=g psi(na)",
            "dimensionless_coupling": "q=ga",
            "dimensionless_energy": "z=Ea^2",
            "discriminant": "Delta=cos(ka)+g sin(ka)/(2k), continuously continued through E=0",
            "clock": "physical unitary time generated by the self-adjoint form owner",
        },
        "theorem_contract": {
            "operator_owner": "the H1 quadratic form is closed and lower semibounded and its operator has the stated point-interaction matching conditions",
            "floquet_spectrum": "spectrum iff abs(Delta(E))<=1; it is purely absolutely continuous",
            "multiplicity": "band interiors have full-line Bloch multiplicity two; nonzero-g edges are simple periodic or antiperiodic fibre edges; g=0 Bragg contacts are double",
            "negative_atlas": "for g<0 the plus edge is h=2y tanh(y/2); a minus edge exists iff -ga>4, with ga=-4 the exact zero threshold",
            "positive_atlas": "nonfixed Bragg partners satisfy ga=2x tan((x-npi)/2); their side is the sign of g and every nonzero-g Bragg gap is open",
            "gap_asymptotic": "the nth high-energy gap has width 2abs(g)/a+O_{ga}(n^-2/a^2)",
            "ids_dos": "on band j, N=(j+acos((-1)^j Delta)/pi)/a and density=abs(Delta_E')/(pi*a*sqrt(1-Delta^2)); N is constant in gaps",
        },
        "references": [
            {"identifier": "10.1098/rspa.1931.0019", "role": "original periodic crystal band-model owner"},
            {"identifier": "10.1090/chel/350", "role": "authoritative point-interaction operator reference"},
            {"identifier": "math/0109129", "role": "pure absolute continuity for periodic singular potentials"},
        ],
        "collision_boundary": {
            "C288": "one isolated point interaction and scattering/resolvent data, not an infinite periodic delta comb with Bloch bands",
            "C308": "non-Hermitian Hatano--Nelson lattice transport, not a self-adjoint continuum singular periodic operator",
            "C318": "finite-range dimerized SSH bulk--edge topology, not a continuum equal-spacing delta-comb band atlas",
            "C323": "finite complete-graph oracle search, not an infinite-volume Floquet Hamiltonian",
        },
        "nonclaims": [
            "No literature-priority claim is made for the Kronig--Penney dispersion, point-interaction realization, or Floquet theory.",
            "The determinant-one transfer matrix is not an Euler factor and Bloch energies are not target zeros.",
            "No target arithmetic datum, root number, automorphy, target divisor, functional equation, Hilbert--Polya operator, or Route-B input is claimed.",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "parameter_grid": {
            "q_values": [qstr(value) for value in Q_VALUES],
            "negative_q_values": ["-8", "-6", "-4", "-3", "-1"],
            "bragg_n": "1..24", "transfer_a": ["1/2", "1", "2"],
            "transfer_scaled_energy": ["-4", "0", "1", "pi_squared", "9pi_squared/4"],
            "ids_band_index": "0..6",
        },
        "negative_atlas_rows": negative,
        "low_edge_rows": low,
        "bragg_rows": bragg,
        "transfer_rows": transfer,
        "ids_dos_rows": ids,
        "enumeration": {
            "negative_atlas_rows": len(negative), "low_edge_rows": len(low),
            "bragg_rows": len(bragg), "transfer_rows": len(transfer),
            "ids_dos_rows": len(ids), "audited_leaf_count": 0,
        },
    }
    before = leaves(data)
    data["enumeration"]["audited_leaf_count"] = before + 1
    body = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha(body)
    return data


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C327 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = make_data()
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(raw)
    print(
        "C327_PRODUCER_PASS "
        f"{data['enumeration']['bragg_rows']} "
        f"{data['enumeration']['audited_leaf_count']} "
        f"{data['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
