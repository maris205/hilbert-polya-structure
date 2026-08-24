#!/usr/bin/env python3
"""Independent C126 checker; deliberately imports no producer code."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c126_chebyshev_skew_evidence.json"


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    result = 1
    value = n
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            result = -result
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        result = -result
    return result


def validate(data: dict) -> None:
    assert data["schema"] == "hcs-c126-chebyshev-contracting-skew-v1"
    assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    source = data["source_model"]
    assert source["candidate_id"] == "HCS-C126"
    assert source["map"] == "F(x,y)=(T_3(x),y/4+x)=(4*x^3-3*x,y/4+x)"
    assert source["fiber_multiplier"] == "1/4"
    assert source["clock"] == "one application of F"
    assert source["orbit_cutoff"] == "none for the theorem; n<=12 only for the replay ledger"
    assert "prime tables" in source["forbidden_data"]

    x = sp.symbols("x")
    f = 4*x**3 - 3*x
    current = x
    replay = data["all_period_theorem"]["finite_symbolic_replay"]
    assert len(replay) == 4
    for n, row in enumerate(replay, 1):
        current = sp.expand(f.subs(x, current))
        target = sp.chebyshevt(3**n, x)
        assert sp.expand(current-target) == 0
        assert row == {"n": n, "degree": 3**n, "matches_T_3_power_n": True}

    theorem = data["all_period_theorem"]
    assert theorem["base_fixed_root_count"] == "3^n distinct real roots"
    assert theorem["root_family_intersection"] == "{1,-1}"
    assert theorem["root_count_derivation"] == "(3^n+1)/2+(3^n+3)/2-2=3^n"
    assert theorem["fixed_point_count"] == "#Fix(F^n)=3^n for every n>=1"
    assert "1-4^(-n)" in theorem["unique_fiber_closure"]
    assert theorem["least_period_preservation"].startswith("the unique fiber lift")

    primitive_rows = data["primitive_orbits"]["prefix_n1_to_n12"]
    stability_rows = data["stability"]["prefix_n1_to_n12"]
    assert len(primitive_rows) == len(stability_rows) == 12
    for n in range(1, 13):
        ds = divisors(n)
        exact = sum(mu(d)*3**(n//d) for d in ds)
        total_orbits = exact // n
        negative_points = sum(mu(d)*(3**(n//d)-1) for d in ds if d % 2) // 2
        negative_orbits = negative_points // n
        expected_primitive = {
            "n": n,
            "fixed_points": 3**n,
            "exact_period_points": exact,
            "primitive_orbits": total_orbits,
            "positive_unstable_orientation_primitive_orbits": total_orbits-negative_orbits,
            "negative_unstable_orientation_primitive_orbits": negative_orbits,
        }
        assert primitive_rows[n-1] == expected_primitive
        m = 3**n
        expected_stability = {
            "n": n,
            "m": m,
            "endpoint_count": 2,
            "positive_interior_count": (m-3)//2,
            "negative_interior_count": (m-1)//2,
            "positive_unstable_orientation_fixed_points": (m+1)//2,
            "negative_unstable_orientation_fixed_points": (m-1)//2,
            "endpoint_unstable_multiplier": str(m*m),
            "positive_interior_unstable_multiplier": str(m),
            "negative_interior_unstable_multiplier": str(-m),
            "stable_multiplier": f"1/{4**n}",
            "endpoint_stability_determinant": f"(1-{m*m})*(1-1/{4**n})",
            "positive_interior_stability_determinant": f"(1-{m})*(1-1/{4**n})",
            "negative_interior_stability_determinant": f"(1+{m})*(1-1/{4**n})",
        }
        assert stability_rows[n-1] == expected_stability

    zeta = data["zeta"]
    assert zeta["closed_form"] == "zeta_F(z)=1/(1-3*z)"
    assert zeta["primitive_product"] == "product_{primitive gamma}(1-z^(period gamma))^(-1)"
    assert zeta["convergence_disk"] == "|z|<1/3 for the defining logarithmic series"
    assert "not a target-facing" in zeta["qualification"]

    stability = data["stability"]
    assert stability["jacobian"] == "DF(x,y)=[[12*x^2-3,0],[1,1/4]]"
    assert stability["hyperbolicity"].startswith("all fixed points")
    assert stability["orientation_counts"] == "positive=(3^n+1)/2 and negative=(3^n-1)/2"
    assert "alpha^r" in stability["primitive_repetition_law"]

    controls = data["negative_controls"]
    unit = controls["unit_fiber_multiplier"]
    assert "whole fixed line" in unit["n1_closure"]
    assert "1-1 vanishes" in unit["failure"]
    gcontrol = controls["non_chebyshev_cubic"]
    g = 4*x**3-2*x
    g2 = sp.expand(g.subs(x, g))
    assert sp.factor(g2-x) == x*(2*x-1)**3*(2*x+1)**3*(4*x**2-3)
    assert gcontrol["base_second_iterate_minus_x_factorization"] == "x*(2*x-1)^3*(2*x+1)^3*(4*x^2-3)"
    assert gcontrol["distinct_base_fix_g2"] == 5
    assert gcontrol["degree_with_multiplicity"] == 9
    assert sp.factor(g2-sp.chebyshevt(9,x)) == x*(192*x**6-240*x**4+80*x**2-5)
    assert "+/-1/2 form a neutral" in gcontrol["failure"]

    progress = data["progress_over_prior_gate"]
    assert "all-period complete real fixed-point atlas" in progress["new_result"]
    assert "no weighted global transfer" in progress["remaining_gap"]

    verdict = data["route_a_evaluator"]
    assert verdict == {
        "canonical_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        "A1_qualification": "ALL_PERIOD_SOURCE_ORBITS_PROVED_BUT_NO_PRIME_LIKE_TARGET_SEMANTICS_OR_MANDATORY_TARGET_CONTROLS",
        "A2_qualification": "ARTIN_MAZUR_ZETA_IS_SOURCE_ORBIT_OWNED_BUT_NOT_A_WEIGHTED_TARGET_FACING_FREDHOLM_DETERMINANT",
        "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COMPLETION_COUNTING_LAW_OR_CONTROLLED_TARGET_CONTINUATION",
        "A4_qualification": "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
        "overall": "ROUTE_A_EXPLORATORY",
        "route_b_invocation_allowed": False,
    }
    assert data["nonclaims"] == [
        "a prime-to-orbit correspondence or target divisor match",
        "a weighted nuclear transfer operator or Fredholm determinant",
        "a target functional equation, Gamma completion, or Riemann-von Mangoldt law",
        "arithmetic/local data, Euler factors, root numbers, or automorphy",
        "a Hilbert--Polya operator, Riemann-zero statement, or Route-B authorization",
    ]
    nonclaims = " ".join(data["nonclaims"])
    for text in ["target divisor", "Euler factors", "root numbers", "Hilbert--Polya", "Route-B"]:
        assert text in nonclaims


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    raw = path.read_bytes()
    validate(json.loads(raw))
    print("C126_INDEPENDENT_CHECK_PASS", sha256(raw).hexdigest(), 12, 12)


if __name__ == "__main__":
    main()
