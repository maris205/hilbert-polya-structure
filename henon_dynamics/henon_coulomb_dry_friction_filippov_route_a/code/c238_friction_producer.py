#!/usr/bin/env python3
"""Deterministic certificate producer for Coulomb dry friction.

The inclusion is frozen with a maximal-monotone/viability convention.  The
finite ledger records exact rational turning maps and high-precision phases;
it is not a claim about an arithmetic orbit owner.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c238_friction_evidence.json"
WORKING_DIGITS = 90
SERIALIZED_DIGITS = 64
mp.mp.dps = WORKING_DIGITS


def ftext(v: F) -> str:
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"


def mpq(v: F | int | str) -> mp.mpf:
    if isinstance(v, mp.mpf):
        return v
    q = v if isinstance(v, F) else F(v)
    return mp.mpf(q.numerator) / q.denominator


def dec(v: mp.mpf, digits: int = SERIALIZED_DIGITS) -> str:
    if abs(v) < mp.mpf("1e-82"):
        v = mp.mpf("0")
    return mp.nstr(v, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def ceil_fraction(q: F) -> int:
    return -((-q.numerator) // q.denominator)


def energy(omega: F, x: F | mp.mpf, v: F | mp.mpf) -> mp.mpf:
    om, xm, vm = mpq(omega), mpq(x), mpq(v)
    return (vm * vm + om * om * xm * xm) / 2


def friction_length(omega: F, c: F) -> F:
    return c / (omega * omega)


def rest_capture(omega: F, c: F, A: F, orientation: int = 1) -> dict:
    """Exact half-cycle map for a rest at x=orientation*A, A>=0."""
    af = friction_length(omega, c)
    if c == 0:
        return {"sticking_initial": False, "half_cycles": None, "turning_points": [], "stopping_turn": None, "stopping_time": None, "friction_length": ftext(af)}
    if A <= af:
        return {"sticking_initial": True, "half_cycles": 0, "turning_points": [ftext(orientation * A)], "stopping_turn": ftext(orientation * A), "stopping_time": "0.0", "friction_length": ftext(af)}
    n = ceil_fraction((A - af) / (2 * af))
    turns = [orientation * ((-1) ** k) * (A - 2 * k * af) for k in range(1, n + 1)]
    final = turns[-1]
    return {"sticking_initial": False, "half_cycles": n, "turning_points": [ftext(q) for q in turns], "stopping_turn": ftext(final), "stopping_time": dec(mp.mpf(n) * mp.pi / mpq(omega)), "friction_length": ftext(af)}


def rest_row(case_id: str, omega: F, c: F, A: F, orientation: int = 1) -> dict:
    cap = rest_capture(omega, c, A, orientation)
    x0 = orientation * A
    af = friction_length(omega, c)
    e0 = energy(omega, x0, F(0))
    ef = energy(omega, F(cap["stopping_turn"]) if cap["stopping_turn"] is not None else x0, F(0)) if cap["stopping_turn"] is not None else None
    return {"case_id": case_id, "omega": ftext(omega), "c": ftext(c), "A": ftext(A), "orientation": orientation, "friction_length": ftext(af), "initial_energy": dec(e0), "sticking_initial": cap["sticking_initial"], "half_cycles": cap["half_cycles"], "turning_points": cap["turning_points"], "stopping_turn": cap["stopping_turn"], "stopping_time": cap["stopping_time"], "final_energy": None if ef is None else dec(ef), "captured": c > 0 and cap["stopping_turn"] is not None and abs(F(cap["stopping_turn"])) <= af}


def first_turn(omega: F, c: F, x0: F, v0: F) -> dict:
    """First v=0 event and subsequent finite capture for c>0."""
    af = friction_length(omega, c)
    om, xm, vm = mpq(omega), mpq(x0), mpq(v0)
    if c == 0:
        return {"regime": "harmonic_no_capture", "center": None, "radius": None, "initial_phase": None, "phase_time": None, "first_turn": None, "remaining_half_cycles": None, "moving_arc_count": None, "stopping_turn": None, "stopping_time": None}
    if v0 == 0:
        if abs(x0) <= af:
            return {"regime": "stick", "center": None, "radius": "0.0", "initial_phase": "0.0", "phase_time": "0.0", "first_turn": ftext(x0), "remaining_half_cycles": 0, "moving_arc_count": 0, "stopping_turn": ftext(x0), "stopping_time": "0.0"}
        orientation = 1 if x0 > 0 else -1
        cap = rest_capture(omega, c, abs(x0), orientation)
        phase0 = "0.0" if orientation > 0 else dec(mp.pi)
        return {"regime": "rest_release", "center": ftext(orientation * af), "radius": dec(mpq(abs(x0)) - mpq(af)), "initial_phase": phase0, "phase_time": dec(mp.pi / om), "first_turn": ftext(orientation * (2 * af - abs(x0))), "remaining_half_cycles": max(0, int(cap["half_cycles"]) - 1), "moving_arc_count": cap["half_cycles"], "stopping_turn": cap["stopping_turn"], "stopping_time": cap["stopping_time"]}
    if v0 > 0:
        center = -af
        R = mp.sqrt((xm + mpq(af)) ** 2 + (vm / om) ** 2)
        theta = mp.atan2(-vm / om, xm + mpq(af))
        phase_time = -theta / om
        turn = -mpq(af) + R
    else:
        center = af
        R = mp.sqrt((xm - mpq(af)) ** 2 + (vm / om) ** 2)
        theta = mp.atan2(-vm / om, xm - mpq(af))
        phase_time = (mp.pi - theta) / om
        turn = mpq(af) - R
    magnitude = abs(turn)
    rem = 0
    if magnitude > mpq(af):
        rem = int(mp.ceil((magnitude - mpq(af)) / (2 * mpq(af))))
    stop_mag = magnitude - 2 * mpq(af) * rem
    stop_turn = (1 if turn >= 0 else -1) * stop_mag * ((-1) ** rem)
    return {"regime": "slip_then_capture", "center": dec(mpq(center)), "radius": dec(R), "initial_phase": dec(theta), "phase_time": dec(phase_time), "first_turn": dec(turn), "remaining_half_cycles": rem, "moving_arc_count": 1 + rem, "stopping_turn": dec(stop_turn), "stopping_time": dec(phase_time + rem * mp.pi / om)}


def general_row(case_id: str, omega: F, c: F, x0: F, v0: F) -> dict:
    out = first_turn(omega, c, x0, v0)
    return {"case_id": case_id, "omega": ftext(omega), "c": ftext(c), "x0": ftext(x0), "v0": ftext(v0), "friction_length": ftext(friction_length(omega, c)), **out, "initial_energy": dec(energy(omega, x0, v0))}


def stick_row(case_id: str, omega: F, c: F, x0: F) -> dict:
    af = friction_length(omega, c)
    if x0 > af:
        acc = -(omega * omega) * x0 + c
        regime = "release_left"
    elif x0 < -af:
        acc = -(omega * omega) * x0 - c
        regime = "release_right"
    elif abs(x0) == af:
        acc = F(0)
        regime = "stick_threshold"
    else:
        acc = F(0)
        regime = "stick_interior"
    return {"case_id": case_id, "omega": ftext(omega), "c": ftext(c), "x0": ftext(x0), "v0": "0", "friction_length": ftext(af), "regime": regime, "selected_acceleration": ftext(acc), "static_inequality": abs(x0) <= af}


def harmonic_row(case_id: str, omega: F, x0: F, v0: F, t: F) -> dict:
    om, tm = mpq(omega), mpq(t)
    xm, vm = mpq(x0), mpq(v0)
    x = xm * mp.cos(om * tm) + vm / om * mp.sin(om * tm)
    v = vm * mp.cos(om * tm) - om * xm * mp.sin(om * tm)
    return {"case_id": case_id, "omega": ftext(omega), "c": "0", "x0": ftext(x0), "v0": ftext(v0), "time": ftext(t), "x": dec(x), "v": dec(v), "energy": dec(energy(omega, x, v)), "frequency": dec(om)}


def dissipation_row(case_id: str, omega: F, c: F, A: F) -> dict:
    af = friction_length(omega, c)
    x1 = 2 * af - A
    e0 = energy(omega, A, F(0)); e1 = energy(omega, x1, F(0))
    drop = e0 - e1
    expected = mpq(c) * abs(mpq(A) - mpq(x1))
    return {"case_id": case_id, "omega": ftext(omega), "c": ftext(c), "A": ftext(A), "friction_length": ftext(af), "first_turn": ftext(x1), "energy_initial": dec(e0), "energy_first_turn": dec(e1), "energy_drop": dec(drop), "c_times_distance": dec(expected), "dissipation_residual": dec(drop - expected)}


REST_CASES = [("rest_a1_3_2", F(1), F(1), F(3, 2), 1), ("rest_a1_3", F(1), F(1), F(3), 1), ("rest_a1_4", F(1), F(1), F(4), 1), ("rest_a1_10", F(1), F(1), F(10), 1), ("rest_a2_2", F(2), F(3), F(2), 1), ("rest_a2_5", F(2), F(3), F(5), 1), ("rest_negative", F(1), F(2), F(7, 2), -1), ("rest_stick", F(2), F(3), F(1, 2), 1)]
GENERAL_CASES = [("vpos", F(1), F(1), F(0), F(2)), ("vpos_left", F(2), F(3), F(-1, 2), F(3, 2)), ("vneg", F(1), F(1), F(0), F(-2)), ("vneg_right", F(2), F(3), F(3, 2), F(-1)), ("vpos_near", F(3), F(2), F(1, 3), F(1, 5)), ("vneg_near", F(3), F(2), F(-1, 4), F(-1, 3)), ("already_stick", F(1), F(1), F(1, 2), F(0)), ("rest_outside", F(1), F(1), F(5, 2), F(0))]
STICK_CASES = [("stick_inside", F(1), F(1), F(1, 2)), ("stick_threshold_plus", F(2), F(3), F(3, 4)), ("release_plus", F(2), F(3), F(2)), ("release_minus", F(2), F(3), F(-2)), ("stick_threshold_minus", F(2), F(3), F(-3, 4))]
HARMONIC_CASES = [("harmonic_quarter", F(1), F(1), F(0), F(1, 2)), ("harmonic_half", F(2), F(1), F(0), F(1, 4)), ("harmonic_mixed", F(3), F(1, 2), F(2, 3), F(1, 5)), ("harmonic_negative", F(1), F(-1, 2), F(1, 3), F(2, 3))]
DISSIPATION_CASES = [("drop_3_2", F(1), F(1), F(3, 2)), ("drop_3", F(1), F(1), F(3)), ("drop_5", F(2), F(3), F(5)), ("drop_7_2", F(1), F(2), F(7, 2)), ("drop_10", F(1), F(1), F(10))]


def build() -> dict:
    rest = [rest_row(*spec) for spec in REST_CASES]
    general = [general_row(*spec) for spec in GENERAL_CASES]
    sticks = [stick_row(*spec) for spec in STICK_CASES]
    harmonic = [harmonic_row(*spec) for spec in HARMONIC_CASES]
    diss = [dissipation_row(*spec) for spec in DISSIPATION_CASES]
    data = {
        "schema": "hcs-c238-coulomb-dry-friction-v1", "candidate_id": "HCS-C238", "evaluation_date": "2026-08-29", "source_commit": SOURCE_COMMIT, "fixed_epoch": FIXED_EPOCH, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "A maximal-monotone Coulomb oscillator has an exact stick--slip capture atlas, half-cycle turning map, and a separate conservative harmonic face.",
        "frozen_object": {"inclusion": "x_dot=v, v_dot=-omega^2*x-c*xi, xi in Sign(v)", "sign_graph": "Sign(v)=+1 if v>0, -1 if v<0, and [-1,1] if v=0", "parameters": "omega>0, c>=0; a_friction=c/omega^2", "selection_law": "at v=0 stick iff |x|<=a_friction; outside release uniquely inward", "clock": "physical continuous mechanical time", "normalization": "E=(v^2+omega^2*x^2)/2", "determinant_convention": "none; no orbit/Fredholm determinant", "arithmetic_origin": "none; source-defined mechanical parameters", "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert--Polya operators"},
        "theorem": {"wellposedness": "The frozen maximal-monotone/viability law gives a unique global forward trajectory; sticking is selected on |x|<=a_friction and an exterior rest releases inward. Backward uniqueness is not claimed after capture.", "energy": "On slip E'=-c|v| and on stick E'=0, so E is nonincreasing.", "rest_map": "For c>0, a positive rest A>a_friction has first half-cycle turn x1=2*a_friction-A; each further moving half-cycle reduces the turning magnitude by 2*a_friction.", "capture_count": "For c>0, the exact number of moving half-cycles from a rest A>a_friction is ceil((A-a_friction)/(2*a_friction)); the stopping turn has absolute value <=a_friction.", "general_phase": "For v0>0 the slip center is -a_friction, R=sqrt((x0+a_friction)^2+(v0/omega)^2), next turn=-a_friction+R; for v0<0 the center is +a_friction and next turn=a_friction-R.", "first_stop": "The initial phase is atan2(-v0/omega,x0+a_friction) for v0>0 and atan2(-v0/omega,x0-a_friction) for v0<0; adding integer pi/omega half-cycles gives an exact finite stopping time.", "harmonic_face": "When c=0, x=x0 cos(omega t)+(v0/omega)sin(omega t), v=v0 cos(omega t)-omega*x0 sin(omega t), and energy is conserved.", "boundary_faces": "At |x|=a_friction the selected state sticks; c>0 captures every sliding trajectory in finite time under the frozen law.", "route_boundary": "The mechanical flow has no intrinsic arithmetic labels, primitive repetition law, target determinant, or Hilbert--Polya operator."},
        "regression": {"rest_rows": rest, "general_rows": general, "stick_rows": sticks, "harmonic_rows": harmonic, "dissipation_rows": diss, "rest_row_count": len(rest), "general_row_count": len(general), "stick_row_count": len(sticks), "harmonic_row_count": len(harmonic), "dissipation_row_count": len(diss), "working_digits": WORKING_DIGITS, "serialized_digits": SERIALIZED_DIGITS},
        "exact_identities": [{"identity_id": "energy_slip", "formula": "d[(v^2+omega^2*x^2)/2]/dt=-c*|v|"}, {"identity_id": "static_set", "formula": "v=0 and |omega^2*x|<=c"}, {"identity_id": "positive_rest_map", "formula": "for c>0, x_1=2(c/omega^2)-A"}, {"identity_id": "turning_reduction", "formula": "for c>0, |A_{k+1}|=|A_k|-2c/omega^2"}, {"identity_id": "capture_count", "formula": "for c>0, n=ceil((A-a_friction)/(2a_friction))"}, {"identity_id": "v_positive_center", "formula": "x=-a_friction+R cos(theta)"}, {"identity_id": "v_negative_center", "formula": "x=+a_friction+R cos(theta)"}, {"identity_id": "harmonic_solution", "formula": "x=x0 cos(omega t)+(v0/omega)sin(omega t)"}, {"identity_id": "harmonic_energy", "formula": "E(t)=E(0) when c=0"}, {"identity_id": "threshold_release", "formula": "x>a_friction => x_ddot=-omega^2*x+c<0; x<-a_friction => x_ddot=-omega^2*x-c>0"}],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "strongest_positive": "A convention-complete maximal-monotone stick--slip theorem and exact finite capture ledger are proved.", "strongest_failure": "There is no arithmetic origin, primitive periodic repetition product, target determinant, or natural Hilbert--Polya lift."},
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [{"key": "Moreau1979", "claim": "maximal-monotone dry-friction vocabulary", "source": "J.-J. Moreau, Application of convex analysis to some problems of dry friction, in Trends in Applications of Pure Mathematics to Mechanics, Vol. 2, Pitman (1979), pp. 263--280"}, {"key": "Brogliato1999", "claim": "Coulomb friction and nonsmooth mechanics context", "source": "B. Brogliato, Nonsmooth Mechanics (1999)"}, {"key": "LaSalle1960", "claim": "energy/invariance terminology only", "source": "J. P. LaSalle, Some extensions of Liapunov's second method (1960)"}],
        "nonclaims": ["literature priority or exhaustive novelty certification", "a stochastic friction law or a general differential inclusion beyond the frozen Sign graph", "target arithmetic, Euler factors, root numbers, automorphy, target divisor or functional equation", "a primitive-orbit zeta, Fredholm determinant, or Hilbert--Polya operator", "external peer review, acceptance, or numerical evidence promoted to a theorem"],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT); args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build(); args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C238_PRODUCER_PASS", "rest_rows": len(data["regression"]["rest_rows"]), "general_rows": len(data["regression"]["general_rows"]), "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
