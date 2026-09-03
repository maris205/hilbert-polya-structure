#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C337."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c337_kicked_rotor_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C337/2026-09-03.yaml"
SOURCE = "db2c816b7b6bd450f51f79b91842cb882b0bd773"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "1844e53da7f5d2c498518b4b1941ec50358505fe37ec959692bb11b57b1475a2"
EVAL_SEMANTIC = "9a378976e7e821c71e87428a969ec3fb20eaa4861837b28b91ed8fece15d5b56"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600

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


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def gaussian(re: Fraction, im: Fraction) -> list[str]:
    return [qstr(re), qstr(im)]


def minus_i_power(power: int) -> tuple[Fraction, Fraction]:
    return ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1)),
            (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(1)))[power % 4]


def direct_kick_coefficient(q: int, degree: int) -> tuple[Fraction, Fraction]:
    if (degree + q) % 2 or degree < abs(q):
        return Fraction(0), Fraction(0)
    right = (degree + q) // 2
    left = (degree - q) // 2
    if right < 0 or left < 0:
        return Fraction(0), Fraction(0)
    scalar = Fraction(1, (2 ** degree) * math.factorial(right) * math.factorial(left))
    re, im = minus_i_power(degree)
    return scalar * re, scalar * im


def bessel_kick_coefficient(q: int, degree: int) -> tuple[Fraction, Fraction]:
    order = abs(q)
    if degree < order or (degree - order) % 2:
        return Fraction(0), Fraction(0)
    j = (degree - order) // 2
    sign = (-1 if q < 0 and order % 2 else 1) * (-1 if j % 2 else 1)
    scalar = Fraction(sign, (2 ** degree) * math.factorial(j) * math.factorial(order + j))
    re, im = minus_i_power(q)
    return scalar * re, scalar * im


def central_moments(x: Fraction) -> list[Fraction]:
    return [
        Fraction(1), Fraction(0), x * x / 2, Fraction(0),
        x * x / 2 + 3 * x**4 / 8, Fraction(0),
        x * x / 2 + 15 * x**4 / 8 + 5 * x**6 / 16,
    ]


def raw_moments(m: int, centered: list[Fraction]) -> list[Fraction]:
    return [sum(Fraction(math.comb(r, j) * m ** (r - j)) * centered[j]
                for j in range(r + 1)) for r in range(7)]


def semantic_yaml_hash(raw: bytes) -> str:
    value = yaml.safe_load(raw)
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha(canonical)


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(child) for child in value.values())
    if type(value) is list:
        return sum(leaves(child) for child in value)
    return 1


def parity_rows() -> list[dict]:
    rows = []
    for ell in range(1, 13):
        for n in range(-16, 17):
            phase = -1 if (ell * n * n) % 2 else 1
            expected = 1 if ell % 2 == 0 else (-1 if n % 2 else 1)
            if phase != expected:
                raise AssertionError("free-phase parity failure")
            rows.append({"ell": ell, "n": n, "free_phase": phase,
                         "operator_face": "identity" if ell % 2 == 0 else "half_turn"})
    return rows


def formal_rows() -> list[dict]:
    rows = []
    for q in range(-14, 15):
        for degree in range(15):
            direct = direct_kick_coefficient(q, degree)
            bessel = bessel_kick_coefficient(q, degree)
            if direct != bessel:
                raise AssertionError("formal Jacobi--Anger coefficient failure")
            rows.append({"q": q, "degree": degree,
                         "direct_exponential": gaussian(*direct),
                         "bessel_formula": gaussian(*bessel)})
    return rows


def moment_rows() -> list[dict]:
    rows = []
    kappas = [Fraction(-3, 2), Fraction(-1), Fraction(-1, 3), Fraction(0),
              Fraction(2, 5), Fraction(1), Fraction(5, 3)]
    for face in ("even_resonance", "odd_antiresonance"):
        for kappa in kappas:
            for m in range(-3, 4):
                for time in range(9):
                    x = kappa * time if face == "even_resonance" else (kappa if time % 2 else Fraction(0))
                    centered = central_moments(x)
                    raw = raw_moments(m, centered)
                    rows.append({
                        "face": face, "kappa": qstr(kappa), "m": m, "time": time,
                        "effective_bessel_argument": qstr(x),
                        "central_moments_0_to_6": [qstr(value) for value in centered],
                        "raw_moments_0_to_6": [qstr(value) for value in raw],
                        "kinetic_energy": qstr(raw[2] / 2),
                    })
    return rows


def operator_rows() -> list[dict]:
    return [
        {
            "ell": ell,
            "time": time,
            "power_reduction": (
                "K_(t*kappa)" if ell % 2 == 0 else ("I" if time % 2 == 0 else "R K_kappa")
            ),
            "amplitude_phase": (
                "(-i)^(n-m) J_(n-m)(kappa*t)" if ell % 2 == 0
                else ("delta_(n,m)" if time % 2 == 0
                      else "(-1)^n (-i)^(n-m) J_(n-m)(kappa)")
            ),
        }
        for ell in range(1, 13) for time in range(10)
    ]


