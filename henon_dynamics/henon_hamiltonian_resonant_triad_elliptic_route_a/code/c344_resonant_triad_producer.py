#!/usr/bin/env python3
"""Deterministic exact/high-precision evidence producer for HCS-C344."""
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
OUTPUT = ROOT / "results/c344_resonant_triad_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C344/2026-09-03.yaml"
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "6cad36134e348ea562025fc6a8dd91003962fe5c50944b4b52d2611d8526ff7b"
EVAL_SEMANTIC = "65c82147824ba8cfdbf1f4dea119bfab26ab6c1df5f36939087e244fc2161ac0"
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

PAIRS = [
    (Fraction(1), Fraction(2)), (Fraction(1), Fraction(3)),
    (Fraction(2), Fraction(3)), (Fraction(2), Fraction(5)),
    (Fraction(3), Fraction(5)), (Fraction(3, 2), Fraction(7, 2)),
    (Fraction(4, 3), Fraction(5, 2)), (Fraction(5, 4), Fraction(9, 4)),
    (Fraction(2), Fraction(2)), (Fraction(3), Fraction(3)),
    (Fraction(5), Fraction(8)), (Fraction(8), Fraction(5)),
]
LEVELS = [Fraction(1), Fraction(2), Fraction(3)]


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def qmp(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def dec(value: mp.mpf) -> str:
    return mp.nstr(value, 60, strip_zeros=False, min_fixed=0, max_fixed=0)


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


def cubic(x: Fraction, n1: Fraction, n2: Fraction, h2: Fraction) -> Fraction:
    return 4*x*(n1-x)*(n2-x)-h2


def rational_bracket(n1: Fraction, n2: Fraction, h2: Fraction,
                     left: Fraction, right: Fraction, iterations: int = 84) -> list[str]:
    fl = cubic(left, n1, n2, h2)
    fr = cubic(right, n1, n2, h2)
    if fl == 0 or fr == 0 or fl*fr >= 0:
        raise AssertionError("invalid root bracket")
    for _ in range(iterations):
        middle = (left+right)/2
        fm = cubic(middle, n1, n2, h2)
        if fm == 0:
            left = middle-Fraction(1, 2**(iterations+8))
            right = middle+Fraction(1, 2**(iterations+8))
            break
        if fl*fm < 0:
            right, fr = middle, fm
        else:
            left, fl = middle, fm
    return [qstr(left), qstr(right)]


def mp_root(n1: Fraction, n2: Fraction, h2: Fraction,
            left: Fraction, right: Fraction) -> mp.mpf:
    lo, hi = qmp(left), qmp(right)
    hh = qmp(h2)
    f = lambda x: 4*x*(qmp(n1)-x)*(qmp(n2)-x)-hh
    flo = f(lo)
    for _ in range(280):
        mid = (lo+hi)/2
        fm = f(mid)
        if flo*fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo+hi)/2


def regular_rows() -> list[dict]:
    rows = []
    mp.mp.dps = 100
    for n1, n2 in PAIRS:
        nminus, nplus = min(n1, n2), max(n1, n2)
        xw = nminus/2
        fw = xw*(n1-xw)*(n2-xw)
        for level in LEVELS:
            h2 = level*fw
            high = n1+n2+h2+1
            while cubic(high, n1, n2, h2) <= 0:
                high *= 2
            rational_intervals = [
                rational_bracket(n1, n2, h2, Fraction(0), xw),
                rational_bracket(n1, n2, h2, xw, nminus),
                rational_bracket(n1, n2, h2, nplus, high),
            ]
            roots = [
                mp_root(n1, n2, h2, Fraction(item[0]), Fraction(item[1]))
                for item in rational_intervals
            ]
            r1, r2, r3 = roots
            modulus = (r2-r1)/(r3-r1)
            period = 2*mp.ellipk(modulus)/mp.sqrt(r3-r1)
            for sign in (-1, 1):
                h = sign*mp.sqrt(qmp(h2))
                delta1 = -h*mp.ellippi((r2-r1)/(qmp(n1)-r1), modulus) / (
                    mp.sqrt(r3-r1)*(qmp(n1)-r1))
                delta2 = -h*mp.ellippi((r2-r1)/(qmp(n2)-r1), modulus) / (
                    mp.sqrt(r3-r1)*(qmp(n2)-r1))
                rows.append({
                    "n1": qstr(n1), "n2": qstr(n2), "level": qstr(level),
                    "h_sign": sign, "h_squared": qstr(h2), "witness_x": qstr(xw),
                    "root_intervals": rational_intervals,
                    "roots_decimal": [dec(value) for value in roots],
                    "root_sum": qstr(n1+n2), "root_pair_sum": qstr(n1*n2),
                    "root_product": qstr(h2/4),
                    "jacobi_modulus_squared": dec(modulus),
                    "intensity_period": dec(period),
                    "phase_increment_1": dec(delta1),
                    "phase_increment_2": dec(delta2),
                    "closure_rule": "full state closes iff both phase increments divided by 2*pi are rational",
                })
    return rows


