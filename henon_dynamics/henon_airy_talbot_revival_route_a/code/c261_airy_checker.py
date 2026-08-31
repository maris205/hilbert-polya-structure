#!/usr/bin/env python3
"""Producer-independent structural, modular, and DFT checker for C261."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import re

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c261_airy_evidence.json"
SOURCE = "98782afe1e754c311ad0736f72ce09dcc7c85c77"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
mp.mp.dps = 86
NUM = re.compile(r"^[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?$")
TOP = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "receipts", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
FLAGS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
SUPPORTS = [[-1, 1], [1, 2], [2, 4], [3, 6, 9], [-5, 0, 10], [1, 3, 5], [2, 3, 6], [4, 6, 10], [-7, -2, 5], [6, 12, 18]]


def ph(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def factors(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    prime = 2
    while prime * prime <= n:
        exponent = 0
        while n % prime == 0:
            exponent += 1
            n //= prime
        if exponent:
            out[prime] = exponent
        prime += 1
    if n > 1:
        out[n] = 1
    return out


def stride(q: int) -> int:
    ans = 1
    for prime, exponent in factors(q).items():
        ans *= prime ** ((exponent - 1) // 3 + 1)
    return ans


def phase_hash(p: int, q: int) -> str:
    values = [(p * pow(n, 3, q)) % q for n in range(q)]
    return sha256(",".join(map(str, values)).encode()).hexdigest()


def number(text: str) -> mp.mpf:
    if not isinstance(text, str) or NUM.fullmatch(text) is None:
        raise AssertionError("decimal syntax")
    value = mp.mpf(text)
    if not mp.isfinite(value):
        raise AssertionError("finite decimal")
    return value


def validate(data: dict, reconstruct: bool = True) -> int:
    checks = 0

    def ck(ok: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            raise AssertionError(label)

    def eq(a, b, label: str) -> None:
        ck(type(a) is type(b) and a == b, label)

    eq(set(data), TOP, "top closure")
    for key, value in (
        ("schema", "hcs-c261-airy-talbot-revival-v1"), ("candidate_id", "HCS-C261"),
        ("evaluation_date", "2026-08-31"), ("source_commit", SOURCE),
        ("fixed_epoch", EPOCH), ("scope_literal", SCOPE),
    ):
        eq(data[key], value, key)
    eq(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    eq(data["payload_sha256"], ph(data), "payload hash")
    frozen_expected = {
        "equation": "u_t+u_xxx=0 on R/(2*pi*Z)",
        "fourier_action": "U(t)e_n=exp(i*n^3*t)e_n",
        "phase_space": "L^2(T), with Sobolev domains for powers of the cubic generator",
        "clock": "physical PDE time t",
        "arithmetic_origin": "none; modular cubic phases enter only after a chosen rational sampling time",
        "determinant_convention": "no infinite-dimensional determinant; finite DFT identities are source receipts only",
        "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert--Polya operators",
    }
    eq(data["frozen_object"], frozen_expected, "frozen object")
    theorem = data["theorem"]
    eq(set(theorem), {"unitary_group", "minimal_full_period", "rational_revival", "strobe_order", "fixed_modes", "state_period", "irrational_sampling", "operator_boundary"}, "theorem closure")
    required_fragments = {
        "unitary_group": "self-adjoint Fourier generator D^3",
        "minimal_full_period": "least positive full-space period is 2*pi",
        "rational_revival": "A_r=q^{-1}",
        "strobe_order": "exact global order q",
        "fixed_modes": "L(q)=product ell^ceil(v_ell(q)/3)",
        "state_period": "2*pi/gcd",
        "irrational_sampling": "exactly of constants",
        "operator_boundary": "neither trace class nor a target Fredholm determinant",
    }
    for key, fragment in required_fragments.items():
        ck(fragment in theorem[key], "theorem " + key)
    route = data["route_a"]
    eq(route["tuple"], ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "route tuple")
    eq(route["overall"], "ROUTE_A_REJECTED", "route overall")
    eq(route["route_b_invocation_allowed"], False, "route B")
    ck("no intrinsic arithmetic" in route["strongest_failure"].lower(), "route failure")
    eq(set(data["scope_flags"]), FLAGS, "flag closure")
    ck(all(value is False for value in data["scope_flags"].values()), "flags false")
    eq(len(data["citations"]), 2, "citation count")
    eq(data["citations"], [
        {"key": "PelloniSmith2024", "claim": "Airy revival and boundary-condition context", "source": "B. Pelloni and D. A. Smith, Studies in Applied Mathematics 153 (2024), e12699", "url": "https://doi.org/10.1111/sapm.12699"},
        {"key": "BoultonFarmakisPelloni2021", "claim": "finite translated-copy revival for periodic linear dispersive problems", "source": "L. Boulton, G. Farmakis, and B. Pelloni, Proceedings of the Royal Society A 477 (2021), 20210241", "url": "https://doi.org/10.1098/rspa.2021.0241"},
    ], "citation metadata and author order")
    ck(len(data["nonclaims"]) >= 6, "nonclaims")

    receipts = data["receipts"]
    eq(receipts["q_max"], 96, "q max")
    eq(receipts["fixed_mode_window"], [-512, 512], "mode window")
    eq(receipts["dft_q_max"], 18, "DFT max")
    eq(receipts["support_row_count"], 10, "support count")
    eq(receipts["working_decimal_digits"], 90, "working digits")
    eq(receipts["printed_significant_digits"], 68, "printed digits")
    ck("proof-driven" in receipts["finite_receipt_boundary"], "receipt boundary")

    expected_pairs = [(0, 1)] + [(p, q) for q in range(2, 97) for p in range(1, q) if gcd(p, q) == 1]
    eq(receipts["modular_row_count"], len(expected_pairs), "modular count")
    eq(len(receipts["modular_rows"]), len(expected_pairs), "modular length")
    row_keys = {"row_id", "p", "q", "phase_exponent_sha256", "strobe_order", "fixed_mode_stride", "fixed_mode_density", "fixed_modes_in_minus512_to_512"}
    for idx, (row, pair) in enumerate(zip(receipts["modular_rows"], expected_pairs), 1):
        eq(set(row), row_keys, f"R{idx} keys")
        eq(row["row_id"], f"R{idx:04d}", f"R{idx} id")
        eq((row["p"], row["q"]), pair, f"R{idx} pair")
        p, q = pair
        eq(row["phase_exponent_sha256"], phase_hash(p, q), f"R{idx} phase hash")
        eq(row["strobe_order"], q, f"R{idx} order")
        L = stride(q)
        eq(row["fixed_mode_stride"], L, f"R{idx} stride")
        eq(row["fixed_mode_density"], f"1/{L}", f"R{idx} density")
        count = sum(1 for n in range(-512, 513) if n % L == 0)
        eq(row["fixed_modes_in_minus512_to_512"], count, f"R{idx} fixed count")
        for n in (-513, -97, -1, 0, 1, 97, 513):
            ck(((p * n**3) % q == 0) == (n % L == 0), f"R{idx} divisibility")
        ck(all(((p * (n + q)**3 - p * n**3) % q == 0) for n in range(-3, 4)), f"R{idx} cubic periodicity")

    expected_dft_pairs = [(p, q) for q in range(2, 19) for p in range(1, q) if gcd(p, q) == 1]
    eq(receipts["dft_row_count"], len(expected_dft_pairs), "DFT count")
    eq(len(receipts["dft_rows"]), len(expected_dft_pairs), "DFT length")
    dkeys = {"row_id", "p", "q", "coefficients", "nonzero_coefficients_at_1e_minus_55", "parseval_residual", "max_inverse_dft_residual"}
    for row, (p, q) in zip(receipts["dft_rows"], expected_dft_pairs):
        eq(set(row), dkeys, "DFT keys")
        eq((row["p"], row["q"]), (p, q), "DFT pair")
        eq(row["row_id"], f"D{p}_{q}", "DFT id")
        eq(len(row["coefficients"]), q, "DFT coefficient count")
        coeffs = []
        for r, item in enumerate(row["coefficients"]):
            eq(set(item), {"r", "re", "im"}, "coefficient keys")
            eq(item["r"], r, "coefficient index")
            coeffs.append(mp.mpc(number(item["re"]), number(item["im"])))
        eq(row["nonzero_coefficients_at_1e_minus_55"], sum(abs(z) > mp.mpf("1e-55") for z in coeffs), "nonzero count")
        ck(number(row["parseval_residual"]) < mp.mpf("1e-60"), "stored parseval")
        ck(number(row["max_inverse_dft_residual"]) < mp.mpf("1e-60"), "stored inverse")
        if reconstruct:
            for r, observed in enumerate(coeffs):
                direct = sum(mp.e ** (2j * mp.pi * ((p*s**3-s*r) % q) / q) for s in range(q)) / q
                ck(abs(observed - direct) < mp.mpf("2e-66"), "DFT coefficient reconstruction")
            ck(abs(sum(abs(z)**2 for z in coeffs) - 1) < mp.mpf("2e-65"), "DFT parseval reconstruction")
            for n in range(q):
                inverse = sum(coeffs[r] * mp.e ** (2j * mp.pi * n*r/q) for r in range(q))
                target = mp.e ** (2j * mp.pi * ((p*n**3) % q) / q)
                ck(abs(inverse-target) < mp.mpf("3e-65"), "DFT inverse reconstruction")

    eq(len(receipts["support_rows"]), len(SUPPORTS), "support length")
    for idx, (row, support) in enumerate(zip(receipts["support_rows"], SUPPORTS), 1):
        eq(row["row_id"], f"S{idx:02d}", "support id")
        eq(row["fourier_support"], support, "support")
        d = 0
        for n in support:
            if n:
                d = gcd(d, abs(n)**3)
        eq(row["gcd_nonzero_cubic_frequencies"], d, "support gcd")
        eq(row["minimal_positive_period"], f"2*pi/{d}", "support period")
        eq(row["return_phase_integer_multiples"], [n**3 // d for n in support], "support phases")
    formulas = {item["id"]: item["formula"] for item in data["exact_identities"]}
    eq(len(formulas), 9, "identity closure")
    eq(formulas["cubic_periodicity"], "(n+q)^3-n^3=q*(3*n^2+3*n*q+q^2)", "cubic identity")
    eq(formulas["fixed_stride"], "q|n^3 iff product_l l^ceil(v_l(q)/3) divides n", "stride identity")
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = validate(data, reconstruct=not args.quick)
    print(f"C261 independent checker: PASS ({checks} assertions; 96 moduli, cubic DFT, fixed modes and state periods)")


if __name__ == "__main__":
    main()