def numeric_rows() -> list[dict]:
    mp.mp.dps = 90
    pairs = [("-5/2", "1/7"), ("-1", "2/5"), ("-1/3", "3/7"),
             ("0", "1/2"), ("2/5", "2/3"), ("1", "3/4"), ("7/3", "4/5")]
    rows = []
    cutoff = 120
    for xs, us in pairs:
        x = mp.mpf(Fraction(xs).numerator) / Fraction(xs).denominator
        u = mp.mpf(Fraction(us).numerator) / Fraction(us).denominator
        weights = [(q, mp.besselj(q, x) ** 2) for q in range(-cutoff, cutoff + 1)]
        norm = mp.fsum(value for _, value in weights)
        characteristic = mp.fsum(value * mp.e ** (1j * q * u) for q, value in weights)
        target_characteristic = mp.besselj(0, 2 * x * mp.sin(u / 2))
        second = mp.fsum(q * q * value for q, value in weights)
        rows.append({
            "x": xs, "u": us, "cutoff": cutoff, "precision_digits": 90,
            "normalization_error": mp.nstr(abs(norm - 1), 65),
            "characteristic_error": mp.nstr(abs(characteristic - target_characteristic), 65),
            "second_moment_error": mp.nstr(abs(second - x * x / 2), 65),
            "evidence_status": "NUMERICAL_OBSERVATION",
        })
    return rows


def make_data() -> dict:
    evaluation_raw = EVALUATION.read_bytes()
    if sha(evaluation_raw) != EVAL_RAW or semantic_yaml_hash(evaluation_raw) != EVAL_SEMANTIC:
        raise AssertionError("evaluation lock mismatch")
    parity = parity_rows()
    formal = formal_rows()
    moments = moment_rows()
    operators = operator_rows()
    numeric = numeric_rows()
    data = {
        "schema": "hcs-c337-integer-kicked-rotor-v1",
        "candidate_id": "HCS-C337",
        "obstruction_id": "HEN-O321",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation": {"path": "evaluations/route_a/HCS-C337/2026-09-03.yaml",
                       "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC},
        "model": {
            "hilbert_space": "L2(T,dtheta/(2pi)) with basis |n>=exp(i n theta)",
            "momentum": "n_hat=-i d/dtheta with integer spectrum",
            "floquet_order": "U_tau=exp(-i tau n_hat^2/2) exp(-i kappa cos(theta))",
            "resonance_sheet": "tau=2pi ell with ell a positive integer",
            "parameter_domain": "kappa real, m integer, t nonnegative integer",
            "kinetic_energy": "n_hat^2/2",
        },
        "theorem_contract": {
            "parity": "even ell gives identity free factor; odd ell gives half-turn R",
            "even_kernel": "<n|U^t|m>=(-i)^(n-m) J_(n-m)(kappa t)",
            "characteristic": "E exp(iu(n-m))=J_0(2 kappa t sin(u/2)) on the even sheet",
            "moments": "centered moments through six and exact ballistic variance are explicit",
            "odd_involution": "for odd ell, U=R K_kappa and U^2=I",
            "boundaries": "all m, kappa=0, t=0, parity, vector phase, and operator order are explicit",
        },
        "references": [
            {"identifier": "10.1103/PhysRevE.54.5948", "role": "primary antiresonance history"},
            {"identifier": "10.1103/PhysRevE.73.026206", "role": "primary general resonance history"},
            {"identifier": "10.1103/PhysRevLett.96.160403", "role": "primary experimental ballistic-resonance context"},
        ],
        "collision_boundary": {
            "C110": "classical nonautonomous Henon Floquet dynamics, not a quantum rotor",
            "C143": "coined quantum walk, not a cosine-kicked momentum lattice",
            "C148": "open Walsh quantum baker, not a closed rotor unitary",
            "C178": "harmonic metaplectic strobe, not the kicked-rotor parity sheet",
            "C224": "two-level Landau--Zener scattering, not a kicked rotor",
            "C318": "static SSH lattice, not a time-periodic rotor",
            "C323": "finite continuous-time quantum search, not Floquet momentum transport",
        },
        "nonclaims": [
            "No literature-priority claim is made for resonance, antiresonance, or Bessel transport.",
            "No general rational resonance, detuning, localization, or quasienergy theorem is claimed.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert--Polya operator, or Route-B input is claimed.",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "parameter_grid": {
            "ell": "1..12", "momentum": "-16..16 for parity and -3..3 for moments",
            "time": "0..8 for moments and 0..9 for operator words",
            "formal_degree": "0..14", "formal_shift": "-14..14",
            "numeric_cutoff": 120, "numeric_precision_digits": 90,
        },
        "parity_rows": parity,
        "formal_kernel_coefficients": formal,
        "moment_rows": moments,
        "operator_rows": operators,
        "numeric_rows": numeric,
        "boundary_rows": {
            "kappa_zero": "even ell gives I; odd ell gives R; momentum probabilities are stationary",
            "t_zero": "J_q(0)=delta_(q,0) and U^0=I",
            "odd_vector_phase": "at kappa=0, |m> acquires (-1)^m under one odd-sheet kick although its ray and probability law are fixed",
            "odd_period": "U^2=I as an operator; individual states may already be one-step eigenstates",
            "even_nonzero": "for kappa nonzero, the even-sheet variance is kappa^2 t^2/2",
            "operator_order": "free-after-kick is frozen; the reversed product is not silently substituted",
        },
        "enumeration": {
            "parity_rows": len(parity), "formal_coefficient_rows": len(formal),
            "moment_rows": len(moments), "operator_rows": len(operators),
            "numeric_rows": len(numeric),
        },
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data)
    data["payload_sha256"] = sha(json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    return data


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C337 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    raw = json.dumps(make_data(), sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(raw)
    print(f"C337_PRODUCER_PASS {sha(raw.encode())}")


if __name__ == "__main__":
    main()