def zero_hamiltonian_rows() -> list[dict]:
    rows = []
    mp.mp.dps = 100
    for n1, n2 in PAIRS:
        nminus, nplus = min(n1, n2), max(n1, n2)
        if n1 == n2:
            rows.append({
                "n1": qstr(n1), "n2": qstr(n2), "face": "equal_invariant_separatrix",
                "modulus_squared": "1", "intensity_formula": "N*tanh(sqrt(N)*(t-t0))^2",
                "amplitude_formula": "sqrt(N)*(sech,sech,-i*tanh) up to the two torus phases",
                "intensity_period": None, "full_state_period": None,
                "endpoint": "heteroclinic between opposite points of the z3-axis equilibrium family",
            })
        else:
            modulus = qmp(nminus/nplus)
            intensity_period = 2*mp.ellipk(modulus)/mp.sqrt(qmp(nplus))
            rows.append({
                "n1": qstr(n1), "n2": qstr(n2), "face": "unequal_invariant_periodic_transfer",
                "modulus_squared": qstr(nminus/nplus),
                "intensity_formula": "Nminus*sn(sqrt(Nplus)*(t-t0)|Nminus/Nplus)^2",
                "amplitude_formula": "cn/dn/(-i sn) with the smaller invariant assigned to cn and sn",
                "intensity_period": dec(intensity_period),
                "full_state_period": dec(2*intensity_period),
                "endpoint": "both zero-amplitude chart crossings are smooth in the complex variables",
            })
    return rows


def relative_equilibrium_rows() -> list[dict]:
    rows = []
    mp.mp.dps = 100
    for n1, n2 in PAIRS:
        s = qmp(n1+n2)
        product = qmp(n1*n2)
        xstar = (s-mp.sqrt(s*s-3*product))/3
        hmax = 2*mp.sqrt(xstar*(qmp(n1)-xstar)*(qmp(n2)-xstar))
        for sign in (-1, 1):
            h = sign*hmax
            omega1 = -h/(2*(qmp(n1)-xstar))
            omega2 = -h/(2*(qmp(n2)-xstar))
            omega3 = -h/(2*xstar)
            if n1 == n2:
                closure = "periodic symmetric relative equilibrium with omega1=omega2 and omega3=omega1+omega2"
            elif (n1, n2) in ((Fraction(5), Fraction(8)), (Fraction(8), Fraction(5))):
                closure = "periodic rational-frequency witness with absolute omega1/omega2 equal to 2 or 1/2"
            else:
                closure = "full state closes iff omega1/omega2 is rational; no generic closure is asserted"
            rows.append({
                "n1": qstr(n1), "n2": qstr(n2), "h_sign": sign,
                "critical_x": dec(xstar), "maximum_abs_h": dec(hmax),
                "omega1": dec(omega1), "omega2": dec(omega2), "omega3": dec(omega3),
                "critical_equation": "3*x^2-2*(N1+N2)*x+N1*N2=0",
                "phase_lock": "omega3=omega1+omega2",
                "closure_classification": closure,
            })
    return rows


