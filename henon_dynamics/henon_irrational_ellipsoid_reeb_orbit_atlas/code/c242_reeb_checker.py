#!/usr/bin/env python3
"""Producer-independent checker for the C242 Reeb-flow certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
import math
from pathlib import Path
import re

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c242_reeb_evidence.json"
SOURCE_COMMIT = "489506cf92bfed721f94f22dd0444a60427f90a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
MAX_ITERATE = 12
SERIALIZED_DIGITS = 64
mp.mp.dps = 90
NUM_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")
TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def dec(x: mp.mpf) -> str:
    if abs(x) < mp.mpf("1e-82"):
        x = mp.mpf("0")
    return mp.nstr(x, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-70, max_fixed=70)


def exact_floor_sqrt2(k: int) -> int:
    m = math.isqrt(2 * k * k)
    while (m + 1) ** 2 <= 2 * k * k:
        m += 1
    while m * m > 2 * k * k:
        m -= 1
    return m


def exact_floor_inv(k: int) -> int:
    m = math.isqrt((k * k) // 2)
    while 2 * (m + 1) ** 2 <= k * k:
        m += 1
    while 2 * m * m > k * k:
        m -= 1
    return m


def check_num(value: object, expected: mp.mpf, label: str, check) -> None:
    ok = isinstance(value, str) and NUM_RE.fullmatch(value) is not None
    check(ok, label + " syntax")
    if ok:
        check(abs(mp.mpf(value) - expected) <= mp.mpf("3e-40") * max(1, abs(expected)), label + " value")


def validate(data: dict) -> int:
    count = 0

    def check(ok: bool, label: str) -> None:
        nonlocal count
        count += 1
        if not ok:
            raise AssertionError(label)

    def exact(actual, expected, label: str) -> None:
        check(type(actual) is type(expected), label + " type")
        check(actual == expected, label)

    check(set(data) == TOP_KEYS, "top-level closure")
    exact(data["schema"], "hcs-c242-ellipsoid-reeb-orbit-atlas-v1", "schema")
    exact(data["candidate_id"], "HCS-C242", "candidate")
    exact(data["evaluation_date"], "2026-08-30", "date")
    exact(data["source_commit"], SOURCE_COMMIT, "source lock")
    exact(data["fixed_epoch"], FIXED_EPOCH, "epoch")
    exact(data["scope_literal"], SCOPE, "scope literal")
    exact(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator lock")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "overall route")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B disabled")
    check(set(data["scope_flags"]) == SCOPE_KEYS and all(v is False for v in data["scope_flags"].values()), "scope firewall")
    check(data["regression"]["working_digits"] == 90 and data["regression"]["serialized_digits"] == 64, "precision lock")
    check(data["regression"]["max_iterate"] == MAX_ITERATE, "cutoff lock")
    check("two coordinate" in data["theorem"]["irrational_classification"], "two-orbit theorem wording")
    check("Morse" in data["theorem"]["rational_boundary"] and "no nondegenerate CZ" in data["theorem"]["rational_boundary"], "rational boundary wording")

    irr = data["regression"]["irrational_cases"]
    check(type(irr) is list and len(irr) == 2, "irrational case count")
    expected_cases = [("irrational_sqrt2", "sqrt2"), ("irrational_inverse_sqrt2", "inv_sqrt2")]
    for ci, case in enumerate(irr):
        cid, kind = expected_cases[ci]
        exact(case["case_id"], cid, f"irrational {ci} id")
        exact(case["ratio_kind"], kind, f"irrational {ci} kind")
        check("sqrt(2)" in case["ratio_is_irrational_witness"], f"irrational {ci} witness")
        rows = case["rows"]
        check(type(rows) is list and len(rows) == 2 * MAX_ITERATE, f"irrational {ci} rows")
        row_keys = {"axis", "iterate", "simple_orbit", "a", "b", "ratio", "action", "period", "transverse_angle", "multiplier_real", "multiplier_imaginary", "multiplier_pair", "cz_index", "floor_certificate", "nondegenerate", "regime"}
        for j, row in enumerate(rows):
            check(set(row) == row_keys, f"irrational row {ci}/{j} keys")
            axis = "gamma1" if j < MAX_ITERATE else "gamma2"
            k = j + 1 if j < MAX_ITERATE else j - MAX_ITERATE + 1
            exact(row["axis"], axis, f"irrational row {ci}/{j} axis")
            exact(row["iterate"], k, f"irrational row {ci}/{j} iterate")
            exact(row["simple_orbit"], "gamma_1" if axis == "gamma1" else "gamma_2", f"irrational row {ci}/{j} orbit")
            if kind == "sqrt2":
                a, b = "sqrt(2)", "1"
            else:
                a, b = "1", "sqrt(2)"
            exact(row["a"], a, f"irrational row {ci}/{j} a")
            exact(row["b"], b, f"irrational row {ci}/{j} b")
            effective = kind if axis == "gamma1" else ("inv_sqrt2" if kind == "sqrt2" else "sqrt2")
            ratio_text = "sqrt(2)" if effective == "sqrt2" else "1/sqrt(2)"
            exact(row["ratio"], ratio_text, f"irrational row {ci}/{j} ratio")
            action = f"{k}*{a}" if axis == "gamma1" else f"{k}*{b}"
            exact(row["action"], action, f"irrational row {ci}/{j} action")
            exact(row["period"], action, f"irrational row {ci}/{j} period")
            exact(row["transverse_angle"], f"2*pi*{k}*({ratio_text})", f"irrational row {ci}/{j} angle")
            ratio_num = mp.sqrt(2) if effective == "sqrt2" else 1 / mp.sqrt(2)
            check_num(row["multiplier_real"], mp.cos(2 * mp.pi * k * ratio_num), f"irrational row {ci}/{j} multiplier real", check)
            check_num(row["multiplier_imaginary"], mp.sin(2 * mp.pi * k * ratio_num), f"irrational row {ci}/{j} multiplier imag", check)
            exact(row["multiplier_pair"], "exp(+/- 2*pi*i*k*ratio)", f"irrational row {ci}/{j} multiplier pair")
            floor_value = exact_floor_sqrt2(k) if effective == "sqrt2" else exact_floor_inv(k)
            exact(row["cz_index"], 2 * floor_value + 1, f"irrational row {ci}/{j} CZ")
            cert = row["floor_certificate"]
            check(set(cert) == {"integer", "left", "right", "inequality"}, f"irrational row {ci}/{j} floor keys")
            exact(cert["integer"], floor_value, f"irrational row {ci}/{j} floor m")
            if effective == "sqrt2":
                exact(cert["left"], floor_value * floor_value, f"irrational row {ci}/{j} floor left")
                exact(cert["right"], 2 * k * k, f"irrational row {ci}/{j} floor right")
                check(cert["left"] <= cert["right"] < (floor_value + 1) ** 2, f"irrational row {ci}/{j} square inequality")
            else:
                exact(cert["left"], 2 * floor_value * floor_value, f"irrational row {ci}/{j} floor left")
                exact(cert["right"], k * k, f"irrational row {ci}/{j} floor right")
                check(cert["left"] <= cert["right"] < 2 * (floor_value + 1) ** 2, f"irrational row {ci}/{j} inverse square inequality")
            exact(row["nondegenerate"], True, f"irrational row {ci}/{j} nondegenerate")
            exact(row["regime"], "irrational", f"irrational row {ci}/{j} regime")

    rats = data["regression"]["rational_cases"]
    check(type(rats) is list and len(rats) == 3, "rational case count")
    expected_rat = [("rational_2_1", 2, 1), ("rational_3_2", 3, 2), ("rational_5_3", 5, 3)]
    for ci, case in enumerate(rats):
        cid, p, q = expected_rat[ci]
        exact(case["case_id"], cid, f"rational {ci} id")
        exact(case["a"], str(p), f"rational {ci} a")
        exact(case["b"], str(q), f"rational {ci} b")
        exact(case["ratio"], f"{p}/{q}", f"rational {ci} ratio")
        exact(case["coprime"], True, f"rational {ci} coprime")
        common = p * q
        exact(case["common_period"], str(common), f"rational {ci} common period")
        check("full boundary" in case["morse_bott_manifold"] and "dimension 3" in case["morse_bott_manifold"], f"rational {ci} MB family")
        exact(case["resonance_certificate"], {"p": p, "q": q, "q*a": common, "p*b": common, "identity": "q*a=p*b"}, f"rational {ci} resonance")
        exact(case["regime"], "rational_morse_bott", f"rational {ci} regime")
        rows = case["coordinate_orbits"]
        check(len(rows) == 2, f"rational {ci} coordinate rows")
        for ri, row in enumerate(rows):
            axis, action = (("gamma1", p) if ri == 0 else ("gamma2", q))
            rkeys = {"axis", "simple_orbit", "action", "period", "common_period_multiple", "transverse_multiplier_at_common_period", "cz_index", "cz_status", "nondegenerate"}
            check(set(row) == rkeys, f"rational {ci}/{ri} keys")
            exact(row["axis"], axis, f"rational {ci}/{ri} axis")
            exact(row["simple_orbit"], "gamma_1" if ri == 0 else "gamma_2", f"rational {ci}/{ri} orbit")
            exact(row["action"], str(action), f"rational {ci}/{ri} action")
            exact(row["period"], str(action), f"rational {ci}/{ri} period")
            exact(row["common_period_multiple"], common, f"rational {ci}/{ri} multiple")
            exact(row["transverse_multiplier_at_common_period"], "1", f"rational {ci}/{ri} multiplier")
            exact(row["cz_index"], None, f"rational {ci}/{ri} CZ null")
            exact(row["cz_status"], "undefined_at_degenerate_morse_bott", f"rational {ci}/{ri} CZ status")
            exact(row["nondegenerate"], False, f"rational {ci}/{ri} degeneracy")

    exact(data["regression"]["irrational_case_count"], 2, "irrational count summary")
    exact(data["regression"]["irrational_row_count"], 48, "irrational row summary")
    exact(data["regression"]["rational_case_count"], 3, "rational count summary")
    exact(data["regression"]["rational_orbit_row_count"], 6, "rational row summary")
    check(len(data["exact_identities"]) == 10, "identity count")
    check(len(data["citations"]) == 2 and all(set(c) == {"key", "claim", "source", "url"} for c in data["citations"]), "citation closure")
    check(len(data["nonclaims"]) == 5 and all(isinstance(x, str) for x in data["nonclaims"]), "nonclaim closure")
    return count


def quick_preflight(data: dict) -> None:
    assert set(data) == TOP_KEYS
    assert data["candidate_id"] == "HCS-C242" and data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    print("C242 quick hostile preflight: PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    if args.quick:
        quick_preflight(data)
    else:
        print(f"C242 independent checker: PASS ({validate(data)} assertions; irrational CZ and rational Morse--Bott ledger)")


if __name__ == "__main__":
    main()
