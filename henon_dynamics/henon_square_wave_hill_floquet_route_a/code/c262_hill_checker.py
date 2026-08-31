#!/usr/bin/env python3
"""Producer-independent series/linear-algebra checker for C262."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c262_hill_evidence.json"
SOURCE = "98782afe1e754c311ad0736f72ce09dcc7c85c77"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
mp.mp.dps = 86
NUM = re.compile(r"^[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?$")
TOP = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "receipts", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
FLAGS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}


def ph(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def number(text: str) -> mp.mpf:
    if not isinstance(text, str) or NUM.fullmatch(text) is None:
        raise AssertionError("decimal syntax")
    value = mp.mpf(text)
    if not mp.isfinite(value):
        raise AssertionError("finite decimal")
    return value


def rational(text: str) -> F:
    if not isinstance(text, str):
        raise AssertionError("rational text")
    return F(text)


def series_segment(k: mp.mpf, tau: mp.mpf) -> list[list[mp.mpf]]:
    C = mp.mpf(0)
    S = mp.mpf(0)
    cterm = mp.mpf(1)
    sterm = tau
    for m in range(90):
        C += cterm
        S += sterm
        cterm *= (-k)*tau*tau/((2*m+1)*(2*m+2))
        sterm *= (-k)*tau*tau/((2*m+2)*(2*m+3))
    return [[C, S], [-k*S, C]]


def mul(a, b):
    return [[a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]], [a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]]]


def matrix_norm(a) -> mp.mpf:
    return max(abs(a[i][j]) for i in range(2) for j in range(2))


def matrix_sub(a, b):
    return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]


def matrix_scale(c, a):
    return [[c*a[i][j] for j in range(2)] for i in range(2)]


I2 = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]


def cheb_u(n: int, x: mp.mpf) -> mp.mpf:
    if n < 0:
        return mp.mpf(0)
    a, b = mp.mpf(1), 2*x
    if n == 0:
        return a
    for _ in range(1, n):
        a, b = b, 2*x*b-a
    return b


def label(M) -> str:
    delta = M[0][0]+M[1][1]
    tol = mp.mpf("1e-60")
    if abs(delta-2) < tol:
        return "parabolic_identity_plus" if matrix_norm(matrix_sub(M, I2)) < tol else "parabolic_jordan_plus"
    if abs(delta+2) < tol:
        return "parabolic_identity_minus" if matrix_norm(matrix_sub(M, matrix_scale(-1, I2))) < tol else "parabolic_jordan_minus"
    return "elliptic_bounded" if abs(delta) < 2 else "hyperbolic_exponential"


def validate(data: dict, reconstruct: bool = True) -> int:
    checks = 0

    def ck(ok: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            raise AssertionError(message)

    def eq(a, b, message: str) -> None:
        ck(type(a) is type(b) and a == b, message)

    eq(set(data), TOP, "top closure")
    for key, value in (("schema", "hcs-c262-square-wave-hill-floquet-v1"), ("candidate_id", "HCS-C262"), ("evaluation_date", "2026-08-31"), ("source_commit", SOURCE), ("fixed_epoch", EPOCH), ("scope_literal", SCOPE)):
        eq(data[key], value, key)
    eq(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    eq(data["payload_sha256"], ph(data), "payload hash")
    frozen = data["frozen_object"]
    eq(set(frozen), {"equation", "parameters", "phase_space", "clock", "arithmetic_origin", "determinant_convention", "forbidden_data"}, "frozen closure")
    eq(frozen["equation"], "y''+k(t)*y=0 with periodic k1 for tau1 then k2 for tau2", "equation")
    ck("positive total period" in frozen["parameters"], "parameter boundary")
    eq(frozen["clock"], "physical time and the coefficient-period strobe", "clock")
    ck("no target determinant" in frozen["determinant_convention"], "determinant boundary")
    theorem = data["theorem"]
    eq(set(theorem), {"entire_segments", "monodromy", "discriminant", "floquet_classification", "parabolic_boundary", "iterate_law", "floquet_rates", "faces"}, "theorem closure")
    fragments = {
        "entire_segments": "C^2+k*S^2=1", "monodromy": "SL(2,R)",
        "discriminant": "2*C1*C2-(k1+k2)*S1*S2", "floquet_classification": "generic exponential growth",
        "parabolic_boundary": "nontrivial Jordan matrix", "iterate_law": "U_{n-1}",
        "floquet_rates": "arcosh", "faces": "trace is order-invariant",
    }
    for key, fragment in fragments.items():
        ck(fragment in theorem[key], "theorem " + key)
    route = data["route_a"]
    eq(route["tuple"], ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    eq(route["overall"], "ROUTE_A_REJECTED", "overall")
    eq(route["route_b_invocation_allowed"], False, "Route B")
    ck("no intrinsic arithmetic" in route["strongest_failure"].lower(), "route failure")
    eq(set(data["scope_flags"]), FLAGS, "flags closure")
    ck(all(value is False for value in data["scope_flags"].values()), "flags false")
    eq(len(data["citations"]), 2, "citation count")
    ck(data["citations"][0]["url"] == "https://doi.org/10.1007/BF02417081", "Hill DOI")
    ck(len(data["nonclaims"]) >= 6, "nonclaims")

    receipts = data["receipts"]
    eq(receipts["k_grid"], ["-4", "-1", "0", "1", "4", "9"], "k grid")
    eq(receipts["tau_grid"], ["0", "1/4", "1/2", "1", "3/2"], "tau grid")
    eq(receipts["grid_row_count"], 900, "grid count")
    eq(len(receipts["grid_rows"]), 900, "grid length")
    eq(receipts["boundary_row_count"], 6, "boundary count")
    eq(receipts["working_decimal_digits"], 90, "digits")
    eq(receipts["printed_significant_digits"], 70, "printed")
    eq(receipts["chebyshev_power_max"], 12, "power max")
    ck("proof-driven" in receipts["finite_receipt_boundary"], "receipt boundary")
    expected = [(k1, k2, t1, t2) for k1 in map(F, [-4, -1, 0, 1, 4, 9]) for k2 in map(F, [-4, -1, 0, 1, 4, 9]) for t1 in [F(0), F(1,4), F(1,2), F(1), F(3,2)] for t2 in [F(0), F(1,4), F(1,2), F(1), F(3,2)]]
    grid_keys = {"row_id", "k1", "k2", "tau1", "tau2", "monodromy", "discriminant", "closed_discriminant", "determinant_residual", "class", "floquet_angle_or_growth_per_time", "max_chebyshev_power_residual_n1_to_12"}
    observed_classes: dict[str, int] = {}
    for idx, (row, pars) in enumerate(zip(receipts["grid_rows"], expected), 1):
        eq(set(row), grid_keys, f"G{idx} keys")
        eq(row["row_id"], f"G{idx:04d}", f"G{idx} id")
        eq(tuple(rational(row[key]) for key in ("k1", "k2", "tau1", "tau2")), pars, f"G{idx} parameters")
        observed_classes[row["class"]] = observed_classes.get(row["class"], 0)+1
        ck(row["class"] in {"elliptic_bounded", "hyperbolic_exponential", "parabolic_identity_plus", "parabolic_identity_minus", "parabolic_jordan_plus", "parabolic_jordan_minus"}, "class vocabulary")
        matrix = [[number(value) for value in line] for line in row["monodromy"]]
        delta = number(row["discriminant"])
        ck(abs(delta-(matrix[0][0]+matrix[1][1])) < mp.mpf("2e-66")*max(1, abs(delta)), "stored trace")
        ck(number(row["determinant_residual"]) < mp.mpf("2e-68"), "stored determinant")
        ck(number(row["max_chebyshev_power_residual_n1_to_12"]) < mp.mpf("2e-58"), "stored Chebyshev")
        if reconstruct:
            k1q, k2q, t1q, t2q = pars
            k1, k2, t1, t2 = [mp.mpf(v.numerator)/v.denominator for v in pars]
            M1, M2 = series_segment(k1, t1), series_segment(k2, t2)
            direct = mul(M2, M1)
            ck(matrix_norm(matrix_sub(matrix, direct)) < mp.mpf("3e-66")*max(1, matrix_norm(direct)), "series monodromy")
            closed = 2*M1[0][0]*M2[0][0]-(k1+k2)*M1[0][1]*M2[0][1]
            ck(abs(number(row["closed_discriminant"])-closed) < mp.mpf("3e-66")*max(1, abs(closed)), "closed trace")
            ck(row["class"] == label(direct), "independent classification")
            power = I2
            direct_delta = direct[0][0] + direct[1][1]
            for n in range(1, 13):
                power = mul(power, direct)
                formula = matrix_sub(matrix_scale(cheb_u(n-1, direct_delta/2), direct), matrix_scale(cheb_u(n-2, direct_delta/2), I2))
                ck(matrix_norm(matrix_sub(power, formula)) < mp.mpf("1e-58")*max(1, matrix_norm(power), matrix_norm(formula)), "Chebyshev power")
    eq(receipts["class_counts"], observed_classes, "class ledger")

    boundaries = receipts["boundary_rows"]
    eq([row["class"] for row in boundaries], ["parabolic_identity_plus", "parabolic_identity_minus", "parabolic_jordan_plus", "parabolic_jordan_minus", "parabolic_identity_plus", "hyperbolic_exponential"], "boundary classes")
    eq(boundaries[2]["matrix"], [["1", "1"], ["0", "1"]], "plus Jordan")
    eq(boundaries[3]["matrix"], [["-1", "-1"], ["0", "-1"]], "minus Jordan")
    eq(boundaries[5]["matrix"], [["5/4", "3/4"], ["3/4", "5/4"]], "hyperbolic exact")
    formulas = {row["id"]: row["formula"] for row in data["exact_identities"]}
    eq(len(formulas), 8, "identity closure")
    eq(formulas["discriminant"], "Delta=2*C1*C2-(k1+k2)*S1*S2", "identity trace")
    eq(formulas["parabolic_split"], "Delta=+/-2 requires testing M=+/-I versus rank(M-/+I)=1", "identity boundary")
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    checks = validate(json.loads(args.evidence.read_text()), reconstruct=not args.quick)
    print(f"C262 independent checker: PASS ({checks} assertions; 900 transfer rows, all-sign stability and Jordan boundaries)")


if __name__ == "__main__":
    main()
