#!/usr/bin/env python3
"""Exact Casdagli-coding audit for closed traces versus marked band paths.

The primary object is the source-faithful ten-state graph.  A six-state
quotient is checked separately, together with the intertwining and decorated
boundary identities needed for the unweighted marked-path series to descend.
All identities are exact in Q[z].
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def source_ten_state_data() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Return Casdagli's ten-state adjacency and source endpoint selectors."""
    outgoing = {
        1: (3, 7, 10),
        2: (4, 8, 9),
        3: (6,),
        4: (5,),
        5: (1,),
        6: (2,),
        7: (1,),
        8: (1,),
        9: (2,),
        10: (2,),
    }
    A = sp.zeros(10)
    for source, targets in outgoing.items():
        for target in targets:
            A[source - 1, target - 1] = 1
    u_row = sp.Matrix([[1, 0, 0, 0, 0, 1, 0, 0, 0, 0]])
    v_col = sp.Matrix([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
    return A, u_row, v_col


def quotient_six_state_data() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    """Return the six-state quotient and ten-to-six incidence matrix.

    The quotient merges {5,7,8} and {6,9,10}.  Its state 6 must retain the
    lift to old state R6 when used as an initial spectral boundary.
    """
    A6 = sp.Matrix(
        [
            [0, 0, 1, 0, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
        ]
    )
    u6 = sp.Matrix([[1, 0, 0, 0, 0, 1]])
    v6 = sp.Matrix([1, 1, 1, 1, 0, 0])
    quotient_map = (1, 2, 3, 4, 5, 6, 5, 5, 6, 6)
    Q = sp.zeros(10, 6)
    for old_state, new_state in enumerate(quotient_map):
        Q[old_state, new_state - 1] = 1
    return A6, u6, v6, Q


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def build_certificate(max_k: int = 15) -> dict[str, object]:
    A10, u10, v10 = source_ten_state_data()
    A6, u6, v6, Q = quotient_six_state_data()
    z, t = sp.symbols("z t")

    if A10 * Q != Q * A6:
        raise AssertionError("ten-to-six dynamical intertwining failed")
    if u10 * Q != u6:
        raise AssertionError("initial boundary projection failed")
    if Q * v6 != v10:
        raise AssertionError("terminal boundary lift failed")

    counts = [int((u10 * A10**k * v10)[0]) for k in range(max_k + 1)]
    expected = [fibonacci(k + 2) for k in range(max_k + 1)]
    if counts != expected:
        raise AssertionError("marked band-path counts do not match F_{k+2}")
    quotient_counts = [int((u6 * A6**k * v6)[0]) for k in range(max_k + 1)]
    if quotient_counts != counts:
        raise AssertionError("decorated quotient boundary counts do not descend")

    determinant = sp.factor((sp.eye(10) - z * A10).det())
    determinant6 = sp.factor((sp.eye(6) - z * A6).det())
    expected_determinant = sp.expand((1 + z) ** 2 * (1 - z + z**2) * (1 - z - z**2))
    if sp.expand(determinant - expected_determinant) != 0:
        raise AssertionError("ten-state determinant factorization mismatch")
    if sp.expand(determinant6 - expected_determinant) != 0:
        raise AssertionError("six-state determinant factorization mismatch")

    boundary = sp.factor((u10 * (sp.eye(10) - z * A10).inv() * v10)[0])
    boundary6 = sp.factor((u6 * (sp.eye(6) - z * A6).inv() * v6)[0])
    expected_boundary = (1 + z) / (1 - z - z**2)
    if sp.cancel(boundary - expected_boundary) != 0:
        raise AssertionError("ten-state boundary resolvent identity mismatch")
    if sp.cancel(boundary6 - expected_boundary) != 0:
        raise AssertionError("six-state boundary resolvent identity mismatch")

    trace_counts = [int(sp.trace(A10**k)) for k in range(1, max_k + 1)]
    return {
        "candidate": "HCS-C13B",
        "decision": "PROVED_SOURCE_FAITHFUL_MARKED_BAND_PATH_SERIES_DIFFERS_FROM_CLOSED_ZETA",
        "scope": "Casdagli ten-state V>=8 coding (lambda>=16 in the modern invariant normalization); this counts marked spectral-band paths, not the energy polynomial d_k(E)",
        "source_extraction": {
            "convention": "rows are current states and columns are next states",
            "outgoing_edges": {
                str(i + 1): [j + 1 for j, value in enumerate(A10.row(i)) if value]
                for i in range(A10.rows)
            },
            "initial_states": [1, 6],
            "terminal_states": [1, 2, 3, 4],
            "source_fibonacci_convention": "Casdagli F_0=F_1=1; source length n count F_n equals standard F_{n+1}",
            "project_index": "path length n=k+1 gives standard F_{k+2}=q_k",
        },
        "ten_state": {
            "adjacency_matrix": [list(map(int, A10.row(i))) for i in range(A10.rows)],
            "initial_boundary_row": list(map(int, u10.row(0))),
            "terminal_boundary_column": list(map(int, v10)),
            "characteristic_polynomial": str(sp.factor(A10.charpoly(t).as_expr())),
        },
        "six_state_quotient": {
            "adjacency_matrix": [list(map(int, A6.row(i))) for i in range(A6.rows)],
            "quotient_incidence_matrix": [list(map(int, Q.row(i))) for i in range(Q.rows)],
            "intertwining": "A10*Q=Q*A6",
            "boundary_identities": "u10*Q=u6 and Q*v6=v10",
            "scope_warning": "state 6 requires the lift to old R6 for the initial spectral boundary; arbitrary local energy weights need not descend",
        },
        "marked_counts": {
            "formula": "u10*A10^k*v10=F_{k+2}",
            "through_k": max_k,
            "values": counts,
        },
        "closed_counts": {
            "formula": "#Fix(sigma^k)=tr(A10^k)",
            "k_1_through_max": trace_counts,
        },
        "formal_identities": {
            "det_I_minus_zA10": str(determinant),
            "det_I_minus_zA6": str(determinant6),
            "artin_mazur_zeta": "1/((1+z)^2*(1-z+z^2)*(1-z-z^2))",
            "ten_state_boundary_resolvent": str(boundary),
            "six_state_boundary_resolvent": str(boundary6),
            "divisor_witness_at_z_minus_1": "after rational continuation, the boundary resolvent has a simple zero at z=-1 while the Artin-Mazur zeta has a double pole",
        },
        "data_policy": "exact rational symbolic algebra; no Riemann prime or zero data",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=Path("results"))
    parser.add_argument("--max-k", type=int, default=15)
    args = parser.parse_args()
    if not 1 <= args.max_k <= 100:
        parser.error("--max-k must lie between 1 and 100")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    output = args.out_dir / "symbolic_boundary_certificate.json"
    with output.open("w", encoding="utf-8") as handle:
        json.dump(build_certificate(args.max_k), handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(f"wrote exact HCS-C13B coding certificate to {output}")


if __name__ == "__main__":
    main()