def make_data() -> dict:
    evaluation_raw = EVALUATION.read_bytes()
    if sha(evaluation_raw) != EVAL_RAW or semantic_yaml_hash(evaluation_raw) != EVAL_SEMANTIC:
        raise AssertionError("evaluation lock mismatch")
    regular = regular_rows()
    zero = zero_hamiltonian_rows()
    relative = relative_equilibrium_rows()
    data = {
        "schema": "hcs-c344-resonant-triad-v1",
        "candidate_id": "HCS-C344",
        "obstruction_id": "HEN-O328",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0", "sha256": EVALUATOR,
        },
        "evaluation": {
            "path": "evaluations/route_a/HCS-C344/2026-09-03.yaml",
            "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC,
        },
        "model": {
            "hamiltonian": "H=z1*z2*conjugate(z3)+conjugate(z1)*conjugate(z2)*z3",
            "poisson_bracket": "{f,g}=-i*sum(df_dzj*dg_dconjugatezj-df_dconjugatezj*dg_dzj)",
            "equations": "i*z1'=conjugate(z2)*z3; i*z2'=conjugate(z1)*z3; i*z3'=z1*z2",
            "invariants": "N1=abs(z1)^2+abs(z3)^2; N2=abs(z2)^2+abs(z3)^2; H",
            "reduction": "x=abs(z3)^2; x'^2=4*x*(N1-x)*(N2-x)-H^2",
            "domain": "all z in complex three-space with source interaction time",
        },
        "theorem_contract": {
            "global_integrability": "the flow is global and H,N1,N2 are generically independent commuting integrals",
            "regular_solution": "every nonzero-H regular intensity is an sn-squared oscillation between the two accessible roots",
            "phase_return": "two complete third-kind integrals reconstruct the torus phases and both rationality conditions are necessary and sufficient for full-state closure",
            "zero_h_boundary": "unequal invariants give full period twice the intensity period; equal invariants give a heteroclinic separatrix",
            "double_root_boundary": "maximal absolute H gives a relative equilibrium whose full state closes exactly at rational frequency ratio",
            "scope_boundary": "no quantized domain theorem, full quantum spectrum, arithmetic orbit ledger, target determinant, or Route-B result is claimed",
        },
        "references": [
            {"identifier": "10.1103/PhysRev.127.1918", "role": "primary coupled optical three-wave amplitude source"},
            {"identifier": "10.1109/JRPROC.1956.275145", "role": "primary Manley-Rowe energy-relation source"},
            {"identifier": "10.1103/RevModPhys.51.275", "role": "authoritative primary resonant three-wave treatment"},
        ],
        "collision_boundary": {
            "C211": "Hamiltonian Lotka-Volterra period annulus, not a complex resonant wave triad with two phase returns",
            "C230": "open Toda Lax scattering, not a cubic three-mode wave interaction",
            "C235": "cyclic population dynamics with mutation, not a canonical complex Hamiltonian triad",
            "C256": "KdV traveling-wave cnoidal profiles, not full finite-dimensional complex-amplitude dynamics",
        },
        "nonclaims": [
            "No priority claim is made for three-wave equations, Manley-Rowe relations, or elliptic integration.",
            "Intensity recurrence alone is not claimed to imply recurrence of the full complex state.",
            "The formal bosonic analogy is not a proved self-adjoint quantization or a complete quantum spectrum.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "parameter_grid": {
            "pairs": [[qstr(a), qstr(b)] for a, b in PAIRS],
            "regular_levels": [qstr(value) for value in LEVELS],
            "hamiltonian_signs": [-1, 1],
            "root_bracket_iterations": 84,
            "decimal_digits": 60,
            "evidence_role": "exact and high-precision finite receipt, not proof by sampling",
        },
        "regular_rows": regular,
        "zero_hamiltonian_rows": zero,
        "relative_equilibrium_rows": relative,
        "boundary_atlas": {
            "origin_and_axes": "the origin and each complex coordinate axis are equilibrium families",
            "n1_or_n2_zero": "if either Manley-Rowe invariant vanishes the state lies on an equilibrium axis",
            "h_zero_unequal": "smooth chart crossings; intensity period is half the full complex-state period",
            "h_zero_equal": "sech/sech/tanh heteroclinic with infinite period",
            "maximal_abs_h": "double accessible root and two-frequency relative equilibrium",
            "coupling_zero": "identity flow; every nonzero real coupling is reduced by time rescaling and sign reversal",
            "complex_conjugation": "complex conjugation paired with time reversal preserves the geometric intensity orbit",
            "formal_quantization": "bosonic cubic interaction is only a formal hint; no operator-domain or spectral theorem is asserted",
        },
        "enumeration": {
            "regular_rows": len(regular), "zero_hamiltonian_rows": len(zero),
            "relative_equilibrium_rows": len(relative), "audited_leaf_count": 0,
        },
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data)
    data["payload_sha256"] = sha(json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    return data


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C344 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    raw = json.dumps(make_data(), sort_keys=True, indent=2, ensure_ascii=False)+"\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(raw)
    print(f"C344_PRODUCER_PASS {sha(raw.encode())}")


if __name__ == "__main__":
    main()
