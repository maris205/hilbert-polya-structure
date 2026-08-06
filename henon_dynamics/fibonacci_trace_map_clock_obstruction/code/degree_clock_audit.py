#!/usr/bin/env python3
"""Exact degree-growth certificate for the Fibonacci two-clock obstruction.

The mathematical theorem is proved in DERIVATION_PACKAGE.md.  This script
certifies its Fibonacci input and records how much per-renormalization-step
energy degree a local polynomial-weight model would need in order to match
the discriminant degree.  The theorem allows an arbitrary finite state
dimension N_k at every level; only the polynomial degree of a local entry is
required to be uniform in k.

No Riemann zeros, primes, floating-point roots, or fitted parameters are used.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import sympy as sp


def fibonacci_lengths(max_k: int) -> dict[int, int]:
    """Return q_k=F_{k+2} in the seed convention q_-1=q_0=1."""
    q = {-1: 1, 0: 1}
    for k in range(0, max_k):
        q[k + 1] = q[k] + q[k - 1]
    return q


def discriminants(max_k: int) -> tuple[sp.Symbol, dict[int, sp.Expr]]:
    """Construct the exact lambda=1 trace polynomials through max_k."""
    E = sp.symbols("E")
    d: dict[int, sp.Expr] = {-2: sp.Integer(2), -1: E, 0: E - 1}
    for k in range(0, max_k):
        d[k + 1] = sp.expand(d[k] * d[k - 1] - d[k - 2])
    return E, d


def exact_symbolic_degree_check(max_symbolic_k: int = 10) -> list[dict[str, int]]:
    """Verify deg_E d_k=q_k by expanding manageable exact polynomials."""
    E, d = discriminants(max_symbolic_k)
    q = fibonacci_lengths(max_symbolic_k)
    rows: list[dict[str, int]] = []
    for k in range(-1, max_symbolic_k + 1):
        degree = int(sp.degree(d[k], E))
        if degree != q[k]:
            raise AssertionError(f"degree mismatch at k={k}: {degree} != {q[k]}")
        rows.append({"k": k, "q_k": q[k], "degree_d_k": degree})
    return rows


def required_local_degree_rows(max_k: int = 30) -> list[dict[str, int | str]]:
    """Record the minimum D_k allowed by deg(B_k(E)^k)<=kD_k.

    For closed traces the boundary-degree offset is zero.  The integer
    ceil(q_k/k) therefore lower-bounds the per-step polynomial degree of any
    level-k local weight that could reproduce d_k at that level, independently
    of the finite state dimension N_k.
    """
    q = fibonacci_lengths(max_k)
    rows: list[dict[str, int | str]] = []
    for k in range(1, max_k + 1):
        needed = (q[k] + k - 1) // k
        rows.append(
            {
                "k": k,
                "physical_length_q_k": q[k],
                "degree_d_k": q[k],
                "linear_clock_k": k,
                "minimum_uniform_edge_degree_for_closed_trace_at_level_k": needed,
                "exact_ratio_q_k_over_k": f"{q[k]}/{k}",
            }
        )
    return rows


def build_certificate(max_k: int, max_symbolic_k: int) -> dict[str, object]:
    symbolic = exact_symbolic_degree_check(max_symbolic_k)
    growth = required_local_degree_rows(max_k)
    required = [int(row["minimum_uniform_edge_degree_for_closed_trace_at_level_k"]) for row in growth]
    if any(b < a for a, b in zip(required, required[1:])):
        # The ceiling sequence is nondecreasing for the registered range; this
        # check is descriptive and is not used in the theorem.
        raise AssertionError("unexpected decrease in registered degree requirement")
    return {
        "candidate": "HCS-C13P",
        "decision": "PROVED_DIMENSION_INDEPENDENT_PASSIVE_PARAMETER_BOUNDED_POLYNOMIAL_DEGREE_CLOCK_OBSTRUCTION",
        "theorem_scope": {
            "model_class": "at each level k, E is a passive parameter in an arbitrary finite matrix B_k(E) of dimension N_k; N_k may grow without restriction, iteration is ordinary multiplication, entry degree D is uniform in k, and E is not dynamically substituted",
            "closed_trace": "for every finite N_k and every B_k(E) with entry degree at most D, deg_E tr(B_k(E)^k) <= kD",
            "marked_boundary": "for level-dependent polynomial boundary vectors u_k(E),v_k(E) with uniformly bounded entry degrees, deg_E u_k(E)^T B_k(E)^k v_k(E) <= D_u+kD+D_v",
            "determinant_coefficients": "for either sign, deg_E [z^k] det(I-z B_k(E))^(+1 or -1) <= kD; increasing N_k alone cannot change this bound",
            "fibonacci_input": "deg_E d_k=q_k=F_{k+2}",
            "conclusion": "none of these order-k observables can equal d_k for all large k under a uniform local polynomial-degree bound, even if N_k grows arbitrarily",
        },
        "claim_boundary": {
            "not_excluded": [
                "physical-time models indexed by q_k",
                "k-dependent weights whose energy degree grows exponentially",
                "the full q_k-order characteristic determinant det(EI-H_k), which is a different observable",
                "nonlinear or composition operators such as f(E) -> f(E^2)",
                "trace-map Koopman models with a moving evaluation functional at ell_lambda(E)",
                "infinite-dimensional constructions using an indirect divisor map or a scalar element nonanalytic at z=0; analytic literal coefficient matches at the escape witnesses are covered by HCS-C13G",
            ],
            "not_a_claim": "this degree certificate does not refute every weighted Fredholm determinant; the separate zero-radius certificate covers a broader but still coefficientwise analytic-germ claim",
        },
        "exact_symbolic_check": {
            "through_k": max_symbolic_k,
            "rows": symbolic,
        },
        "integer_growth_audit": {
            "through_k": max_k,
            "last_q_k": growth[-1]["physical_length_q_k"],
            "last_minimum_edge_degree": growth[-1]["minimum_uniform_edge_degree_for_closed_trace_at_level_k"],
        },
        "data_policy": "exact integer and symbolic algebra only; no Riemann prime or zero data",
    }


def write_results(out_dir: Path, max_k: int, max_symbolic_k: int) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = required_local_degree_rows(max_k)
    certificate = build_certificate(max_k, max_symbolic_k)
    with (out_dir / "degree_clock_certificate.json").open("w", encoding="utf-8") as handle:
        json.dump(certificate, handle, indent=2, sort_keys=True)
        handle.write("\n")
    with (out_dir / "degree_growth.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=Path("results"))
    parser.add_argument("--max-k", type=int, default=30)
    parser.add_argument("--max-symbolic-k", type=int, default=10)
    args = parser.parse_args()
    if not 1 <= args.max_symbolic_k <= 12:
        parser.error("--max-symbolic-k must lie between 1 and 12")
    if not args.max_symbolic_k <= args.max_k <= 1000:
        parser.error("require max-symbolic-k <= max-k <= 1000")
    write_results(args.out_dir, args.max_k, args.max_symbolic_k)
    print(f"wrote exact HCS-C13P degree/clock audit to {args.out_dir}")


if __name__ == "__main__":
    main()
