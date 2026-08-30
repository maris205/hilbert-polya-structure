#!/usr/bin/env python3
"""Deterministic certificate producer for the ellipsoid Reeb-flow atlas.

The model is the restriction of the standard contact form to
E(a,b)={pi|z1|^2/a+pi|z2|^2/b<=1}.  The receipt deliberately separates the
irrational (two non-degenerate coordinate orbits) and rational (Morse--Bott)
regimes.  It is a source-local symplectic calculation, not an arithmetic
orbit construction.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
import math
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "489506cf92bfed721f94f22dd0444a60427f90a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
WORKING_DIGITS = 90
SERIALIZED_DIGITS = 64
MAX_ITERATE = 12
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c242_reeb_evidence.json"
mp.mp.dps = WORKING_DIGITS


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def dec(x: mp.mpf) -> str:
    if abs(x) < mp.mpf("1e-82"):
        x = mp.mpf("0")
    return mp.nstr(x, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-70, max_fixed=70)


def floor_sqrt2(k: int) -> int:
    """Exact floor(k*sqrt(2)) using an integer-square inequality."""
    m = math.isqrt(2 * k * k)
    while (m + 1) * (m + 1) <= 2 * k * k:
        m += 1
    while m * m > 2 * k * k:
        m -= 1
    return m


def floor_inv_sqrt2(k: int) -> int:
    """Exact floor(k/sqrt(2)) from 2*m^2 <= k^2."""
    m = math.isqrt((k * k) // 2)
    while 2 * (m + 1) * (m + 1) <= k * k:
        m += 1
    while 2 * m * m > k * k:
        m -= 1
    return m


def irrational_row(axis: str, k: int, kind: str) -> dict:
    # The transverse ratio is a/b on gamma_1 and b/a on gamma_2.
    effective_kind = kind if axis == "gamma1" else ("inv_sqrt2" if kind == "sqrt2" else "sqrt2")
    a_text, b_text = (("sqrt(2)", "1") if kind == "sqrt2" else ("1", "sqrt(2)"))
    if effective_kind == "sqrt2":
        floor_value = floor_sqrt2(k)
        ratio_text = "sqrt(2)"
        ratio_numeric = mp.sqrt(2)
        square_test = {"integer": floor_value, "left": floor_value * floor_value, "right": 2 * k * k, "inequality": "m^2 <= 2*k^2 < (m+1)^2"}
    else:
        floor_value = floor_inv_sqrt2(k)
        ratio_text = "1/sqrt(2)"
        ratio_numeric = 1 / mp.sqrt(2)
        square_test = {"integer": floor_value, "left": 2 * floor_value * floor_value, "right": k * k, "inequality": "2*m^2 <= k^2 < 2*(m+1)^2"}
    action_text = f"{k}*{a_text}" if axis == "gamma1" else f"{k}*{b_text}"
    phase = 2 * mp.pi * k * ratio_numeric
    c, s = mp.cos(phase), mp.sin(phase)
    return {
        "axis": axis,
        "iterate": k,
        "simple_orbit": "gamma_1" if axis == "gamma1" else "gamma_2",
        "a": a_text,
        "b": b_text,
        "ratio": ratio_text,
        "action": action_text,
        "period": action_text,
        "transverse_angle": f"2*pi*{k}*({ratio_text})",
        "multiplier_real": dec(c),
        "multiplier_imaginary": dec(s),
        "multiplier_pair": "exp(+/- 2*pi*i*k*ratio)",
        "cz_index": 2 * floor_value + 1,
        "floor_certificate": square_test,
        "nondegenerate": True,
        "regime": "irrational",
    }


def rational_case(case_id: str, p: int, q: int) -> dict:
    common = p * q
    rows = []
    for axis, action in (("gamma1", p), ("gamma2", q)):
        rows.append({
            "axis": axis,
            "simple_orbit": "gamma_1" if axis == "gamma1" else "gamma_2",
            "action": str(action),
            "period": str(action),
            "common_period_multiple": common,
            "transverse_multiplier_at_common_period": "1",
            "cz_index": None,
            "cz_status": "undefined_at_degenerate_morse_bott",
            "nondegenerate": False,
        })
    return {
        "case_id": case_id,
        "a": str(p),
        "b": str(q),
        "ratio": f"{p}/{q}",
        "coprime": math.gcd(p, q) == 1,
        "common_period": str(common),
        "morse_bott_manifold": "the full boundary partial E(a,b), dimension 3; orbit-space family dimension 2",
        "coordinate_orbits": rows,
        "resonance_certificate": {"p": p, "q": q, "q*a": common, "p*b": common, "identity": "q*a=p*b"},
        "regime": "rational_morse_bott",
    }


def build() -> dict:
    irr = []
    for kind in ("sqrt2", "inv_sqrt2"):
        irr.append({
            "case_id": "irrational_sqrt2" if kind == "sqrt2" else "irrational_inverse_sqrt2",
            "ratio_kind": kind,
            "ratio_is_irrational_witness": "sqrt(2) is not rational by the integer-square contradiction",
            "rows": [irrational_row(axis, k, kind) for axis in ("gamma1", "gamma2") for k in range(1, MAX_ITERATE + 1)],
        })
    rats = [rational_case("rational_2_1", 2, 1), rational_case("rational_3_2", 3, 2), rational_case("rational_5_3", 5, 3)]
    data = {
        "schema": "hcs-c242-ellipsoid-reeb-orbit-atlas-v1",
        "candidate_id": "HCS-C242",
        "evaluation_date": "2026-08-30",
        "source_commit": SOURCE_COMMIT,
        "fixed_epoch": FIXED_EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The standard ellipsoid Reeb flow has exactly two simple coordinate orbits in the irrational regime, an exact iterate/CZ atlas, and a separately certified rational Morse--Bott boundary.",
        "frozen_object": {
            "domain": "E(a,b)={pi|z1|^2/a+pi|z2|^2/b<=1} in C^2",
            "contact_form": "lambda_0=1/2 sum_j (x_j dy_j-y_j dx_j) restricted to partial E(a,b)",
            "reeb_flow": "phi_t(z1,z2)=(exp(2*pi*i*t/a)z1, exp(2*pi*i*t/b)z2)",
            "coordinate_orbits": "gamma_1={z2=0}, gamma_2={z1=0}",
            "action_period": "A(gamma_1)=T(gamma_1)=a and A(gamma_2)=T(gamma_2)=b",
            "trivialization": "coordinate complex-line trivialization used by Hutchings (xi|gamma_1 is the second C summand; xi|gamma_2 the first)",
            "clock": "contact/Reeb time",
            "normalization": "action equals period under lambda_0 and the displayed ellipsoid convention",
            "arithmetic_origin": "none; a,b are source-defined geometric parameters",
            "forbidden_data": "target primes/zeros, local arithmetic, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert--Polya operators",
        },
        "theorem": {
            "irrational_classification": "If a/b is irrational, every closed Reeb orbit on the boundary is one of the two coordinate circles; all nontrivial iterates are nondegenerate.",
            "actions": "A(gamma_1^k)=k*a and A(gamma_2^k)=k*b, with the same values for periods.",
            "multipliers": "The transverse return pair is exp(+/-2*pi*i*k*a/b) for gamma_1^k and exp(+/-2*pi*i*k*b/a) for gamma_2^k.",
            "cz_formula": "With the coordinate complex-line trivialization used by Hutchings, mu_CZ(gamma_1^k)=2 floor(k*a/b)+1 and mu_CZ(gamma_2^k)=2 floor(k*b/a)+1 in the irrational case.",
            "rational_boundary": "If a/b=p/q in lowest terms, the common period q*a=p*b carries the Morse--Bott family equal to the full boundary; coordinate circles are degenerate members and no nondegenerate CZ integer is assigned before perturbation.",
            "sqrt2_certificate": "For the sqrt(2) sentinels, every floor is certified by integer inequalities m^2<=2k^2<(m+1)^2 or 2m^2<=k^2<2(m+1)^2; no floating-point floor is used.",
            "route_boundary": "The atlas has an analytic A1 orbit theorem but no intrinsic arithmetic carrier or target determinant match.",
        },
        "regression": {
            "irrational_cases": irr,
            "rational_cases": rats,
            "irrational_case_count": len(irr),
            "irrational_row_count": sum(len(x["rows"]) for x in irr),
            "rational_case_count": len(rats),
            "rational_orbit_row_count": sum(len(x["coordinate_orbits"]) for x in rats),
            "working_digits": WORKING_DIGITS,
            "serialized_digits": SERIALIZED_DIGITS,
            "max_iterate": MAX_ITERATE,
        },
        "exact_identities": [
            {"identity_id": "reeb_flow", "formula": "phi_t=(e^(2*pi*i*t/a),e^(2*pi*i*t/b))"},
            {"identity_id": "coordinate_action", "formula": "A(gamma_1)=a; A(gamma_2)=b"},
            {"identity_id": "iterate_action", "formula": "A(gamma_j^k)=k*A(gamma_j)"},
            {"identity_id": "gamma1_cz", "formula": "mu_CZ(gamma_1^k)=2 floor(k*a/b)+1 for a/b irrational"},
            {"identity_id": "gamma2_cz", "formula": "mu_CZ(gamma_2^k)=2 floor(k*b/a)+1 for a/b irrational"},
            {"identity_id": "transverse_multiplier", "formula": "rho_trans=exp(+/-2*pi*i*k*ratio)"},
            {"identity_id": "rational_resonance", "formula": "q*a=p*b for a/b=p/q"},
            {"identity_id": "sqrt2_floor", "formula": "m=floor(k sqrt(2)) iff m^2<=2k^2<(m+1)^2"},
            {"identity_id": "inverse_sqrt2_floor", "formula": "m=floor(k/sqrt(2)) iff 2m^2<=k^2<2(m+1)^2"},
            {"identity_id": "irrational_nonresonance", "formula": "sqrt(2) notin Q by infinite descent on an integer square"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "A convention-complete analytic classification of simple coordinate orbits, all iterates, return multipliers, CZ indices, and rational Morse--Bott degeneration.",
            "strongest_failure": "No intrinsic rational-prime carrier, target determinant, or Hilbert--Polya spectral bridge is present.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "Hutchings2013", "claim": "ECH index and coordinate complex-line trivialization conventions", "source": "Michael Hutchings, Lecture notes on embedded contact homology, arXiv:1303.5789", "url": "https://arxiv.org/abs/1303.5789"},
            {"key": "HWZ1998", "claim": "contact/Reeb dynamics and symplectic field theory foundations", "source": "H. Hofer, K. Wysocki, E. Zehnder, The dynamics on three-dimensional strictly convex energy surfaces, Ann. Math. (1998)", "url": "https://doi.org/10.2307/120994"},
        ],
        "nonclaims": [
            "literature priority or exhaustive novelty certification",
            "a perturbation-independent CZ assignment in the rational Morse--Bott case",
            "an arithmetic origin, prime/prime-power labeling, Euler factors, root numbers, or automorphy",
            "a target zeta/Fredholm determinant, zero match, or Hilbert--Polya operator",
            "external peer review, acceptance, or numerical evidence promoted to a theorem",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C242_PRODUCER_PASS", "irrational_rows": data["regression"]["irrational_row_count"], "rational_cases": data["regression"]["rational_case_count"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
