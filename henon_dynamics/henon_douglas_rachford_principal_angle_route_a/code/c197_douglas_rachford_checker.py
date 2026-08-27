#!/usr/bin/env python3
"""Producer-independent exact checker for the C197 certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c197_douglas_rachford_evidence.json"
SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EXPECTED_HEADLINE = (
    "Every relaxed Douglas--Rachford map for two finite-dimensional real "
    "subspaces has an exact principal-angle block atlas, a sharp convergence "
    "window and rate, and an orthogonal rotation boundary at lambda=2"
)


def dec(value: str) -> F:
    return F(value)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(x, a):
    return [[x * a[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def power(a, n):
    out, base = eye(len(a)), a
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def determinant2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def direct_block(c: F, s: F, lam: F):
    identity = eye(2)
    p_u = [[F(1), F(0)], [F(0), F(0)]]
    p_v = [[c * c, c * s], [c * s, s * s]]
    r_u = add(scale(F(2), p_u), scale(F(-1), identity))
    r_v = add(scale(F(2), p_v), scale(F(-1), identity))
    unrelaxed = scale(F(1, 2), add(identity, mul(r_v, r_u)))
    return add(scale(F(1) - lam, identity), scale(lam, unrelaxed))


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def block_diag(parts):
    n = sum(len(part) for part in parts)
    out = [[F(0) for _ in range(n)] for _ in range(n)]
    offset = 0
    for part in parts:
        for i in range(len(part)):
            for j in range(len(part)):
                out[offset + i][offset + j] = part[i][j]
        offset += len(part)
    return out


def det_polynomial_from_blocks(parts):
    polynomial = [F(1)]
    for part in parts:
        if len(part) == 1:
            polynomial = poly_mul(polynomial, [F(1), -part[0][0]])
        else:
            polynomial = poly_mul(polynomial, [F(1), -tr(part), determinant2(part)])
    return polynomial


def expected_regime(lam):
    if lam == 0:
        return "identity_boundary"
    if 0 < lam < 2:
        return "strict_contraction"
    if lam == 2:
        return "orthogonal_rotation_boundary"
    return "expansive_off_fixed_space"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    assertions = 0

    def check(condition, message):
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c197-douglas-rachford-v1", "schema")
    check(data["candidate_id"] == "HCS-C197", "candidate")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["evaluator"]["sha256"] == EVALUATOR_SHA256, "evaluator")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["headline"] == EXPECTED_HEADLINE, "headline")
    check(data["citations"][0]["doi"] == "10.1090/S0002-9947-1956-0084194-4", "source DOI")
    check(data["citations"][1]["doi"] == "10.1016/j.jat.2014.06.002", "rate DOI")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(value is False for value in data["scope_flags"].values()), "scope flags")

    angle_lookup = {row["label"]: (dec(row["cosine"]), dec(row["sine"]))
                    for row in data["regression"]["angles"]}
    for label, (c, s) in angle_lookup.items():
        check(c * c + s * s == 1, f"Pythagorean identity {label}")

    for row in data["regression"]["block_rows"]:
        c, s = angle_lookup[row["angle_label"]]
        lam = dec(row["lambda"])
        matrix = direct_block(c, s, lam)
        reported = [[dec(x) for x in line] for line in row["matrix"]]
        for i in range(2):
            for j in range(2):
                check(reported[i][j] == matrix[i][j], "direct projector block")
        check(dec(row["trace"]) == tr(matrix), "block trace")
        determinant = determinant2(matrix)
        check(dec(row["determinant"]) == determinant, "block determinant")
        check(determinant == 1 - lam * (2 - lam) * s * s, "modulus law")
        for n, value in enumerate(row["power_traces_0_to_8"]):
            check(dec(value) == tr(power(matrix, n)), "block power trace")
        check(dec(row["spectral_radius_squared"]) == determinant, "spectral radius")
        check(row["fixed_dimension"] == (2 if lam == 0 else 0), "block fixed dimension")
        check(row["regime"] == expected_regime(lam), "block regime")

    for row in data["regression"]["composite_rows"]:
        lam = dec(row["lambda"])
        parts = [eye(1), eye(1), [[1 - lam]], [[1 - lam]]]
        for label in row["angle_labels"]:
            c, s = angle_lookup[label]
            parts.append(direct_block(c, s, lam))
        matrix = block_diag(parts)
        check(len(matrix) == row["dimension"] == 8, "composite dimension")
        polynomial = det_polynomial_from_blocks(parts)
        check([dec(x) for x in row["det_I_minus_zT_coefficients"]] == polynomial, "det polynomial")
        for n, value in enumerate(row["power_traces_0_to_8"]):
            check(dec(value) == tr(power(matrix, n)), "composite power trace")
        nonfixed = parts[2:]
        rate_squared = max(
            abs(part[0][0]) ** 2 if len(part) == 1 else determinant2(part)
            for part in nonfixed
        )
        check(dec(row["off_fixed_rate_squared"]) == rate_squared, "sharp rate")
        check(row["fixed_dimension_for_nonzero_lambda"] == 2, "reported fixed dimension")
        check(row["mismatch_dimension"] == 2, "mismatch dimension")
        check(row["regime"] == expected_regime(lam), "composite regime")

    summary = data["summary"]
    check(summary["angle_count"] == len(angle_lookup) == 4, "angle count")
    check(summary["lambda_count"] == len(data["regression"]["lambdas"]) == 7, "lambda count")
    check(summary["block_row_count"] == len(data["regression"]["block_rows"]) == 28, "block rows")
    check(summary["composite_row_count"] == len(data["regression"]["composite_rows"]) == 21, "composite rows")
    check(summary["exact_matrix_cells"] == 112, "matrix cells")
    check(summary["exact_power_trace_cells"] == 441, "trace cells")
    print(json.dumps({
        "status": "C197_CHECKER_PASS",
        "assertions": assertions,
        "block_rows": summary["block_row_count"],
        "composite_rows": summary["composite_row_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
