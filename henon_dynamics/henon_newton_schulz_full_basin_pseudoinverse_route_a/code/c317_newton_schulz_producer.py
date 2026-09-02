#!/usr/bin/env python3
"""Deterministic exact matrix evidence for HCS-C317."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c317_newton_schulz_evidence.json"
SOURCE = "1938bae19e5a92f9ce2411aafdc68323bd641bd0"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
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

SQUARE_SPECS = [
    ("nilpotent-j5", [("0", 5)]),
    ("nilpotent-mixed", [("0", 2), ("0", 4)]),
    ("scalar-half", [("1/2", 1)]),
    ("jordan-half-3", [("1/2", 3)]),
    ("jordan-minus-half-4", [("-1/2", 4)]),
    ("mixed-interior", [("1/3", 2), ("-1/2", 3)]),
    ("unit-one-semisimple", [("1", 1), ("1/2", 1)]),
    ("unit-minus-one-semisimple", [("-1", 1), ("1/3", 1)]),
    ("unit-i-semisimple", [("I", 1), ("1/2", 1)]),
    ("unit-jordan-3", [("1", 3)]),
    ("super-three-halves", [("3/2", 1)]),
    ("super-minus-two-j2", [("-2", 2)]),
    ("mixed-peripheral", [("1", 2), ("-1", 1), ("1/2", 2)]),
    ("zero-plus-half", [("0", 3), ("1/2", 2)]),
]

RECT_SPECS = [
    ("tall-3x2-r2", 3, 2, ["1", "3"], [("1/2", 2)]),
    ("wide-2x3-r2", 2, 3, ["1", "2"], [("1/2", 1), ("-1/3", 1)]),
    ("singular-square-4-r2", 4, 4, ["1", "2"], [("-1/2", 2)]),
    ("tall-5x3-r1", 5, 3, ["2"], [("0", 1)]),
    ("square-5-r3", 5, 5, ["1/2", "1", "4"], [("0", 2), ("1/2", 1)]),
    ("zero-3x5", 3, 5, [], []),
]

ALPHA_SPECS = [
    ("full-2", 2, 2, ["1", "2"]),
    ("rank2-4x3", 4, 3, ["1", "3"]),
    ("repeated-max-4", 4, 4, ["1", "2", "2"]),
    ("zero-3x2", 3, 2, []),
]


def sx(text):
    return sp.sympify(text, locals={"I": sp.I})


def ss(value) -> str:
    return sp.sstr(sp.simplify(value))


def matrix_rows(matrix: sp.Matrix) -> list[list[str]]:
    return [[ss(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def jordan(lam, size):
    block = sp.eye(size) * lam
    for i in range(size - 1): block[i, i + 1] = 1
    return block


def block_diagonal(blocks):
    return sp.diag(*[jordan(sx(lam), size) for lam, size in blocks]) if blocks else sp.zeros(0)


def similarity(n):
    p = sp.eye(n)
    for i in range(n - 1): p[i, i + 1] = i + 1
    if n > 2: p[0, n - 1] = 1
    return p


def modulus(text):
    value = sx(text)
    return sp.sqrt(sp.simplify(value * sp.conjugate(value)))


def classify(blocks):
    if not blocks:
        return sp.Integer(0), 0, "nilpotent", 1
    radii = [modulus(lam) for lam, _ in blocks]
    rho = max(radii, key=lambda x: float(x))
    peripheral = max(size for (lam, size), radius in zip(blocks, radii) if sp.simplify(radius-rho) == 0)
    if rho == 0:
        return rho, peripheral, "finite-termination", max(size for _, size in blocks)
    if rho < 1: regime = "convergent"
    elif rho == 1 and peripheral == 1: regime = "bounded-nonvanishing"
    elif rho == 1: regime = "polynomially-unbounded"
    else: regime = "double-exponential-divergence"
    return rho, peripheral, regime, None


def iterate(A, X, steps):
    out = []
    for k in range(steps):
        residual = sp.eye(A.rows) - A * X
        out.append({"k": k, "dyadic_power": 2**k, "x": matrix_rows(X), "left_residual": matrix_rows(residual)})
        X = sp.simplify(X * (2 * sp.eye(A.rows) - A * X))
    return out


def build_square(case_id, blocks):
    canonical = block_diagonal(blocks); n = canonical.rows; transform = similarity(n)
    residual0 = sp.simplify(transform * canonical * transform.inv())
    A = sp.diag(*range(1, n + 1)); X0 = sp.simplify(A.inv() * (sp.eye(n) - residual0))
    snapshots = iterate(A, X0, 6)
    for row in snapshots:
        assert sp.Matrix([[sx(v) for v in rr] for rr in row["left_residual"]]) == residual0 ** row["dyadic_power"]
    rho, peripheral, regime, nilindex = classify(blocks)
    jordan_rows = []
    for lam_text, size in blocks:
        lam = sx(lam_text)
        for k in range(6):
            power = 2**k
            jordan_rows.append({"lambda": lam_text, "size": size, "k": k, "power": power,
                "coefficients": [ss(0 if j > power else sp.binomial(power, j) * lam ** (power-j)) for j in range(size)]})
    return {"case_id": case_id, "dimension": n, "blocks": [{"lambda": x, "size": s} for x, s in blocks],
            "a": matrix_rows(A), "similarity": matrix_rows(transform), "initial_residual": matrix_rows(residual0),
            "initial_x": matrix_rows(X0), "spectral_radius": ss(rho), "largest_peripheral_jordan_size": peripheral,
            "regime": regime, "nilpotency_index": nilindex, "snapshots": snapshots, "jordan_binomial_rows": jordan_rows}


def canonical_a(m, n, singulars):
    A = sp.zeros(m, n)
    for i, value in enumerate(singulars): A[i, i] = sx(value)
    return A


def projectors(m, n, rank):
    P, Q = sp.zeros(m), sp.zeros(n)
    for i in range(rank): P[i, i] = Q[i, i] = 1
    return P, Q


def compatible_x(m, n, singulars, blocks):
    rank = len(singulars); X = sp.zeros(n, m)
    if rank:
        sigma = sp.diag(*[sx(x) for x in singulars]); residual = block_diagonal(blocks)
        B = sp.simplify(sigma.inv() * (sp.eye(rank) - residual))
        X[:rank, :rank] = B
    return X


def iterate_rect(A, X, P, steps=6):
    out = []
    for k in range(steps):
        residual = sp.simplify(P - A * X)
        out.append({"k": k, "dyadic_power": 2**k, "x": matrix_rows(X), "compressed_residual": matrix_rows(residual)})
        X = sp.simplify(X * (2 * sp.eye(A.rows) - A * X))
    return out


def build_rect(case_id, m, n, singulars, blocks):
    rank = len(singulars); A = canonical_a(m, n, singulars); P, Q = projectors(m, n, rank)
    X0 = compatible_x(m, n, singulars, blocks); snapshots = iterate_rect(A, X0, P)
    R0 = sp.simplify(P - A * X0)
    for row in snapshots:
        got = sp.Matrix([[sx(v) for v in rr] for rr in row["compressed_residual"]])
        assert got == R0 ** row["dyadic_power"]
    rho, peripheral, regime, nilindex = classify(blocks)
    return {"case_id": case_id, "m": m, "n": n, "rank": rank, "singular_values": singulars,
            "a": matrix_rows(A), "p_projector": matrix_rows(P), "q_projector": matrix_rows(Q),
            "initial_x": matrix_rows(X0), "compatibility_left": matrix_rows(sp.simplify(Q*X0*P-X0)),
            "spectral_radius": ss(rho), "largest_peripheral_jordan_size": peripheral,
            "regime": regime, "nilpotency_index": nilindex, "snapshots": snapshots}


def incompatible_rows():
    specs = [
        ("tall-c", 3, 2, ["1", "3"], [("1/2", 2)], "C"),
        ("wide-d", 2, 3, ["1", "2"], [("1/2", 1), ("-1/3", 1)], "D"),
        ("square-c", 4, 4, ["1", "2"], [("-1/2", 2)], "C"),
        ("square-d", 4, 4, ["1", "2"], [("-1/2", 2)], "D"),
        ("square-e", 4, 4, ["1", "2"], [("-1/2", 2)], "E"),
        ("square-cde", 4, 4, ["1", "2"], [("-1/2", 2)], "CDE"),
    ]
    rows = []
    for case_id, m, n, singulars, blocks, kind in specs:
        rank = len(singulars); A = canonical_a(m, n, singulars); P, Q = projectors(m, n, rank)
        X = compatible_x(m, n, singulars, blocks)
        if "C" in kind: X[0, rank] = 1
        if "D" in kind: X[rank, 0] = 1
        if "E" in kind: X[rank, rank] = 1
        violation = sp.simplify(Q*X*P-X)
        rows.append({"case_id": case_id, "m": m, "n": n, "rank": rank, "off_support_kind": kind,
                     "a": matrix_rows(A), "p_projector": matrix_rows(P), "q_projector": matrix_rows(Q),
                     "initial_x": matrix_rows(X), "compatibility_violation": matrix_rows(violation),
                     "snapshots": iterate_rect(A, X, P, 5), "converges_to_moore_penrose": False})
    return rows


def alpha_rows():
    rows = []
    for case_id, m, n, singulars in ALPHA_SPECS:
        A = canonical_a(m, n, singulars); rank = len(singulars)
        if rank == 0:
            alphas = [("arbitrary-zero", sp.Rational(7, 3))]
        else:
            smax = max(sx(x) for x in singulars); scale = smax**2
            alphas = [("zero", 0), ("safe-half", sp.Rational(1, 2)/scale), ("safe-center", 1/scale),
                      ("sharp-boundary", 2/scale), ("outside", 3/scale), ("negative", -1/scale)]
        for label, alpha in alphas:
            X = sp.simplify(alpha * A.conjugate().T)
            direction_rows = []
            for value in singulars:
                sigma = sx(value); residual = sp.simplify(1-alpha*sigma**2)
                if abs(float(residual)) < 1: limit = ss(1/sigma)
                elif label == "sharp-boundary" and residual == -1: limit = "0"
                else: limit = None
                direction_rows.append({"sigma": value, "initial_residual": ss(residual), "predicted_limit": limit,
                    "iterate_coefficients": [ss((1-residual**(2**k))/sigma) for k in range(6)]})
            if rank == 0: classification = "rank-zero-canonical-zero"
            elif label in ("safe-half", "safe-center"): classification = "converges-pseudoinverse"
            elif label == "sharp-boundary": classification = "spectral-truncation-boundary"
            elif label == "zero": classification = "zero-fixed"
            else: classification = "divergent"
            rows.append({"case_id": f"{case_id}-{label}", "m": m, "n": n, "rank": rank,
                         "singular_values": singulars, "alpha": ss(alpha), "classification": classification,
                         "initial_x": matrix_rows(X), "directions": direction_rows})
    return rows


def payload_hash(data):
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def leaf_count(value):
    if type(value) is dict: return sum(leaf_count(v) for v in value.values())
    if type(value) is list: return sum(leaf_count(v) for v in value)
    return 1


def main():
    if sys.flags.optimize:
        raise RuntimeError("C317 producer refuses optimized Python")
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=OUTPUT); args = parser.parse_args()
    square = [build_square(*spec) for spec in SQUARE_SPECS]
    rectangular = [build_rect(*spec) for spec in RECT_SPECS]
    incompatible = incompatible_rows(); alpha = alpha_rows()
    data = {
        "schema": "hcs-c317-newton-schulz-full-basin-v1", "candidate_id": "HCS-C317",
        "obstruction_id": "HEN-O301", "evaluation_date": "2026-09-03", "fixed_epoch": EPOCH,
        "source_commit": SOURCE, "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {"dynamics": "X_{k+1}=X_k(2I-AX_k)", "square_residual": "R_k=I-AX_k",
                  "singular_residual": "R_k=AA^dagger-AX_k on range(A)"},
        "theorem_contract": {
            "square_basin": "X_k tends to A^{-1} iff rho(I-AX_0)<1",
            "jordan_rate": "Theta((2^k)^(s-1) rho^(2^k)) with finite nilpotent termination",
            "pseudoinverse_basin": "X_k tends to A^dagger iff X_0=QX_0P and the compressed residual has spectral radius below one",
            "canonical_corridor": "X_0=alpha A^* converges iff 0<alpha<2/sigma_max^2 for nonzero A",
            "boundary": "the sharp alpha endpoint deletes every maximal-singular-value direction; rank zero is separate",
        },
        "square_cases": square, "compatible_rectangular_cases": rectangular,
        "incompatible_rectangular_cases": incompatible, "canonical_alpha_cases": alpha,
        "collision_boundary": {
            "C257": "scalar quadratic Newton--Cayley dynamics owns root basins and source zeta; C317 owns matrix inverse and Moore--Penrose basins",
            "C201": "heavy-ball owns second-order optimization recurrences; C317 owns residual powers and arbitrary nonnormal Jordan blocks",
            "C309": "matrix Riccati is a continuous symmetric flow; C317 is a discrete rectangular matrix iteration",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "Exact-arithmetic convergence is not a floating-point stability theorem.",
            "Residual squaring is source-local and is not an arithmetic primitive-orbit construction.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
            "The package does not assert literature priority for Newton--Schulz or generalized-inverse iteration.",
        ],
        "references": [
            {"identifier": "10.1002/zamm.19330130111", "role": "original reciprocal-matrix iteration"},
            {"identifier": "10.1214/aoms/1177731489", "role": "Hotelling matrix-calculation lineage"},
            {"identifier": "10.1090/S0025-5718-1965-0179915-5", "role": "generalized-inverse iteration"},
        ],
    }
    data["enumeration"] = {"square_case_count": len(square), "square_snapshot_count": sum(len(x["snapshots"]) for x in square),
        "jordan_binomial_row_count": sum(len(x["jordan_binomial_rows"]) for x in square),
        "compatible_rectangular_case_count": len(rectangular),
        "compatible_snapshot_count": sum(len(x["snapshots"]) for x in rectangular),
        "incompatible_case_count": len(incompatible), "incompatible_snapshot_count": sum(len(x["snapshots"]) for x in incompatible),
        "canonical_alpha_case_count": len(alpha), "canonical_direction_count": sum(len(x["directions"]) for x in alpha)}
    data["enumeration"]["audited_leaf_count"] = leaf_count(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C317_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__": main()
