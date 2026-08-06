#!/usr/bin/env python3
"""Exact value-growth audit at two escaping spectral-section energies.

After a strict trace-map escape triple, the half-traces obey
|x[k+1]| > |x[k]|*|x[k-1]|.  Their logarithms therefore grow at least on a
Fibonacci scale, so the discriminant values grow super-exponentially in the
renormalization clock and their ordinary generating series has radius zero.
This script records the exact rational inequalities.  The all-level
implication is a proved lemma, not an inference from the finite audit window.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def half_traces(energy: int, coupling: int, through_k: int) -> dict[int, Fraction]:
    x = {
        -2: Fraction(1),
        -1: Fraction(energy, 2),
        0: Fraction(energy - coupling, 2),
    }
    for k in range(0, through_k):
        x[k + 1] = 2 * x[k] * x[k - 1] - x[k - 2]
    return x


def first_product_escape_index(x: dict[int, Fraction]) -> int:
    for n in sorted(x):
        if n - 2 not in x:
            continue
        a, b, c = abs(x[n - 2]), abs(x[n - 1]), abs(x[n])
        if 1 < a < b < c:
            return n
    raise AssertionError("strict escape triple not found")


def decimal_digits_fraction(value: Fraction) -> int:
    """Return decimal digits of the numerator; denominators stay powers of 2."""
    return len(str(abs(value.numerator)))


def witness(energy: int, through_k: int) -> dict[str, object]:
    x = half_traces(energy, coupling=1, through_k=through_k)
    end = first_product_escape_index(x)
    checks: list[dict[str, object]] = []
    for k in range(end, through_k):
        left = abs(x[k + 1])
        right = abs(x[k]) * abs(x[k - 1])
        if not left > right:
            raise AssertionError(f"product growth failed at energy={energy}, k={k}")
        checks.append(
            {
                "from_k": k,
                "abs_x_next_gt_abs_x_times_abs_x_prev": True,
                "next_numerator_decimal_digits": decimal_digits_fraction(left),
            }
        )
    return {
        "energy": energy,
        "coupling": 1,
        "escape_triple_ending_at_k": end,
        "escape_absolute_values": [str(abs(x[j])) for j in (end - 2, end - 1, end)],
        "product_growth_checks": checks,
        "final_k": through_k,
        "final_half_trace": str(x[through_k]),
        "final_numerator_decimal_digits": decimal_digits_fraction(x[through_k]),
    }


def build_certificate(through_k: int = 18) -> dict[str, object]:
    return {
        "candidate": "HCS-C13G",
        "decision": "PROVED_ZERO_RADIUS_RENORMALIZATION_CLOCK_OBSTRUCTION_AT_EXACT_ESCAPE_ENERGIES",
        "witness_semantics": "E=0 and E=-1 are finite-periodic-approximant spectral-section energies at lambda=1; their escaping orbits are not asserted to lie in the infinite Fibonacci Hamiltonian spectrum",
        "exact_witnesses": [witness(0, through_k), witness(-1, through_k)],
        "theorem_scope": {
            "all_level_proof": "the strict escape inequality propagates forever; if a_r=log|x_{n+r}| then a_{r+1}>a_r+a_{r-1}, hence a_r>=c F_{r+2}",
            "fibonacci_discriminant": "at lambda=1 and E*=0,-1, lim_k |d_k(E*)|^(1/k)=infinity",
            "coefficient_series": "the ordinary renormalization-clock series sum_k d_k(E*) z^k has radius of convergence zero",
            "analytic_germ": "no scalar germ analytic at z=0 can have coefficients d_k(E*) for all sufficiently large k",
            "log_determinant": "no normalized nonvanishing analytic determinant germ Delta(z), Delta(0)=1, can satisfy d_k(E*)=-k[z^k]log Delta(z) for all sufficiently large k",
            "operator_consequence": "fixed bounded-operator resolvents and analytic trace-class Fredholm determinants are excluded from these literal coefficientwise realizations because they define positive-radius germs",
        },
        "claim_boundary": {
            "excluded": "literal renormalization-clock coefficient or logarithmic-trace realization by any fixed scalar generating function analytic at z=0, including finite matrices as a special case",
            "not_excluded": [
                "physical-time q_k-step chronological products",
                "k-dependent operator families",
                "moving evaluation functionals such as delta_ell(E) composed with the trace-map Koopman operator when no fixed analytic scalar germ is claimed",
                "nonlinear composition operators whose proposed scalar output is not a fixed analytic germ with the literal target coefficients",
                "formal zero-radius series or operators whose relevant scalar matrix element is not analytic at z=0",
                "weights that are singular or undefined at the exact witness energies",
                "an indirect divisor correspondence that does not identify d_k(E*) with renormalization-clock coefficients or logarithmic traces",
            ],
        },
        "data_policy": "exact Fraction arithmetic only; no floating point and no Riemann prime or zero data",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=Path("results"))
    parser.add_argument("--through-k", type=int, default=18)
    args = parser.parse_args()
    if not 8 <= args.through_k <= 24:
        parser.error("--through-k must lie between 8 and 24")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    output = args.out_dir / "value_growth_certificate.json"
    with output.open("w", encoding="utf-8") as handle:
        json.dump(build_certificate(args.through_k), handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(f"wrote exact HCS-C13G value-growth certificate to {output}")


if __name__ == "__main__":
    main()
