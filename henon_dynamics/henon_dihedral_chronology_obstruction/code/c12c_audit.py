#!/usr/bin/env python3
"""Exact audit for HCS-C12C.

The program has two independent jobs:

1. reproduce the Möbius/Burnside orbit counts of Gallas (2007); and
2. certify that every period-six squarefree dihedral component is rational.

No floating-point arithmetic is used.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from math import isqrt
from pathlib import Path

import sympy as sp


def divisors(n: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
    return small + large[::-1]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    prime_count = 0
    p = 2
    remaining = n
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            prime_count += 1
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


@dataclass(frozen=True)
class OrbitCount:
    period: int
    exact_points: int
    cyclic_orbits: int
    axial_exact_points: int
    parabolic_exact_points: int
    diagonal_orbits: int
    nondiagonal_orbits: int
    chiral_cyclic_orbits: int
    chiral_doublets: int
    dihedral_orbits: int


def orbit_count(n: int) -> OrbitCount:
    ds = divisors(n)
    nu = sum(mobius(n // d) * 2**d for d in ds)
    axial = sum(mobius(n // d) * 2 ** ((d + 1) // 2) for d in ds)
    parabolic = sum(mobius(n // d) * 2 ** ((d + 2) // 2) for d in ds)
    if nu % n:
        raise ArithmeticError(f"exact point count is not divisible by n={n}")
    cyclic = nu // n
    diagonal = axial if n % 2 else axial // 2
    nondiagonal = 0 if n % 2 else parabolic // 2
    chiral = cyclic - diagonal - nondiagonal
    if chiral % 2:
        raise ArithmeticError(f"chiral cyclic count is odd at n={n}")
    doublets = chiral // 2
    dihedral = diagonal + nondiagonal + doublets
    if dihedral != (cyclic + diagonal + nondiagonal) // 2:
        raise AssertionError("Burnside identity failed")
    return OrbitCount(
        period=n,
        exact_points=nu,
        cyclic_orbits=cyclic,
        axial_exact_points=axial,
        parabolic_exact_points=parabolic,
        diagonal_orbits=diagonal,
        nondiagonal_orbits=nondiagonal,
        chiral_cyclic_orbits=chiral,
        chiral_doublets=doublets,
        dihedral_orbits=dihedral,
    )


def period_six_certificate() -> dict[str, object]:
    sigma, parameter, t = sp.symbols("sigma A t")
    c6 = sigma - 2
    d6 = sigma**2 + 4 * sigma - 4 * parameter
    n6 = (
        sigma**5
        + 2 * sigma**4
        - 4 * (5 * parameter + 4) * sigma**3
        + 8 * parameter * sigma**2
        + 4 * (16 * parameter**2 + 12 * parameter + 9) * sigma
        + 128 * parameter**2
        - 96 * parameter
        + 72
    )
    discriminant = sp.factor(sp.discriminant(n6, parameter))
    expected = 16 * (sigma - 6) * (sigma + 2) * (3 * sigma**2 - 8 * sigma - 12) ** 2
    if sp.expand(discriminant - expected) != 0:
        raise AssertionError("period-six discriminant factorization failed")

    c2 = sp.Poly(n6, parameter).coeff_monomial(parameter**2)
    c1 = sp.Poly(n6, parameter).coeff_monomial(parameter)
    q = 3 * sigma**2 - 8 * sigma - 12
    # On N6=0, Y=(2*c2*A+c1)/(4*q) obeys Y^2=(sigma-6)(sigma+2).
    hill_numerator = sp.factor((2 * c2 * parameter + c1) ** 2 - discriminant)
    quotient_on_curve = sp.factor(hill_numerator / n6)
    expected_quotient = sp.factor(4 * c2)
    if sp.factor(quotient_on_curve - expected_quotient) != 0:
        raise AssertionError("quadratic completion identity failed")

    sigma_param = 2 + 2 * (t + 1 / t)
    y_param = 2 * (t - 1 / t)
    conic_check = sp.factor(y_param**2 - (sigma_param - 6) * (sigma_param + 2))
    if conic_check != 0:
        raise AssertionError("rational parametrization failed")

    return {
        "C6": str(c6),
        "D6": str(d6),
        "N6": str(n6),
        "disc_A_N6": str(discriminant),
        "squarefree_double_cover": "Y^2 = (sigma - 6)*(sigma + 2)",
        "birational_Y": str(sp.factor((2 * c2 * parameter + c1) / (4 * q))),
        "rational_parametrization": {
            "sigma": str(sigma_param),
            "Y": str(y_param),
        },
        "component_genera": {"C6": 0, "D6": 0, "N6_normalization": 0},
        "weight_one_H1_dimensions": {"C6": 0, "D6": 0, "N6_normalization": 0},
    }


def write_results(max_period: int, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = [orbit_count(n) for n in range(1, max_period + 1)]
    with (out_dir / "dihedral_counts.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0])))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)

    n6 = period_six_certificate()
    published_period14_display = {
        "cyclic_orbits": 1161,
        "displayed_chiral_doublets": 500,
        "diagonal_orbits": 56,
        "nondiagonal_orbits": 119,
    }
    recomputed14 = asdict(rows[13]) if max_period >= 14 else asdict(orbit_count(14))
    table14_sum = (
        2 * published_period14_display["displayed_chiral_doublets"]
        + published_period14_display["diagonal_orbits"]
        + published_period14_display["nondiagonal_orbits"]
    )
    certificate = {
        "candidate": "HCS-C12C",
        "decision": "STOP_SCOPED_PRIOR_MARKER_COLLISION_NO_GLOBAL_DETERMINANT",
        "arithmetic": "exact integer and symbolic computation; no floats",
        "max_period": max_period,
        "low_period_counts": [asdict(row) for row in rows[:8]],
        "period_six": n6,
        "period14_source_table_audit": {
            "published_display": published_period14_display,
            "displayed_partition_sum": table14_sum,
            "recomputed": recomputed14,
            "diagnosis": (
                "The displayed 500 is internally inconsistent: 2*500+56+119=1175, "
                "not 1161. Equations (2)--(7) give 493 doublets."
            ),
        },
        "invariant_sector_projection": {
            "group": "D_n = <H,R | H^n=R^2=1, RHR=H^-1>",
            "coarse_quotient_action": "H acts identically on P_n / D_n",
            "invariant_projector": "P_inv=(1/(2n))*sum_{g in D_n} g",
            "frobenius_trace": "Tr(F^r|V^D_n)=(1/(2n))*sum_g Tr(F^r g|V)",
            "lost_data": [
                "marked phase inside each orbit",
                "reversal orientation and unweighted chiral-doublet multiplicity",
                "non-trivial D_n isotypic sectors",
                "unaveraged joint Frobenius-Henon-reflection traces",
            ],
            "scope_note": (
                "Cyclic phase quotienting is standard for an autonomous scalar orbit zeta; "
                "this identity limits equivariant-data claims but is not a generic zeta no-go."
            ),
        },
    }
    with (out_dir / "certificate.json").open("w", encoding="utf-8") as handle:
        json.dump(certificate, handle, indent=2, sort_keys=True)
        handle.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-period", type=int, default=35)
    parser.add_argument("--out-dir", type=Path, default=Path("results"))
    args = parser.parse_args()
    if args.max_period < 6:
        parser.error("--max-period must be at least 6")
    write_results(args.max_period, args.out_dir)
    print(f"wrote exact HCS-C12C audit to {args.out_dir}")


if __name__ == "__main__":
    main()
