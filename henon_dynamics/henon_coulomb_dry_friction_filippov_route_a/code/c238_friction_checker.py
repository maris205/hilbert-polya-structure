#!/usr/bin/env python3
"""Producer-independent checker for the C238 dry-friction certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c238_friction_evidence.json"
SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
SERIALIZED_DIGITS = 64
mp.mp.dps = 90

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
NUM_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")

REST_CASES = [("rest_a1_3_2", F(1), F(1), F(3, 2), 1), ("rest_a1_3", F(1), F(1), F(3), 1), ("rest_a1_4", F(1), F(1), F(4), 1), ("rest_a1_10", F(1), F(1), F(10), 1), ("rest_a2_2", F(2), F(3), F(2), 1), ("rest_a2_5", F(2), F(3), F(5), 1), ("rest_negative", F(1), F(2), F(7, 2), -1), ("rest_stick", F(2), F(3), F(1, 2), 1)]
GENERAL_CASES = [("vpos", F(1), F(1), F(0), F(2)), ("vpos_left", F(2), F(3), F(-1, 2), F(3, 2)), ("vneg", F(1), F(1), F(0), F(-2)), ("vneg_right", F(2), F(3), F(3, 2), F(-1)), ("vpos_near", F(3), F(2), F(1, 3), F(1, 5)), ("vneg_near", F(3), F(2), F(-1, 4), F(-1, 3)), ("already_stick", F(1), F(1), F(1, 2), F(0)), ("rest_outside", F(1), F(1), F(5, 2), F(0))]
STICK_CASES = [("stick_inside", F(1), F(1), F(1, 2)), ("stick_threshold_plus", F(2), F(3), F(3, 4)), ("release_plus", F(2), F(3), F(2)), ("release_minus", F(2), F(3), F(-2)), ("stick_threshold_minus", F(2), F(3), F(-3, 4))]
HARMONIC_CASES = [("harmonic_quarter", F(1), F(1), F(0), F(1, 2)), ("harmonic_half", F(2), F(1), F(0), F(1, 4)), ("harmonic_mixed", F(3), F(1, 2), F(2, 3), F(1, 5)), ("harmonic_negative", F(1), F(-1, 2), F(1, 3), F(2, 3))]
DISSIPATION_CASES = [("drop_3_2", F(1), F(1), F(3, 2)), ("drop_3", F(1), F(1), F(3)), ("drop_5", F(2), F(3), F(5)), ("drop_7_2", F(1), F(2), F(7, 2)), ("drop_10", F(1), F(1), F(10))]


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(v):
    if isinstance(v, mp.mpf):
        return v
    q = v if isinstance(v, F) else F(v)
    return mp.mpf(q.numerator) / q.denominator


def dec(v: mp.mpf) -> str:
    if abs(v) < mp.mpf("1e-82"): v = mp.mpf("0")
    return mp.nstr(v, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-70, max_fixed=70)


def close(value: str, expected: mp.mpf, label: str, check, tol=mp.mpf("2e-40")) -> None:
    syntax = isinstance(value, str) and NUM_RE.fullmatch(value) is not None
    check(syntax, label + " syntax")
    check(syntax and abs(mp.mpf(value) - expected) <= tol * max(1, abs(expected)), label + " value")


def afriction(omega: F, c: F) -> F:
    return c / (omega * omega)


def ceil_frac(q: F) -> int:
    return -((-q.numerator) // q.denominator)


def energy(omega: F, x, v) -> mp.mpf:
    om, xm, vm = mpq(omega), mpq(x), mpq(v)
    return (vm * vm + om * om * xm * xm) / 2


def independent_rest(omega: F, c: F, A: F, orientation: int):
    af = afriction(omega, c)
    if c == 0:
        return False, None, [], None, None
    if A <= af:
        return True, 0, [orientation * A], orientation * A, mp.mpf(0)
    n = ceil_frac((A - af) / (2 * af))
    turns = [orientation * ((-1) ** k) * (A - 2 * k * af) for k in range(1, n + 1)]
    return False, n, turns, turns[-1], mp.mpf(n) * mp.pi / mpq(omega)


def independent_first_turn(omega: F, c: F, x0: F, v0: F) -> dict:
    af = afriction(omega, c)
    om, xm, vm = mpq(omega), mpq(x0), mpq(v0)
    if c == 0:
        return {"regime": "harmonic_no_capture", "center": None, "radius": None, "initial_phase": None, "phase_time": None, "first_turn": None, "remaining_half_cycles": None, "moving_arc_count": None, "stopping_turn": None, "stopping_time": None}
    if v0 == 0:
        if abs(x0) <= af:
            return {"regime": "stick", "center": None, "radius": "0.0", "initial_phase": "0.0", "phase_time": "0.0", "first_turn": str(x0), "remaining_half_cycles": 0, "moving_arc_count": 0, "stopping_turn": str(x0), "stopping_time": "0.0"}
        sign = 1 if x0 > 0 else -1
        _, n, turns, final, tm = independent_rest(omega, c, abs(x0), sign)
        phase0 = "0.0" if sign > 0 else dec(mp.pi)
        return {"regime": "rest_release", "center": str(sign * af), "radius": dec(mpq(abs(x0)) - mpq(af)), "initial_phase": phase0, "phase_time": dec(mp.pi / om), "first_turn": str(sign * (2 * af - abs(x0))), "remaining_half_cycles": max(0, n - 1), "moving_arc_count": n, "stopping_turn": str(final), "stopping_time": dec(tm)}
    if v0 > 0:
        center = -af; R = mp.sqrt((xm + mpq(af)) ** 2 + (vm / om) ** 2); theta = mp.atan2(-vm / om, xm + mpq(af)); phase = -theta / om; turn = -mpq(af) + R
    else:
        center = af; R = mp.sqrt((xm - mpq(af)) ** 2 + (vm / om) ** 2); theta = mp.atan2(-vm / om, xm - mpq(af)); phase = (mp.pi - theta) / om; turn = mpq(af) - R
    mag = abs(turn); rem = 0 if mag <= mpq(af) else int(mp.ceil((mag - mpq(af)) / (2 * mpq(af))))
    stop_mag = mag - 2 * mpq(af) * rem
    stop = (1 if turn >= 0 else -1) * stop_mag * ((-1) ** rem)
    return {"regime": "slip_then_capture", "center": dec(mpq(center)), "radius": dec(R), "initial_phase": dec(theta), "phase_time": dec(phase), "first_turn": dec(turn), "remaining_half_cycles": rem, "moving_arc_count": 1 + rem, "stopping_turn": dec(stop), "stopping_time": dec(phase + rem * mp.pi / om)}


def quick_preflight(data: dict) -> None:
    assert set(data) == TOP_KEYS
    assert data["schema"] == "hcs-c238-coulomb-dry-friction-v1" and data["candidate_id"] == "HCS-C238"
    assert data["source_commit"] == SOURCE_COMMIT and data["fixed_epoch"] == FIXED_EPOCH and data["scope_literal"] == SCOPE
    assert data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert len(data["regression"]["rest_rows"]) == 8 and len(data["regression"]["general_rows"]) == 8
    print("C238 quick hostile preflight: PASS")


def validate(data: dict) -> int:
    checks = 0
    def check(ok: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not ok: raise AssertionError(label)
    def exact(a, b, label: str) -> None:
        check(type(a) is type(b), label + " type"); check(a == b, label)

    check(set(data) == TOP_KEYS, "top closure")
    exact(data["schema"], "hcs-c238-coulomb-dry-friction-v1", "schema"); exact(data["candidate_id"], "HCS-C238", "candidate"); exact(data["evaluation_date"], "2026-08-29", "date"); exact(data["source_commit"], SOURCE_COMMIT, "source"); exact(data["fixed_epoch"], FIXED_EPOCH, "epoch"); exact(data["scope_literal"], SCOPE, "scope")
    exact(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator"); check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple"); check(data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route verdict"); check(set(data["scope_flags"]) == SCOPE_KEYS and all(v is False for v in data["scope_flags"].values()), "scope firewall")
    check(data["regression"]["working_digits"] == 90 and data["regression"]["serialized_digits"] == 64, "precision")
    check("unique global forward trajectory" in data["theorem"]["wellposedness"] and "Backward uniqueness is not claimed" in data["theorem"]["wellposedness"], "forward-only wellposedness scope")
    check(data["theorem"]["rest_map"].startswith("For c>0,") and data["theorem"]["capture_count"].startswith("For c>0,"), "positive-friction capture scope")

    rr = data["regression"]["rest_rows"]; check(len(rr) == 8 and data["regression"]["rest_row_count"] == 8, "rest count")
    rkeys = {"case_id", "omega", "c", "A", "orientation", "friction_length", "initial_energy", "sticking_initial", "half_cycles", "turning_points", "stopping_turn", "stopping_time", "final_energy", "captured"}
    for i, row in enumerate(rr):
        check(set(row) == rkeys, f"rest {i} keys"); cid, om, c, A, orient = REST_CASES[i]; exact(row["case_id"], cid, f"rest {i} id"); exact(row["omega"], str(om), f"rest {i} omega"); exact(row["c"], str(c), f"rest {i} c"); exact(row["A"], str(A), f"rest {i} A"); exact(row["orientation"], orient, f"rest {i} orientation")
        af = afriction(om, c); exact(row["friction_length"], str(af), f"rest {i} af"); close(row["initial_energy"], energy(om, orient * A, F(0)), f"rest {i} E0", check)
        stick, n, turns, final, tm = independent_rest(om, c, A, orient); exact(row["sticking_initial"], stick, f"rest {i} initial stick"); exact(row["half_cycles"], n, f"rest {i} count"); exact(row["turning_points"], [str(q) for q in turns], f"rest {i} turns"); exact(row["stopping_turn"], str(final), f"rest {i} final turn"); close(row["stopping_time"], tm, f"rest {i} stop time", check); close(row["final_energy"], energy(om, final, F(0)), f"rest {i} Ef", check); exact(row["captured"], c > 0 and final is not None and abs(final) <= af, f"rest {i} captured")
        check(final is not None and abs(final) <= af, f"rest {i} threshold")

    gr = data["regression"]["general_rows"]; check(len(gr) == 8 and data["regression"]["general_row_count"] == 8, "general count")
    gkeys = {"case_id", "omega", "c", "x0", "v0", "friction_length", "regime", "center", "radius", "initial_phase", "phase_time", "first_turn", "remaining_half_cycles", "moving_arc_count", "stopping_turn", "stopping_time", "initial_energy"}
    for i, row in enumerate(gr):
        check(set(row) == gkeys, f"general {i} keys"); cid, om, c, x0, v0 = GENERAL_CASES[i]; exact(row["case_id"], cid, f"general {i} id"); exact(row["omega"], str(om), f"general {i} omega"); exact(row["c"], str(c), f"general {i} c"); exact(row["x0"], str(x0), f"general {i} x0"); exact(row["v0"], str(v0), f"general {i} v0"); exact(row["friction_length"], str(afriction(om, c)), f"general {i} af")
        expected = independent_first_turn(om, c, x0, v0)
        for key in ("regime", "center", "radius", "initial_phase", "phase_time", "first_turn", "remaining_half_cycles", "moving_arc_count", "stopping_turn", "stopping_time"):
            exact(row[key], expected[key], f"general {i} {key}")
        close(row["initial_energy"], energy(om, x0, v0), f"general {i} energy", check)
        if expected["stopping_turn"] is not None:
            val = mp.mpf(expected["stopping_turn"]) if NUM_RE.fullmatch(expected["stopping_turn"]) else mp.mpf(0)
            check(abs(val) <= mpq(afriction(om, c)) + mp.mpf("1e-35"), f"general {i} capture threshold")

    sr = data["regression"]["stick_rows"]; check(len(sr) == 5 and data["regression"]["stick_row_count"] == 5, "stick count")
    skeys = {"case_id", "omega", "c", "x0", "v0", "friction_length", "regime", "selected_acceleration", "static_inequality"}
    for i, row in enumerate(sr):
        check(set(row) == skeys, f"stick {i} keys"); cid, om, c, x0 = STICK_CASES[i]; exact(row["case_id"], cid, f"stick {i} id"); exact(row["omega"], str(om), f"stick {i} omega"); exact(row["c"], str(c), f"stick {i} c"); exact(row["x0"], str(x0), f"stick {i} x0"); exact(row["v0"], "0", f"stick {i} v0"); af = afriction(om, c); exact(row["friction_length"], str(af), f"stick {i} af")
        if x0 > af: regime, acc, inside = "release_left", -(om * om) * x0 + c, False
        elif x0 < -af: regime, acc, inside = "release_right", -(om * om) * x0 - c, False
        elif abs(x0) == af: regime, acc, inside = "stick_threshold", F(0), True
        else: regime, acc, inside = "stick_interior", F(0), True
        exact(row["regime"], regime, f"stick {i} regime"); exact(row["selected_acceleration"], str(acc), f"stick {i} acc"); exact(row["static_inequality"], inside, f"stick {i} inequality")

    hr = data["regression"]["harmonic_rows"]; check(len(hr) == 4 and data["regression"]["harmonic_row_count"] == 4, "harmonic count")
    hkeys = {"case_id", "omega", "c", "x0", "v0", "time", "x", "v", "energy", "frequency"}
    for i, row in enumerate(hr):
        check(set(row) == hkeys, f"harmonic {i} keys"); cid, om, x0, v0, t = HARMONIC_CASES[i]; exact(row["case_id"], cid, f"harmonic {i} id"); exact(row["omega"], str(om), f"harmonic {i} omega"); exact(row["c"], "0", f"harmonic {i} c"); exact(row["x0"], str(x0), f"harmonic {i} x0"); exact(row["v0"], str(v0), f"harmonic {i} v0"); exact(row["time"], str(t), f"harmonic {i} t")
        omm, tm, xm, vm = mpq(om), mpq(t), mpq(x0), mpq(v0); xx = xm * mp.cos(omm * tm) + vm / omm * mp.sin(omm * tm); vv = vm * mp.cos(omm * tm) - omm * xm * mp.sin(omm * tm); close(row["x"], xx, f"harmonic {i} x", check); close(row["v"], vv, f"harmonic {i} v", check); close(row["energy"], energy(om, xx, vv), f"harmonic {i} E", check); close(row["frequency"], omm, f"harmonic {i} frequency", check)

    dr = data["regression"]["dissipation_rows"]; check(len(dr) == 5 and data["regression"]["dissipation_row_count"] == 5, "dissipation count")
    dkeys = {"case_id", "omega", "c", "A", "friction_length", "first_turn", "energy_initial", "energy_first_turn", "energy_drop", "c_times_distance", "dissipation_residual"}
    for i, row in enumerate(dr):
        check(set(row) == dkeys, f"dissipation {i} keys"); cid, om, c, A = DISSIPATION_CASES[i]; exact(row["case_id"], cid, f"dissipation {i} id"); exact(row["omega"], str(om), f"dissipation {i} omega"); exact(row["c"], str(c), f"dissipation {i} c"); exact(row["A"], str(A), f"dissipation {i} A"); af = afriction(om, c); x1 = 2 * af - A; e0 = energy(om, A, F(0)); e1 = energy(om, x1, F(0)); drop = e0 - e1; expected = mpq(c) * abs(mpq(A) - mpq(x1)); exact(row["friction_length"], str(af), f"dissipation {i} af"); exact(row["first_turn"], str(x1), f"dissipation {i} turn"); close(row["energy_initial"], e0, f"dissipation {i} E0", check); close(row["energy_first_turn"], e1, f"dissipation {i} E1", check); close(row["energy_drop"], drop, f"dissipation {i} drop", check); close(row["c_times_distance"], expected, f"dissipation {i} work", check); close(row["dissipation_residual"], drop - expected, f"dissipation {i} residual", check, tol=mp.mpf("3e-35")); check(abs(drop - expected) < mp.mpf("1e-35"), f"dissipation {i} exact")

    check(len(data["exact_identities"]) == 10, "identity count"); check(len(data["citations"]) == 3 and all(set(c) == {"key", "claim", "source"} for c in data["citations"]), "citation closure"); check(len(data["nonclaims"]) == 5 and all(isinstance(q, str) for q in data["nonclaims"]), "nonclaim closure")
    return checks


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE); parser.add_argument("--quick", action="store_true"); args = parser.parse_args(); data = json.loads(args.evidence.read_text())
    if args.quick: quick_preflight(data)
    else: print(f"C238 independent checker: PASS ({validate(data)} assertions; maximal-monotone capture, phase ledger and harmonic face)")


if __name__ == "__main__":
    main()
